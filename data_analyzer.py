# from getpass import getpass
from mysql.connector import connect, Error
import pandas as pd
import numpy as np
import csv

###########################################
## Upload to mysql server
###########################################
def sql_uploader(new_data, venue_id):
    
    print(f'new_data: size = {len(new_data)}\n{new_data}')
    try:
        with connect(
            host= host_name,
            user= user_name,
            password= pwd,
            database = db_name
        ) as connection:
            print(f'sql_uploader db_connection ACHIEVED!.......... \n{connection}')

            with connection.cursor() as cursor:
                cursor.execute("SELECT database();")
                record = cursor.fetchone()
                print("Your are connected to database: ", record)

                
                if opr_mode == 0:
                    try:
                        # use INSERT if first time adding results for a venue
                        cursor.execute(f'INSERT INTO {percentages_table}\
                                            VALUES(%s,\
                                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s);', tuple(new_data))
                        
                    except Error as e:
                        print(f'Got an error in INSERT')
                        print(e)
                elif opr_mode == 1:
                    print("Opr_mode = 1 selected Error!!!")
                    ''' #TODO Future implementation maybe? 
                        #Reason: currently we trucate the table and insert new data, so requires to read all the tables from the start everytime we run the program
                        #With this operation mode, we could just ingest the latest inserted data and update the percentages table by adding and averaging with the old data.
                        #this mode will be more efficient when the data becomes huge
                    try:
                        ## read the existing data
                        cursor.execute(f'SELECT *\
                                        FROM {percentages_table}\
                                        WHERE venue_id = {venue_id}')
                        old_data = pd.DataFrame(cursor.fetchall()).to_numpy(dtype=float)
                        old_data = old_data[0] # get rid of double brackets and convert to one bracket only
                        print(f'old_data: size = {len(old_data)}\n{old_data}')
                        
                    except Error as e:
                        print(f'Got an error in INSERT')
                        print(e)

                    print("...........Finished reading results")

                    ## Update the data
                    updated_data = np.add(old_data, new_data)
                    updated_data[3:] = np.divide(updated_data[3:],2) # divide the percentages by 2 to get the average, otherwise % will exceed 100% overtime
                    print(f'updated_data: size = {len(updated_data)}\n{updated_data}')
                    try:
                        cursor.execute(f'UPDATE {percentages_table}\
                                        SET num_races = {updated_data[1]}, num_days = {updated_data[2]},\
                                        Stra1_1 = {updated_data[3]},Stra1_2 = {updated_data[4]},Stra1_3 = {updated_data[5]},Stra1_4 = {updated_data[6]},Stra1_5 = {updated_data[7]},Stra1_6 = {updated_data[8]},\
                                        Stra2_1 = {updated_data[9]},Stra2_2 = {updated_data[10]},Stra2_3 = {updated_data[11]},Stra2_4 = {updated_data[12]},Stra2_5 = {updated_data[13]},Stra2_6 = {updated_data[14]},\
                                        Stra3_1 = {updated_data[15]},Stra3_2 = {updated_data[16]},Stra3_3 = {updated_data[17]},Stra3_4 = {updated_data[18]},Stra3_5 = {updated_data[19]},Stra3_6 = {updated_data[20]},\
                                        Stra4_11 = {updated_data[21]},Stra4_12 = {updated_data[22]},Stra4_13 = {updated_data[23]},Stra4_14 = {updated_data[24]},Stra4_15 = {updated_data[25]},Stra4_21 = {updated_data[26]},Stra4_22 = {updated_data[27]},Stra4_23 = {updated_data[28]},Stra4_24 = {updated_data[29]},Stra4_25 = {updated_data[30]},Stra4_31 = {updated_data[31]},Stra4_32 = {updated_data[32]},Stra4_33 = {updated_data[33]},Stra4_34 = {updated_data[34]},Stra4_35 = {updated_data[35]},Stra4_41 = {updated_data[36]},Stra4_42 = {updated_data[37]},Stra4_43 = {updated_data[38]},Stra4_44 = {updated_data[39]},Stra4_45 = {updated_data[40]},Stra4_51 = {updated_data[41]},Stra4_52 = {updated_data[42]},Stra4_53 = {updated_data[43]},Stra4_54 = {updated_data[44]},Stra4_55 = {updated_data[45]},Stra4_61 = {updated_data[46]},Stra4_62 = {updated_data[47]},Stra4_63 = {updated_data[48]},Stra4_64 = {updated_data[49]},Stra4_65 = {updated_data[50]},\
                                        Stra5_11 = {updated_data[51]},Stra5_12 = {updated_data[52]},Stra5_13 = {updated_data[53]},Stra5_14 = {updated_data[54]},Stra5_15 = {updated_data[55]},Stra5_21 = {updated_data[56]},Stra5_22 = {updated_data[57]},Stra5_23 = {updated_data[58]},Stra5_24 = {updated_data[59]},Stra5_25 = {updated_data[60]},Stra5_31 = {updated_data[61]},Stra5_32 = {updated_data[62]},Stra5_33 = {updated_data[63]},Stra5_34 = {updated_data[64]},Stra5_35 = {updated_data[65]},Stra5_41 = {updated_data[66]},Stra5_42 = {updated_data[67]},Stra5_43 = {updated_data[68]},Stra5_44 = {updated_data[69]},Stra5_45 = {updated_data[70]},Stra5_51 = {updated_data[71]},Stra5_52 = {updated_data[72]},Stra5_53 = {updated_data[73]},Stra5_54 = {updated_data[74]},Stra5_55 = {updated_data[75]},Stra5_61 = {updated_data[76]},Stra5_62 = {updated_data[77]},Stra5_63 = {updated_data[78]},Stra5_64 = {updated_data[79]},Stra5_65 = {updated_data[80]}\
                                        WHERE venue_id = {venue_id}')

                    except Error as e:
                        print(f'Got an error in UPDATE')
                        print(e)
                    '''
                else:
                    print("ERROR! Please choose a correct type of operation mode!!!")
                
                connection.commit()
                print(f'sql_uploader db_connection COMMITTED!!!..........\n')

    except Error as e:
        print("Error in connection")
        print(e)


