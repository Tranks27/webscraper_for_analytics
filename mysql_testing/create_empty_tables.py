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
            cursor.execute("DROP TABLE IF EXISTS race_results;")
            print("Creating table")
            cursor.execute("CREATE TABLE race_results(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")

            print("Creating table")
            cursor.execute("CREATE TABLE central_park_bags(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")

            print("Creating table")
            cursor.execute("CREATE TABLE crayford(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")

            print("Creating table")
            cursor.execute("CREATE TABLE hove(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")

            print("Creating table")
            cursor.execute("CREATE TABLE kingsley_bags(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")

            print("Creating table")
            cursor.execute("CREATE TABLE monmore(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")


            print("Creating table")
            cursor.execute("CREATE TABLE newcastle_bags(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")


            print("Creating table")
            cursor.execute("CREATE TABLE perry_barr_bags(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")


            print("Creating table")
            cursor.execute("CREATE TABLE romford_bags(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")

            print("Creating table")
            cursor.execute("CREATE TABLE sheffield_bags(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")

            print("Creating table")
            cursor.execute("CREATE TABLE sunderland_bags(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")

            print("Creating table")
            cursor.execute("CREATE TABLE towcester(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")

            print("Creating table")
            cursor.execute("CREATE TABLE towcester_bags(R1 CHAR(5),\
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
						  R12 CHAR(5));")
            print("Table is created.....")
            # for i,row in csvData.iterrows():
            #     if NaN in row:
            #         print(row)
            #         cursor.execute("INSERT INTO race_results VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", tuple(row))
            connection.commit()
except Error as e:
    print(e)