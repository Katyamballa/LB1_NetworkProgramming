Получение курса валют с сайта НБУ

Описание проекта
Этот проект представляет собой скрипт на Python, который получает курс валют с сайта Национального банка Украины (НБУ) за определенный период времени. Скрипт использует библиотеку `requests` для отправки HTTP-запросов и обработки полученных данных.


## Установка и запуск

1. Убедитесь, что Python установлен

2. Установите библиотеку requests

3. Скачайте и запустите скрипт

Запустите скрипт:

python3 currency_rates.py

4. Проверьте результаты

После выполнения скрипта будет создан файл exchange_rates.json. Этот файл содержит данные о курсе валют за указанный период.

Пример запроса к API

https://bank.gov.ua/NBU_Exchange/exchange_site?start=20240916&end=20240923&valcode=usd&sort=exchangedate&order=desc&json

Автор
Kateryna
