from selenium import webdriver
import pickle

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
# task№1
# driver.get("https://vk.com/")
# driver.add_cookie({
#     "name":"username",
#     "value": "user123"
# })
# driver.refresh()
# assert driver.get_cookie("username") in driver.get_cookies() and driver.get_cookie("username")["value"]=="user123" , "no needed cookie"
# print(driver.get_cookie("username")["value"])

# task№2
driver.get("https://tochka.com/")
cookies = driver.get_cookies()
print(cookies)
# deleted_cookie_name = driver.get_cookie("NID")
# print(deleted_cookie_name)
# driver.delete_cookie("ipp_key")
driver.delete_all_cookies()
driver.refresh()
print(driver.get_cookies())
# input()