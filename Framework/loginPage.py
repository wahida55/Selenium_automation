from selenium.webdriver.common.by import By

from Shop import ShopPage


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.username_password = (By.ID, "password")
        self.sign_in = (By.ID, "signInBtn")
    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.username_password).send_keys("Learning@830$3mK2")
        self.driver.find_element(*self.sign_in).click()
        shoppage = ShopPage(self.driver)
        return shoppage
