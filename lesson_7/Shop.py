from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as  FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class shop():
    def __init__(self,driver):
        self.driver = driver
        self.driver.get ("https://www.saucedemo.com/")
        self.WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )


class LoginPage:
    def __init__(self, driver):
     self.driver = driver

    def login(self, username, password):
     self.driver.find_element(By.ID, "user-name").send_keys(username)
     self.driver.find_element(By.ID, "password").send_keys(password)
     self.driver.find_element(By.ID, "login-button").click()

class ProductPage:
    def __init__(self, driver):
    self.driver = driver

    def add_to_cart(self, product_name):
            # Находим кнопку "Add to cart" для конкретного товара
    button = self.driver.find_element(
    By.XPATH,
    f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
    )
    button.click()
      print(f"Товар '{product_name}' добавлен в корзину")

    def click(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
)

        self.driver.find_element(By.ID, "checkout").click()
        self.WebDriverWait(self.driver,5).until(
            EC.presence_of_all_elements_located((By.ID, "first-name"))
)


def decoration(self):
    self.driver.find_element(By.ID, "first-name").send_keys("Марья")
    self.driver.find_element(By.ID, "last-name").send_keys("Козлова")
    self.driver.find_element(By.ID, "postal-code").send_keys("123456")
    self.driver.find_element(By.ID, "continue").click()
    self.WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )


