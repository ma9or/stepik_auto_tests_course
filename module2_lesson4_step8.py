from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

browser.execute_script("window.scrollBy(0, 500);")
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
print(button)

btn = browser.find_element(By.ID, "book")
btn.click()

x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
input1.send_keys(y)
print(x)
print(y)

button = browser.find_element(By.ID, "solve")
button.click()


time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()