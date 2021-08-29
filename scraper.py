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

###########################################################
###### Get the links to all 12 races at a venue
###########################################################
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



###########################################################
###### Operate on each link
###########################################################
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
p6 = []

for url in links:

    # url = links[0]
    driver.get(url)
    time.sleep(2)
    try:
        
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "page-content"))
        )
    finally:
        data = elem.text
        
    flag_part2 = False
    # print(elem)
    # print(data)
    data_arr_part1 = [] 
    data_arr_part2 = []
    for line in data.splitlines():
        if not flag_part2:
            data_arr_part1.append(str(''.join(line)))
        if(line == 'RUNNERS' or flag_part2 == True):
            flag_part2 = True
            data_arr_part2.append(str(''.join(line)))
        # print(line)

    # print(data_arr_part1)
    # print("end of part1")
    # print(data_arr_part2)


    count_1st = 0
    count_2nd = 0
    count_3rd = 0
    # data_length = len(data_arr)
    for i,val in enumerate(data_arr_part1):
        if(val == '1st'):
            count_1st += 1
            if(count_1st == 3):
                r3.append(str(data_arr_part1[i+1][0])) #get the first value of that string
            elif(count_1st == 2):
                r2.append(str(data_arr_part1[i+1][0]))
            else:
                r1.append(str(data_arr_part1[i+1][0])) 
        elif(val == '2nd'):
            count_2nd += 1
            if(count_2nd == 2):
                r3.append(str(data_arr_part1[i+1][0])) #get the first value of that string
            else:
                r2.append(str(data_arr_part1[i+1][0]))
        elif(val == '3rd'):
            count_3rd += 1
            if(count_1st + count_2nd < 3 and count_3rd == 1):
                r3.append(str(data_arr_part1[i+1][0]))
            else:
                print("There has been a tie for one position")

    for i,val in enumerate(data_arr_part2):
        if('1. ' in val):
            if(data_arr_part2[i+1] == 'SCRATCHED'):
                p1.append('-')
            else:
                p1.append(str(data_arr_part2[i+2])) #get the first value of that string
        elif('2. ' in val):
            if(data_arr_part2[i+1] == 'SCRATCHED'):
                p2.append('-')
            else:
                p2.append(str(data_arr_part2[i+2])) 
        elif('3. ' in val):
            if(data_arr_part2[i+1] == 'SCRATCHED'):
                p3.append('-')
            else:
                p3.append(str(data_arr_part2[i+2])) 
        elif('4. ' in val):
            if(data_arr_part2[i+1] == 'SCRATCHED'):
                p4.append('-')
            else:
                p4.append(str(data_arr_part2[i+2])) 
        elif('5. ' in val):
            if(data_arr_part2[i+1] == 'SCRATCHED'):
                p5.append('-')
            else:
                p5.append(str(data_arr_part2[i+2])) 
        elif('6. ' in val):
            if(data_arr_part2[i+1] == 'SCRATCHED'):
                p6.append('-')
            else:
                p6.append(str(data_arr_part2[i+2])) 
   


    

print(r1)
print(r2)
print(r3)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)

page = url.split("/")[-2]
filename = f'{page}.txt'
with open(filename, 'w') as f:
    f.write("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" %(r1, r2, r3, p1, p2, p3, p4, p5, p6))


driver.close()