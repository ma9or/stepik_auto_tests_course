import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
button.click()

first_window = browser.window_handles[0]
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)



x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
input1.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

#confirm = browser.switch_to.alert
#confirm.accept()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()