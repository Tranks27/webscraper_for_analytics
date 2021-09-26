#################################################
## script to write the percentages table title
#################################################
# with open('to_copy.txt', 'w') as f:

#     for i in range(6):  
#         f.write(f'Stra1_{i+1} DECIMAL(5,2),')
#     f.write('\\\n')

#     for i in range(6):  
#         f.write(f'Stra2_{i+1} DECIMAL(5,2),')
#     f.write('\\\n')

#     for i in range(6):  
#         f.write(f'Stra3_{i+1} DECIMAL(5,2),')
#     f.write('\\\n')

#     for i in range(6):
#         for j in range(5):
#             f.write(f'Stra4_{i+1}{j+1} DECIMAL(5,2),')
#     f.write('\\\n')

#     for i in range(6):
#         for j in range(5):
#             f.write(f'Stra5_{i+1}{j+1} DECIMAL(5,2),')
    

#################################################
## sql Updater
#################################################
# with open('to_copy.txt', 'w') as f:
#     j = 3
#     ## Strategy 1
#     for i in range(6):  
#         f.write(f'Stra1_{i+1} = {{updated_data[{j}]}},')
#         j = j+1
#     f.write('\\')

#     ## Strategy 2
#     f.write('\n')
#     for i in range(6):
#         f.write(f'Stra2_{i+1} = {{updated_data[{j}]}},')
#         j = j+1
#     f.write('\\')

#     ## Strategy 3
#     f.write('\n')
#     for i in range(6):
#         f.write(f'Stra3_{i+1} = {{updated_data[{j}]}},')
#         j = j+1
#     f.write('\\')

#     ## Strategy 4
#     f.write('\n')
#     for k in range(6):
#         for i in range(5):
#             f.write(f'Stra4_{k+1}{i+1} = {{updated_data[{j}]}},')
#             j = j+1
#     f.write('\\')

#     ## Strategy 5
#     f.write('\n')
#     for k in range(6):
#         for i in range(5):
#             if k == 5 and i == 4:
#                 f.write(f'Stra5_{k+1}{i+1} = {{updated_data[{j}]}}')
#             else:
#                 f.write(f'Stra5_{k+1}{i+1} = {{updated_data[{j}]}},')
#             j = j+1
#     f.write('\\')


#################################################
## data_importer.py integrated
#################################################
'''
import csv
# from getpass import getpass
from mysql.connector import connect, Error
import pandas as pd

# def data_channeller(row, )
def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def main():
    # Read data into a variable
    csvData = pd.read_csv('/home/tranks/scrapeBySelenium/webscraper_for_analytics/New_data.csv', delimiter=',')
    # print(csvData)
    try:
        with connect(
            host="localhost",
            # user=input("Enter username: "),
            # password=getpass("Enter password: "),
            user='root',
            password='12345',
            database = "test"
        ) as connection:
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute("SELECT database();")
                record = cursor.fetchone()
                print("Your are connected to database: ", record)

                ## Import the data into their respective venue tables
                for index,row in csvData.iterrows():
                    # Check for the venue_name headers
                    if not row[0].isdigit() and not is_float(row[0]):
                        data = csvData.iloc[index+1:index+10]
                        # print(data)
                        for i,r in data.iterrows():
                            try:
                                cursor.execute(f'INSERT INTO {row[0]} VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);', tuple(r))
                            except Error as e:
                                print(f'Got to error in executing row number {i}')
                                print(e)
                connection.commit()
    except Error as e:
        print("Error in connection")
        print(e)



if __name__ == '__main__':
    main()
'''