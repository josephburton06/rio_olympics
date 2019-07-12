import numpy as np
import pandas as pd

from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

def create_top_sport():

    '''
    The following is used to read the csv with information on athletes.  It drops na's in the height and
    weight columns since those will be used to classify an athlete's sport.  An approximate age column is
    created.
    '''

    df = pd.read_csv('athletes.csv')
    df.dropna(inplace=True)

    '''
    Create columm for approximate age.
    '''

    df.dob = pd.to_datetime(df.dob)
    df['age'] = 2016-df['dob'].dt.year

    return df

def create_enc(df, columns):
    '''
    The following will create encoded columns based on a list of columns as an argument. The original column
    will stay intact.  Ex: create_enc(df, ['sport', 'nationality'])
    '''
    for col in columns:
        df[col+'_enc'] = df[col]
        encoder = LabelEncoder()
        encoder.fit(df[col])
        df[col+'_enc'] = encoder.transform(df[col])
    return df