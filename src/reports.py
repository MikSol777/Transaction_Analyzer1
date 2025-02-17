import pandas as pd
import logging
from typing import Optional
from datetime import datetime, timedelta
from src.decorators import save_report_to_file


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


@save_report_to_file
def spending_by_weekday(transactions: pd.DataFrame, date: Optional[str] = None) -> pd.DataFrame:
    """Функция возвращает средние траты в каждый из дней недели за последние три месяца (от переданной даты)."""
    if date is None:
        date = datetime.today().strftime("%Y-%m-%d")
    logging.info(f"Используем дату: {date}")
    current_date = datetime.strptime(date, "%Y-%m-%d")
    logging.info(f"Текущая дата: {current_date}")
    three_months_ago = current_date - timedelta(days=90)
    logging.info(f"Дата три месяца назад: {three_months_ago}")
    transactions["date"] = pd.to_datetime(transactions["date"])
    recent_transactions = transactions[transactions["date"] >= three_months_ago]
    logging.info(f"Количество транзакций за последние 3 месяца: {len(recent_transactions)}")
    recent_transactions["weekday"] = recent_transactions["date"].dt.day_name()
    result = recent_transactions.groupby("weekday")["amount"].mean().sort_index()
    result_df = result.reset_index(name="average_spending")
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    result_df["weekday"] = pd.Categorical(result_df["weekday"], categories=days_of_week, ordered=True)
    result_df = result_df.sort_values("weekday").reset_index(drop=True)
    logging.info(f"Средние траты по дням недели:\n{result_df}")

    return result_df
