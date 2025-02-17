import pandas as pd
from src.reports import spending_by_weekday

transactions_data = [
    {"date": "2025-02-17", "amount": 100},
    {"date": "2025-02-16", "amount": 50},
    {"date": "2025-01-20", "amount": 200},
    {"date": "2025-01-10", "amount": 150},
    {"date": "2024-11-15", "amount": 80},
    {"date": "2024-11-05", "amount": 120}
]

transactions_df = pd.DataFrame(transactions_data)

def test_spending_by_weekday():
    result = spending_by_weekday(transactions_df, '2025-02-17')
    assert result.shape == (3, 2)
    assert result['average_spending'].isnull().sum() == 0
    assert 'weekday' in result.columns
    assert 'average_spending' in result.columns