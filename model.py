import re

import cv2
import numpy as np
from regex import regex


def get_closest_value(node,nodes, coef):
    # оставляем только те ноды, в которых есть цифры
    values = [x[1] for x in nodes]
    filtered_idx = [
        index for index, value in enumerate(values) if re.search('\d', value)
    ]
    filtered_nodes = [nodes[idx] for idx in filtered_idx]

    # центр ключевого bbox
    node_x0y0x1y1 = node[0][0]+node[0][2]
    x0,y0,x1,y1 = tuple(node_x0y0x1y1)
    node_centre = np.array([x0+(x1-x0)/2,y0+(y1-y0)/2])

    # центры ближайших bbox
    nodes_x0y0x1y1 = list(map(lambda x: x[0][0]+x[0][2], filtered_nodes))
    nodes_centres = np.array(
        list(
            map(lambda x: np.array([x[0]+(x[2]-x[0])/2,x[1]+(x[3]-x[1])/2]),nodes_x0y0x1y1)
        )
    )

    # ближайший центр
    ## считаем расстояния, а пока умножаем

    distances = ((np.asarray(nodes_centres) - node_centre) ** 2)**(1/2)#!!!
    distances[:, 1] *= coef #!!!
    distances = np.sum(distances, axis=1)

    ## для перестраховки удаляем дистанции 0
    distances = distances[np.where(distances>0)]

    ## находим индексы и получаем значения
    idx = np.argmin(distances)
    closest_value = re.findall('\d{1,}[\.,]{0,}\d{0,}[ ]{0,1}[%]{0,1}', filtered_nodes[idx][1])[0] #!!!3
    closest_dist = distances[idx]
    closest_conf = filtered_nodes[idx][-1]
    key_conf = node[-1]
    closest_bbox = filtered_nodes[idx][0][0] + filtered_nodes[idx][0][2]
    return closest_value, closest_dist, closest_bbox


def predict_tg(filename, reader):
    tg_coef = 2.5
    key_idxs = []

    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    result = reader.readtext(
        image, paragraph=False, batch_size=8
    )  # '1 август 2022.jpg'
    key = [
        "err",  # Приоритетнее
        "постов (cp)",  #!!!2
        "читают",  #!!!1
    ]
    # Удаляем ERR24
    for i, res in enumerate(result):
        text = res[1]
        if (
            ("err24" in text.lower())
            or ("erf24" in text.lower())
            or ("errz4" in text.lower())
        ):
            result.pop(i)

    # Поиск ключа
    for i, res in enumerate(result):
        # print(i)
        text = res[1].lower()
        for k in key:
            if k not in ["err", "vr"]:
                pattern = "[.\s]{0,}(" + str(k) + ")" + "{e<=2}" + "[\s.]{0,}"
            else:
                pattern = "[.\s]{0,}" + str(k) + "[\s.]{0,}"
            regul = regex.findall(pattern, text, overlapped=True)
            if regul:
                pattern = "\d{1,}[\.\s]{0,}\d{0,}[%]{0,}[^a-zA-ZА-Яа-яёЁ\.]{0,}"  # [^\D]\d{1,}[\.\s]{0,}\d{0,}[%]{0,}[^a-zA-ZА-Яа-яёЁ\.\s]
                find_digit_key = re.findall(pattern, text)
                if find_digit_key and k == "err":
                    digit = find_digit_key[0]
                    # Нашли ключевое слово в ERR + число
                    # Возвращаем False, tuple(value, bbox)
                    return digit, res[0][0] + res[0][2]
                key_idxs.append(i)
                break

    if not key_idxs:
        # Не валидный файл
        return None

    else:
        # Не нашли число в ключевом слове
        key_nodes = [result[idx] for idx in key_idxs]

        another_idxs = [idx for idx, x in enumerate(result) if x not in key_idxs]
        another_nodes = [result[idx] for idx in another_idxs]

        closest_values = []
        closest_distances = []
        closest_bboxes = []
        # print(key_nodes)
        for node in key_nodes:
            closet_value, dist, bbox = get_closest_value(node, another_nodes, tg_coef)
            closest_values.append(closet_value)
            closest_distances.append(dist)
            closest_bboxes.append(bbox)
        digit = closest_values[closest_distances.index(min(closest_distances))]
        bbox = closest_bboxes[closest_distances.index(min(closest_distances))]
        return digit, bbox


def predict_dzen(filename, reader):
    dzen_coef = 1
    key_idxs = []

    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    result = reader.readtext(image, paragraph=False, batch_size=8) # '1 август 2022.jpg'

    key = [
        'дочитывания'
    ]
    # Поиск ключа
    for i, res in enumerate(result):
        text = res[1].lower()
        for k in key:
            pattern = '[.\s]{0,}(' + str(k) +')'+ '{e<=2}'+'[\s.]{0,}'
            regul = regex.findall(pattern, text, overlapped=True)
            if regul:
                key_idxs.append(i)
    if not key_idxs:
        # Не валидный файл
        return 'Невалидный файл'
    else:
        # Не нашли число в ключевом слове
        key_nodes = [result[idx] for idx in key_idxs]
        # Берем самую нижнюю
        if len(key_nodes) >= 2:
            key_nodes = [key_nodes[-1]]
        another_idxs = [idx for idx, x in enumerate(result) if x not in key_idxs]
        another_nodes = [result[idx] for idx in another_idxs]
        another_nodes = [x for x in another_nodes if x[-2].isdigit()]

        closest_values = []
        closest_distances = []
        closest_bboxes = []
        for node in key_nodes:
            closet_value, dist, bbox = get_closest_value(node, another_nodes, dzen_coef)
            closest_values.append(closet_value)
            closest_distances.append(dist)
            closest_bboxes.append(bbox)
        digit = closest_values[closest_distances.index(min(closest_distances))]
        bbox = closest_bboxes[closest_distances.index(min(closest_distances))]
        return digit, bbox


