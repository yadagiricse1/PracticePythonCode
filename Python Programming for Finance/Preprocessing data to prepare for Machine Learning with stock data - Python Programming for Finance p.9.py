import numpy as np
import pandas as pd
import pickle


def process_data_labels(ticker):
    hm_days=7
    df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/sp500_joined_closes.csv',index_col=0)
    tickers=df.columns.values.tolist()
    df.fillna(0,inplace=True)
    for i in range(1,hm_days+1):
        df['{}_{}d'.format(ticker,i)]=(df[ticker].shift(-i)-df[ticker])/df[ticker]
        #print(df['{}_{}d'.format(ticker,i)])
    df.fillna(0,inplace=True)
    return tickers,df
    
process_data_labels('XOM')

    
