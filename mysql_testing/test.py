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
            result_np = result.to_numpy().transpose() #transpose the matrix so that each row contains each race's data

            # print(result)
            print(result_np)

            ## Odds by ranking
            rank1_odds = result_np[0][int(result_np[0][6]) - 1]
            rank2_odds = result_np[0][int(result_np[0][7]) - 1]
            rank3_odds = result_np[0][int(result_np[0][8]) - 1]
            print(f'rank123_odds: {rank1_odds}, {rank2_odds}, {rank3_odds}')
            # print(f'here: {result_np[int(result_np[8][0]) - 1][0]}')

            ## Odds of the first 3 favorites 
            lowest1_odds = sorted(result_np[0][:5])[0] #comparison between the first 6 players' odds
            lowest2_odds = sorted(result_np[0][:5])[1]
            lowest3_odds = sorted(result_np[0][:5])[2]
            print(f'lowest123_odds: {lowest1_odds}, {lowest2_odds}, {lowest3_odds}')

            stra1_cnts = np.zeros((6,), dtype=int)
            stra2_cnts = np.zeros((5,6), dtype=int)
            stra3_cnts = np.zeros((5,6), dtype=int)

            print(f'Strategy 1: \n{stra1_cnts}\n')
            print(f'Strategy 2: \n{stra2_cnts}\n')
            print(f'Strategy 3: \n{stra3_cnts}\n')
            connection.commit()
except Error as e:
    print(e)