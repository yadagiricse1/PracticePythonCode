import numpy as np
import pandas as pd
import pickle
from collections import Counter


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
    
#process_data_labels('XOM')
def buy_sell_hold(*args):
    cols=[c for c in args]
    requirement=0.02
    for col in cols:
        if col >requirement:
            return 1
        if col<requirement:
            return -1
    return 0
    
def extract_featuresets(ticker):
    tickers,df=process_data_labels(ticker)
    df['{}_target'.format(ticker)]=list(map(buy_sell_hold,
                                            df['{}_1d'.format(ticker)],
                                            df['{}_2d'.format(ticker)],
                                            df['{}_3d'.format(ticker)],
                                            df['{}_4d'.format(ticker)],
                                            df['{}_5d'.format(ticker)],
                                            df['{}_6d'.format(ticker)],
                                            df['{}_7d'.format(ticker)]
                                            ))
    vals=df['{}_target'.format(ticker)].values.tolist()
    str_vals=[str(i) for i in vals]
    print('Data Spread',Counter(str_vals))
    df.fillna(0,inplace=True)
    df=df.replace([np.inf,-np.inf],np.nan)
    df.dropna(0,inplace=True)
    df_vals=df[[ticker for ticker in tickers]].pct_change()
    df_vals=df_vals.replace([np.inf,-np.inf],0)
    df_vals.dropna(0,inplace=True)
    X=df_vals.values
    y=df['{}_target'.format(ticker)].values
    return X,y,df
    
extract_featuresets('XOM')

    

    
