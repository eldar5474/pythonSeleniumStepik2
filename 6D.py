from selenium import webdriver
from selenium.webdriver.support.ui import Select


import time
def calc(x, y):
    return str(int(x)+int(y))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    one = browser.find_element_by_id("num1")
    two = browser.find_element_by_id("num2")
   # print (calc(one.text, two.text))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(calc(one.text, two.text))
    browser.find_element_by_css_selector(".btn.btn-default").click()

finally:
    time.sleep(30)
    browser.quit()
