import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(6) #global timeout
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class = 'products']/div")
count = len(results)
actual_list=[]
assert count > 0
for result in results :
     result.find_element(By.XPATH,"div/button").click()
     actual_list.append(result.find_element(By.XPATH,"h4").text)
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
driver.find_element(By.XPATH,"//div[@class='action-block']/button").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//div[@class='promoWrapper']/button").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
promo = driver.find_element(By.CLASS_NAME,"promoInfo").text
assert promo == "Code applied ..!"

#Sum validation
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for price in prices:
     sum = sum+ int(price.text)
print(sum)
totAmt = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == totAmt

dis_amt = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert dis_amt < sum

#Product validation
expected_list =["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]

assert expected_list == actual_list









