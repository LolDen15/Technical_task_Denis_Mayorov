from YandexPage import Search

def test_yandex_search(browser):
    yandex_page = Search(browser)
    yandex_page.go_to_site()
    assert yandex_page.click_all_services_button() == True
    yandex_page.click_pictures_button()
    yandex_page.switch_window()
    assert yandex_page.get_current_url() == 'https://yandex.ru/images/'
    yandex_page.click_popular_request_list()
    assert yandex_page.get_text_element() == yandex_page.get_text_input()
    yandex_page.click_first_pictures()
    first_link = yandex_page.get_link_image()
    yandex_page.click_next_button()
    assert first_link != yandex_page.get_link_image()
    yandex_page.click_pref_button()
    assert first_link == yandex_page.get_link_image()

