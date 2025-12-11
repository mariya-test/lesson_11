from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.service import Service as  EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
WebDriverWait(driver,5).until(
     EC.presence_of_element_located((By.ID, "user-name"))
 )
 driver.find_element(By.ID, "user-name").send_keys("standard_user")
 driver.find_element(By.ID, "password").send_keys("secret_sauce")
 driver.find_element(By.ID, "login-button").click()

 WebDriverWait(driver, 5).until(
     EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
 )

items_add = [
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Onesie"
]

for items_name in items_add:
    add_to_cart = driver.find_element(By.XPATH, f"//div[text()='{items_name}']/ancestor::div[@class='inventory_item']//button"
    )
    add_to_cart.click()
    print(f'Добавлено в корзину')

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
)

driver.find_element(By.ID, "checkout").click()
WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.ID, "first-name"))
)

driver.find_element(By.ID, "first-name").send_keys("Марья")
driver.find_element(By.ID, "last-name").send_keys("Козлова")
driver.find_element(By.ID, "postal-code").send_keys("123456")
driver.find_element(By.ID, "continue").click()
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
)

total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
total_text = total_element.text
total_amount = total_text.replace("Total: $", "")

print(f"Total amount: {total_text}")


assert total_amount == "58.29", f"Ожидается общая сумма $58.29"

print("OK")
driver.quit()