import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
input1.send_keys(y)
print(x)

print(y)


option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
option2.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
