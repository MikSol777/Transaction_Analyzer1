import json
from typing import Callable


def save_report_to_file(func: Callable):
    """Декоратор для записи отчета в файл 'data/reports.json"""

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        filename = "data/reports.json"

        try:
            # Записываем данные в файл, перезаписывая его
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
            print(f"Отчет записан в файл: {filename}")
        except Exception as e:
            print(f"Ошибка при записи отчета в файл: {e}")

        return result

    return wrapper
