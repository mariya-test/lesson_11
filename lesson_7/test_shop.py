from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as  FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from lesson_7.Shop import shop




def test_shop():
    browser = webdriver.Firefox()

    shop = Shop(browser)
    shop.auto()
    shop.items_add()
    shop.click()
    shop.decoration()
total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
total_text = total_element.text
total_amount = total_text.replace("Total: $", "")

print(f"Total amount: {total_text}")


assert total_amount == "58.29", f"Ожидается общая сумма $58.29"

print("OK")
driver.quit()