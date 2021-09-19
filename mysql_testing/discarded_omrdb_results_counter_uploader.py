from mysql.connector import connect, Error
import pandas as pd
import numpy as np
import csv

##TODO: Choose type of operation
mode = 1 # 0 = INSERT(used only for the first time); 1 = SELECT & UPDATE 

def main():
    ###########################################
    ## Read the csv and sum up all the entries & get percentages
    ###########################################
    # Read data into a variable
    csvData = pd.read_csv('/home/tranks/scrapeBySelenium/webscraper_for_analytics/mysql_testing/single_venue_strategy_results.csv', delimiter=',', skip_blank_lines=True)

    ## convert the pd dataframe to numpy array
    result = csvData.to_numpy()
    # print(result)

    ## sum up the arrays element-wise and store the result in single array
    venue_id = result[0][0] # copy venue_id value
    sum_arr = result[0]
    for i in range(len(result)-1):
        sum_arr = np.add(sum_arr, result[i+1])
    # print(sum_arr)

    ## pop out the last element, i.e. num_races
    num_races = sum_arr[1] # copy venue_id value
    sum_arr = np.delete(sum_arr,[0,1]) # delete the venue_id and num_races from the array
    # print(sum_arr)
    # print(num_races)

    ## convert into percentages and create the array to be uploaded to mysql
    new_data = np.array([venue_id, num_races])
    for i in range(len(sum_arr)):
        new_data = np.append(new_data, round(float(sum_arr[i]/num_races)*100, 2))
    print(f'new_data: size = {len(new_data)}\n{new_data}')
    
    ###########################################
    ## Upload to mysql server
    ###########################################
    table_name = "strategies_results"
    try:
        with connect(
            host="localhost",
            user='root',
            password='12345',
            database = "online_movie_rating"
        ) as connection:
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute("SELECT database();")
                record = cursor.fetchone()
                print("Your are connected to database: ", record)

                if mode == 0:
                    try:
                        # use INSERT if first time adding results for a venue
                        cursor.execute(f'INSERT INTO {table_name}\
                                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
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
                elif mode == 1:
                    try:
                        ## use  SELECT and UPDATE if not first time
                        cursor.execute(f'SELECT *\
                                        FROM {table_name}\
                                        WHERE venue_id = {venue_id}')
                        old_data = pd.DataFrame(cursor.fetchall()).to_numpy(dtype=float)
                        old_data = old_data[0] # get rid of double brackets and convert to one bracket only
                        print(f'old_data: size = {len(old_data)}\n{old_data}')
                        
                    except Error as e:
                        print(f'Got an error in INSERT')
                        print(e)

                        ## read the values from the table
                        # existing_data = np.zeros((80,), dtype=float)
                        # for i in range(len(result)):
                            # print(i)
                            # existing_data[i] = 5
                    print("Done reading results")

                    ## Update the results
                    updated_data = np.add(old_data, new_data)
                    print(f'updated_data: size = {len(updated_data)}\n{updated_data}')
                    try:
                        cursor.execute(f'UPDATE {table_name}\
                                        SET num_races = {updated_data[1]},\
                                        Stra1_1 = {updated_data[2]},Stra1_2 = {updated_data[3]},Stra1_3 = {updated_data[4]},Stra1_4 = {updated_data[5]},Stra1_5 = {updated_data[6]},Stra1_6 = {updated_data[7]},\
                                        Stra2_1 = {updated_data[8]},Stra2_2 = {updated_data[9]},Stra2_3 = {updated_data[10]},Stra2_4 = {updated_data[11]},Stra2_5 = {updated_data[12]},Stra2_6 = {updated_data[13]},\
                                        Stra3_1 = {updated_data[14]},Stra3_2 = {updated_data[15]},Stra3_3 = {updated_data[16]},Stra3_4 = {updated_data[17]},Stra3_5 = {updated_data[18]},Stra3_6 = {updated_data[19]},\
                                        Stra4_11 = {updated_data[20]},Stra4_12 = {updated_data[21]},Stra4_13 = {updated_data[22]},Stra4_14 = {updated_data[23]},Stra4_15 = {updated_data[24]},Stra4_21 = {updated_data[25]},Stra4_22 = {updated_data[26]},Stra4_23 = {updated_data[27]},Stra4_24 = {updated_data[28]},Stra4_25 = {updated_data[29]},Stra4_31 = {updated_data[30]},Stra4_32 = {updated_data[31]},Stra4_33 = {updated_data[32]},Stra4_34 = {updated_data[33]},Stra4_35 = {updated_data[34]},Stra4_41 = {updated_data[35]},Stra4_42 = {updated_data[36]},Stra4_43 = {updated_data[37]},Stra4_44 = {updated_data[38]},Stra4_45 = {updated_data[39]},Stra4_51 = {updated_data[40]},Stra4_52 = {updated_data[41]},Stra4_53 = {updated_data[42]},Stra4_54 = {updated_data[43]},Stra4_55 = {updated_data[44]},Stra4_61 = {updated_data[45]},Stra4_62 = {updated_data[46]},Stra4_63 = {updated_data[47]},Stra4_64 = {updated_data[48]},Stra4_65 = {updated_data[49]},\
                                        Stra5_11 = {updated_data[50]},Stra5_12 = {updated_data[51]},Stra5_13 = {updated_data[52]},Stra5_14 = {updated_data[53]},Stra5_15 = {updated_data[54]},Stra5_21 = {updated_data[55]},Stra5_22 = {updated_data[56]},Stra5_23 = {updated_data[57]},Stra5_24 = {updated_data[58]},Stra5_25 = {updated_data[59]},Stra5_31 = {updated_data[60]},Stra5_32 = {updated_data[61]},Stra5_33 = {updated_data[62]},Stra5_34 = {updated_data[63]},Stra5_35 = {updated_data[64]},Stra5_41 = {updated_data[65]},Stra5_42 = {updated_data[66]},Stra5_43 = {updated_data[67]},Stra5_44 = {updated_data[68]},Stra5_45 = {updated_data[69]},Stra5_51 = {updated_data[70]},Stra5_52 = {updated_data[71]},Stra5_53 = {updated_data[72]},Stra5_54 = {updated_data[73]},Stra5_55 = {updated_data[74]},Stra5_61 = {updated_data[75]},Stra5_62 = {updated_data[76]},Stra5_63 = {updated_data[77]},Stra5_64 = {updated_data[78]},Stra5_65 = {updated_data[79]}\
                                        WHERE venue_id = {venue_id}')

                    except Error as e:
                        print(f'Got an error in UPDATE')
                        print(e)
                else:
                    print("ERROR! Please chose correct type of mode!!!")

                connection.commit()

    except Error as e:
        print("Error in connection")
        print(e)
    
if __name__ == '__main__':
    main()


