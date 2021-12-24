# Команда для запуска автоматических тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path C:\Users\Skepk\Downloads\chromedriver.exe tests\tests_yanmark.py

import pytest
from pages.yandmarket import MainPage

def test_open_catalog(web_browser):
    page = MainPage(web_browser)
    page.find_run_button = 'каталог товаров'
    page.find_run_button.click()
    assert page.open_new_page == page.open_catalog

def test_open_scores(web_browser):
    page = MainPage(web_browser)
    page.find = 'баллы'
    page.find_run_btn.click()
    assert page.open_new_page == page.open_scores

def test_open_orders(web_browser):
    page = MainPage(web_browser)
    page.find = 'заказы'
    page.find_run_btn.click()
    assert page.open_new_page == page.open_orders

def test_open_favorites(web_browser):
    page = MainPage(web_browser)
    page.find = 'избранное'
    page.find_run_btn.click()
    assert page.open_new_page == page.open_favorites

def test_open_basket(web_browser):
    page = MainPage(web_browser)
    page.find = 'корзина'
    page.find_run_btn.click()
    assert page.open_new_page == page.open_basket

def test_open_Moscow(web_browser):
    page = MainPage(web_browser)
    page.find = 'Mocква'
    page.find_run_btn.click()
    assert page.open_new_page == page.open_map

def test_open_new_year2022(web_browser):
    page = MainPage(web_browser)
    page.find = 'новый год'
    page.find_run_btn_6.click()
    assert page.open_new_page == page.open_new_year2022

def test_open_express(web_browser):
    page = MainPage(web_browser)
    page.find = 'экспресс'
    page.find_run_btn_7.click()
    assert page.open_new_page == page.open_express_page

