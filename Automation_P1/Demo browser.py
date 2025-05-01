import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
time.sleep(2)