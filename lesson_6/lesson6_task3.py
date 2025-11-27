from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get(" https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


element = WebDriverWait(driver,50).until(
    EC.presence_of_element_located((By.XPATH, "//img"))
)
img = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "//img"))
)
src_value = img.get_attribute("scr")
print(src_value)
driver.quit()