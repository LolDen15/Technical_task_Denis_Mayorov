Требования
Для запуска этого тестового задания вам понадобится следующее:

Python 3
pip (менеджер пакетов для Python)
Следующие пакеты для Python:
selenium
pytest
Вы можете установить необходимые пакеты, выполнив следующую команду:

Copy code
pip install -r requirements.txt

Установить chromedriver в Path переменные среды или в файле conftest.py строка 6.
Прописать путь к chromedriver`y 
driver = webdriver.Chrome(executable_path='Путь к файлу') 
