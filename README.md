# webscraper_for_analytics
Scrape data from a ### website and analyse it according to the strategies in this table
<img src="/strategies.png" alt="Current Strategies"/>

Uses Selenium, Python and MySQL

## Requirements
1. Import this folder /webscraper_for_analytics/mysql_testing/Exported_data_from_mysql(backup) into your mysql server (used MySQL workbench in my case)
2. Create a python3 environment
3. $ pip install -r requirements.txt

Others: 
1. chromedriver (in the same version as your current chrome browser version)

## Steps
1. Insert venue links into venue_links.txt
2. $ python3 scraper.py
3. $ python3 data_analyzer.py
4. Look at the results in the 0_xxx and 1_xxx tables

