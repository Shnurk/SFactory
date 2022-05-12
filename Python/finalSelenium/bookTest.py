import pytest
from datetime import datetime
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


def test_main_book(test_time):
    driver.get('https://www.labirint.ru/books/')
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="genre-name"][1]')))

    assert title.text == 'Книги'


def test_foreign_book(test_time):
    driver.get('https://www.labirint.ru/genres/965/')
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="genre-name"][1]')))

    assert 'Билингвы' in title.text


def test_baby_book(test_time):
    driver.get('https://www.labirint.ru/genres/1850/')
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="genre-name"][1]')))

    assert 'детей' in title.text


def test_comics_book(test_time):
    driver.get('https://www.labirint.ru/genres/2993/')
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="genre-name"][1]')))

    assert 'Манга' in title.text


def test_religion_book(test_time):
    driver.get('https://www.labirint.ru/genres/2386/')
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="genre-name"][1]')))

    assert 'Религия' in title.text


def test_art_book(test_time):
    driver.get('https://www.labirint.ru/genres/1852/')
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="genre-name"][1]')))

    assert 'Художественная' in title.text


@pytest.fixture(scope='session', autouse=True)
def end():
    yield
    driver.quit()