def main():
    try:
        with connect(
            # user=input("Enter username: "),
            # password=getpass("Enter password: "),
            host= host_name,
            user= user_name,
            password= pwd,
            database = db_name
        ) as connection:
            print(f'main db_connection achieved.......... \n{connection}')

            with connection.cursor() as cursor:
                cursor.execute("SELECT database();")
                record = cursor.fetchone()
                print("Your are connected to database: ", record)
                
                
                ###########################################
                ## Apply strategies on each venue, each day 
                ###########################################
                sum_arr = np.zeros((80,), dtype=int)
                days_to_add = 0
                ## Count number of entries in the venue table
                cursor.execute(f'SELECT COUNT(*)\
                                FROM {venue_name};')
                entries_cnt = int(pd.DataFrame(cursor.fetchone()).to_numpy())
                # print(f'row count = {entries_cnt}')
                
                ## Start the operation of calculating strategy results 
                for starting_row in range(0,entries_cnt-1,9):
                    # print(f'starting_row = {starting_row}')
                    days_to_add = days_to_add + 1
                    ## select the 9 rows block
                    cursor.execute(f'SELECT *\
                                    FROM {venue_name}\
                                    LIMIT {starting_row},9;')
                    result = pd.DataFrame(cursor.fetchall())
                    # print(result.to_numpy())
                    result_np = result.to_numpy().transpose() #transpose the matrix so that each row contains each race's data
                    # print(result_np)
                    
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
                            # print(f'rank123_odds: {rank1_odds}, {rank2_odds}, {rank3_odds}')

                            ## Odds of the first 3 favorites 
                            original_odds = result_np[race_i][:6]
                            print(f'original odds = {original_odds}')
                            sorted_odds = sorted(original_odds, key=float) #comparison between the first 6 players' odds
                            # print(f'sorted odds = {sorted_odds}')
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

                    # convert stra 4 & 5 into 1-d array
                    stra4_cnts = np.reshape(stra4_cnts, 30)
                    stra5_cnts = np.reshape(stra5_cnts, 30)
                    # print(f'Strategy 1: \n{stra1_cnts}\n')
                    # print(f'Strategy 2: \n{stra2_cnts}\n')
                    # print(f'Strategy 3: \n{stra3_cnts}\n')
                    # print(f'Strategy 4: \n{stra4_cnts}\n')
                    # print(f'Strategy 5: \n{stra5_cnts}\n')

                    ## merge all the strategies in single array
                    all_stras = [stra1_cnts,stra2_cnts,stra3_cnts,stra4_cnts,stra5_cnts]
                    merged_stras = np.concatenate(all_stras)

                    ## prepend two values at the beginning
                    non_abandoned_cnt = races_cnt - abandon_cnt # number of non-abandoned races in the venue each day
                    merged_stras = np.insert(merged_stras, 0,non_abandoned_cnt) # prepend the num_races
                    merged_stras = np.insert(merged_stras, 0,venue_id) # prepend the venue_id
                    # print(f'merged_stras = \n{merged_stras}')
                    
                    ## Accumulate the data for each day
                    sum_arr = np.add(sum_arr, merged_stras)

                ###########################################
                ## Get the percentages array
                ###########################################        
                num_races = sum_arr[1]
                sum_arr = np.delete(sum_arr,[0,1]) # delete the venue_id and num_races from the array
                ## convert into percentages and create the array to be uploaded to mysql
                new_data = np.array([venue_id, num_races, days_to_add])
                for i in range(len(sum_arr)):
                    new_data = np.append(new_data, round(float(sum_arr[i]/num_races)*100, 2))
                # print(f'new_data: size = {len(new_data)}\n{new_data}')
                
                connection.commit()
                print(f'main db_connection COMMITTED!!!..........\n')
    except Error as e:
        print(e)

    ###########################################
    ## Call sql_uploader()
    ########################################### 
    sql_uploader(new_data, venue_id)