def test_open_odezda(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'одежда'
    page.find_run_btn_8.click()
    assert page.open_new_page == page.open_odezda

def test_open_tovary_dlia_doma(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'дом'
    page.find_run_btn_9.click()
    assert page.open_new_page == page.open_tovary_dlia_doma

def test_open_elektronika(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'электроника'
    page.find_run_btn_10.click()
    assert page.open_new_page == page.open_elektronika

def test_open_bytovaia_tekhnika(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'бытовая техника'
    page.find_run_btn_11.click()
    assert page.open_new_page == page.open_bytovaia_tekhnika

def test_open_tovary_dlia_doma(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'товары для дома'
    page.find_run_btn_9.click()
    assert page.open_new_page == page.open_tovary_dlia_doma

def test_open_children(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'дeтям'
    page.find_run_btn_12.click()
    assert page.open_new_page == page.open_children

def test_open_sport(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'спорт'
    page.find_run_btn_13.click()
    assert page.open_new_page == page.open_sport

def test_open_broadcasts(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'трансляции'
    page.find_run_btn_14.click()
    assert page.open_new_page == page.open_broadcasts-page

def test_open_sell_on_the_market(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'продавайте на маркете'
    page.find_run_btn_15.click()
    assert page.open_new_page == page.open_sell_on_the_market

def test_check_main_search_rus(web_browser):
    """ Make sure main search works fine. """
    page = MainPage(web_browser)
    page.search = 'playstation 5'
    page.search_run_button.click()
    # Verify that user can see the list of products:
    assert page.products_titles.count() >= 1
    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'playstation 5' in title.lower(), msg

def test_check_wrong_input_in_search0(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """
    page = MainPage(web_browser)
    # Try to enter "плэйстэйшн5" with Russian keyboard:
    page.search = 'здфн ыефешщт 5'
    page.search_run_button.click()
    # Verify that user can see the list of products:
    assert page.products_titles.count() >= 1
    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'playstation 5' in title.lower(), msg

def test_check_main_search_eng(web_browser):
    """ Make sure main search works fine. """
    page = MainPage(web_browser)
    page.search = 'playstation 5'
    page.search_run_button.click()
    # Verify that user can see the list of products:
    assert page.products_titles.count() >= 1
    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'playstation 5' in title.lower(), msg

def test_check_wrong_input_in_search1(web_browser):
    page = MainPage(web_browser)
    page.search = 'здфн ыефешщт 5'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'playstation 5' in title.lower(), msg

@pytest.mark.xfail(reason="Filter by price doesn't work")
def test_check_sort_by_price(web_browser):
    """ Make sure that sort by price works fine.
        Note: this test case will fail because there is a bug in
              sorting products by price.
    """
    page = MainPage(web_browser)
    page.search = 'стойка Onkron'
    page.search_run_button.click()
    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    # Get prices of the products in Search results
    all_prices = page.products_prices.get_text()
    # Convert all prices from strings to numbers
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices), "Сортировка по цене не работает!"


def test_check_sort_by_price(web_browser):
    page = MainPage(web_browser)
    page.search = 'сковорода'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"

def test_main_search_natural_spruse(web_browser):
    page = MainPage(web_browser)
    page.search = 'санки'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'санки' in title.lower(), msg

def test_open_odezhda_obuv_i_aksessuary(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'одежда и обувь'
    page.find_run_btn_16.click()
    assert page.open_new_page == page.open_odezhda_obuv_i_aksessuary

def test_open_tovary_dlia_sporta_i_otdykha(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'спорт и отдых'
    page.find_run_btn_17.click()
    assert page.open_new_page == page.open_tovary_dlia_sporta_i_otdykha

def test_open_detskie_tovary(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'детские товары'
    page.find_run_btn_18.click()
    assert page.open_new_page == page.open_detskie_tovary

def test_open_elektronika(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'электроника'
    page.find_run_btn_19.click()
    assert page.open_new_page == page.open_elektronika

def test_open_kompiuternaia_tekhnika(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'компьютеры'
    page.find_run_btn_20.click()
    assert page.open_new_page == page.open_kompiuternaia_tekhnika

def test_open_choice_goods(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'как выбрать товар'
    page.find_run_btn_21.click()
    assert page.open_new_page == page.open_choice_goods

def test_open_conditions(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'оплата и доставка'
    page.find_run_btn_22.click()
    assert page.open_new_page == page.open_conditions

def test_open_troubleshooting(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'обратная связь'
    page.find_run_btn_23.click()
    assert page.open_new_page == page.open_troubleshooting

def test_open_about(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'о сервисе'
    page.find_run_btn_24.click()
    assert page.open_new_page == page.open_about

def test_open_jobs_pages_usability(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'участие в исследованиях'
    page.find_run_btn_25.click()
    assert page.open_new_page == page.open_jobs_pages_usability

def test_open_return(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'возвраты'
    page.find_run_btn_26.click()
    assert page.open_new_page == page.open_return

def test_open_partner(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'личный кабинет продавца'
    page.find_run_btn_27.click()
    assert page.open_new_page == page.open_partner

def test_open_blog(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'новости компании'
    page.find_run_btn_28.click()
    assert page.open_new_page == page.open_blog

def test_open_marketaff(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'партнёрская программа'
    page.find_run_btn_29.click()
    assert page.open_new_page == page.open_marketaff

def test_open_yandex_market_in_facebook(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'яндекс маркет в facebook'
    page.find_run_btn_30.click()
    assert page.open_new_page == page.open_yandex_market_in_facebook

def test_open_yandex_market_in_vk(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'яндекс маркет в vk'
    page.find_run_btn_31.click()
    assert page.open_new_page == page.open_yandex_market_in_vk

def test_open_yandex_market_in_instagram(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'яндекс маркет в instagram'
    page.find_run_btn_32.click()
    assert page.open_new_page == page.open_yandex_market_in_instagram

def test_open_auth(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'войти'
    page.find_run_btn_33.click()
    assert page.open_new_page == page.open_auth

def test_check_sort_by_price(web_browser):
    page = MainPage(web_browser)
    page.search = 'лыжи'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"

def test_main_search_natural_spruse(web_browser):
    page = MainPage(web_browser)
    page.search = 'коньки'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'санки' in title.lower(), msg

def test_check_sort_by_price(web_browser):
    page = MainPage(web_browser)
    page.search = 'фен'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"

def test_main_search_natural_spruse(web_browser):
    page = MainPage(web_browser)
    page.search = 'мыло'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'санки' in title.lower(), msg

def test_check_sort_by_price(web_browser):
    page = MainPage(web_browser)
    page.search = 'дрель'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"

def test_main_search_natural_spruse(web_browser):
    page = MainPage(web_browser)
    page.search = 'кострюля'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'санки' in title.lower(), msg

def test_check_sort_by_price(web_browser):
    page = MainPage(web_browser)
    page.search = 'стол'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"

def test_main_search_natural_spruse(web_browser):
    page = MainPage(web_browser)
    page.search = 'стул'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'санки' in title.lower(), msg

def test_check_sort_by_price(web_browser):
    page = MainPage(web_browser)
    page.search = 'кровать'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"

def test_main_search_natural_spruse(web_browser):
    page = MainPage(web_browser)
    page.search = 'подушка'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'санки' in title.lower(), msg

def test_check_sort_by_price(web_browser):
    page = MainPage(web_browser)
    page.search = 'одеяло'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"

def test_main_search_natural_spruse(web_browser):
    page = MainPage(web_browser)
    page.search = 'наволочка'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'санки' in title.lower(), msg
def test_check_sort_by_price(web_browser):
    page = MainPage(web_browser)
    page.search = 'пододеяльник'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"

def test_main_search_natural_spruse(web_browser):
    page = MainPage(web_browser)
    page.search = 'телевизор'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'санки' in title.lower(), msg
