from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    y = browser.find_element_by_id("input_value")
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(y.text))
    browser.find_element_by_css_selector("label[for='robotCheckbox']").click()
    browser.find_element_by_css_selector("label[for='robotsRule']").click()
    browser.find_element_by_css_selector("button.btn.btn-default").click()

finally:
    time.sleep(30)
    browser.quit()