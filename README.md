# Modul-28-market-tests
Финальное тестовое задание для студентов курса.
Написание автоматизированных тестов с использованием PyTest и Selenium для интернет-магазина, в котором есть большое количество товаров, а также функционал поиска и сортировки / фильтрации товаров.

В задании представлен:

Тестовый дизайн — разнообразие и важность проверяемых сценариев.

Качество кода — использование PageObject, параметризации тестов, качество локаторов для элементов, следование стилю PEP8 (запуск инструмента pylint, чтобы увидеть, где стоит изменить свой код, чтобы он соответствовал PEP8).

Описание, что именно проверяют данные тестовые сценарии и какие команды необходимо выполнить для запуска тестов (описанные команды должны работать на любом компьютере с установленным Python3 + PyTest).


Описание: 

Запуск тестов:
Установка библиотек из requirements.txt "при открытии файла .txt всплывает подсказка 'установить', согласиться с ней" 
или запустить в терминале команду pip install -r requirements.txt



https://chromedriver.chromium.org/downloads - скачать версию Selenium WebDriver, совместимую с вашим браузером (тесты проводились в браузере Chrome)

В приведенном примере полная команда для запуска тестов:

python -m pytest -v --driver Chrome --driver-path C:\Users\Skepk\Downloads\chromedriver.exe tests\tests_yanmark.py

Тесты проверяют открытие основных разделов сайта интернет-магазина, поиск различных категорий товаров в различных вариациях.
