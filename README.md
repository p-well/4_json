# Получение json данных в красивом виде по аналогии с pprint

Принимается неотформатированный json-файл и приводится к более читабельному виду. 

# Как запустить

Запускаем код выполнив в командной строке:

```
python pprint_json.py -p <путь к файлу> , либо
python pprint_json.py --page <путь к файлу>

```
Путь указывается без угловых скобок или кавычек

# Пример вывода

```
[
    {
        "Cells": {
            "OperatingCompany": "Ароматный Мир",
            "global_id": 14371450,
            "TypeService": "реализация продовольственных товаров",
            "District": "район Кунцево",
            "AdmArea": "Западный административный округ",
            "Name": "Ароматный Мир",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "IsNetObject": "да",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "вторник",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "среда",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "четверг",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "пятница",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "суббота",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "воскресенье",
                    "Hours": "09:30-22:30"
                }
            ],
            "ClarificationOfWorkingHours": null,
            "geoData": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "Address": "улица Академика Павлова, дом 10"
        },
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1
    }
]
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
