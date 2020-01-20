# Zerodha Test Project: Bhavcopy 

## Problem Statement:

BSE publishes a "Bhavcopy" file every day here: https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx

1. Write a Python script that:
    - Download the Equity bhavcopy zip from the above page
    - Extract and parses the CSV file in it
    - Write the records into Redis into appropriate data structures
    - (Fields: code, name, open, high, low, close)
2. Write a simple CherryPy python web application that:
    - Renders an HTML5 + CSS3 page that lists the top 10 stock entries from the Redis DB in a table
    - Has a searchbox that lets you search the entries by the 'name' field in Redis and renders it in a table
    - Make the page look nice!
3. Commit the code to Github. 
4. Host the application on AWS or Heroku or a similar provider
5. Share both the links.
