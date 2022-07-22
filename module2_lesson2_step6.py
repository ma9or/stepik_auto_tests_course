import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = " http://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = x_element.text
y = calc(x)
browser.execute_script("window.scrollBy(0, 100);")
input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
input1.send_keys(y)
print(x)

print(y)


option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
option2.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
