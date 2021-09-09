import csv
# from getpass import getpass
from mysql.connector import connect, Error
import pandas as pd

# def data_channeller(row, )
def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def main():
    # Read data into a variable
    csvData = pd.read_csv('/home/tranks/scrapeBySelenium/webscraper_for_analytics/New_data.csv', delimiter=',')
    # print(csvData)
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

                ## Import the data into their respective venue tables
                for index,row in csvData.iterrows():
                    # Check for the venue_name headers
                    if not row[0].isdigit() and not is_float(row[0]):
                        data = csvData.iloc[index+1:index+10]
                        # print(data)
                        for i,r in data.iterrows():
                            try:
                                cursor.execute(f'INSERT INTO {row[0]} VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', tuple(r))
                            except Error as e:
                                print(f'Got to error in executing row number {i}')
                                print(e)
                connection.commit()
    except Error as e:
        print("Error in connection")
        print(e)



if __name__ == '__main__':
    main()