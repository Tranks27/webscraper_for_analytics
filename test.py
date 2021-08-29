from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time

options = Options()
options.add_argument('--headless') # headless browser so GUI is not shown
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()


url = "https://www.neds.com.au/racing/central-park-bags/7567831f-f219-41ee-8a1c-cb2a1e03d451"
driver.get(url)
time.sleep(3)
try:
    
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "page-content"))
    )
finally:
    content = elem.find_elements_by_class_name('race-switcher-list__link')
    links = []
    for link in content:
        # print(link.get_attribute('innerHTML'))
        # print(link.get_attribute('href'))
        links.append(link.get_attribute('href'))
    

print(links)

# page = url.split("/")[-2]
# filename = f'{page}.txt'
# with open(filename, 'w') as f:
#     f.write(content.text)

driver.close()