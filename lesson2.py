from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

wiki_icon_elem = driver.find_element("class name", "wikipedia-icon")
print(wiki_icon_elem)
wiki_input_field = driver.find_element("id","Wikipedia1_wikipedia-search-input")
print(wiki_input_field)
wiki_search_button = driver.find_element("css selector", ".wikipedia-search-button")
print(wiki_search_button)
start_button = driver.find_element("class name", "widget-content").find_element("tag name", "button")
print(start_button)