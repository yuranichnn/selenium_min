import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class TableHandler:
    _TABLE_LOCATOR = ("xpath", "//table[@id='example']")
    _ROWS_LOCATOR = ("xpath", "./tbody/tr")
    _COLUMNS_LOCATOR = ("xpath", "./td")
    _SALARY_LOCATOR = ("xpath", "./tbody//span[@class='dtr-data']")
    _HEAD_LOCATOR = ("xpath", "./thead//th")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def _table(self) -> WebElement:
        return self.driver.find_element(*self._TABLE_LOCATOR)

    @property
    def _rows(self) -> list[WebElement]:
        table = self._table
        return table.find_elements(*self._ROWS_LOCATOR)

    def _cells_by_row(self, row_number) -> list[WebElement]:
        row = self._rows[row_number - 1]
        return row.find_elements(*self._COLUMNS_LOCATOR)

    def get_cell_content(self, row_number, column_number):
        cell = self._cells_by_row(row_number)[column_number - 1]
        return cell.text

    def get_row_content(self, row_number) -> list[str]:
        return [cell.text for cell in self._cells_by_row(row_number) if cell.text]

    def get_column_content(self, column_number) -> list[str]:
        column_content = []
        for row in range(len(self._rows)):
            row_content = self._cells_by_row(row + 1)
            cell = row_content[column_number - 1].text
            column_content.append(cell)
        return column_content

    def get_salary_by_row(self, row_number):
        cell = self._cells_by_row(row_number)[0]
        cell.click()
        salary = self._table.find_element(*self._SALARY_LOCATOR).text
        cell.click()
        return salary

    @property
    def _heads(self) -> list[WebElement]:
        table = self._table
        return table.find_elements(*self._HEAD_LOCATOR)

    def sort_by_column_head(self,head_number):
        begin_column = self.get_column_content(head_number)
        head = self._heads[head_number - 1]
        head.click()
        finish_column = self.get_column_content(head_number)
        assert begin_column!=finish_column, "Сортировка не работает"
