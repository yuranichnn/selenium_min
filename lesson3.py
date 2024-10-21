import time

from selenium import webdriver

# Задание №1

driver = webdriver.Firefox()

VK_URL = "https://vk.com/"
GOOGLE_URL = "https://www.google.com/"


def get_info_by_url(url=None):
    driver.get(url) if url is not None else ...
    title = driver.title
    url = driver.current_url
    assert url == url, print("Открылась не та страница")
    return {"title": title, "url": url}


print(get_info_by_url(VK_URL)["title"])
print(get_info_by_url(GOOGLE_URL)["title"])
driver.back()
get_info_by_url()
driver.refresh()
print(get_info_by_url()["url"])
driver.forward()
assert get_info_by_url()["url"] == GOOGLE_URL, print(
    f"URL-адрес не изменился, текущий url = {get_info_by_url()["url"]}")
driver.close()
