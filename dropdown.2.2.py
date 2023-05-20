from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(z):
    return str(int(x) + int(y))


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    y = y_element.text
    z = (int(x) + int(y))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(calc(z))

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(15)

finally:
    browser.quit()
