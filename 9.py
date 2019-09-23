from selenium import webdriver
import os
import time
try:
    browser= webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element_by_name("firstname").send_keys("Ivan")
    browser.find_element_by_name("lastname").send_keys("Ivanov")
    browser.find_element_by_name("email").send_keys("blabla@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_css_selector(".btn.btn-primary").click()
finally:
    time.sleep(30)
    browser.quit()