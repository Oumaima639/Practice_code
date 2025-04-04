import pandas as pd
import numpy as np
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime
from urllib import request

########################################################################################################################
#Scrape and Extract
########################################################################################################################
url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

table_attribs = ['Country','GDP_USD_millions']
db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
csv_path = './Countries_by_GDP.csv'


def extract(url, table_attribs):
    response = request.urlopen(url)
    data = response.read().decode('utf-8')
    parsed_data = BeautifulSoup(data, 'html.parser')

    tables = parsed_data.find_all('tbody')
    rows_data = []
    if len(tables) > 2:
        rows = tables[2].find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 3:
                country = cols[0].text.strip()
                gdp = cols[2].text.strip()
                if country and gdp and gdp != '—':
                    rows_data.append({'Country': country, 'GDP_USD_millions': gdp})

    df = pd.DataFrame(rows_data, columns=table_attribs)

    if df.empty:
        print("Warning: No data was extracted. Check the webpage structure.")
    else:
        print(f"Extracted {len(df)} rows of data")
        print(df.head())

    return df


def transform(df):
    def clean_gdp(gdp_str):
        return float(''.join(char for char in gdp_str if char.isdigit() or char == '.'))

    df["GDP_USD_billions"] = df["GDP_USD_millions"].apply(clean_gdp) / 1000
    df["GDP_USD_billions"] = df["GDP_USD_billions"].round(2)
    df = df.drop(columns=["GDP_USD_millions"])
    return df

########################################################################################################################


########################################################################################################################
#Extraction ends here
########################################################################################################################
#Transformation starts here
########################################################################################################################
########################################################################################################################
#Transformation ends here
########################################################################################################################
#Loading starts here
########################################################################################################################
def load_to_csv(df,csv_path):
    df.to_csv(csv_path)

def load_to_db(df,conn,table_name):
    df.to_sql(table_name,conn,if_exists='replace',index=False)
    print('Data successfully loaded')
########################################################################################################################
#Querying starts here
########################################################################################################################
def run_query(query,sql_connection):
    df = pd.read_sql_query(query,sql_connection)
    print('Query executed successfully')
    print(df)
########################################################################################################################
                                             #Logging starts here
########################################################################################################################

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("./etl_project_log.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
                                                #Function calls
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
log_progress('ETL_job_started') #Initiating ETL process

log_progress('Extraction starts') #start extracting
df = extract(url,table_attribs)
log_progress('Extraction ended')

log_progress('Transformation starts') #start transforming
df = transform(df)
log_progress('Transformation ended')

log_progress('Loading begins') #load to csv
loaded_data = load_to_csv(df,csv_path)
log_progress('loading ended')

sql_connection = sqlite3.connect('World_Economies.db')
log_progress('SQLite3 connection initiated')

load_to_db(df,sql_connection,table_name)

log_progress('Data loaded to Database as table. Running the query.')
query = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 100"
run_query(query,sql_connection)

log_progress('Process Complete.')

sql_connection.close()

