from src.utils import get_greeting, get_exchange_rate, get_top_transactions, process_card
import pytest
from unittest.mock import patch
import pandas as pd



@pytest.fixture
def mock_read_excel():
    mock_df = pd.DataFrame(
        {
            "Дата операции": ["2022-01-01", "2022-01-02"],
            "Номер карты": ["1234", "5678"],
            "Сумма операции с округлением": [100, 200],
            "Категория": ["Food", "Transport"],
            "Дата платежа": ["2022-01-01", "2022-01-02"],
            "Сумма операции": [100, 200],
            "Валюта операции": ["RUB", "USD"],
            "Сумма платежа": [100, 200],
            "Описание": ["Dinner", "Bus ride"],
        }
    )
    with patch("pandas.read_excel", return_value=mock_df):
        yield mock_df


def test_get_greeting():
    assert get_greeting("2023-03-10 08:00:00") == "Доброе утро"
    assert get_greeting("2023-03-10 14:00:00") == "Добрый день"
    assert get_greeting("2023-03-10 19:00:00") == "Добрый вечер"
    assert get_greeting("2023-03-10 23:00:00") == "Доброй ночи"


def test_process_card():
    card_number = "1234567890123456"
    expenses = [100, 200, 50]
    result = process_card(card_number, expenses)
    assert result["last_digits"] == "3456"
    assert result["total_spent"] == 350.00
    assert result["cashback"] == 3.00


def test_get_top_transactions():
    transactions = [
        {"Дата платежа": "2023-01-01", "Сумма платежа": 300, "Категория": "Food", "Описание": "Dinner"},
        {"Дата платежа": "2023-01-02", "Сумма платежа": 500, "Категория": "Transport", "Описание": "Taxi"},
        {"Дата платежа": "2023-01-03", "Сумма платежа": 100, "Категория": "Food", "Описание": "Lunch"},
    ]

    top_transactions = get_top_transactions(transactions)
    assert len(top_transactions) == 3
    assert top_transactions[0]["amount"] == 500


def test_get_exchange_rate():
    mock_data = {"rates": {"USD": 75.0, "EUR": 85.0}, "base": "RUB", "date": "2023-03-10"}

    with patch("requests.get") as mock_get:
        mock_response = patch("requests.Response")
        mock_response.status_code = 200
        mock_response.json = lambda: mock_data
        mock_get.return_value = mock_response

        result = get_exchange_rate()
        assert result == [{"currency": "USD", "rate": 75.0}, {"currency": "EUR", "rate": 85.0}]