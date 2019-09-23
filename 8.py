import time
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
   # x = browser.find_element_by_id("input_value")
    browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
    browser.execute_script("return arguments[0].scrollIntoView(true);",browser.find_element_by_css_selector(".btn.btn-primary"))
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    browser.find_element_by_css_selector(".btn.btn-primary").click()



finally:
  #  browser.quit()
    time.sleep(30)