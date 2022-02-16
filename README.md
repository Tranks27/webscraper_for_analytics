# webscraper_for_analytics
Scrape data from a Neds website and extract desired data into MySQL server tables for analysis. Strategies analysed are as shown here.
<img src="/strategies.png" alt="Current Strategies"/>

Uses Selenium, Python and MySQL

## Requirements
1. Import this folder /webscraper_for_analytics/mysql_testing/Exported_data_from_mysql(backup) into your mysql server (used MySQL workbench in my case)
2. Create a python3 environment
3. $ pip install -r requirements.txt

Others: 
1. chromedriver (in the same version as your current chrome browser version)
2. others maybe?

## Steps
1. Insert venue links into venue_links.txt.
2. $ python3 scraper.py
3. Check for TBD values in the New_data.csv.
4. $ python3 data_analyzer.py
5. Look at the results in the 0_xxx and 1_xxx tables

## NOTE
1. [STEP 1] Avoid venues with 'CLOSED' races.
2. [STEP 3] Replace the whole race with '-' if found.
