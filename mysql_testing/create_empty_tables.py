import csv
# from getpass import getpass
from mysql.connector import connect, Error
import pandas as pd

# Read data into a variable
csvData = pd.read_csv('/home/tranks/scrapeBySelenium/webscraper_for_analytics/New_data.csv', delimiter=',')

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
            
            # print("Creating table")
            # cursor.execute("CREATE TABLE race_results(R1 CHAR(5),\
			# 			  R2 CHAR(5),\
            #               R3 CHAR(5),\
			# 			  R4 CHAR(5),\
            #               R5 CHAR(5),\
			# 			  R6 CHAR(5),\
            #               R7 CHAR(5),\
			# 			  R8 CHAR(5),\
            #               R9 CHAR(5),\
			# 			  R10 CHAR(5),\
            #               R11 CHAR(5),\
			# 			  R12 CHAR(5));")
            # print("Table is created.....")

            venues = ['belle_vue','belle_vue_bags','central_park','central_park_bags',\
                        'crayford', 'crayford_bags',\
                        'doncaster','doncaster_bags','harlow','harlow_bags',\
                        'henlow','henlow_bags','hove','hove_bags',\
                        'kinsley','kinsley_bags','monmore','monmore_bags',\
                        'newcastle','newcastle_bags','nottingham','nottingham_bags',\
                        'perry_barr','perry_barr_bags','romford','romford_bags',\
                        'sheffield','sheffield_bags','sunderland','sunderland_bags',\
                        'swindon','swindon_bags','yarmouth','yarmouth_bags',\
                        'pelaw_grange','pelaw_grange_bags','towcester','towcester_bags']
            print(venues)
            for venue in venues:
                cursor.execute(f'DROP TABLE IF EXISTS {venue};')
                print("Creating table")
                cursor.execute(f'CREATE TABLE {venue}(R1 CHAR(5),\
                            R2 CHAR(5),\
                            R3 CHAR(5),\
                            R4 CHAR(5),\
                            R5 CHAR(5),\
                            R6 CHAR(5),\
                            R7 CHAR(5),\
                            R8 CHAR(5),\
                            R9 CHAR(5),\
                            R10 CHAR(5),\
                            R11 CHAR(5),\
                            R12 CHAR(5));')
                print("Table is created.....")

            

            
            # for i,row in csvData.iterrows():
            #     if NaN in row:
            #         print(row)
            #         cursor.execute("INSERT INTO race_results VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", tuple(row))
            connection.commit()
except Error as e:
    print(e)