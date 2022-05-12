import pytest
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.settings import chm_driver

driver = chm_driver
driver.set_window_size(1920, 1080)
wait = WebDriverWait(driver, 10)


@pytest.fixture(scope="function")
def test_time():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f"\nТест шел: {end_time - start_time}")


def test_logo(test_time):
    driver.get('https://www.labirint.ru/')
    logo = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'b-header-b-logo-e-logo-wrap')))

    assert logo.get_attribute('title') == 'Лабиринт - самый большой книжный интернет магазин'


def test_cabinet_a(test_time):
    driver.get('https://www.labirint.ru/cabinet/')
    cabinet = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="js-auth__title new-auth__title"][1]')))
    assert cabinet.text == 'Полный доступ к Лабиринту'


def test_like_a(test_time):
    driver.get('https://www.labirint.ru/cabinet/putorder/')
    likely = wait.until(
        EC.presence_of_element_located((By.ID, 'cabinet')))

    assert "Отложите интересные вам товары" in likely.text


def test_cart_a(test_time):
    driver.get('https://www.labirint.ru/cart/')
    cart = wait.until(
        EC.presence_of_element_located((By.ID, 'ui-id-4')))

    assert cart.text == 'Моя корзина'

def test_fall_menu_book(test_time):
    driver.get('https://www.labirint.ru')

    element_to_hover_over = driver.find_element_by_xpath('//ul[@class="b-header-b-menu-e-list"]/li[1]/span/a')
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    menu = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="header-genres"]/div/ul[@class="b-menu-second-container"]/li[2]/a')))

    assert menu.text == 'Главное 2022'


def test_fall_menu_more(test_time):
    driver.get('https://www.labirint.ru')

    element_to_hover_over = driver.find_element_by_xpath('//li[@data-toggle="header-more"]')
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    menu = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="header-more"]/div/ul['
                                                  '@class="b-menu-second-container"]/li[5]/a')))

    assert menu.text == 'CD/DVD'


def test_fall_menu_club(test_time):
    driver.get('https://www.labirint.ru')

    element_to_hover_over = driver.find_element_by_xpath('//li[@data-toggle="header-club"]')
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    menu = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="header-club"]/div/div/div/div/div/span')))

    assert menu.text == 'Журнал'

@pytest.fixture(scope='session', autouse=True)
def end():
    yield
    driver.quit()
