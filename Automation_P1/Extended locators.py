import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/client/#/auth/login")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter your email address']").send_keys("demo@gmail.com")
driver.find_element(By.ID,"userPassword").send_keys("Hello@1234")
driver.find_element(By.ID,"confirmPassword").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
#driver.find_element(By.XPATH,"//input[@id='login']").click() ERROR IN WEBSITE
time.sleep(2)

