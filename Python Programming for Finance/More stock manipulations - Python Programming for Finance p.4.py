import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
import pandas_datareader.data as web
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
 

style.use('ggplot')

df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/tsla.csv',parse_dates=True,index_col=0)  # parse_dates=True try parsing the index

df_ohlc=df['Adj Close'].resample('10D').ohlc()
df_volume=df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True) # by doing this we are removing date as a index.none of our colums acts as index

df_ohlc['Date']=df_ohlc['Date'].map(mdates.date2num) # now we are converting dates to mdates

ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)  # this means 6 rows and one column
ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1) 
ax1.xaxis_date()
candlestick_ohlc(ax1,df_ohlc.values,width=2,colorup='g')

#plt.setp(ax1.get_xticklabels(), visible=False)  # this will hepl in hiding date label for one of the graph
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)
plt.show()