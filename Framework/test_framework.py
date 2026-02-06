
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Shop import ShopPage
from loginPage import LoginPage


def test_framework(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginpage = LoginPage(driver)
    shoppage = loginpage.login()
    shoppage.add_to_cart("Blackberry")
    checkout_conf = ShopPage.checkout(driver)
    checkout_conf.checkout_and_confirm()
    checkout_conf.delivery_address("ind")
    checkout_conf.validate()