###########################################
## Update the final overall percentages table
########################################### 
def overall_analytics_updater():
    try:
        with connect(
            host= host_name,
            user= user_name,
            password= pwd,
            database = db_name
        ) as connection:
            print(f'overall_analytics_updater db_connection ACHIEVED!.......... \n{connection}')

            with connection.cursor() as cursor:
                cursor.execute("SELECT database();")
                record = cursor.fetchone()
                print("Your are connected to database: ", record)

                ## Count number of entries in the venue table
                cursor.execute(f'SELECT COUNT(*)\
                                FROM {percentages_table};')
                rows_cnt = int(pd.DataFrame(cursor.fetchone()).to_numpy())
                
                print(f'rows_cnt = {rows_cnt}')

                ## Get all the entries and add them up
                cursor.execute(f'SELECT *\
                                FROM {percentages_table};')
                
                overall_data = pd.DataFrame(cursor.fetchall()).to_numpy(dtype=float)
                print(f'overall_data: size = {len(overall_data)}\n{overall_data}')
                # overall_data = overall_data[0] # get rid of double brackets and convert to one bracket only
                # print(f'overall_data: size = {len(overall_data)}\n{overall_data}')
                
                ## Update the data
                updated_overall_data = overall_data[0]
                for i,data_i in enumerate(overall_data):
                    if i > 0:
                        updated_overall_data = np.add(updated_overall_data, data_i)
                        
                updated_overall_data[3:] = np.divide(updated_overall_data[3:],rows_cnt).round(decimals=2) # divide the percentages by 2 to get the average, otherwise % will exceed 100% overtime
                np.set_printoptions(suppress=True) # get rid of scientific notation
                updated_overall_data = np.delete(updated_overall_data,[0,2]) # delete venue_id and num_days
                updated_overall_data = np.insert(updated_overall_data,0,1) # put overall_id = 1 #TODO hardcoded
                # print(f'updated_overall_data: size = {len(updated_overall_data)}\n{updated_overall_data}')
                
                ## upload to the overall_analytics_table in mysql server
                try:
                    # use INSERT if first time adding results for a venue
                    cursor.execute(f'INSERT INTO {overall_table}\
                                        VALUES(\
                                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s);', tuple(updated_overall_data))
                    
                except Error as e:
                    print(f'Got an error in INSERT')
                    print(e)


                connection.commit()
                print(f'overall_analytics_updater db_connection COMMITTED!!!..........\n')
    except Error as e:
        print(e)

