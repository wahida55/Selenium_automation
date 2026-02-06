from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_confirmation:
    def __init__(self,driver):
        self.driver = driver
        self.chck_btn = (By.XPATH, "//button[@class='btn btn-success']")
        self.address = (By.ID, "country")
        self.enterred_address = (By.LINK_TEXT, "India")
        self.submit = (By.CSS_SELECTOR, "[type='submit']")
        self.confirm = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.validate = (By.CLASS_NAME, "alert-success")


    def checkout_and_confirm(self):
        self.driver.find_element(*self.chck_btn).click()


    def delivery_address(self,country_name):
        self.driver.find_element(*self.address).send_keys(country_name)
        wait = WebDriverWait(*self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((self.enterred_address)))
        self.driver.find_element(*self.enterred_address).click()
        self.driver.find_element(*self.confirm).click()
        self.driver.find_element(* self.submit).click()

    def validate(self):
        successText = self.driver.find_element(*self.validate).text
        assert "Success! Thank you!" in successText
