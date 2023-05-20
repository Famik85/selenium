from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Открыть страницу https://suninjuly.github.io/math.html.
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x.

    # Посчитать математическую функцию от x (код для этого приведён ниже).
    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x_element = x_element.get_attribute('valuex')
    x = x_element
    y = calc(x)
    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)
    # Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    option1.click()

    # Выбрать radiobutton "Robots rule!".
    option1 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    option1.click()

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(20)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # 1