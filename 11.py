from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element_by_css_selector("button.trollface.btn.btn-primary").click()
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
    browser.find_element_by_tag_name("button").click()


finally:
    time.sleep(30)
    browser.quit()