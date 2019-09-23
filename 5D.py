from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    sunduk = browser.find_element_by_id("treasure")
    valuex = sunduk.get_attribute("valuex")
    browser.find_element_by_id("answer").send_keys(calc(valuex))
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector(".btn.btn-default").click()
finally:
    time.sleep(30)
    browser.quit()

