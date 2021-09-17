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
            
            
            ###########################################
            ## Apply strategies on each venue, each day 
            ###########################################
            venue_name = 'testing_data_online_movie_rating'
            venue_id = 1
            for starting_row in range(0,80,9):
                print(starting_row)
               
                # starting_row = 0
                
                cursor.execute(f'SELECT *\
                                FROM {venue_name}\
                                LIMIT {starting_row},9;')
                result = pd.DataFrame(cursor.fetchall())
                # print(result.to_numpy())
                result_np = result.to_numpy().transpose() #transpose the matrix so that each row contains each race's data
                print(result_np)
                
                ## Variables to store counts
                stra1_cnts = np.zeros((6,), dtype=int)
                stra2_cnts = np.zeros((6,), dtype=int)
                stra3_cnts = np.zeros((6,), dtype=int)
                stra4_cnts = np.zeros((6,5), dtype=int)
                stra5_cnts = np.zeros((6,5), dtype=int)
                num_players = 6
                races_cnt = 12

                # Replace '-' with 'inf' since '-' is not float and thus can't be sorted() and min()
                result_np = np.where(result_np == '-', 'inf', result_np)
                # print("after")
                # print(result_np)
            
                ## Go through all 12 races
                for race_i,current_race in enumerate(result_np):
                    # print(race_i)
                    # print(current_race)
                    dash_count = np.count_nonzero(current_race == 'inf')
                    abandon_cnt = 0 # count the number of abandoned races

                    # Skip if abandoned race
                    # 9 '-'s mean whole race is abandoned, not just player scratching 
                    if dash_count == 9: 
                        print("Abandoned race found! Skip!!!")
                        abandon_cnt = abandon_cnt + 1
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
            
                non_abandoned_cnt = races_cnt - abandon_cnt # number of non-abandoned races in the venue each day
                print(f'Strategy 1: \n{stra1_cnts}\n')
                print(f'Strategy 2: \n{stra2_cnts}\n')
                print(f'Strategy 3: \n{stra3_cnts}\n')
                # print(f'Strategy 4: \n{stra4_cnts}\n')
                # print(f'Strategy 5: \n{stra5_cnts}\n')

                # convert stra4 & 5 into 1-d array
                stra4_cnts = np.reshape(stra4_cnts, 30)
                stra5_cnts = np.reshape(stra5_cnts, 30)
                print(f'Strategy 4: \n{stra4_cnts}\n')
                print(f'Strategy 5: \n{stra5_cnts}\n')

                ## merge all the strategies in single array
                all_stras = [stra1_cnts,stra2_cnts,stra3_cnts,stra4_cnts,stra5_cnts]
                merged_stras = np.concatenate(all_stras)
                merged_stras = np.insert(merged_stras, 0,non_abandoned_cnt) # prepend the num_races
                merged_stras = np.insert(merged_stras, 0,venue_id) # prepend the venue_id

                ## Write/Append the current venue's data into the file
                with open('single_venue_strategy_results.csv', 'a+') as f:
                    writer = csv.writer(f)

                    # check if the file is empty: if NO, write newline char, if YES do nothing,
                    f.seek(0) # Move read cursor to the start of file
                    data = f.read(10)
                    if len(data) > 0:
                        f.write("\n")
                    else:
                        writer.writerow(['venue_id','num_races',\
                                        'Stra1_1','Stra1_2','Stra1_3','Stra1_4','Stra1_5','Stra1_6',\
                                        'Stra2_1','Stra2_2','Stra2_3','Stra2_4','Stra2_5','Stra2_6',\
                                        'Stra3_1','Stra3_2','Stra3_3','Stra3_4','Stra3_5','Stra3_6',\
                                        'Stra4_11','Stra4_12','Stra4_13','Stra4_14','Stra4_15','Stra4_21','Stra4_22','Stra4_23','Stra4_24','Stra4_25','Stra4_31','Stra4_32','Stra4_33','Stra4_34','Stra4_35','Stra4_41','Stra4_42','Stra4_43','Stra4_44','Stra4_45','Stra4_51','Stra4_52','Stra4_53','Stra4_54','Stra4_55','Stra4_61','Stra4_62','Stra4_63','Stra4_64','Stra4_65',\
                                        'Stra5_11','Stra5_12','Stra5_13','Stra5_14','Stra5_15','Stra5_21','Stra5_22','Stra5_23','Stra5_24','Stra5_25','Stra5_31','Stra5_32','Stra5_33','Stra5_34','Stra5_35','Stra5_41','Stra5_42','Stra5_43','Stra5_44','Stra5_45','Stra5_51','Stra5_52','Stra5_53','Stra5_54','Stra5_55','Stra5_61','Stra5_62','Stra5_63','Stra5_64','Stra5_65'])
                    
                    writer.writerow(merged_stras)


            connection.commit()
except Error as e:
    print(e)