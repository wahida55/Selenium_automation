import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"email").send_keys("wahida55@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.CLASS_NAME,"form-check-input").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
msg=driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
assert "success" in msg
time.sleep(2)