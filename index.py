import selenium
import pandas as pd
import sqlite3
import os
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Creating a sleenium webdriver
driver = selenium.webdriver.Chrome()

# navigating to the page containing the csv download button
driver.get("https://jobs.homesteadstudio.co/data-engineer/assessment/download/")

# click csv download button
button = driver.find_element(by=By.CLASS_NAME, value="wp-block-button")
button.click()

WebDriverWait(driver, 10).until(
    lambda driver: os.path.exists("skill_test_data.xlsx")
)

# reading csv file to Pandas Dataframe
df = pd.read_excel("skill_test_data.xlsx", sheet_name="data")
with open("temp_file.txt", "w") as f:
    f.write(df.to_string())
f.close()
with open("temp_file.txt", "r") as f:
    print(f.read())
# closing the selenium WebDriver
driver.quit()



# creating pivot table
pivot_table = df.pivot_table(index ="date", columns = "metric", values = "values", aggfunc = sum)

# sorting pivot table by revenue in descending order
pivot_table = pivot_table.sort_values(by="Attributed Rev (1d)", ascending=False)

# creating SQLite database
conn = sqlite3.connect("pivot_table.db")

# insert pivot table into SQLite databse
pivot_table.to_sql("pivot_table", conn, if_exists="replace")

# closing SQLite connection
conn.close()