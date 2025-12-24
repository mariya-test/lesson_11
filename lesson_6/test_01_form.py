from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.service import Service as  EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_form_fields():
service = EdgeService()
driver = webdriver.Edge(service=service)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
address = driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
email = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
Phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787 ")
city = driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
country = driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
company = driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
    )
zip_code_field = driver.find_element(By.ID, "zip-code")
zip_code_class = zip_code_field.get_attribute("class")
assert "alert-danger" in zip_code_class, "Поле Zip не подсвечивается красным"

fields_to_chek = [
    'first-name','last-name','address', 'e-mail','phone', 'city', 'country',
    'job-position', 'company'
]
for field_name in fields_to_chek:
    field = driver.find_element(By.ID, f"{field_name}")
    field_class = field.get_attribute("class")
    assert "alert py-2 alert-success" in field_class

driver.quit()

#for field_id in ['first_name_id', 'last_name_id', 'address', ]:  # Добавь нужные ID полей
 #   field = driver.find_element(By.ID, field_id)
  #  field_style = field.get_attribute('style')
   # assert 'green' in field_style, f"Field with ID {field_id} is not highlighted green"


#(assert "rgb(186, 219, 204)" in border_color, f"Поле {field_id} не подсвечено зеленым



