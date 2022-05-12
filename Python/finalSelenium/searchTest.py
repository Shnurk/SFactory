import pytest
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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


@pytest.mark.parametrize("search",
                         ['Рязань', 'Москва', 'Тюмень', '', 'м', 'Мо', 'аролва поавлп', 'New York', 'askf ajfd fn',
                          'U4l0G 2 U 0#7', '123'])
def test_map_form_find(test_time, search):
    driver.get('https://www.labirint.ru')
    element_to_click = driver.find_element_by_xpath('//form[@id="searchform"]/div/span/input[1]')
    click_act = ActionChains(driver).click(element_to_click)
    click_act.perform()
    element_to_click.send_keys(search)
    element_to_click.send_keys(Keys.ENTER)

    form = wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="index-top-title"]')))

    assert search in form.text


@pytest.fixture(scope='session', autouse=True)
def end():
    yield
    driver.quit()
