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


# Read the links from the venue_links.txt and store them
with open('venue_links.txt', 'r') as f:
    venue_links = f.readlines()

for venue_link in venue_links:
    



###########################################################
###### Get the links to all 12 races at a venue
###########################################################
# url = "https://www.neds.com.au/racing/central-park-bags/7567831f-f219-41ee-8a1c-cb2a1e03d451"
    driver.get(venue_link)
    time.sleep(2)
    try:
        
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "page-content"))
        )
    finally:
        contents = elem.find_elements_by_class_name('race-switcher-list__link')
        race_links = []
        for race_link in contents:
            # print(link.get_attribute('innerHTML'))
            print(race_link.get_attribute('href'))
            race_links.append(race_link.get_attribute('href'))
            
        print("NEXT Venue--------------------------\n")
