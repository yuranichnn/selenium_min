import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

GRID_TAB = ("xpath", "//a[@data-rb-event-key='grid']")
TABLE = ("xpath", "//div[@class='tab-content']")

driver.get("https://demoqa.com/selectable")
wait.until(EC.element_to_be_clickable(GRID_TAB)).click()
time.sleep(4)


def get_table_elements(table_locator) -> dict:
    table_elements = {}
    table = driver.find_element(*table_locator)
    rows = table.find_elements("xpath", "//div[contains(@id,'row')]")
    columns = table.find_elements("xpath", "(//div[contains(@id,'row')])[1]/li")

    for number_row in range(1, len(rows) + 1):
        for number_column in range(1, len(columns) + 1):
            table_elements[f"{number_row},{number_column}"] = driver.find_element("xpath",
                                                                                 f"(//div[contains(@id,'row')])[{number_row}]/li[{number_column}]")

    return table_elements


def choose_random_element(table_elements: dict):
    random_key = random.choice(list(table_elements.keys()))
    table_element = table_elements[random_key]
    print(f"Выбран элемент таблицы с индексом - {random_key}")

    return table_element

def is_elem_choose(web_element) -> bool:
    if "active" in web_element.get_attribute("class"):
        return True
    else:
        return False

table_elements = get_table_elements(TABLE)
random_element_1 = choose_random_element(table_elements)
random_element_2 = choose_random_element(table_elements)
wait.until(EC.element_to_be_clickable(random_element_1)).click()
wait.until(EC.element_to_be_clickable(random_element_2)).click()
assert is_elem_choose(random_element_1), "элемент не выбран"
assert is_elem_choose(random_element_2), "элемент не выбран"
wait.until(EC.element_to_be_clickable(random_element_1)).click()
wait.until(EC.element_to_be_clickable(random_element_2)).click()
assert not is_elem_choose(random_element_1), "элемент выбран"
assert not is_elem_choose(random_element_2), "элемент выбран"

driver.close()




