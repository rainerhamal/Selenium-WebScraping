# Selenium-WebScraping
  Web scraping, data wrangling and database inserts using Python

<h1>Requirements</h1>

Python 3.8 or higher
Selenium
Pandas
SQLite3
Installation

<h1>Usage</h1>

Clone the repository:
git clone https://github.com/your-username/Selenium-WebScraping.git
Navigate to the project directory:
cd Selenium-WebScraping
Run the following command to download the CSV file and print the contents of the Pandas DataFrame to the terminal:
python main.py
Config file

The code uses a config.py file to store the database and spreadsheet file information. This file is ignored by Git, so you can store your sensitive information in there without worrying about it being committed to the repository.

<h1>Example config.py file:</h1>

DATABASE_FILENAME = "databaseName.db"
SPREADSHEET_FILENAME = "fileName.xlsx"

<h1>Troubleshooting</h1>

If you are having trouble running the code, please check the following:

Make sure that you have Python 3.8 or higher installed.
Make sure that you have the Selenium, Pandas, and SQLite3 packages installed.
Make sure that the CSV file and the config file are in the same directory as the main.py file.
If you are still having trouble, please post a question on GitHub or Stack Overflow.
