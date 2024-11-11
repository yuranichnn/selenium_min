from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time
import os

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
# task№1
driver.get("https://vk.com/")
driver.add_cookie({
    "name":"username",
    "value": "user123"
})
driver.refresh()
assert driver.get_cookie("username") in driver.get_cookies() and driver.get_cookie("username")["value"]=="user123" , "no needed cookie"
print(driver.get_cookie("username")["value"])

# task№2
driver.get("https://vk.com/")
deleted_cookie_name = "domain_sid"
driver.delete_cookie(deleted_cookie_name)
driver.refresh()
assert deleted_cookie_name not in driver.get_cookies(), "кука не удалена"

# task№3
driver.get("https://obi.ru/")
ITEM = ("xpath", "(//span[text()='В корзину'])[1]")
wait.until(EC.element_to_be_clickable(ITEM)).click()

pickle.dump(driver.get_cookies(), open(os.path.join(os.getcwd(), "cookies", "cookies.pkl"), "wb"))
driver.delete_all_cookies()
driver.refresh()

cookies = pickle.load(open(os.path.join(os.getcwd(), "cookies", "cookies.pkl"), "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
driver.close()


time.sleep(5)
