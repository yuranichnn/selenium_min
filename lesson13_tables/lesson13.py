import time
from selenium import webdriver
from lesson13_tables.table_handler import TableHandler

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

table = TableHandler(driver)
driver.get("https://datatables.net/")

print(table.get_cell_content(1,2))
print(table.get_row_content(row_number=2))
print(table.get_column_content(column_number=2))
print(table.get_salary_by_row(row_number=1))
table.sort_by_column_head(head_number=1)
input()

