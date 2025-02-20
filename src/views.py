import pandas as pd
import json
import os
from src.utils import get_greeting, get_stock_prices, get_exchange_rate, get_top_transactions, process_card


def process_transaction(file_path, current_time):
    """Главная функция обработки данных"""
    df = pd.read_excel(file_path)

    required_columns = ["Дата операции", "Номер карты", "Сумма операции с округлением", "Категория"]
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Отсутствуют обязательные колонки в файле: {', '.join(required_columns)}")

    transactions = []
    card_expenses = {}

    for _, row in df.iterrows():
        card_number = row["Номер карты"]
        expense = row["Сумма операции с округлением"]
        transaction = {
            "Дата операции": row["Дата операции"],
            "Дата платежа": row["Дата платежа"],
            "Номер карты": card_number,
            "Сумма операции": row["Сумма операции"],
            "Валюта операции": row["Валюта операции"],
            "Сумма платежа": row["Сумма платежа"],
            "Категория": row["Категория"],
            "Описание": row["Описание"],
            "Сумма операции с округлением": row["Сумма операции с округлением"],
        }
        transactions.append(transaction)

        if card_number not in card_expenses:
            card_expenses[card_number] = []
        card_expenses[card_number].append(expense)

    greeting = get_greeting(current_time)
    cards_info = [process_card(card_number, expenses) for card_number, expenses in card_expenses.items()]
    top_transactions = get_top_transactions(transactions)
    exchange_rate = get_exchange_rate()
    sp500_stocks = get_stock_prices()

    response = {
        "greeting": greeting,
        "cards": cards_info,
        "top_transactions": top_transactions,
        "currency_rates": exchange_rate,
        "stock_prices": sp500_stocks,
    }

    output_path = "data/transaction_response.json"
    if not os.path.exists("data"):
        os.makedirs("data")

    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(response, json_file, ensure_ascii=False, indent=4)

    print(f"Данные успешно сохранены в файл {output_path}")
    return json.dumps(response, ensure_ascii=False, indent=4)


# current_time = "2025-02-16 14:30:00"
# file_path = '../data/operations.xlsx'
# json_response = process_transaction(file_path, current_time)
# print(json_response)
