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
        # database = "test"
        database = "online_movie_rating"
    ) as connection:
        print(connection)

        with connection.cursor() as cursor:
            cursor.execute("SELECT database();")
            record = cursor.fetchone()
            print("Your are connected to database: ", record)
            
            ###########################################
            ## TABLE 1
            ###########################################
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

            ###########################################
            ## TABLE 2
            ###########################################
            # venues = ['belle_vue','belle_vue_bags','central_park','central_park_bags',\
            #             'crayford', 'crayford_bags',\
            #             'doncaster','doncaster_bags','harlow','harlow_bags',\
            #             'henlow','henlow_bags','hove','hove_bags',\
            #             'kinsley','kinsley_bags','monmore','monmore_bags',\
            #             'newcastle','newcastle_bags','nottingham','nottingham_bags',\
            #             'perry_barr','perry_barr_bags','romford','romford_bags',\
            #             'sheffield','sheffield_bags','sunderland','sunderland_bags',\
            #             'swindon','swindon_bags','yarmouth','yarmouth_bags',\
            #             'pelaw_grange','pelaw_grange_bags','towcester','towcester_bags']
            # print(venues)
            # for venue in venues:
            #     cursor.execute(f'DROP TABLE IF EXISTS {venue};')
            #     print("Creating table")
            #     cursor.execute(f'CREATE TABLE {venue}(R1 CHAR(5),\
            #                 R2 CHAR(5),\
            #                 R3 CHAR(5),\
            #                 R4 CHAR(5),\
            #                 R5 CHAR(5),\
            #                 R6 CHAR(5),\
            #                 R7 CHAR(5),\
            #                 R8 CHAR(5),\
            #                 R9 CHAR(5),\
            #                 R10 CHAR(5),\
            #                 R11 CHAR(5),\
            #                 R12 CHAR(5));')
            #     print("Table is created.....")

            ###########################################
            ## TABLE 3
            ###########################################
            # stra_list = []
            print("Creating table")
            cursor.execute('DROP TABLE IF EXISTS strategies_results;')
            cursor.execute('CREATE TABLE strategies_results (venue_id INT PRIMARY KEY AUTO_INCREMENT, num_races INT,\
                                                                Stra1_1 DECIMAL(5,2),Stra1_2 DECIMAL(5,2),Stra1_3 DECIMAL(5,2),Stra1_4 DECIMAL(5,2),Stra1_5 DECIMAL(5,2),Stra1_6 DECIMAL(5,2),\
                                                                Stra2_1 DECIMAL(5,2),Stra2_2 DECIMAL(5,2),Stra2_3 DECIMAL(5,2),Stra2_4 DECIMAL(5,2),Stra2_5 DECIMAL(5,2),Stra2_6 DECIMAL(5,2),\
                                                                Stra3_1 DECIMAL(5,2),Stra3_2 DECIMAL(5,2),Stra3_3 DECIMAL(5,2),Stra3_4 DECIMAL(5,2),Stra3_5 DECIMAL(5,2),Stra3_6 DECIMAL(5,2),\
                                                                Stra4_11 DECIMAL(5,2),Stra4_12 DECIMAL(5,2),Stra4_13 DECIMAL(5,2),Stra4_14 DECIMAL(5,2),Stra4_15 DECIMAL(5,2),Stra4_21 DECIMAL(5,2),Stra4_22 DECIMAL(5,2),Stra4_23 DECIMAL(5,2),Stra4_24 DECIMAL(5,2),Stra4_25 DECIMAL(5,2),Stra4_31 DECIMAL(5,2),Stra4_32 DECIMAL(5,2),Stra4_33 DECIMAL(5,2),Stra4_34 DECIMAL(5,2),Stra4_35 DECIMAL(5,2),Stra4_41 DECIMAL(5,2),Stra4_42 DECIMAL(5,2),Stra4_43 DECIMAL(5,2),Stra4_44 DECIMAL(5,2),Stra4_45 DECIMAL(5,2),Stra4_51 DECIMAL(5,2),Stra4_52 DECIMAL(5,2),Stra4_53 DECIMAL(5,2),Stra4_54 DECIMAL(5,2),Stra4_55 DECIMAL(5,2),Stra4_61 DECIMAL(5,2),Stra4_62 DECIMAL(5,2),Stra4_63 DECIMAL(5,2),Stra4_64 DECIMAL(5,2),Stra4_65 DECIMAL(5,2),\
                                                                Stra5_11 DECIMAL(5,2),Stra5_12 DECIMAL(5,2),Stra5_13 DECIMAL(5,2),Stra5_14 DECIMAL(5,2),Stra5_15 DECIMAL(5,2),Stra5_21 DECIMAL(5,2),Stra5_22 DECIMAL(5,2),Stra5_23 DECIMAL(5,2),Stra5_24 DECIMAL(5,2),Stra5_25 DECIMAL(5,2),Stra5_31 DECIMAL(5,2),Stra5_32 DECIMAL(5,2),Stra5_33 DECIMAL(5,2),Stra5_34 DECIMAL(5,2),Stra5_35 DECIMAL(5,2),Stra5_41 DECIMAL(5,2),Stra5_42 DECIMAL(5,2),Stra5_43 DECIMAL(5,2),Stra5_44 DECIMAL(5,2),Stra5_45 DECIMAL(5,2),Stra5_51 DECIMAL(5,2),Stra5_52 DECIMAL(5,2),Stra5_53 DECIMAL(5,2),Stra5_54 DECIMAL(5,2),Stra5_55 DECIMAL(5,2),Stra5_61 DECIMAL(5,2),Stra5_62 DECIMAL(5,2),Stra5_63 DECIMAL(5,2),Stra5_64 DECIMAL(5,2),Stra5_65 DECIMAL(5,2));')
            print("Table is created.....")

            # for i,row in csvData.iterrows():
            #     if NaN in row:
            #         print(row)
            #         cursor.execute("INSERT INTO race_results VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", tuple(row))
            connection.commit()
except Error as e:
    print(e)