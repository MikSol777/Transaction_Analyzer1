import pandas as pd
import os
import datetime
import requests
from dotenv import load_dotenv


def get_greeting(current_time):
    """Функция приветствия в зависимости от времени суток"""
    current_hour = datetime.datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S").hour
    if 5 <= current_hour < 12:
        return "Доброе утро"
    elif 12 <= current_hour < 18:
        return "Добрый день"
    elif 18 <= current_hour < 22:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def process_card(card_number, expenses):
    """Функция обработки информации по карте"""
    if pd.isna(card_number) or card_number is None:
        card_number = "Unknown"

    card_number = str(card_number).strip()

    if len(card_number) >= 4:
        last_4_digits = card_number[-4:]
    else:
        last_4_digits = "Unknown"

    total_expenses = sum(expenses)
    cashback = total_expenses // 100
    return {"last_digits": last_4_digits, "total_spent": round(total_expenses, 2), "cashback": round(cashback, 2)}


def get_top_transactions(transactions):
    """Функция для получения топ-5 транзакций"""
    sorted_transactions = sorted(transactions, key=lambda x: x["Сумма платежа"], reverse=True)
    return [
        {
            "date": tx["Дата платежа"],
            "amount": int(tx["Сумма платежа"]),
            "category": tx["Категория"],
            "description": tx["Описание"],
        }
        for tx in sorted_transactions[:5]
    ]


def get_exchange_rate():
    """Функция для получения курса валют"""
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/latest?base=RUB"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return [
            {"currency": "USD", "rate": round(data["rates"]["USD"], 2)},
            {"currency": "EUR", "rate": round(data["rates"]["EUR"], 2)},
        ]
    else:
        print("Error fetching exchange rates:", response.status_code)
        return []


def get_stock_prices():
    """Функция для получения стоимости акций из S&P500"""
    load_dotenv()
    api_key = os.getenv("API_KEY_ALPHA")
    sp500_tickers = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    stock_prices = []

    for ticker in sp500_tickers:
        url = f"https://www.alphavantage.co/query"
        params = {"function": "TIME_SERIES_INTRADAY", "symbol": ticker, "interval": "1min", "apikey": api_key}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if "Time Series (1min)" in data:
                latest_time = next(iter(data["Time Series (1min)"]))
                latest_data = data["Time Series (1min)"][latest_time]
                price = latest_data["4. close"]
                stock_prices.append({"stock": ticker, "price": float(price)})
            else:
                print(f"Ошибка получения данных для {ticker}")
        else:
            print(f"Ошибка при запросе для {ticker}: {response.status_code}")
    return stock_prices
