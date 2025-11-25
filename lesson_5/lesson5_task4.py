from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
un = "input[name='username']"
search_input = driver.find_element(By.CSS_SELECTOR, un)
search_input.send_keys("tomsmith")


pw = "input[id='password']"
search_input = driver.find_element(By.CSS_SELECTOR, pw)
search_input.send_keys("SuperSecretPassword!")
sleep(2)


log = "button.radius"
push_log = driver.find_element(By.CSS_SELECTOR, log)
push_log.click()


flash_element = driver.find_element(By.CSS_SELECTOR, "div#flash.flash.success")
print(flash_element.text)
sleep(5)
driver.quit()

