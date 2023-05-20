

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

import time

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://www.ukr.net")
time.sleep(5)

login = driver.find_element(By.TAG_NAME, "login")
login.send_keys("famik.85@ukr.net")
time.sleep(5)

pass_find = driver.find_element(By.TAG_NAME, "password")
pass_find.send_keys("famik.pass")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, "button.Ol0-ktls").click()



# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
