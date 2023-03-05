from BaseBrowser import BaseBrowser
from selenium.webdriver.common.by import By
import logging
import datetime

class YandexSeacrhLocators:
    #Локаторы для первого задания
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search3__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_SUGGEST_POPUP = (By.CLASS_NAME, 'mini-suggest__popup-content' )
    LOCATOR_YANDEX_PAGE_CONTENT = (By.CLASS_NAME, 'main__content' )
    LOCATOR_YANDEX_PATH_ITEM = (By.CLASS_NAME, 'path__item' )
    # Локаторы для второго задания
    LOCATOR_YANDEX_ALL_SERVICES = (By.CSS_SELECTOR, 'a.services-pinned__all')
    LOCATOR_YANDEX_PICTURES = (By.CSS_SELECTOR, "a[aria-label='Картинки']")
    LOCATOR_YANDEX_POPULAR_REQUEST = (By.CLASS_NAME, "PopularRequestList-SearchText")
    LOCATOR_YANDEX_SUGGEST_INPUT = (By.CLASS_NAME, 'mini-suggest__input')
    LOCATOR_YANDEX_SERP_ITEM_POS_0 = (By.CLASS_NAME, 'serp-item_pos_0')
    LOCATOR_YANDEX_IMAGE_ORIGIN = (By.CLASS_NAME, 'MMImage-Origin')
    LOCATOR_YANDEX_BUTTON_PREV = (By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonPrev')
    LOCATOR_YANDEX_BUTTON_NEXT = (By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonNext')

class Search(BaseBrowser):
    logging.basicConfig(filename='LogInfo.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.FileHandler('LogInfo.log'))
    data = datetime.datetime.now()

    def enter_word(self, word):
        search_field = self.find_element1(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        self.find_element1(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON).click()

    def check_main_content(self):
        return self.find_element1(YandexSeacrhLocators.LOCATOR_YANDEX_PAGE_CONTENT) != None

    def check_suggest_popup(self):
        return self.find_element1(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST_POPUP) != None

    def check_path_item(self):
        list_main_content = self.find_elements1(YandexSeacrhLocators.LOCATOR_YANDEX_PATH_ITEM)
        main_content = [i.text for i in list_main_content if len(i.text) > 0]
        return main_content

    def click_all_services_button(self):
        self.find_element1(YandexSeacrhLocators.LOCATOR_YANDEX_ALL_SERVICES).click()
        self.logger.info(f'Нажали на кнопку все сервисы  - {self.data}')
        return True

    def click_pictures_button(self):
        self.find_element1(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURES).click()
        self.logger.info(f'Нажали кнопку картинки из всех сервисов - {self.data}')

    def click_popular_request_list(self):
        self.find_element1(YandexSeacrhLocators.LOCATOR_YANDEX_POPULAR_REQUEST).click()
        self.logger.info(f'Нажали на популярные картинки - {self.data}')

    def get_text_element(self):
        text_element = self.get_text_element1(YandexSeacrhLocators.LOCATOR_YANDEX_POPULAR_REQUEST)
        self.logger.info(f'Получили текста элемента - {self.data}')
        return text_element

    def get_text_input(self):
        text_input = self.get_text_attribute(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST_INPUT, 'value')
        self.logger.info(f'Получили текст из поиска - {self.data}')
        return text_input

    def click_first_pictures(self):
        self.find_element1(YandexSeacrhLocators.LOCATOR_YANDEX_SERP_ITEM_POS_0).click()
        self.logger.info(f'Нажали на первую картинку из поиска - {self.data}')

    def get_link_image(self):
        link_image = self.get_text_attribute(YandexSeacrhLocators.LOCATOR_YANDEX_IMAGE_ORIGIN, 'src')
        self.logger.info(f'Получили ссылку на картинку - {self.data}')
        return link_image

    def click_pref_button(self):
        self.find_element1(YandexSeacrhLocators.LOCATOR_YANDEX_BUTTON_PREV).click()
        self.logger.info(f'Нажали на кнопку вернуться назад - {self.data}')

    def click_next_button(self):
        self.find_element1(YandexSeacrhLocators.LOCATOR_YANDEX_BUTTON_NEXT).click()
        self.logger.info(f'Получили тектс элемента - {self.data}')

    def get_current_url(self):
        return self.driver.current_url