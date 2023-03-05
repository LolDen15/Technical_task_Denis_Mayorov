from YandexPage import Search

def test_yandex_search(browser):
    yandex_page = Search(browser)
    yandex_page.go_to_site()
    yandex_page.enter_word("Тензор")
    assert yandex_page.check_suggest_popup() == True
    yandex_page.click_on_the_search_button()
    assert yandex_page.check_main_content() == True
    assert yandex_page.check_link_tensor() == 'tensor.ru'
