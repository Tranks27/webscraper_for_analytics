from mysql.connector import connect, Error
import pandas as pd
import numpy as np
import csv


def main():
    # Read data into a variable
    csvData = pd.read_csv('/home/tranks/scrapeBySelenium/webscraper_for_analytics/mysql_testing/single_venue_strategy_results.csv', delimiter=',', skip_blank_lines=True)

    ## convert the pd dataframe to numpy array
    result = csvData.to_numpy()
    print(result)

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
    percentage_sum_arr = np.array([venue_id, num_races])
    for i in range(len(sum_arr)):
        percentage_sum_arr = np.append(percentage_sum_arr, round(float(sum_arr[i]/num_races)*100, 2))
    print(percentage_sum_arr)

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

                try:
                    ## use INSERT if first time adding results for a venue
                    # cursor.execute(f'INSERT INTO {table_name} VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                    #                                                     %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                    #                                                     %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                    #                                                     %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                    #                                                     %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                    #                                                     %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                    #                                                     %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                    #                                                     %s,%s,%s,%s,%s,%s,%s,%s,%s,%s);', tuple(percentage_sum_arr))
                    
                    ## use  SELECT and UPDATE if not first time
                    cursor.execute(f'SELECT *\
                                    FROM {table_name}\
                                    WHERE venue_id = {venue_id}')
                    result = pd.DataFrame(cursor.fetchall()).to_numpy(dtype=float)
                    result = result[0] # get rid of double brackets and convert to one bracket only
                    print(result)


                    ## read the values from the table
                    # existing_data = np.zeros((80,), dtype=float)
                    # for i in range(len(result)):
                        # print(i)
                        # existing_data[i] = 5
                    print("Done reading results")

                    cursor.execute(f'UPDATE {table_name}\
                                    SET num_races = 6\
                                    WHERE venue_id = {venue_id}')

                    # print(existing_data)
                except Error as e:
                    print(f'Got an error in INSERT/UPDATE')
                    print(e)

                connection.commit()

    except Error as e:
        print("Error in connection")
        print(e)

if __name__ == '__main__':
    main()


