# Проект ТопБлог 
<a href="">Команда ИИнтеграция</a>
## Описание кейса
В рамках хакатона "Цифрового прорыва" 2023 в Северо-Западном федеральном округе необходимо было решить "Кейс по сбору аналитических данных блога".

> Проект «ТопБЛОГ» – это конкурс и образовательная программа для блогеров и SMM-специалистов. В рамках конкурсной части проекта заданием для участников является выполнение поставленных KPI за определенный период. Важность решения кейса – автоматизация человеческого труда, что дает повышение уровня эффективности и креативности, а также облегчение труда сотрудников.

>Участникам хакатона предстоит создать программный модуль фотоаналитики по распознаванию необходимых показателей и корректное их распределение в заданную форму (таблицу).

## Подготовка

Перед получением данных по кейсы, наша команда проанализировала большинство возможных сценариев того, что необходимо реализовать и представить заказчику.

В первую очередь необходимо было понять с какими данными нам предстоит работать. Узнав, что проект «ТопБЛОГ» работает со статистикой на различных <a href='https://topblog.rsv.ru/faq'>площадках</a> (ВКонтакте, Одноклассники, Дзен, Telegram, Yappy, RUTUBE или YouTube.) мы предположили что это будут скриншоты статистики у каждого пользователя.
Для распознавания символов решено было использовать <a href="https://cloud.yandex.ru/docs/vision/concepts/ocr/">OCR</a> 

Также наша команда реализовала предварительно интерфейс, чтобы его легче было реализовать во время хакатона.

## Хакатон
Кейсосодержатель представил данные в виде различных форматов `(.png, .jpeg, .jpg, .heic, .pptx, .docx)`. Так как изначально предполагалось, что будут только форматы изображений.


## Решение
Для реализации парсинга данных со скриншота использовалась предобученная модель <a href='https://github.com/JaidedAI/EasyOCR/tree/master'>EasyOCR</a>, которая работает совместно с нашими алгоритмами 