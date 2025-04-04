import glob #we're going to create multiple functions to deal with different file formats this will help us determine the required format for each function
import pandas as pd
import xml.etree.ElementTree as ET #to parse xml files
from datetime import datetime #to properly log information

#the following files have to be globally available
log_file = 'log_file.text'
target_file = 'transformed_data.csv'

#first step is to define a function to extract data from each file format
#to extract from csv
def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process) #this function reads the csv file into a dataframe
    return dataframe #this returns the dataframe each time the function is called

#to extract from json
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines=True) #the 'lines=True' tells pandas to treat each line in the json file as a seperate json object, without this line an error would be generated in case of a JSON Lines fomrat
    return dataframe

#to extract from xml
def extract_from_xml(file_to_process):
    tree = ET.parse(file_to_process) #parse the xml file
    root = tree.getroot()
    data_list = [] #this will contain the data before converting it to a dataframe
    for person in root :
        name = person.find('name').text
        height = float(person.find('height').text)
        weight = float(person.find('weight').text)
        data_list.append({'name':name,'height':height,'weight':weight})
    dataframe = pd.DataFrame(data_list)
    return dataframe




