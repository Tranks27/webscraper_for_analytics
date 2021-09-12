# from getpass import getpass
from mysql.connector import connect, Error
import pandas as pd
import numpy as np

# Read data into a variable
# csvData = pd.read_csv('/home/tranks/scrapeBySelenium/webscraper_for_analytics/New_data.csv', delimiter=',')

try:
    with connect(
        host="localhost",
        # user=input("Enter username: "),
        # password=getpass("Enter password: "),
        user='root',
        password='12345',
        database = "online_movie_rating"
    ) as connection:
        print(connection)

        with connection.cursor() as cursor:
            cursor.execute("SELECT database();")
            record = cursor.fetchone()
            print("Your are connected to database: ", record)
            
            selected_row = 0
            # print("Creating table")
            cursor.execute(f'SELECT *\
	                        FROM testing_data_online_movie_rating\
	                        LIMIT {selected_row},9;')
            result = pd.DataFrame(cursor.fetchall())
            result_np = result.to_numpy()
            # num_rows = int(cursor.rowcount)
            # x = map(list, list(result))
            # x = sum(x, [])

            # D = np.fromiter(iter=x, dtype=float, count=-1)
            # D.reshape(num_rows, -1)

            print(result)
            print(result_np)
            # for x in result:
            #     print(x)
            
            lowest_odds = result_np[0][int(result_np[6][0]) - 1]
            print(f'lowest odds: {lowest_odds}')

# ROW_NUMBER() OVER()  AS row_id\
            
            connection.commit()
except Error as e:
    print(e)