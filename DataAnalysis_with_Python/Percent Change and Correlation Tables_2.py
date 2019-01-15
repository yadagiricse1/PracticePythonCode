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


main_df=pd.DataFrame()

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
     
fig=plt.figure()
ax1=plt.subplot2grid((1,1),(0,0))
HPI_data2=pd.read_pickle('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/fiddy_states3.pickle')     
benchmark=HPI_Benchmark()      

HPI_data2.plot(ax=ax1)
benchmark.plot(ax=ax1,color='k',linewidth=10)

plt.legend().remove()
plt.show()
  


     