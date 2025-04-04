import pandas as pd #to load the data parsed to dataframe
import sqlite3 #to load the df to a database
from urllib import request #because i had an issue with th requests lib i can only work with urllib
from bs4 import BeautifulSoup #to parse the scraped data

#the url : https://www.scrapethissite.com/pages/simple/
#the data we'll be working on will be a list of countries for each country we have the name, the name of the capital the population and the surface (area) in km2.


url = "https://www.scrapethissite.com/pages/simple/"
table_attribs = ["Country", "Capital", "Population", "Surface"] #the attributes will be the columns in database
db_name = "List_of_countries.db"
table_name = "Countries_info"
csv_path = "./Coutries_info.csv"

def extract(url,table_attribs):
    response =request.urlopen(url) #this line opens the url to start scraping afterwords. this is the equivalent of a get request
    data = response.read().decode("utf-8") #this reads the raw data (the first part) and then decodes the content using utf-8
    parsed_data = BeautifulSoup(data,'html parser') #the parses the data extracted with the html parser

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#why html parser :
    #decent speed
    #no additional dependencies required
    #less lenient than lxml or html5lib
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    countries = parsed_data.find_all('div',Class = 'country')
    countries_data = []
    for country in countries:
        country_name = country.find('h3')
        capital = country.find('span', Class = 'country-capital')
        population = country.find('span', Class = 'country-population')
        area = country.find('span', Class = 'country-area')

    country_data = {
            'Country': country_name.text.strip() if country_name else None,
            'Capital': capital.text.strip() if capital else None,
            'Population': population.text.strip() if population else None,
            'Surface': area.text.strip() if area else None
        }
    countries_data.append(country_data)

df = extract(url,table_attribs)
print(df)

