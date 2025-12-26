from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as  ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#открыть страницу
driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
#нажать на кнопку поле ввода
button = driver.find_element(By.ID, "delay")
button.clear()
button.send_keys(45)
#ввести пример
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()


WebDriverWait(driver, 46).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
)
#сравнить результат
result = driver.find_element(By.CLASS_NAME, "screen").text
assert result =="15", f"Ожидаем результат 15"

print("ok")

driver.quit()