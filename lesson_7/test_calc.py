import pytest
from selenium import webdriver
from lesson_7.Calc import Calc

def driver():
    driver = webdriver.Chrome()
    calc = Calc
    calc.open()
    calc.click()
    calc.enter_values()
    calc.wait()
    calc.result()
    assert result == "15", f"Ожидаем результат 15"