def table_truncater():
    try:
        with connect(
            host= host_name,
            user= user_name,
            password= pwd,
            database = db_name
        ) as connection:
            print(f'overall_analytics_updater db_connection ACHIEVED!.......... \n{connection}')

            with connection.cursor() as cursor:
                cursor.execute("SELECT database();")
                record = cursor.fetchone()
                print("Your are connected to database: ", record)

                ## truncate the tables 0 and 1
                cursor.execute(f'TRUNCATE TABLE {percentages_table}')
                cursor.execute(f'TRUNCATE TABLE {overall_table}')

                connection.commit()
                print(f'table_truncater db_connection COMMITTED!!!..........\n')

    except Error as e:
        print(f'Got an error in INSERT')
        print(e)

###########################################
## check if a string is of float type
########################################### 
def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

###########################################
## load the scraped data to mysql server according to venue names
########################################### 
def import_csvData_to_mysql(csv_fname):
    # Read data into a variable
    csvData = pd.read_csv(csv_fname, delimiter=',')
    # print(csvData)
    try:
        with connect(
            host= host_name,
            user= user_name,
            password= pwd,
            database = db_name
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
    # ##TODO: Choose type of operation
    opr_mode = 0 # 0 = INSERT(used only for the first time); 1 = SELECT & UPDATE existing data
    csv_fname = './New_data.csv'
    percentages_table = '1_indv_venue_analytics'
    overall_table = '0_overall_analytics'
    
    # mysql server deets
    host_name = 'localhost'
    user_name = 'root'
    pwd = '12345'
    db_name = 'test'

    venue_names = ('central_park', 'central_park_bags', 'crayford', 'crayford_bags', 'doncaster',\
                    'doncaster_bags', 'harlow', 'harlow_bags', 'henlow', 'henlow_bags',\
                    'hove', 'hove_bags', 'kinsley_bags', 'monmore', 'newcastle_bags',\
                    'nottingham_bags', 'pelaw_grange_bags', 'perry_barr_bags', 'romford', 'romford_bags',\
                    'sheffield_bags', 'sunderland_bags', 'swindon_bags', 'towcester', 'towcester_bags',\
                    'yarmouth_bags') # total 26 venues
    
    import_csvData_to_mysql(csv_fname) # read csv file called "New_data.csv" and upload the data into mysql server
    table_truncater() # clear out the values from the tables 0 and 1
    
    for v_i,v_name in enumerate(venue_names):
        ## Loop through all the venues 
        venue_name = v_name # name of venue table that we want to extract new data form
        venue_id = v_i + 1 # opr_mode 0: venue_id for new venue, opr_mode 1: venue_id that we want to update. NOTE: venue_id is only defined in the percentages table, not in the actual venue table, hence the necessity of inputing both venue_id & venue_name
        
        # print(f'venue_name = {venue_name}, id = {venue_id}')
        ## Start main, apply strategies
        main()

    overall_analytics_updater() # update the final overall table

