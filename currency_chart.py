import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def fetch_exchange_rates(start_date, end_date, currency_code="USD"):
    """Получить данные о курсах валют."""
    url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode={currency_code}&sort=exchangedate&order=asc&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка при получении данных:", response.status_code)
        return []

def plot_exchange_rates(data):
    """Построить график изменения курса валют."""
    dates = [datetime.strptime(item["exchangedate"], "%d.%m.%Y") for item in data]
    rates = [item["rate"] for item in data]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, rates, marker='o', linestyle='-', label="Курс валют")
    plt.title("Изменение курса валют", fontsize=16)
    plt.xlabel("Дата", fontsize=14)
    plt.ylabel("Курс (грн)", fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Укажите диапазон дат
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    start_date_str = start_date.strftime("%Y%m%d")
    end_date_str = end_date.strftime("%Y%m%d")

    # Загрузка данных
    currency_code = input("Введите код валюты (например, USD): ").strip().upper()
    exchange_data = fetch_exchange_rates(start_date_str, end_date_str, currency_code)

    if exchange_data:
        # Построение графика
        plot_exchange_rates(exchange_data)
    else:
        print("Нет данных для построения графика.")