import time

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


def test_map_form_find(test_time):
    driver.get('https://www.labirint.ru/maps/')
    element_to_click = driver.find_element_by_xpath('//div[@class="delivery-region-popup '
                                                    'delivery-map-wrapper__header-text-inline"][1]')
    click_act = ActionChains(driver).click(element_to_click)
    click_act.perform()
    form = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="change-region-content"]/div[1]')))

    assert 'регион' in form.text


@pytest.mark.parametrize("city", ['Рязань', 'Москва', 'Тюмень', '', 'м', 'Мо', 'аролва поавлп', 'New York', 'askf ajfd fn',
                                  'U4l0G 2 U 0#7', '123'])
def test_map_city_fill(test_time, city):
    element_to_click = driver.find_element_by_xpath('//div[@class="delivery-region-popup '
                                                    'delivery-map-wrapper__header-text-inline"][1]')
    click_act = ActionChains(driver).click(element_to_click)
    click_act.perform()

    find_input = driver.find_element_by_xpath('//form[@id="select-post-form"]/input[1]')
    click_act = ActionChains(driver).click(find_input)
    click_act.perform()

    find_input.send_keys(Keys.CONTROL + "a")
    find_input.send_keys(Keys.DELETE)
    find_input.send_keys(city)
    click_act.perform()
    time.sleep(2)

    find_element = wait.until(
        EC.presence_of_element_located((By.XPATH, '//ul[@id="ui-id-1"]/li[2]')))

    assert city in find_element.text


@pytest.mark.parametrize("place",
                         ['Ясенево', 'Алтуфьево', 'Москва', '', 'м', 'Мо', 'аролва поавлп', 'New York', 'askf ajfd fn',
                          'U4l0G 2 U 0#7', '123'])
def test_map_place_fill(test_time, place):
    city_to_click = driver.find_element_by_xpath('//div[@class="delivery-region-popup '
                                                 'delivery-map-wrapper__header-text-inline"][1]')
    click_act = ActionChains(driver).click(city_to_click)
    click_act.perform()

    find_input = driver.find_element_by_xpath('//form[@id="select-post-form"]/input[1]')
    click_act = ActionChains(driver).click(find_input)
    click_act.perform()

    find_input.send_keys(Keys.CONTROL + "a")
    find_input.send_keys(Keys.DELETE)
    find_input.send_keys('Москва')
    click_act.perform()
    time.sleep(2)

    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="b-region-win-list js-regions-list"]')))

    city_to_click = driver.find_element_by_xpath('//div[@class="b-region-win-list js-regions-list"]/ul/li[1]/a')
    click_act = ActionChains(driver).click(city_to_click)
    click_act.perform()
    time.sleep(2)

    element_to_click = driver.find_element_by_xpath('//div[@class="delivery-search-panel '
                                                    'delivery-block_underline"]/input[1]')

    click_act = ActionChains(driver).click(element_to_click)
    click_act.perform()

    element_to_click.send_keys(Keys.CONTROL + "a")
    element_to_click.send_keys(Keys.DELETE)
    element_to_click.send_keys(place)
    click_act.perform()
    time.sleep(2)

    find_element = wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="delivery-point-info_scrollable"]/div['
                                                  '@class="delivery-point delivery-point_underscored '
                                                  'delivery-point_relative content-default js-delivery-point"][not('
                                                  'contains(@style,"display: none"))][1]/div/div['
                                                  '@class="ml40"]/div/div[1]')))

    assert place in find_element.text


@pytest.fixture(scope='session', autouse=True)
def end():
    yield
    driver.quit()


