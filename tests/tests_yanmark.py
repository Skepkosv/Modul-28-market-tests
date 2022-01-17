# Команда для запуска автоматических тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path C:\Users\Skepk\Downloads\chromedriver.exe tests\tests_yanmark.py

import pytest
from pages.yandmarket import MainPage

def test_open_catalog(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    assert page.find_run_button

def test_open_scores(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_1.click()
    assert page.find_run_btn_1

def test_open_orders(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_2.click()
    assert page.find_run_btn_2

def test_open_favorites(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_3.click()
    assert page.find_run_btn_3

def test_open_basket(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_4.click()
    assert page.find_run_btn_4

def test_open_Moscow(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_5.click()
    assert page.find_run_btn_5

def test_open_yandex(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_6.click()
    assert page.find_run_btn_6

def test_open_express(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_7.click()
    assert page.find_run_btn_7

def test_open_odezda(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_8.click()
    assert page.find_run_btn_8

def test_open_tovary_dlia_doma(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_9.click()
    assert page.find_run_btn_9

def test_open_elektronika(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_10.click()
    assert page.find_run_btn_10

def test_open_bytovaia_tekhnika(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_11.click()
    assert page.find_run_btn_11

def test_open_tovary_dlia_doma1(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_9.click()
    assert page.find_run_btn_9

def test_open_children(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_12.click()
    assert page.find_run_btn_12

def test_open_stroika(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_13.click()
    assert page.find_run_btn_13

def test_open_broadcasts(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_14.click()
    assert page.find_run_btn_14

def test_open_sell_on_the_market(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_15.click()
    assert page.find_run_btn_15

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
def test_check_sort_by_price10(web_browser):
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


def test_check_sort_by_price9(web_browser):
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

def test_main_search_natural_spruse8(web_browser):
    page = MainPage(web_browser)
    page.search = 'санки'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'санки' in title.lower(), msg

def test_check_sort_by_price8(web_browser):
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

def test_main_search_natural_spruse7(web_browser):
    page = MainPage(web_browser)
    page.search = 'коньки'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'коньки' in title.lower(), msg

def test_check_sort_by_price7(web_browser):
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

def test_main_search_natural_spruse6(web_browser):
    page = MainPage(web_browser)
    page.search = 'мыло'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'мыло' in title.lower(), msg

def test_check_sort_by_price6(web_browser):
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

def test_main_search_natural_spruse5(web_browser):
    page = MainPage(web_browser)
    page.search = 'кастрюля'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'кастрюля' in title.lower(), msg

def test_check_sort_by_price5(web_browser):
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

def test_main_search_natural_spruse4(web_browser):
    page = MainPage(web_browser)
    page.search = 'табурет nika эконом 2 (тэ2), металл/искусственная кожа, цвет: слоновая кость'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'табурет nika эконом 2 (тэ2), металл/искусственная кожа, цвет: слоновая кость' in title.lower(), msg

def test_check_sort_by_price4(web_browser):
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

def test_main_search_natural_spruse3(web_browser):
    page = MainPage(web_browser)
    page.search = 'подушка'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'подушка' in title.lower(), msg

def test_check_sort_by_price1(web_browser):
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

def test_main_search_natural_spruses1(web_browser):
    page = MainPage(web_browser)
    page.search = 'наволочка'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'наволочка' in title.lower(), msg

def test_check_sort_by_price2(web_browser):
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

def test_main_search_natural_spruse2(web_browser):
    page = MainPage(web_browser)
    page.search = 'телевизор'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'телевизор' in title.lower(), msg

def test_open_odezhda_obuv_i_aksessuary(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_16.click()
    assert page.find_run_btn_16

def test_open_tovary_dlia_sporta_i_otdykha(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_17.click()
    assert page.find_run_btn_17

def test_open_detskie_tovary(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_18.click()
    assert page.find_run_btn_18

def test_open_elektroniks(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_19.click()
    assert page.find_run_btn_19

def test_open_kompiuternaia_tekhnika(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_20.click()
    assert page.find_run_btn_20

def test_open_choice_goods(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_21.click()
    assert page.find_run_btn_21

def test_open_conditions(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_22.click()
    assert page.find_run_btn_22

def test_open_troubleshooting(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_23.click()
    assert page.find_run_btn_23

def test_open_about(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_24.click()
    assert page.find_run_btn_24

def test_open_jobs_pages_usability(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_25.click()
    assert page.find_run_btn_25

def test_open_return(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_26.click()
    assert page.find_run_btn_26

def test_open_partner(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_27.click()
    assert page.find_run_btn_27

def test_open_blog(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_28.click()
    assert page.find_run_btn_28

def test_open_marketaff(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_29.click()
    assert page.find_run_btn_29

def test_open_yandex_market_in_facebook(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_30.click()
    assert page.find_run_btn_30

def test_open_yandex_market_in_vk(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_31.click()
    assert page.find_run_btn_31

def test_open_yandex_market_in_instagram(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_32.click()
    assert page.find_run_btn_32

def test_open_auth(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_33.click()
    assert page.find_run_btn_33

def test_prodyktu(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_34.click()
    assert page.find_run_btn_34

def test_krasota(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_35.click()
    assert page.find_run_btn_35
