# from getpass import getpass
from mysql.connector import connect, Error
import pandas as pd
import numpy as np

import csv
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

            # Variables to store counts
            stra1_cnts = np.zeros((6,), dtype=int)
            stra2_cnts = np.zeros((6,), dtype=int)
            stra3_cnts = np.zeros((6,), dtype=int)
            stra4_cnts = np.zeros((6,5), dtype=int)
            stra5_cnts = np.zeros((6,5), dtype=int)
            num_players = 6

            # Replace '-' with 'inf' since '-' is not float and thus can't be sorted() and min()
            result_np = np.where(result_np == '-', 'inf', result_np)
            
            # print("after")
            # print(result_np)

            for race_i,current_race in enumerate(result_np):
                print(race_i)
                print(current_race)
                dash_count = np.count_nonzero(current_race == 'inf')

                # Skip if abandoned race
                # 9 '-'s mean whole race is abandoned, not just player scratching 
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
                    original_odds = result_np[race_i][:6]
                    print(f'original odds = {original_odds}')
                    sorted_odds = sorted(original_odds, key=float) #comparison between the first 6 players' odds
                    print(f'sorted odds = {sorted_odds}')
                    lowest1_odds = sorted_odds[0] 
                    lowest2_odds = sorted_odds[1]
                    lowest3_odds = sorted_odds[2]
                    lowest4_odds = sorted_odds[3]
                    lowest5_odds = sorted_odds[4]
                    lowest6_odds = sorted_odds[5]
                    # print(f'lowest123_odds: {lowest1_odds}, {lowest2_odds}, {lowest3_odds},{lowest4_odds}, {lowest5_odds}, {lowest6_odds}')
                    
                    ###########################################
                    ## Strategy 1: Who wins?
                    ###########################################
                    if(rank1_odds == lowest1_odds):
                        stra1_cnts[0] = stra1_cnts[0] + 1
                    if(rank1_odds == lowest2_odds):
                        stra1_cnts[1] = stra1_cnts[1] + 1
                    if(rank1_odds == lowest3_odds):
                        stra1_cnts[2] = stra1_cnts[2] + 1
                    if(rank1_odds == lowest4_odds):
                        stra1_cnts[3] = stra1_cnts[3] + 1
                    if(rank1_odds == lowest5_odds):
                        stra1_cnts[4] = stra1_cnts[4] + 1
                    if(rank1_odds == lowest6_odds):
                        stra1_cnts[5] = stra1_cnts[5] + 1

                    ###########################################
                    ## Strategy 2: Who's second?
                    ###########################################
                    if(rank2_odds == lowest1_odds):
                        stra2_cnts[0] = stra2_cnts[0] + 1
                    if(rank2_odds == lowest2_odds):
                        stra2_cnts[1] = stra2_cnts[1] + 1
                    if(rank2_odds == lowest3_odds):
                        stra2_cnts[2] = stra2_cnts[2] + 1
                    if(rank2_odds == lowest4_odds):
                        stra2_cnts[3] = stra2_cnts[3] + 1
                    if(rank2_odds == lowest5_odds):
                        stra2_cnts[4] = stra2_cnts[4] + 1
                    if(rank2_odds == lowest6_odds):
                        stra2_cnts[5] = stra2_cnts[5] + 1

                    ###########################################
                    ## Strategy 3: Who's third?
                    ###########################################
                    if(rank3_odds == lowest1_odds):
                        stra3_cnts[0] = stra3_cnts[0] + 1
                    if(rank3_odds == lowest2_odds):
                        stra3_cnts[1] = stra3_cnts[1] + 1
                    if(rank3_odds == lowest3_odds):
                        stra3_cnts[2] = stra3_cnts[2] + 1
                    if(rank3_odds == lowest4_odds):
                        stra3_cnts[3] = stra3_cnts[3] + 1
                    if(rank3_odds == lowest5_odds):
                        stra3_cnts[4] = stra3_cnts[4] + 1
                    if(rank3_odds == lowest6_odds):
                        stra3_cnts[5] = stra3_cnts[5] + 1

                    ###########################################
                    ## Strategy 4: forecast based on odds
                    ###########################################
                    if(rank1_odds == sorted_odds[0]):     # fav wins
                        if(rank2_odds == sorted_odds[1]): # check who comes after
                            stra4_cnts[0][0] = stra4_cnts[0][0] + 1
                        elif(rank2_odds == sorted_odds[2]):
                            stra4_cnts[0][1] = stra4_cnts[0][1] + 1
                        elif(rank2_odds == sorted_odds[3]):
                            stra4_cnts[0][2] = stra4_cnts[0][2] + 1
                        elif(rank2_odds == sorted_odds[4]):
                            stra4_cnts[0][3] = stra4_cnts[0][3] + 1
                        elif(rank2_odds == sorted_odds[5]):
                            stra4_cnts[0][4] = stra4_cnts[0][4] + 1
                    elif(rank1_odds == sorted_odds[1]):   # 2nd fav wins
                        if(rank2_odds == sorted_odds[0]):
                            stra4_cnts[1][0] = stra4_cnts[1][0] + 1
                        elif(rank2_odds == sorted_odds[2]):
                            stra4_cnts[1][1] = stra4_cnts[1][1] + 1
                        elif(rank2_odds == sorted_odds[3]):
                            stra4_cnts[1][2] = stra4_cnts[1][2] + 1
                        elif(rank2_odds == sorted_odds[4]):
                            stra4_cnts[1][3] = stra4_cnts[1][3] + 1
                        elif(rank2_odds == sorted_odds[5]):
                            stra4_cnts[1][4] = stra4_cnts[1][4] + 1
                    elif(rank1_odds == sorted_odds[2]):   # 3rd fav wins
                        if(rank2_odds == sorted_odds[0]):
                            stra4_cnts[2][0] = stra4_cnts[2][0] + 1
                        elif(rank2_odds == sorted_odds[1]):
                            stra4_cnts[2][1] = stra4_cnts[2][1] + 1
                        elif(rank2_odds == sorted_odds[3]):
                            stra4_cnts[2][2] = stra4_cnts[2][2] + 1
                        elif(rank2_odds == sorted_odds[4]):
                            stra4_cnts[2][3] = stra4_cnts[2][3] + 1
                        elif(rank2_odds == sorted_odds[5]):
                            stra4_cnts[2][4] = stra4_cnts[2][4] + 1     
                    elif(rank1_odds == sorted_odds[3]):   # 4th fav wins
                        if(rank2_odds == sorted_odds[0]):
                            stra4_cnts[3][0] = stra4_cnts[3][0] + 1
                        elif(rank2_odds == sorted_odds[1]):
                            stra4_cnts[3][1] = stra4_cnts[3][1] + 1
                        elif(rank2_odds == sorted_odds[2]):
                            stra4_cnts[3][2] = stra4_cnts[3][2] + 1
                        elif(rank2_odds == sorted_odds[4]):
                            stra4_cnts[3][3] = stra4_cnts[3][3] + 1
                        elif(rank2_odds == sorted_odds[5]):
                            stra4_cnts[3][4] = stra4_cnts[3][4] + 1
                    elif(rank1_odds == sorted_odds[4]):   # 5th fav wins
                        if(rank2_odds == sorted_odds[0]):
                            stra4_cnts[4][0] = stra4_cnts[4][0] + 1
                        elif(rank2_odds == sorted_odds[1]):
                            stra4_cnts[4][1] = stra4_cnts[4][1] + 1
                        elif(rank2_odds == sorted_odds[2]):
                            stra4_cnts[4][2] = stra4_cnts[4][2] + 1
                        elif(rank2_odds == sorted_odds[3]):
                            stra4_cnts[4][3] = stra4_cnts[4][3] + 1
                        elif(rank2_odds == sorted_odds[5]):
                            stra4_cnts[4][4] = stra4_cnts[4][4] + 1
                    elif(rank1_odds == sorted_odds[5]):   # 6th fav wins
                        if(rank2_odds == sorted_odds[0]):
                            stra4_cnts[5][0] = stra4_cnts[5][0] + 1
                        elif(rank2_odds == sorted_odds[1]):
                            stra4_cnts[5][1] = stra4_cnts[5][1] + 1
                        elif(rank2_odds == sorted_odds[2]):
                            stra4_cnts[5][2] = stra4_cnts[5][2] + 1
                        elif(rank2_odds == sorted_odds[3]):
                            stra4_cnts[5][3] = stra4_cnts[5][3] + 1
                        elif(rank2_odds == sorted_odds[4]):
                            stra4_cnts[5][4] = stra4_cnts[5][4] + 1

                    ###########################################
                    ## Strategy 5: forecast based on boxes
                    ###########################################
                    if(rank1_odds == original_odds[0]):     # box 1 wins
                        if(rank2_odds == original_odds[1]): # check who comes after
                            stra5_cnts[0][0] = stra5_cnts[0][0] + 1
                        elif(rank2_odds == original_odds[2]):
                            stra5_cnts[0][1] = stra5_cnts[0][1] + 1
                        elif(rank2_odds == original_odds[3]):
                            stra5_cnts[0][2] = stra5_cnts[0][2] + 1
                        elif(rank2_odds == original_odds[4]):
                            stra5_cnts[0][3] = stra5_cnts[0][3] + 1
                        elif(rank2_odds == original_odds[5]):
                            stra5_cnts[0][4] = stra5_cnts[0][4] + 1
                    elif(rank1_odds == original_odds[1]):   # box 2 wins
                        if(rank2_odds == original_odds[0]):
                            stra5_cnts[1][0] = stra5_cnts[1][0] + 1
                        elif(rank2_odds == original_odds[2]):
                            stra5_cnts[1][1] = stra5_cnts[1][1] + 1
                        elif(rank2_odds == original_odds[3]):
                            stra5_cnts[1][2] = stra5_cnts[1][2] + 1
                        elif(rank2_odds == original_odds[4]):
                            stra5_cnts[1][3] = stra5_cnts[1][3] + 1
                        elif(rank2_odds == original_odds[5]):
                            stra5_cnts[1][4] = stra5_cnts[1][4] + 1
                    elif(rank1_odds == original_odds[2]):   # box 3 wins
                        if(rank2_odds == original_odds[0]):
                            stra5_cnts[2][0] = stra5_cnts[2][0] + 1
                        elif(rank2_odds == original_odds[1]):
                            stra5_cnts[2][1] = stra5_cnts[2][1] + 1
                        elif(rank2_odds == original_odds[3]):
                            stra5_cnts[2][2] = stra5_cnts[2][2] + 1
                        elif(rank2_odds == original_odds[4]):
                            stra5_cnts[2][3] = stra5_cnts[2][3] + 1
                        elif(rank2_odds == original_odds[5]):
                            stra5_cnts[2][4] = stra5_cnts[2][4] + 1     
                    elif(rank1_odds == original_odds[3]):   # box 4 wins
                        if(rank2_odds == original_odds[0]):
                            stra5_cnts[3][0] = stra5_cnts[3][0] + 1
                        elif(rank2_odds == original_odds[1]):
                            stra5_cnts[3][1] = stra5_cnts[3][1] + 1
                        elif(rank2_odds == original_odds[2]):
                            stra5_cnts[3][2] = stra5_cnts[3][2] + 1
                        elif(rank2_odds == original_odds[4]):
                            stra5_cnts[3][3] = stra5_cnts[3][3] + 1
                        elif(rank2_odds == original_odds[5]):
                            stra5_cnts[3][4] = stra5_cnts[3][4] + 1
                    elif(rank1_odds == original_odds[4]):   # box 5 wins
                        if(rank2_odds == original_odds[0]):
                            stra5_cnts[4][0] = stra5_cnts[4][0] + 1
                        elif(rank2_odds == original_odds[1]):
                            stra5_cnts[4][1] = stra5_cnts[4][1] + 1
                        elif(rank2_odds == original_odds[2]):
                            stra5_cnts[4][2] = stra5_cnts[4][2] + 1
                        elif(rank2_odds == original_odds[3]):
                            stra5_cnts[4][3] = stra5_cnts[4][3] + 1
                        elif(rank2_odds == original_odds[5]):
                            stra5_cnts[4][4] = stra5_cnts[4][4] + 1
                    elif(rank1_odds == original_odds[5]):   # box 6 wins
                        if(rank2_odds == original_odds[0]):
                            stra5_cnts[5][0] = stra5_cnts[5][0] + 1
                        elif(rank2_odds == original_odds[1]):
                            stra5_cnts[5][1] = stra5_cnts[5][1] + 1
                        elif(rank2_odds == original_odds[2]):
                            stra5_cnts[5][2] = stra5_cnts[5][2] + 1
                        elif(rank2_odds == original_odds[3]):
                            stra5_cnts[5][3] = stra5_cnts[5][3] + 1
                        elif(rank2_odds == original_odds[4]):
                            stra5_cnts[5][4] = stra5_cnts[5][4] + 1
            
            print(f'Strategy 1: \n{stra1_cnts}\n')
            print(f'Strategy 2: \n{stra2_cnts}\n')
            print(f'Strategy 3: \n{stra3_cnts}\n')
            print(f'Strategy 4: \n{stra4_cnts}\n')
            print(f'Strategy 5: \n{stra5_cnts}\n')
                


            connection.commit()
except Error as e:
    print(e)