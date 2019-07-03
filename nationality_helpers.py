import numpy as np
import pandas as pd

def create_top_medalist():
    '''
    This function is used to create a dataframe of athletes that received medals for countries that 
    received more than 50 medals.
    '''
    df = pd.read_csv('athletes.csv')
    df.dropna(inplace=True)

    df['medal_or_nm'] =  df['gold'] + df['silver'] + df['bronze']
    df_medals = df[df.medal_or_nm >= 1]

    country_count = pd.DataFrame(df_medals.groupby('nationality')['medal_or_nm'].agg('sum'))
    country_count.columns = ['country_count']

    df_medals = df_medals.merge(country_count, on='nationality')

    df_medals = df_medals[df_medals.country_count > 50]

    return df_medals