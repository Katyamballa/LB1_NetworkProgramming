Вот полный README.md файл в формате Markdown:

# Получение курса валют с сайта НБУ

## Описание проекта
Этот проект представляет собой скрипт на Python, который получает курс валют с сайта Национального банка Украины (НБУ) за определенный период времени. Скрипт использует библиотеку `requests` для отправки HTTP-запросов и обработки полученных данных.

## Функционал
- Отправка GET-запроса к API НБУ.
- Получение данных о курсе валют за указанный период.
- Сохранение результата в файл `exchange_rates.json`.

## Требования
- Python 3.8 и выше.
- Установленная библиотека `requests`.

## Установка и запуск

### 1. Убедитесь, что Python установлен
## На Mac вы можете установить Python через Homebrew:

## brew install python

## Проверьте версию Python:

## python3 --version

### 2. Установите библиотеку requests

## Рекомендуется использовать виртуальную среду:

## Создание виртуальной среды:

## python3 -m venv venv

## Активация виртуальной среды:

## source venv/bin/activate

## Установка библиотеки:

## pip install requests

### 3. Скачайте и запустите скрипт

## Сохраните следующий код в файл currency_rates.py:

import requests
import json

# URL для запроса
url = "https://bank.gov.ua/NBU_Exchange/exchange_site"

# Параметры запроса
params = {
    "start": "20240916",  # Дата начала
    "end": "20240923",    # Дата окончания
    "valcode": "usd",     # Код валюты
    "sort": "exchangedate",
    "order": "desc",
    "json": ""
}

try:
    # Выполнение GET-запроса
    response = requests.get(url, params=params)

    # Проверка статуса
    if response.status_code == 200:
        data = response.json()  # Парсим JSON ответ
        print("Курс валют получен успешно!")

        # Сохранение данных в файл
        with open("exchange_rates.json", "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Результаты сохранены в 'exchange_rates.json'")
    else:
        print(f"Ошибка: {response.status_code}")
except Exception as e:
    print(f"Произошла ошибка: {e}")

## Запустите скрипт:

python3 currency_rates.py

### 4. Проверьте результаты

## После выполнения скрипта будет создан файл exchange_rates.json. Этот файл содержит данные о курсе валют за указанный период.

## Пример JSON-ответа

## Пример данных, которые могут быть получены:

[
    {
        "r030": 840,
        "txt": "Долар США",
        "rate": 36.5686,
        "cc": "USD",
        "exchangedate": "2024-09-23"
    },
    {
        "r030": 978,
        "txt": "Євро",
        "rate": 38.9223,
        "cc": "EUR",
        "exchangedate": "2024-09-23"
    }
]

## Структура проекта
	•	currency_rates.py: Основной скрипт.
	•	exchange_rates.json: Файл с результатами.
	•	README.md: Документация проекта.

## Пример запроса к API

## API НБУ предоставляет курсы валют. Пример запроса:

https://bank.gov.ua/NBU_Exchange/exchange_site?start=20240916&end=20240923&valcode=usd&sort=exchangedate&order=desc&json

## Параметры:
	•	start: начальная дата в формате YYYYMMDD.
	•	end: конечная дата в формате YYYYMMDD.
	•	valcode: код валюты (например, usd, eur).
	•	sort: параметр сортировки (например, exchangedate).
	•	order: порядок сортировки (asc или desc).
	•	json: формат ответа.

## Автор
## Kateryna
## Если у вас есть вопросы, свяжитесь со мной.