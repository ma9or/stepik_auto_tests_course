from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"


browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
x = x_element.text
y_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
y = y_element.text



sum_el = str(int(x) + int(y))

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(value=sum_el)


button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(60)
    # закрываем браузер после всех манипуляций
browser.quit()
