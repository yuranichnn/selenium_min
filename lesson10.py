from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

urls = ["https://hyperskill.org/login",
        "https://www.avito.ru/",
        "https://www.ozon.ru/"
        ]
wait = WebDriverWait(driver, 10, 1)

for i in range(2):
    driver.switch_to.new_window("tab")

all_tabs = driver.window_handles
HS_ELEM = ("xpath", "//a[text()='All courses']")
AVITO_ELEM = ("xpath", "//a[text()='Для бизнеса']")
OZON_ELEM = ("xpath", "//a[text()='Помощь']")

element_list = [HS_ELEM, AVITO_ELEM, OZON_ELEM]


def get_title_click_elem(descriptor, url, element):
    driver.switch_to.window(descriptor)
    driver.get(url)
    title = driver.title
    wait.until(ES.element_to_be_clickable(element)).click()
    return title


number = 0
for tab in all_tabs:
    print(get_title_click_elem(tab, urls[number], element_list[number]))
    number += 1
input()
driver.quit()