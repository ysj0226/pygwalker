from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import sys

# driver = webdriver.Chrome()

# driver.get('http://localhost:8501/')

# def document_initialised(driver):
#     return driver.execute_script("return initialised")

# WebDriverWait(driver, timeout=10).until(document_initialised)
# el = driver.find_element(By.TAG_NAME, "p")
# assert el.text == "finish"

# print(driver.page_source)
# with open('./GitHub_Action_Results.html', 'w', encoding='utf-8') as f:
#     f.write(driver.page_source)




#从服务中获取html信息上传到action
def get_html(uri, path):

    service = ChromeService(executable_path=ChromeDriverManager().install())

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url=uri)

    # Click the link to activate the alert
    # driver.find_element(By.LINK_TEXT, "Hello Selenium!").click()

    # Wait for the alert to be displayed and store it in a variable
    alert = WebDriverWait(driver, sys.maxsize).until(expected_conditions.alert_is_present())

    # Store the alert text in a variable
    # text = alert.text

    # Press the OK button
    alert.accept()

    print(driver.page_source)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(driver.page_source)


if __name__ == '__main__':
    url = sys.argv[1]
    path = sys.argv[2]
    get_html(url,path)