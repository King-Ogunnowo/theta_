from IPython.display import display, Markdown, Latex
import pandas as pd
import numpy as np
import datetime
from datetime import *

def select_dtype(data = 'df', dtype = 'dtype'):
    datatype = df.select_dtypes(include = [dtype])
    return datatype

def fill_null(dataframe = 'df'):
    cat_values = df.select_dtypes(include = ['object'])
    num_values = df.select_dtypes(include = ['number'])
    for column in cat_values:
        dataframe[column] = dataframe[column].fillna('unknown')
    for column in num_values:
        dataframe[column] = dataframe[column].fillna(0)
    return dataframe


def data_info(dataframe:pd.DataFrame = 'df'):
    num_values = dataframe.select_dtypes(include = ['number'])
    cat_values = dataframe.select_dtypes(include = ['object'])
    display(Markdown('### Null values in dataframe'))
    print(dataframe.isnull().sum())
    display(Markdown('### shape of dataframe'))
    print(dataframe.shape)
    display(Markdown('### Number of numerical attributes:'))
    print(len(num_values.columns))
    display(Markdown('### Number of categorical attributes:'))
    print(len(cat_values.columns))
    display(Markdown('### unique values in categorical attributes:'))
    for column in cat_values:
        display(Markdown('{}:'.format(column)))
        print(df[column].unique())

def get_age(Date):
    
    today_date = int(str(date.today()).strip('-')[0:4])
    age = today_date - Date
    
    return age
    

def bin_values(dataframe = 'df', col = 'column', bins = 'range', labels = ['labels'], column_name = 'column_name'):
    dataframe[column_name] = pd.cut(dataframe[col], bins = bins, labels = labels)
    return dataframe

def datetime_seperator(dataframe = 'df',  column = 'datetime column'):
    
    if dataframe[column].dtype != 'datetime64[ms]':
        dataframe[column] = pd.to_datetime(dataframe[column])
        
    dataframe['day'] = dataframe[column].dt.day_name()
    dataframe['month'] = dataframe[column].dt.strftime('%B')
    dataframe['year'] = dataframe[column].dt.year
    
    return dataframe

def label_encoder(column):
    column = column.astype('category')
    return column.cat.codes

def normalizer(column):
    
    results = []
    
    for x in column: 
        results.append((x - column.min())/(column.max() - column.min()))
            
    return results


