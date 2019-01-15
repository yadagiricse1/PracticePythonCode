import bs4 as bs
import requests
import pickle
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import os



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
            
compile_data()        
    
                
            
            
