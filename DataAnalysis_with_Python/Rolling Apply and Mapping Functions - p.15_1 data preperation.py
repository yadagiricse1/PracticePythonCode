import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
api_key=open('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/quandlapikey.txt','r').read() 
# the above key we can get it from quandl website .after login click account settings and click API KEY
#print(api_key)



def states_list():
    fiddy_stats=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_stats[0][0][1:]

#quandl.get("SGE/USAMORTG", authtoken="bNovya7KzxzgkVjpy1Ts", start_date="1970-01-01", end_date="1970-01-01")
def grab_initial_state_data():
    main_df=pd.DataFrame()
    states=states_list()
    for abbv in states:
        query="FMAC/HPI_"+str(abbv)
        df=quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value':str(abbv)},inplace=True)
        #df=df.pct_change() # this will give percentage change in value with respective to previous value
        df[abbv]=(df[abbv]-df[abbv][0])/df[abbv][0]*100.0
        if main_df.empty:
            main_df=df
        else:
            main_df=main_df.join(df)
    print(main_df.head())
    
    pickle_out=open('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/fiddy_states3.pickle','wb') # wb stands for write bites
    pickle.dump(main_df,pickle_out)
    pickle_out.close()

#grab_initial_state_data()     

def HPI_Benchmark():
     df=quandl.get("FMAC/HPI_USA", authtoken=api_key)
     df.rename(columns={'Value':'United States'},inplace=True)
     df['United States']=(df['United States']-df['United States'][0])/df['United States'][0]*100.0
     return df
     
def mortgage_30y():
    df=quandl.get("FMAC/MORTG",trim_start='1975-01-01' ,authtoken=api_key)
    df.rename(columns={'Value':'M30'},inplace=True)
    df['M30']=(df['M30']-df['M30'][0])/df['M30'][0]*100.0
    df=df.resample('M').last()#df=df.resample('1D').mean()     df=df.resample('M').mean()# use both 2 lines instead of df=df.resample('M').last()
    return df
def sp500_data():
    df = quandl.get("YAHOO/INDEX_GSPC", trim_start="1975-01-01", authtoken=api_key)
    df["Adjusted Close"] = (df["Adjusted Close"]-df["Adjusted Close"][0]) / df["Adjusted Close"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Adjusted Close':'sp500'}, inplace=True)
    df = df['sp500']
    return df

def gdp_data():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Value':'GDP'}, inplace=True)
    df = df['GDP']
    return df

def us_unemployment():
    df = quandl.get("ECPI/JOB_G", trim_start="1975-01-01", authtoken=api_key)
    df["Unemployment Rate"] = (df["Unemployment Rate"]-df["Unemployment Rate"][0]) / df["Unemployment Rate"][0] * 100.0
    df=df.resample('1D').mean()
    df=df.resample('M').mean()
    return df
#sp500=sp500_data()
#US_GDP=gdp_data() 
#US_unemployment=us_unemployment()
#m30=mortgage_30y()
HPI_data2=pd.read_pickle('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/fiddy_states3.pickle')    
HPI_bench=HPI_Benchmark()
#HPI=HPI_data2.join([m30,US_unemployment,US_GDP])
#print(m30)
#print(states_HPI_M30.corr())
HPI_data2.dropna(inplace=True)
print(HPI_data2)
print(HPI_data2.corr())
HPI_data2.to_pickle('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/HPI.pickle')