from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as  ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

button = driver.find_element(By.ID, "delay")
button.clear()
button.send_keys(45)
sleep(2)

driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()


WebDriverWait(driver, 46).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
)

result = result_screen
assert result =="15", f"Ожидаем результат 15"

print("ok")

driver.quit()