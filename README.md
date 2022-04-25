# webscraper_for_analytics
Scrape data from a betting website and extract desired data into MySQL server tables for analysis. Strategies analysed are as shown here.
<img src="/strategies.png" alt="Current Strategies"/>

Uses Selenium, Python and MySQL

## Requirements
1. Install MySQL Workbench, start connection to local MySQL server and create a database named "test"
2. Import this folder /webscraper_for_analytics/mysql_testing/Exported_data_from_mysql(backup) into your mysql server
3. Create a python3 environment with
```
  $ pip3 install virtualenv
  $ virtualenv venv
  $ source venv/bin/activate
```
4. Install the required modules
```
  $ pip3 install -r requirements.txt
```
5. Install the chromedriver (in the same version as your current chromium/google chrome browser version)
- Download the chromedriver from the offcial website here. https://chromedriver.chromium.org/
- Move the chromedriver to file in PATH
```
  $ sudo mv ~/path/to/chromedriver /usr/local/bin/
  $ sudo chmod +x /usr/local/bin/chromedriver
```

## Steps to follow for demo
1. Insert venue links into venue_links.txt.
2. $ python3 scraper.py
3. Check for TBD values in the New_data.csv.
4. $ python3 data_analyzer.py
5. Look at the results in the 0_xxx and 1_xxx tables

## NOTE
1. [STEP 1] Avoid venues with 'CLOSED' races.
2. [STEP 3] Replace the whole race with '-' if found.
