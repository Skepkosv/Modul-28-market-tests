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
    # //*[@id="catalogPopupButton"]
    find_run_button = WebElement(id='catalogPopupButton')

    # "Баллы" ссылка на вэб-элемент
    find_run_btn_1 = WebElement(xpath='//div[1]/a')

    # "Заказы" ссылка на вэб-элемент
    find_run_btn_2 = WebElement(xpath='//div[2]/div/a/span')

    # "Избранное" ссылка на вэб-элемент
    find_run_btn_3 = WebElement(xpath='//div[3]/div[1]/div[3]/div')

    # "Корзина" ссылка на вэб-элемент
    find_run_btn_4 = WebElement(xpath='//div[4]/div/div/a/span')

    # Кнопка вэб-элемента "Москва"
    find_run_btn_5 = WebElement(xpath='//div[1]/button[1]/div[2]')

    # "Яндекс.ру" ссылка на вэб-элемент
    find_run_btn_6 = WebElement(xpath='//div[3]/noindex/div/div/div[1]/div/div/a[1]')

    # "экспресс" cсылка на вэб-элемент
    find_run_btn_7 = WebElement(xpath='//div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]')

    # "одежда" cсылка на вэб-элемент
    find_run_btn_8 = WebElement(xpath='//div[1]/div[1]/div[3]/div[1]/a[1]/span[1]')

    # "дом" cсылка на вэб-элемент
    find_run_btn_9 = WebElement(xpath='//div[4]/div[1]/a[1]/span[1]')

    # "электроника" cсылка на вэб-элемент
    find_run_btn_10 = WebElement(xpath='//div[5]/div[1]/a[1]/span[1]')

    # "бытовая техника" cсылка на вэб-элемент
    find_run_btn_11 = WebElement(xpath='//noindex[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/a[1]')

    # "детям" cсылка на вэб-элемент
    find_run_btn_12 = WebElement(xpath='//div[7]/div[1]/a[1]/span[1]')

    # "спорт" cсылка на вэб-элемент
    find_run_btn_13 = WebElement(xpath='//div[8]/div/a/span')

    # "трансляции" ссылка на вэб-элемент
    find_run_btn_14 = WebElement(xpath='//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]')

    # "продавайте на маркете" ссылка на вэб-элемент
    find_run_btn_15 = WebElement(xpath='//div[2]/div[2]/div[1]/a[1]/span[1]')

    # "одежда и обувь" ссылка на вэб-элемент
    find_run_btn_16 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[1]/a')

    # "спорт и отдых" ссылка на вэб-элемент
    find_run_btn_17 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[2]/a')

    # "детские товары" ссылка на вэб-элемент
    find_run_btn_18 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[3]/a')

    # "электроника" ссылка на вэб-элемент
    find_run_btn_19 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[4]/a')

    # "компьютеры" ссылка на вэб-элемент
    find_run_btn_20 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[5]/a')

    # Наименование товаров в списке
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Кнопка сортировки по цене
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Цена товаров в результате поиска
    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')

    # "как выбрать товар" ссылка на вэб-элемент
    find_run_btn_21 = WebElement(xpath='//noindex/div[3]/div[2]/div[1]/div[1]/a[1]')

    # "оплата и доставка" ссылка на вэб-элемент
    find_run_btn_22 = WebElement(xpath='//div[3]/div[2]/div[1]/div[1]/a[2]')

    # "обратная связь" ссылка на вэб-элемент
    find_run_btn_23 = WebElement(xpath='//div[3]/div[2]/div[1]/div[1]/a[3]')

    # "о сервисе" ссылка на вэб-элемент
    find_run_btn_24 = WebElement(xpath='//div[3]/div[2]/div[1]/div[1]/a[4]')

    # "участие в исследованиях" ссылка на вэб-элемент
    find_run_btn_25 = WebElement(xpath='//noindex/div[3]/div[2]/div[1]/div[1]/a[5]')

    # "возвраты" ссылка на вэб-элемент
    find_run_btn_26 = WebElement(xpath='//div[3]/div[2]/div[1]/div[1]/a[6]')

    # "личный кабинет продавца" ссылка на вэб-элемент
    find_run_btn_27 = WebElement(xpath='//div[3]/div[2]/div[1]/div[2]/a[1]')

    # "новости компании" ссылка на вэб-элемент
    find_run_btn_28 = WebElement(xpath='//div[3]/div[2]/div[1]/div[3]/a[1]')

    # "партнёрская программа" ссылка на вэб-элемент
    find_run_btn_29 = WebElement(xpath='//div[3]/div[2]/div[1]/div[3]/a[2]')

    # "яндекс маркет в facebook" ссылка на вэб-элемент
    find_run_btn_30 = WebElement(xpath='//div[3]/div[2]/div[2]/div[1]/div[2]/a[1]')

    # "яндекс маркет в vk" ссылка на вэб-элемент
    find_run_btn_31 = WebElement(xpath='//div[3]/div[2]/div[2]/div/div[2]/a[2]')

    # "яндекс маркет в instagram" ссылка на вэб-элемент
    find_run_btn_32 = WebElement(xpath='//div[3]/div[2]/div[2]/div/div[2]/a[3]')

    # "войти" ссылка на вэб-элемент
    find_run_btn_33 = WebElement(xpath='//div[5]/div/div/div[1]/a/span')
