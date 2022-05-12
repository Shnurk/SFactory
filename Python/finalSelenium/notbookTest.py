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


def test_main_game(test_time):
    driver.get('https://www.labirint.ru/games/')
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="genre-name"][1]')))

    assert 'Игры' in title.text


def test_main_office(test_time):
    driver.get('https://www.labirint.ru/office/')
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="genre-name"][1]')))

    assert 'Канцелярские' in title.text


def test_main_souvenir(test_time):
    driver.get('https://www.labirint.ru/souvenir/')
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="genre-name"][1]')))

    assert 'Сувениры' in title.text


def test_main_home(test_time):
    driver.get('https://www.labirint.ru/household/')
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="genre-name"][1]')))

    assert 'дома' in title.text


@pytest.fixture(scope='session', autouse=True)
def end():
    yield
    driver.quit()

