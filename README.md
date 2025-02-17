# Transaction_Analyzer_1
Курсовая работа 

## Содержание
1. [sky.pro](https://my.sky.pro)
2. Проект находится в стадии разработки.
 
## Реализованные функции
1. **`get_greeting`** - Функция приветствия в зависимости от времени суток
2. **`process_card`** - Функция обработки информации по карте
3. **`get_top_transactions`** - Функция для получения топ-5 транзакций
4. **`get_exchange_rate`** - Функция для получения курса валют
5. **`get_stock_prices`** - Функция для получения стоимости акций из S&P500
6. **`process_transaction`** - Главная функция обработки данных
7. **`spending_by_weekday`** - Функция возвращает средние траты в каждый из дней недели за последние три месяца (от переданной даты)
8. **`search_transactions`** - Ищет транзакции по запросу в описании или категории

## Реализованные декораторы
1. **`save_report_to_file`** -Декоратор для записи отчета в файл 'data/reports.json

## Тесты проекта
Добавлено тестирование функций через pytest.

## Логгеры модулей в проекте
1. **`spending_by_weekday`**


~~~
File        	        function        		 coverage

src\decorators.py	save_report_to_file	          100%
src\decorators.py	save_report_to_file.wrapper	  89%
src\reports.py	        spending_by_weekday		  94%
src\services.py 	search_transactions		  100%
src\views.py    	get_greeting			  100%  
src\views.py	        process_card		          78%
src\views.py	        get_top_transactions		  100%
src\views.py	        get_exchange_rate		  80%
src\views.py	        get_stock_prices		  0%
src\views.py	       Яprocess_transaction		  96%
Total	 						  81%
~~~~


## Инструкция по установке
1. Выполнить клонирование репозитория [BankWidget](https://github.com/MikSol777/progect-bank-wiget) себе на компьютер
2. В терминале, находясь в корневой папке проекта, активировать виртуальное окружение через poetry
3. Выполнить установку пакетов из списка зависимостей в файле _pyproject.toml_.
