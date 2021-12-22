import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://market.yandex.ru/'

        super().__init__(web_driver, url)

    # "Искать товары" главное поле //*[@id="header-search"]
    search = WebElement(id='header-search')

    # "Найти" кнопка /html/body/div[2]/div[3]/noindex/div/div/div[2]/div[2]/div/div/form/div/button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # "каталог товаров" кнопка вэб-элемента //*[@id="catalogPopupButton"]
    find_run_button = WebElement(id='catalogPopupButton')

    # "Баллы" ссылка на вэб-элемент /html/body/div[2]/div[3]/noindex/div/div/div[2]/div[3]/div[1]/div[1]/div/div/div[1]/a/button/span/div[2]
    find_run_btn_1 = WebElement(xpath='//a[button/span/div[2]]')

    # "Заказы" ссылка на вэб-элемент /html/body/div[2]/div[3]/noindex/div/div/div[2]/div[3]/div[1]/div[2]/div/a/span/div[2]
    find_run_btn_2 = WebElement(xpath='//a[contains(span/div[2]) and text()="заказы")]')

    # "Избранное" ссылка на вэб-элемент /html/body/div[2]/div[3]/noindex/div/div/div[2]/div[3]/div[1]/div[3]/div/a/span/div[2]
    find_run_btn_3 = WebElement(xpath='//a[contains(span/div[2]) and text()="избранное")]')

    # "Корзина" ссылка на вэб-элемент  /html/body/div[2]/div[3]/noindex/div/div/div[2]/div[3]/div[1]/div[4]/div/div/a/span/div[2]
    find_run_btn_4 = WebElement(xpath='//a[contains(span/div[2]) and text()="корзина")]')

    # Кнопка вэб-элемента "Москва" /html/body/div[2]/div[4]/noindex/div/div/div/div/div[1]/div[1]/div/div/div/div/button
    find_run_btn_5 = WebElement(xpath='//button[@type="Москва"]')

    # "Новый год" ссылка на вэб-элемент /html/body/div[1]/div[4]/noindex/div/div/div/div/div[1]/div[2]/div/a
    find_run_btn_6 = WebElement(xpath='//a[contains(@href, "/special/new-year2022")]')

    # "экспресс" cсылка на вэб-элемент /html/body/div[1]/div[4]/noindex/div/div/div/div/div[1]/div[3]/div/a
    find_run_btn_7 = WebElement(xpath='//a[contains(@href, "/catalog--express/23272130")]')

    # "одежда" cсылка на вэб-элемент /html/body/div[1]/div[4]/noindex/div/div/div/div/div[1]/div[4]/div/a
    find_run_btn_8 = WebElement(xpath='//a[contains(@href, "/catalog--odezda-obuv-i-aksessuary/54432")]')

    # "дом" cсылка на вэб-элемент /html/body/div[1]/div[4]/noindex/div/div/div/div/div[1]/div[5]/div/a
    find_run_btn_9 = WebElement(xpath='//a[contains(@href, "/catalog--tovary-dlia-doma/54422")]')

    # "электроника" cсылка на вэб-элемент /html/body/div[1]/div[4]/noindex/div/div/div/div/div[1]/div[6]/div/a
    find_run_btn_10 = WebElement(xpath='//a[contains(@href, "/catalog--elektronika/54440")]')

    # "бытовая техника" cсылка на вэб-элемент /html/body/div[1]/div[4]/noindex/div/div/div/div/div[1]/div[7]/div/a
    find_run_btn_11 = WebElement(xpath='//a[contains(@href, "/catalog--bytovaia-tekhnika/54419")]')

    # "детям" cсылка на вэб-элемент /html/body/div[1]/div[4]/noindex/div/div/div/div/div[1]/div[8]/div/a
    find_run_btn_12 = WebElement(xpath='//a[contains(@href, "/catalog--tovary-dlia-sporta-i-otdykha/54436")]')

    # "спорт" cсылка на вэб-элемент /html/body/div[1]/div[4]/noindex/div/div/div/div/div[1]/div[9]/div/a
    find_run_btn_13 = WebElement(xpath='//a[contains(@href, "/catalog--detskie-tovary/54421")]')

    # "трансляции" ссылка на вэб-элемент /html/body/div[1]/div[4]/noindex/div/div/div/div/div[2]/div[1]/div/div/div/div/a
    find_run_btn_14 = WebElement(xpath='//a[contains(@href, "/live")]')

    # "продавайте на маркете" ссылка на вэб-элемент
    find_run_btn_15 = WebElement(css_selector='а._3Lwc_')

    # "одежда и обувь" ссылка на вэб-элемент //*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[1]/a
    find_run_btn_16 = WebElement(xpath='//a[contains(@href, "/catalog--odezhda-obuv-i-aksessuary/54432")]')

    # "спорт и отдых" ссылка на вэб-элемент //*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[2]/a
    find_run_btn_17 = WebElement(xpath='//a[contains(@href, "/catalog--tovary-dlia-sporta-i-otdykha/54436")]')

    # "детские товары" ссылка на вэб-элемент //*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[3]/a
    find_run_btn_18 = WebElement(xpath='//a[contains(@href, "/catalog--detskie-tovary/54421")]')

    # "электроника" ссылка на вэб-элемент //*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[4]/a
    find_run_btn_19 = WebElement(xpath='//a[contains(@href, "/catalog--elektronika/54440")]')

    # "компьютеры" ссылка на вэб-элемент //*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[5]/a
    find_run_btn_20 = WebElement(xpath='//a[contains(@href, "/catalog--kompiuternaia-tekhnika/54425")]')

    # Наименование товаров в списке
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Кнопка сортировки по цене
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Цена товаров в результате поиска
    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')

    # "как выбрать товар" ссылка на вэб-элемент /html/body/div[1]/div[7]/div/noindex/div[3]/div[2]/div[1]/div[1]/a[1]
    find_run_btn_21 = WebElement(xpath='//a[1][contains(@href, "/support/market/choice-goods/product-search.html")]')

    # "оплата и доставка" ссылка на вэб-элемент /html/body/div[1]/div[7]/div/noindex/div[3]/div[2]/div[1]/div[1]/a[2]
    find_run_btn_22 = WebElement(xpath='//a[2][contains(@href, "/my/order/conditions")]')

    # "обратная связь" ссылка на вэб-элемент /html/body/div[1]/div[7]/div/noindex/div[3]/div[2]/div[1]/div[1]/a[3]
    find_run_btn_23 = WebElement(xpath='//a[3][contains(@href, "/support/market/troubleshooting/general.html")]')

    # "о сервисе" ссылка на вэб-элемент /html/body/div[1]/div[7]/div/noindex/div[3]/div[2]/div[1]/div[1]/a[4]
    find_run_btn_24 = WebElement(xpath='//a[4][contains(@href, "/about")]')

    # "участие в исследованиях" ссылка на вэб-элемент /html/body/div[1]/div[7]/div/noindex/div[3]/div[2]/div[1]/div[1]/a[5]
    find_run_btn_25 = WebElement(xpath='//a[5][contains(@href, "jobs/usability")]')

    # "возвраты" ссылка на вэб-элемент /html/body/div[1]/div[7]/div/noindex/div[3]/div[2]/div[1]/div[1]/a[6]
    find_run_btn_26 = WebElement(xpath='//a[6][contains(@href, "/support/market/return.html")]')

    # "личный кабинет продавца" ссылка на вэб-элемент /html/body/div[1]/div[7]/div/noindex/div[3]/div[2]/div[1]/div[2]/a[1]
    find_run_btn_27 = WebElement(
        xpath='//a[1][contains(@href, "https://passport.yandex.ru/auth?mode=auth&amp;from=market&amp;retpath=https://partner.market.yandex.ru")]')

    # "новости компании" ссылка на вэб-элемент /html/body/div[1]/div[7]/div/noindex/div[3]/div[2]/div[1]/div[3]/a[1]
    find_run_btn_28 = WebElement(xpath='//a[1][contains(@href, "https://market.yandex.ru/blog")]')

    # "партнёрская программа" ссылка на вэб-элемент /html/body/div[1]/div[7]/div/noindex/div[3]/div[2]/div[1]/div[3]/a[2]
    find_run_btn_29 = WebElement(xpath='//a[2][contains(@href, "https://aff.market.yandex.ru")]')

    # "яндекс маркет в facebook" ссылка на вэб-элемент /html/body/div[1]/div[7]/div/noindex/div[3]/div[2]/div[2]/div/div[2]/a[1]
    find_run_btn_30 = WebElement(xpath='//a[1][contains(@href, "https://www.facebook.com/yandex.market/")]')

    # "яндекс маркет в vk" ссылка на вэб-элемент /html/body/div[1]/div[7]/div/noindex/div[3]/div[2]/div[2]/div/div[2]/a[2]
    find_run_btn_31 = WebElement(xpath='//a[2][contains(@href, "https://vk.com/yandex.market")]')

    # "яндекс маркет в instagram" ссылка на вэб-элемент /html/body/div[1]/div[7]/div/noindex/div[3]/div[2]/div[2]/div/div[2]/a[3]
    find_run_btn_32 = WebElement(xpath='//a[3][contains(@href, "https://www.instagram.com/yandex.market/")]')

    # "войти" ссылка на вэб-элемент <span class="_1qOET">Войти</span>
    find_run_btn_33 = WebElement(css_selector='_1qOET')
