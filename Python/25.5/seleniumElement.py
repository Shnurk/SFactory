import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('C:/Users/Andrew/PycharmProjects/driver/chromedriver.exe')
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)

@pytest.fixture(autouse=True)
def testing():

   # Переходим на страницу авторизации
   driver.get('http://petfriends1.herokuapp.com/login')

   yield

   driver.quit()


def test_show_my_pets():
   # Вводим email
   driver.find_element_by_id('email').send_keys('andy_naso@mail.ru')
   # Вводим пароль
   driver.find_element_by_id('pass').send_keys('EaV3UJjQsKHv4JM')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя

   driver.get('http://petfriends1.herokuapp.com/my_pets')

   v_photo = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@id="all_my_pets"]/table/tbody/tr[1]/th/img')))
   v_age = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@id="all_my_pets"]/table/tbody/tr[1]/td[3]')))
   v_name = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@id="all_my_pets"]/table/tbody/tr[1]/td[1]')))
   v_atype = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="all_my_pets"]/table/tbody/tr[1]/td[2]')))

   photo =driver.find_element_by_xpath('//div[@id="all_my_pets"]/table/tbody/tr[1]/th/img')
   name = driver.find_element_by_xpath('//div[@id="all_my_pets"]/table/tbody/tr[1]/td[1]')
   age = driver.find_element_by_xpath('//div[@id="all_my_pets"]/table/tbody/tr[1]/td[3]')
   atype= driver.find_element_by_xpath('//div[@id="all_my_pets"]/table/tbody/tr[1]/td[2]')

   assert photo.get_attribute('src') == ''
   assert age.text == '9'
   assert name.text == 'Фуфайкин'
   assert atype.text == 'Интернет-зверь'

   assert v_photo.get_attribute('src') == ''
   assert v_age.text == '9'
   assert v_name.text == 'Фуфайкин'
   assert v_atype.text == 'Интернет-зверь'

    # python -m pytest -v seleniumElement.py

