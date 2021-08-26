from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver.implicitly_wait(10)
url = "https://www.neds.com.au/racing/central-park-bags/64b3a7de-9262-4e57-bc75-42a9a27cf696"
driver.get(url)
try:
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "page-content"))
    )
finally:
# elem = driver.find_element_by_xpath("//div[@class='racing-content-inner']")
    # print(elem.text)
    page = url.split("/")[-2]
    filename = f'{page}_r1.txt'
    with open(filename, 'w') as f:
        f.write(elem.text)
    


# driver.close()