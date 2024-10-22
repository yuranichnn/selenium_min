# Задание №1
import time
from faker import Faker

from selenium import webdriver

driver = webdriver.Firefox()
fake = Faker()
FULL_NAME = "//input[@id='userName']"
EMAIL = "//input[@id='userEmail']"
CURRENT_ADDRESS = "//textarea[@id='currentAddress']"
PERMANENT_ADDRESS = "//textarea[@id='permanentAddress']"


def get_element(locator):
    try:
        return driver.find_element("xpath", f"{locator}")
    except:
        raise Exception(f"Элемент с локатором '{locator}' не найден.")


def fill_input_field(locator, data):
    input_field = get_element(locator)
    input_field.clear()
    input_field.send_keys(data)
    assert input_field.get_attribute("value") == data, "Введенные данные не совпадают"


driver.get("https://demoqa.com/text-box")
fill_input_field(FULL_NAME, fake.name())
fill_input_field(EMAIL, fake.email())
fill_input_field(CURRENT_ADDRESS, fake.address())
fill_input_field(PERMANENT_ADDRESS, fake.address())
time.sleep(5)


# Задание №2
USERNAME = "//input[@id='username']"
PASSWORD = "//input[@id='password']"
LOGIN_BUTTON = "//button/i[normalize-space()='Login']"
LOGOUT_BUTTON = "//a/i[normalize-space()='Logout']"

login = "tomsmith"
password = "SuperSecretPassword!"


def check_login():
    login_button = get_element(LOGIN_BUTTON)
    login_button.click()
    try:
        assert get_element(LOGOUT_BUTTON).is_displayed() is True
    except:
        raise Exception("Авторизация не успешна")
    print("Авторизация успешна")


driver.get("https://the-internet.herokuapp.com/login")
fill_input_field(USERNAME, login)
fill_input_field(PASSWORD, password)
check_login()
driver.close()


