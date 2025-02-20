import pytest
import json
from unittest.mock import patch
import pandas as pd
from src.views import process_transaction


def test_process_transaction(mock_read_excel):
    file_path = "fake_path.xlsx"
    current_time = "2023-03-10 15:00:00"

    with patch("src.views.get_exchange_rate", return_value=[{"currency": "USD", "rate": 75.0}]), patch(
        "src.views.get_stock_prices", return_value=[{"stock": "AAPL", "price": 145.3}]
    ):
        result = process_transaction(file_path, current_time)

        result_obj = json.loads(result)
        assert "greeting" in result_obj
        assert "cards" in result_obj
        assert "top_transactions" in result_obj
        assert "currency_rates" in result_obj
        assert "stock_prices" in result_obj


def test_missing_columns():
    mock_df = pd.DataFrame(
        {
            "Дата операции": ["2022-01-01"],
            "Номер карты": ["1234"],
            "Сумма операции с округлением": [100],
        }
    )
    with patch("pandas.read_excel", return_value=mock_df):
        with pytest.raises(
            ValueError,
            match="Отсутствуют обязательные колонки в файле: Дата операции, Номер карты, Сумма операции с округлением, Категория",
        ):
            file_path = "fake_path.xlsx"
            current_time = "2023-03-10 15:00:00"
            process_transaction(file_path, current_time)
