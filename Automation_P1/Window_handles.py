import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
print(driver.title)
driver.find_element(By.LINK_TEXT,"Click Here").click()
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
print(driver.find_element(By.TAG_NAME,"h3").text)
print(driver.title)
time.sleep(2)