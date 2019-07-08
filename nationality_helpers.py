import numpy as np
import pandas as pd

from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

def create_top_medalist():
    '''
    This function is used to create a dataframe of athletes that received medals for countries that 
    received more than 90 medals.
    '''
    df = pd.read_csv('athletes.csv')
    df.dropna(inplace=True)

    '''
    Below will create a column that contains the total number of medals that athlete won.
    '''

    df['medal_or_nm'] =  df['gold'] + df['silver'] + df['bronze']
    df = df[df.medal_or_nm >= 1]

    country_count = pd.DataFrame(df.groupby('nationality')['medal_or_nm'].agg('sum'))
    country_count.columns = ['country_count']
    df = df.merge(country_count, on='nationality')
    df = df[df.country_count > 90]

    athlete_count = pd.DataFrame(df.groupby('sport')['name'].agg('count'))
    athlete_count.columns = ['athlete_count']
    df = df.merge(athlete_count, on='sport')
    df = df[df.athlete_count > 30]

    '''
    DOB to datetime.
    '''

    df.dob = pd.to_datetime(df.dob)

    categorical_features = df.dtypes==object
    categorical_cols = df.columns[categorical_features].tolist()
    le = LabelEncoder()
    df[categorical_cols] = df[categorical_cols].apply(lambda col: le.fit_transform(col))

    '''
    Create columm for approximate age.
    '''

    df['age'] = 2016-df['dob'].dt.year

    return df