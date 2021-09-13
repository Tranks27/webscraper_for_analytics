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
            # print(result.to_numpy())
            result_np = result.to_numpy().transpose() #transpose the matrix so that each row contains each race's data
            # for i in result_np:
            # result_np = list(result_np)
            
            print(result_np)
            # result_np = np.array2string(result_np, separator=',')

            stra1_cnts = np.zeros((6,), dtype=int)
            stra2_cnts = np.zeros((6,), dtype=int)
            stra3_cnts = np.zeros((5,6), dtype=int)
            stra4_cnts = np.zeros((5,6), dtype=int)

            result_np = np.where(result_np == '-', 'inf', result_np)
            
            # print("after")
            # print(result_np)

            for race_i,current_race in enumerate(result_np):
                print(race_i)
                print(current_race)
                dash_count = np.count_nonzero(current_race == 'inf')
                if dash_count == 9:
                    print("Abandoned race found! Skip!!!")
                    # result_np = np.delete(result_np, race_i, 0)
                else:
                    ## Odds by ranking
                    rank1_odds = result_np[race_i][int(result_np[race_i][6]) - 1]
                    rank2_odds = result_np[race_i][int(result_np[race_i][7]) - 1]
                    rank3_odds = result_np[race_i][int(result_np[race_i][8]) - 1]
                    print(f'rank123_odds: {rank1_odds}, {rank2_odds}, {rank3_odds}')

                    ## Odds of the first 3 favorites 
                    sorted_odds = sorted(result_np[race_i][:6], key=float) #comparison between the first 6 players' odds
                    print(f'sorted odds = {sorted_odds}')
                    lowest1_odds = sorted_odds[0] 
                    lowest2_odds = sorted_odds[1]
                    lowest3_odds = sorted_odds[2]
                    lowest4_odds = sorted_odds[3]
                    lowest5_odds = sorted_odds[4]
                    lowest6_odds = sorted_odds[5]
                    print(f'lowest123_odds: {lowest1_odds}, {lowest2_odds}, {lowest3_odds},{lowest4_odds}, {lowest5_odds}, {lowest6_odds}')

                    if(lowest1_odds == rank1_odds):
                        stra1_cnts[0] = stra1_cnts[0] + 1
                    elif(lowest2_odds == rank1_odds):
                        stra1_cnts[1] = stra1_cnts[1] + 1
                    elif(lowest3_odds == rank1_odds):
                        stra1_cnts[2] = stra1_cnts[2] + 1
                    elif(lowest4_odds == rank1_odds):
                        stra1_cnts[3] = stra1_cnts[3] + 1
                    elif(lowest5_odds == rank1_odds):
                        stra1_cnts[4] = stra1_cnts[4] + 1
                    elif(lowest6_odds == rank1_odds):
                        stra1_cnts[5] = stra1_cnts[5] + 1

            print(f'Strategy 1: \n{stra1_cnts}\n')
            print(f'Strategy 2: \n{stra2_cnts}\n')
            print(f'Strategy 3: \n{stra3_cnts}\n')
            print(f'Strategy 4: \n{stra4_cnts}\n')


            


            connection.commit()
except Error as e:
    print(e)