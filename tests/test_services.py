import unittest
import json
from src.services import search_transactions

transactions = [
    {"description": "Покупка кофе в кафе", "category": "Еда", "amount": 100},
    {"description": "Оплата интернета", "category": "Услуги", "amount": 300},
    {"description": "Покупка билетов в кино", "category": "Развлечения", "amount": 500},
]


class TestSearchTransactions(unittest.TestCase):

    def test_search_transactions_found(self):

        query = "кофе"
        expected_result = [{"description": "Покупка кофе в кафе", "category": "Еда", "amount": 100}]
        result = json.loads(search_transactions(query, transactions))
        self.assertEqual(result, expected_result)

    def test_search_transactions_case_insensitive(self):

        query = "КОФЕ"
        expected_result = [{"description": "Покупка кофе в кафе", "category": "Еда", "amount": 100}]
        result = json.loads(search_transactions(query, transactions))
        self.assertEqual(result, expected_result)

    def test_search_transactions_not_found(self):

        query = "груша"
        expected_result = []
        result = json.loads(search_transactions(query, transactions))
        self.assertEqual(result, expected_result)

    def test_search_transactions_multiple_results(self):

        query = "покупка"
        expected_result = [
            {"description": "Покупка кофе в кафе", "category": "Еда", "amount": 100},
            {"description": "Покупка билетов в кино", "category": "Развлечения", "amount": 500},
        ]
        result = json.loads(search_transactions(query, transactions))
        self.assertEqual(result, expected_result)

    def test_search_transactions_json_format(self):

        query = "интернет"
        result = search_transactions(query, transactions)
        self.assertIsInstance(result, str)
        try:
            json.loads(result)
        except ValueError:
            self.fail("Возвращаемый результат не является валидным JSON")
