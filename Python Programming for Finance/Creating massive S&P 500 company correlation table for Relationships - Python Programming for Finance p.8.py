import bs4 as bs
import requests
import pickle
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import os
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')



def save_sp500_tickers():
    resp=requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup=bs.BeautifulSoup(resp.text,'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers=[]
    for row in table.findAll('tr')[1:]:
        ticker=row.findAll('td')[0].text
        tickers.append(ticker)
    with open('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/sp500tickers.pickle','wb') as f:
        pickle.dump(tickers,f)
    print(tickers)
    return tickers
    
#save_sp500_tickers()
def get_data_from_yahoo(reload_sp500=False):
    count=0
    if reload_sp500:
        tickers=save_sp500_tickers()
    else:
        with open('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/sp500tickers.pickle','rb') as f:
            tickers=pickle.load(f)
        if not  os.path.exists('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/stock_dfs'):
            os.makedirs('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/stock_dfs')
        start=dt.datetime(2000,1,1)
        end= dt.datetime(2016,12,31)
        for ticker in tickers:
            #print(ticker)
            if not  os.path.exists('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/stock_dfs/{}.csv'.format(ticker)):
                #df=web.DataReader(ticker,'yahoo',start,end)
                df = web.DataReader(ticker, "yahoo", start, end)
                df.to_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/stock_dfs/{}.csv'.format(ticker))
            else:
                count+=1
                print('Already Have {}'.format(ticker))
                print(count)
        
                
    
#get_data_from_yahoo()

def compile_data():
    with open('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/sp500tickers.pickle','rb') as f:
            tickers=pickle.load(f)
    main_df=pd.DataFrame()
    
    for count, ticker in enumerate(tickers):
        try:
            df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/stock_dfs/{}.csv'.format(ticker))
            df.set_index('Date',inplace=True)
            df.drop(['Open','Close','High','Low','Volume'],1,inplace=True)
            df.rename(columns={'Adj Close':ticker},inplace=True)
            if main_df.empty:
                main_df=df
            else:
                main_df=main_df.join(df,how='outer')
            
        except OSError as e:
            print(ticker)
    #print(main_df.head())
    main_df.to_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/sp500_joined_closes.csv')
            
#compile_data()      

def visualize_data():
    df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/sp500_joined_closes.csv')
    #df['AAPL'].plot()
    #plt.show()
    df_corr=df.corr()
    #print(df_corr.head())
    data=df_corr.values
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    heatmap=ax.pcolor(data,cmap=plt.cm.RdYlGn)  # pcolor means plot color cm --cmap.RdYlGn --RedYellowGreen
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0])+0.5,minor=False)
    ax.set_yticks(np.arange(data.shape[1])+0.5,minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top() # to get axis labels at the top
    columns_labels =df_corr.columns
    row_labels =df_corr.index
    ax.set_xticklabels(columns_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)#  by default tick labels are horizontal. making it vertical is more readable
    heatmap.set_clim(-1,1) # to set the  color limits -1 is min(red) and +1 is max(green)  color limit(clim)
    plt.tight_layout()
    
    
    plt.show()
    
    
                
visualize_data()           
            
