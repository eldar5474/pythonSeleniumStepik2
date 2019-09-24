import unittest
from selenium import webdriver
link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
class TestUnit(unittest.TestCase):
    def test_registration1(self):
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
        self.assertEqual("Congratulations! You have successfully registered!", browser.find_element_by_xpath("//h1").text)
        browser.quit()
    def test_registration2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
        input1 = browser.find_element_by_xpath('/html/body/div/form/div/input[@name = "first_name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath('/html/body/div/form/div/input[@name = "last_name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath('/html/body/div/form/div/input[@name = "firstname"]')
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_xpath('/html/body/div/form/div/input[@id = "country"]')
        input4.send_keys("Russia")
        button = browser.find_element_by_xpath('/html/body/div/form/div[6]/button[3]')
        button.click()
        browser.quit()

if __name__ == "__main__":
    unittest.main()