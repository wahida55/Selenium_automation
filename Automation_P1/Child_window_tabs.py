#Actions class in selenium helps with the mouse hover functionality
import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.click_and_hold().perform() # long press #perform is mandatory with actions
action.context_click().perform() #Right click
action.double_click().perform() # Double click
action.drag_and_drop().perform() #Drag and drop from source to target

time.sleep(2)