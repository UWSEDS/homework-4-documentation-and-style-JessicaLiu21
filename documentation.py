"""This Python module aims to test whether a dataframe meets certain conditions."""
import numpy as np 
import pandas as pd

def check_type_column(data_frame):
    """
    @param data_frame: dataframe
    @return: return True if checking condition is true
    """
    return np.sum([data_frame[x].map(type).nunique() -1 for x in data_frame.columns]) == 0

def check_nan_values(data_frame):
    """
    @param data_frame: dataframe
    @return: return True if checking condition is true
    """
    return data_frame.isnull().values.any()

def check_rows_morethan_one(data_frame):
    """
    @param data_frame: dataframe
    @return: return True if checking condition is true
    """
    return data_frame.shape[0] > 1

def test_create_dataframe(data_frame, columns_name):
    """
    @param data_frame: dataframe; columns_name: list
    @return: return True if checking condition is true
    """
    if (len(data_frame) >= 10 and data_frame.equals(data_frame.dtypes)\
        and sorted(data_frame.columns) == sorted(columns_name)):
        return True
    return False

def download_to_csv(url_link):
    """
    @param url_link: string
    @return: return True if checking condition is true
    """
    data_frame = pd.read_csv(url_link)   
    return data_frame 

URL = 'https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD'
DATA = download_to_csv(URL)
COLUMNS = list(DATA.columns)
print(" The DataFrame meets the requirements in HW2: ", test_create_dataframe(DATA, COLUMNS))
print(" The DataFrame's all columns have the correct data type: ", check_type_column(DATA)) 
print(" The DataFrame has null values: ", check_nan_values(DATA))
print(" The DataFrame has at least one row: ", check_rows_morethan_one(DATA))
