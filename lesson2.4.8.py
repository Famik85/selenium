from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
       )
    button1 = browser.find_element(By.ID, "book")
    button1.click()



    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)

    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

    time.sleep(10)

finally:
    browser.quit()