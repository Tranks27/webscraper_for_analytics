import pandas as pd
import numpy as np

import csv
# Read data into a variable
csvData = pd.read_csv('/home/tranks/scrapeBySelenium/webscraper_for_analytics/mysql_testing/single_venue_strategy_results.csv', delimiter=',', skip_blank_lines=True)

## convert the pd dataframe to numpy array
result = csvData.to_numpy()
print(result)

## sum up the arrays element-wise and store the result in single array
venue_id = result[0][0] # copy venue_id value
sum_arr = result[0]
for i in range(len(result)-1):
    sum_arr = np.add(sum_arr, result[i+1])
print(sum_arr)

## pop out the last element, i.e. num_races
num_races = sum_arr[1] # copy venue_id value
sum_arr = np.delete(sum_arr,[0,1]) # delete the venue_id and num_races from the array
print(sum_arr)
print(num_races)

## convert into percentages and create the array to be uploaded to mysql
percentage_sum_arr = np.array([venue_id, num_races])
for i in range(len(sum_arr)):
    percentage_sum_arr = np.append(percentage_sum_arr, round(float(sum_arr[i]/num_races)*100, 2))
print(percentage_sum_arr)

###########################################
## Upload to mysql
###########################################





