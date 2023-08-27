import json
import pathlib
from dataclasses import dataclass, asdict
from typing import Optional

import pandas as pd
from PIL import Image, ImageDraw
from easyocr import easyocr
from tqdm import tqdm

from model import predict_tg, predict_dzen, predict_vk, predict_yt

reader = easyocr.Reader(["ru", "en"])

PLATFORMS = {
    "tg": {"metrics": ["ERR"], "function": predict_tg},
    "zn": {"metrics": ["Количество дочитываний"], "function": predict_dzen},
    "vk": {"metrics": ["Количество подписчиков"], "function": predict_vk},
    "yt": {"metrics": ["Подписчики", "Просмотры"], "function": predict_yt},
}

ALLOW_EXTENSIONS = [".jpg", ".png", ".PNG", ".jpeg"]


@dataclass
class Metrica:
    name: str
    value: Optional[str]


@dataclass
class Result:
    id: str
    platform: str
    original_file: str
    processed_file: Optional[str]
    metrics: list[Metrica]


def process_excel() -> dict:
    result = {}

    for blog_id, image in pd.read_excel("data.xlsx").values:
        result[pathlib.Path(image)] = blog_id

    return result


def get_images(dir: str) -> list[pathlib.Path]:
    return [
        p
        for p in pathlib.Path(f"{dir}/images").iterdir()
        if p.is_file() and p.suffix in ALLOW_EXTENSIONS
    ]


def process_image(platform: str, image: pathlib.Path, blog_id: str) -> Result:
    filename = str(image)
    platform_info = PLATFORMS[platform]

    result = platform_info["function"](filename, reader)

    if result is None or (
        platform == "yt" and result[0][0] is None and result[0][1] is None
    ):
        return Result(
            id=blog_id,
            original_file=filename,
            processed_file=None,
            metrics=[],
            platform=platform,
        )

    pillow = Image.open(filename)
    draw = ImageDraw.Draw(pillow)

    # Для ютуба result такой
    # (['640', 23300.0], [[1140, 442, 1228, 490], [1509, 643, 1585, 663]])
    if platform == "yt":
        for box in result[1]:
            draw.rectangle(box, outline=(255, 0, 0), width=2)
    else:
        draw.rectangle(result[1], outline=(255, 0, 0), width=2)

    processed_path = pathlib.Path(f"{platform}/processed_images")
    processed_path.mkdir(parents=True, exist_ok=True)
    processed_image_filename = str((processed_path / image.name))

    pillow.save(processed_image_filename)

    if platform == "yt":
        metrics = []

        for count, value in enumerate(result[0]):
            metrics.append(Metrica(name=platform_info["metrics"][count], value=value))
    else:
        metrics = [Metrica(name=platform_info["metrics"][0], value=result[0])]

    return Result(
        id=blog_id,
        original_file=image.name,
        processed_file=image.name,
        metrics=metrics,
        platform=platform,
    )


def generate_excel(platform: str, results: list[Result]):
    platform_info = PLATFORMS[platform]
    frame_data = []

    columns = []

    for metrica in platform_info["metrics"]:
        columns.append(metrica)

    columns.append("image")

    for result in results:
        data = []
        if len(result.metrics) > 0:
            for metrica in result.metrics:
                if metrica is None:
                    data.append(None)
                else:
                    data.append(metrica.value)
        else:
            for i in range(len(platform_info["metrics"])):
                data.append("invalid")

        image_filename = pathlib.Path(result.original_file).name

        data.append(image_filename)
        frame_data.append(data)

    df = pd.DataFrame(frame_data, columns=columns)
    df.to_excel(f"{platform}/{platform}.xlsx", index=False)


def main() -> None:
    image_to_blog = process_excel()

    images = []

    for platform in PLATFORMS:
        for image in get_images(platform):
            images.append((platform, image))

    pbar = tqdm(images)

    results = {platform: [] for platform in PLATFORMS}

    for platform, image in pbar:
        pbar.set_description(
            f"Обработка платформы: {platform}, изображение: {image.name}"
        )
        result = process_image(platform, image, image_to_blog[image])
        results[platform].append(result)

    for platform, results in results.items():
        generate_excel(platform, results)
        json.dump(
            [asdict(item) for item in results],
            pathlib.Path(f"{platform}.json").open("w"),
        )


main()
