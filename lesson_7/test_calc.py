import pytest
from selenium import webdriver
from lesson_7.Calc import Calc


def test_calculator():
    driver = webdriver.Chrome()
    calc = Calc(driver)
    calc.open()
    calc.set_delay(45)
    calc.enter_expression("7+8=")

    result = calc.get_result()
    assert result == "15", f"Ожидался результат 15, получено {result}"
    driver.quit()


