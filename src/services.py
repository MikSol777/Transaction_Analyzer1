import json
import re


def search_transactions(query, transactions):
    """Ищет транзакции по запросу в описании или категории"""
    query_pattern = re.compile(re.escape(query), re.IGNORECASE)
    result = [
        transaction for transaction in transactions
        if query_pattern.search(transaction['description']) or query_pattern.search(transaction['category'])
    ]
    return json.dumps(result, ensure_ascii=False, indent=4)