def predict_vk(filename, reader):
    vk_coef = 1.5
    key_idxs = []
    all_digit = []

    is_friend = False
    is_subs = False
    frend_subs = []
    is_recomended = False

    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    result = reader.readtext(
        image, paragraph=False, batch_size=8
    )  # '1 август 2022.jpg'

    key = [
        "подписчиков",  # Приоритетнее
        "подписки",
        "участники",
        "друзей",
        "друг",
        "друзья",
    ]

    # Поиск ключа
    for i, res in enumerate(result):
        text = res[1].lower()
        for k in key:
            if k not in ["друг", "друзей"]:
                pattern = "[.\s]{0,}(" + str(k) + ")" + "{e<=2}" + "[\s.]{0,}"
            else:
                pattern = "[.\s]{0,}" + str(k) + "[\s.]{0,}"
            regul = regex.findall(pattern, text, overlapped=True)
            if regex.findall("(рекомендуют)", text, overlapped=True):
                is_recomended = True

            if regul:
                pattern = "\d{1,}[\.\s]{0,}\d{0,}[%]{0,}[^a-zA-ZА-Яа-яёЁ\.]{0,}"
                find_digit_key = re.findall(pattern, text)

                if find_digit_key and k in ["подписчиков", "участники"]:
                    digit = re.findall(pattern, text.replace("з", "3"))[0]
                    all_digit.append((digit, res[0][0] + res[0][2]))

                # Если есть друзья
                if k in ["подписчиков"] and not is_subs:
                    try:
                        digit = find_digit_key[0]
                        frend_subs.append((digit, res[0][0] + res[0][2]))
                        is_subs = True
                    except:
                        is_subs = True
                        frend_subs.append(i)

                elif k in ["друзей", "друг", "друзья"]:
                    try:
                        digit = find_digit_key[0]
                        frend_subs.append((digit, res[0][0] + res[0][2]))
                        is_friend = True
                    except:
                        is_friend = True
                        frend_subs.append(i)

                key_idxs.append(i)
                break

    if not key_idxs:
        return None
    elif (
        all_digit and not is_friend
    ) or is_recomended:  # Если много паттернов с числами
        all_digit = max(
            [
                (
                    re.findall(
                        r"\d{1,}[\.]{0,}\d{0,}", str(all_digit[i][0]).replace("з", "3")
                    )[0],
                    all_digit[i][1],
                )
                for i in range(len(all_digit))
            ],
            key=lambda x: x[0],
        )
        return all_digit

    # Если есть друзья и подписчики
    elif is_friend and is_subs and not is_recomended:
        values = frend_subs.copy()
        try:
            values = [v for v in values if isinstance(v, tuple)]

            digit = float(values[0][0]) + float(values[1][0])
            bbox = [
                min([values[0][1][0]] + [values[1][1][0]]),
                min([values[0][1][1]] + [values[1][1][1]]),
                max([values[0][1][2]] + [values[1][1][2]]),
                max([values[0][1][3]] + [values[1][1][3]]),
            ]
            return digit, bbox

        except Exception as e:
            values = []
            for fs in frend_subs:
                # Не нашли число в ключевом слове
                key_nodes = [result[fs]]

                another_idxs = [idx for idx, x in enumerate(result) if x not in [fs]]
                another_nodes = [result[idx] for idx in another_idxs]

                closest_values = []
                closest_distances = []
                closest_bboxes = []

                for node in key_nodes:
                    closet_value, dist, bbox = get_closest_value(
                        node, another_nodes, vk_coef
                    )
                    closest_values.append(closet_value)
                    closest_distances.append(dist)
                    closest_bboxes.append(bbox)
                digit = closest_values[closest_distances.index(min(closest_distances))]
                bbox = closest_bboxes[closest_distances.index(min(closest_distances))]
                if (digit, bbox) not in values:
                    values.append((digit, bbox))

            values = [
                (
                    re.findall(r"\d{1,}[\.]{0,}\d{0,}", str(values[i][0]))[0],
                    values[i][1],
                )
                for i in range(len(values))
            ]

            digit = float(values[0][0]) + float(values[1][0])
            bbox = [
                min([values[0][1][0]] + [values[1][1][0]]),
                min([values[0][1][1]] + [values[1][1][1]]),
                max([values[0][1][2]] + [values[1][1][2]]),
                max([values[0][1][3]] + [values[1][1][3]]),
            ]
            return digit, bbox

    else:
        # Не нашли число в ключевом слове
        key_nodes = [result[idx] for idx in key_idxs]
        another_idxs = [idx for idx, x in enumerate(result) if x not in key_idxs]
        another_nodes = [result[idx] for idx in another_idxs]
        closest_values = []
        closest_distances = []
        closest_bboxes = []

        for node in key_nodes:
            closet_value, dist, bbox = get_closest_value(node, another_nodes, vk_coef)
            closest_values.append(closet_value)
            closest_distances.append(dist)
            closest_bboxes.append(bbox)
        digit = closest_values[closest_distances.index(min(closest_distances))]
        bbox = closest_bboxes[closest_distances.index(min(closest_distances))]
        return digit, bbox
