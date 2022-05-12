import time
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


def test_first_book_page(test_time):
    driver.get('https://www.labirint.ru/')
    first_book = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="product__info-wrapper"][1]/a')))
    title = first_book.get_attribute('title').split()[0]
    click_act = ActionChains(driver).click(first_book)
    click_act.perform()
    h_book = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="product-title"]/h1')))
    price = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="buying-priceold-val"]/span')))
    img = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="product-image"]/img')))

    assert title in h_book.text
    assert price.text != ''
    assert img.get_attribute('src') != ''


def test_top_add_cart_book(test_time):
    driver.get('https://www.labirint.ru/')
    first_book = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="product__info-wrapper"][1]/a')))
    click_act = ActionChains(driver).click(first_book)
    click_act.perform()

    cart_button = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="buying-btns"]/a')))
    click_act = ActionChains(driver).click(cart_button)
    click_act.perform()

    time.sleep(5)

    counter = wait.until(
        EC.presence_of_element_located((By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-cart '
                                                  'basket-in-cart-a"][1]')))

    assert counter.text == '1'


def test_main_add_cart_book(test_time):
    driver.get('https://www.labirint.ru/')
    first_book = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="product__info-wrapper"][1]/a')))
    click_act = ActionChains(driver).click(first_book)
    click_act.perform()

    driver.execute_script("window.scrollTo(0, 400)")

    cart_button = driver.find_element_by_xpath('//a[@id="buyto-buyids"]')
    driver.execute_script(f'window.scrollBy(0, 200);')
    click_act = ActionChains(driver).click(cart_button)
    click_act.perform()
    driver.execute_script(f'window.scrollBy(0, -200);')
    time.sleep(5)

    counter = wait.until(
        EC.presence_of_element_located((By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-cart '
                                                  'basket-in-cart-a"][1]')))

    assert counter.text == '4'



@pytest.fixture(scope='session', autouse=True)
def end():
    yield
    driver.quit()