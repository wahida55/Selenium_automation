from selenium.webdriver.common.by import By

from checkout_confirmation import Checkout_confirmation


class ShopPage:
    def __init__(self,driver):
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, " a[href*='shop']")
        self.product_cart = (By.XPATH, "//div[@class='card h-100']")
        self.cart_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_to_cart(self,product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cart)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

    def checkout(self):
        self.driver.find_element(*self.cart_button).click()
        checkout_conf = Checkout_confirmation(self.driver)
        return checkout_conf

