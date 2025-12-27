from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as  FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from lesson_7.Shop import shop


def test_shop():
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    product_page = ProductPage(driver)
    product_page.add_to_cart("Sauce Labs Backpack")
    product_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    product_page.add_to_cart("Sauce Labs Onesie")

    cart_page = CartPage(driver)
    cart_page.go_to_cart()
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Марья", "Козлова", "123456")
    total = checkout_page.get_total()

    assert total == "$58.29", f"Ожидалась сумма $58.29, получено {total}"
    driver.quit()
