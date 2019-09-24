from selenium import webdriver
import time
link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath("//div/input[@placeholder = 'Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//div/input[@placeholder = 'Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//div/input[@placeholder = 'Input your email']")
    input3.send_keys("blabla@mail.ru")
    input4 = browser.find_element_by_xpath("//div/input[@placeholder = 'Input your phone:']")
    input4.send_keys("+799912345678")
    input5 = browser.find_element_by_xpath("//div/input[@placeholder = 'Input your address:']")
    input5.send_keys("Moskov, arbat 2a")
    button = browser.find_element_by_xpath("//button[@type = 'submit']")
    button.click()
finally:
    time.sleep(50)
    # закрываем браузер после всех манипуляций
   # browser.quit()
