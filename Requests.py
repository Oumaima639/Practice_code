from urllib import request #to communicate with the web page
import pandas as pd #for storage and manipulation
from bs4 import BeautifulSoup #to interpret the html document
import sqlite3 #for creating the database instance


###########################################################################################
#this is an API request to get the list of the top 50 movies in the URL provided
###########################################################################################


db_name='Movies.db'
table_name = 'Top_50'
csv_path = r"C:\Users\ZD449RK\PycharmProjects\pythonProject7\Top_50_films.csv"
df=pd.DataFrame(columns=['Average rank','Film','Year'])
count=0

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

r = request.urlopen(url) #because we're working with urllib / the equivalent if we imported requests lib would be : request.get(url)
data=r.read().decode('utf-8')
parsed_data=BeautifulSoup(data,'html.parser')

tables=parsed_data.find_all('tbody') #reads all the rows in every table in the web page
rows=tables[1].find_all(name='tr')

for row in rows:
    if count<50:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break
print (df)

df.to_csv(csv_path)
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()


