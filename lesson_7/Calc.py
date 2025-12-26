from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calc:
    def __init__(self, driver):
        self.driver = driver
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def click(self):
        self.button = driver.find_element(By.ID, "delay")
        self.button.clear()
        self.button.send_keys(45)

    def enter_values(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def wait(self):
        self.WebDriverWait(driver, 46).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
)
    def result(self):
       self. result = driver.find_element(By.CLASS_NAME, "screen").text

        print("ok")


 self.driver.quit()