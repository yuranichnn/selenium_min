from pyexpat.errors import messages

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--window-size=1920,1080")
options.page_load_strategy = 'normal'

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, timeout=15, poll_frequency=1)

driver.get("https://omayo.blogspot.com/")
text_disappear = ("xpath", "//div[@id='deletesuccess']")
text_delay = ("xpath", "//div[@id='delayedText']")
button3 = ("xpath", "//input[@id='timerButton']")
try_it_button = ("xpath", "//button[text()='Try it']")
my_button_disabled = ("xpath", "//button[@id='myBtn' and @disabled]")

wait.until(EC.invisibility_of_element_located(text_disappear), message=f"Текст с локатором '{text_disappear[1]}' виден")
wait.until(EC.visibility_of_element_located(text_delay), message=f"Текст с локатором '{text_delay[1]}' не виден")
wait.until(EC.element_to_be_clickable(button3), message="Не кликабельный")
wait.until(EC.element_to_be_clickable(try_it_button)).click()
wait.until(EC.visibility_of_element_located(my_button_disabled))