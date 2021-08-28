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


url = "https://www.neds.com.au/racing/central-park/0366193e-00c4-4dd3-be97-e0c9ff1de00a"
driver.get(url)
time.sleep(3)
try:
    
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "page-content"))
    )
finally:
    data = elem.text
    

    print(elem)
    print(data)
    data_arr = [] 
    for line in data.splitlines():
        data_arr.append(str(''.join(line)))
    # print(''.join(line))
    
    # print(data_arr)
    # ranking/results (1st, 2nd, 3rd)
    r1 = []
    r2 = []
    r3 = []
    # Players/runners
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []

    data_length = len(data_arr)
    for i,val in enumerate(data_arr):
        if(val == '1st'):
            r1.append(str(data_arr[i+1]))
            print("i got here")

    print(r1)

    page = url.split("/")[-2]
    filename = f'{page}_r1.txt'
    with open(filename, 'w') as f:
        f.write(elem.text)
    


driver.close()