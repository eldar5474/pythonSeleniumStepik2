import math
from selenium import webdriver
x = str(math.ceil(math.pow(math.pi, math.e)*10000));
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")
    link = browser.find_element_by_link_text(x).click()

    input1 = browser.find_element_by_name('first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:

    time.sleep(30)
    browser.quit()