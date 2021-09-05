from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
import csv

options = Options()
options.add_argument('--headless') # headless browser so GUI is not shown
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()


url = 'https://www.neds.com.au/racing/central-park/76c6660e-8159-4857-893a-10aefbd9a93e'
driver.get(url)
time.sleep(2)
try:
    
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "page-content"))
    )
finally:
    data = elem.text

print(data)
driver.close()