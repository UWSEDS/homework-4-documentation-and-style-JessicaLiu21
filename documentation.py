"""This Python module aims to test whether a dataframe meets certain conditions."""
## import the needed packages 
import pandas as pd

## test function  1
def test_create_dataframe(data_frame, columns_name):
    '''This function tests the whether the input  DataFrame has at least 10 rows'''
    if not len(data_frame) >= 10: 
        return False
    if not data_frame.equals(data_frame.dtypes): 
        return False
    if not sorted(data_frame.columns) == sorted(columns_name): 
        return False
    return True

## test function 2
def check_values_correct_types(data_frame):
    '''This function tests that all columns have values of the correct type.'''
    for i in data_frame:
        if not data_frame.dtypes[1] == data_frame.dtypes[i]:
            return False
    return True

## test function 3 
def check_nan_values(data_frame):
    ''' This function tests whether the dataframe has null values.'''  
    return data_frame.isnull().values.any()

## test function 4 
def check_rows_morethan_one(data_frame):
    ''' This function tests whether the daraframe has at least one row.'''    
    return len(data_frame) >= 1

def download_to_csv(url_link):
    '''This function aims to download a DataFrame from website'''   
    return pd.read_csv(url_link) 

URL = 'https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD'
DATA = download_to_csv(URL)
COLUMNS = list(DATA.columns)

# test function 1
print(" The DataFrame meets the requirements in HW2: ", test_create_dataframe(DATA, COLUMNS))
# test function 2 
print(" All columns have the correct data type: ", check_values_correct_types(DATA)) 
# test function 3
print(" The DataFrame has null values: ", check_nan_values(DATA))
# test function 4 
print(" The DataFrame has at least one row: ", check_rows_morethan_one(DATA))



