import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

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
action = ActionChains(driver)

driver.get("https://seiyria.com/bootstrap-slider/")

# driver.find_element("xpath", "//a[@href='#example-2']").click()
SLIDER_LOCATOR = ("xpath","//div[@id='example-6']//div[@role='slider' and not (contains(@class,'hide'))]")
CURRENT_VALUE_LOCATOR = ("xpath", "//div[@id='example-6']//span[contains(text(),'Value')]/span")
slider = driver.find_element(*SLIDER_LOCATOR)
current_value = driver.find_element(*CURRENT_VALUE_LOCATOR)
action.move_to_element(slider).perform()


def move_slider(slider, min_point_attr, max_point_attr, current_point_attr, target_point):
    min = int(slider.get_attribute(min_point_attr))
    max = int(slider.get_attribute(max_point_attr))
    current_position = int(slider.get_attribute(current_point_attr))
    if min<=target_point<current_position:
        while str(target_point)!=slider.get_attribute(current_point_attr):
            slider.send_keys(Keys.ARROW_LEFT)
    elif current_position<int(target_point)<=max:
        while slider.get_attribute(current_point_attr) != str(target_point):
            slider.send_keys(Keys.ARROW_RIGHT)
    else:
        raise Exception("Целевое значение слайдера вне диапозона слайдера")
    assert slider.get_attribute(current_point_attr)==current_value.text==str(target_point), "Ошибка значения слайдера"

move_slider(slider,"aria-valuemin","aria-valuemax", "aria-valuenow", 10)
input()
driver.close()
