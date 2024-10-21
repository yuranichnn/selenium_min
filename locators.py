# Задание №2
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://hyperskill.org/tracks")


def is_find_element(*args) ->list:
    element_list = list()
    for elem in args:
        element = driver.find_element(*elem)
        element_list.append(element)
    driver.close()
    return element_list


# Header
LOGO_BUTTON = ("xpath", "//header//a[@class='nav-link'][div]")
EXPLORE_BUTTON = ("xpath", "//header//a[normalize-space()='Explore']")
PRICING_BUTTON = ("xpath", "//header//a[@href='/pricing']")
FOR_BUSINESS_BUTTON = ("xpath", "//header//a[normalize-space()='For Business']")
SIGN_IN_BUTTON = ("xpath", "//header//span[normalize-space()='Sign in']")
START_FOR_FREE_BUTTON = ("xpath", "//header//span[normalize-space()='Start for free']")

# Body
PROJECTS_BUTTON = ("xpath", "//main//a[@click-event-target='projects']")
TRACKS_BUTTON = ("xpath", "//main//a[@click-event-target='tracks']")
PYTHON_BUTTON = ("xpath", "//main//a[@click-event-target='python']")
JAVA_BUTTON = ("xpath", "//main//a[@click-event-target='java']")
KOTLIN_BUTTON = ("xpath", "//main//a[@click-event-target='kotlin']")
JS_BUTTON = ("xpath", "//main//a[@click-event-target='javascript']")
GO_BUTTON = ("xpath", "//main//a[@click-event-target='go']")
SCALA_BUTTON = ("xpath", "//main//a[@click-event-target='scala']")
SHELL_BUTTON = ("xpath", "//main//a[@click-event-target='shell']")
PYTHON_CARD_ZOOKEEPER = ("xpath", "//main//a[@aria-label='Zookeeper with Python']")
PYTHON_CARD_BILL = ("xpath", "//main//a[@aria-label='Bill Splitter']")
ALL_COURSES_FILTER = ("xpath", "//main//a[normalize-space()='All courses']")
TOP_COURSES_FILTER = ("xpath", "//main//a[normalize-space()='Top courses']")
PYTHON_FILTER = ("xpath", "//main//a[text()='Python ']")
BACKEND_FILTER = ("xpath", "//main//a[normalize-space()='Backend']")
PYTHON_DEV_CARD = ("xpath", "//main//span[contains(text(),'Acquire key skills to build')]")
KOTLIN_CORE_CARD = ("xpath", "//main//span[contains(text(),'Kotlin, developed by JetBrains')]")
LOAD_MORE_BUTTON = ("xpath", "//main//span[normalize-space()='Load more']")
# Footer
PYTHON_FOOTER_BUTTON = ("xpath", "//footer//a[text()='Python']")
JAVA_FOOTER_BUTTON = ("xpath", "//footer//a[text()='Java']")
FULL_CATALOG_BUTTON = ("xpath","//footer//a[text()='Java']")
HELP_CENTER_BUTTON = ("xpath", "//footer//a[normalize-space()='Help Center']")
GOOGLE_PLAY_BUTTON = ("xpath", "//footer//a[img[contains(@alt,'Google Play')]]")
APP_STORE_BUTTON = ("xpath", "//footer//a[img[contains(@alt,'App Store')]]")
