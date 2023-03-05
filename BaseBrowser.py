from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseBrowser:

    #Объявление клиента браузера
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://ya.ru/"
        #Неаявное ожидание элемента
        self.driver.implicitly_wait(20)

    #Поиск элемента
    def find_element1(self, locator, time=10):
        #Явное ожидание элемента
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator), message=f"Не получилось найти элемент с локатором: {locator}")

    #Поиск множества элементов
    def find_elements1(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator), message=f"Не получилось найти элемент с локатором: {locator}")

    #Переход на сайт
    def go_to_site(self):
        self.driver.get(self.url)

    #Переключение между окнами в браузере
    def switch_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        self.driver.close()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    #Получить текст элемента
    def get_text_element1(self, locator, time=10):
        text_element = WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator), message=f"Не получилось найти элемент с локатором: {locator}")
        return text_element.text

    #Получить атрибут элемената
    def get_text_attribute(self,locator,attribute,time=10):
        attribute_element = self.driver.find_element(*locator).get_attribute(attribute)
        return attribute_element