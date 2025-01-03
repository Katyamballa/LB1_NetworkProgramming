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