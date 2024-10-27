from selenium import webdriver
import os
import time

upload_path = os.path.join(os.getcwd(), "lesson5", "upload_files")
downloads_path = os.path.join(os.getcwd(), "lesson5", "downloads")

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--window-size=1920,1080")
options.page_load_strategy = 'eager'
preferences = {
    "download.default_directory": downloads_path,
    "safebrowsing.enabled": True,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
}
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(options=options)


def clear_directory(directory):
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f"Ошибка при удалении {file_path}: {e}")
    else:
        os.makedirs(directory, exist_ok=True)
        print(f"Директории не было, но мы её создали - '{directory}'")


# Задание №1
driver.get("https://demoqa.com/upload-download")
upload_field = driver.find_element("xpath", "//input[@type='file']")
upload_field.send_keys(os.path.join(upload_path, "example.txt"))
time.sleep(3)


# Задание №2
driver.get("http://the-internet.herokuapp.com/download")
download_elements = driver.find_elements("xpath", "//a[contains(@href, 'download')]")
clear_directory(downloads_path)

for element in download_elements:
    try:
        element.click()
    except Exception as e:
        print(f"Ошибка при скачивании элемента {element.get_attribute('value')}: {e}")

print(f"Скачивание завершено, загружено {len(os.listdir(downloads_path))} файлов из {len(download_elements)}")
