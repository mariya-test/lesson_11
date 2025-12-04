from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get(" https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
)

third_image = driver.find_element(By.ID, "award")
src_value = third_image.get_attribute("src")
print(src_value)
driver.quit()
