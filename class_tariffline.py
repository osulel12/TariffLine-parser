from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException as no_element
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import time

with webdriver.Chrome(ChromeDriverManager(version="114.0.5735.90").install()) as browser:
    # Переходим на нужный сайт
    browser.get('https://www.macmap.org/en/download')
    time.sleep(60)
