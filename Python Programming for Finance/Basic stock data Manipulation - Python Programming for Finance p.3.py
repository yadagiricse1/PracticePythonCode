import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
import pandas_datareader.data as web

style.use('ggplot')

df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/tsla.csv',parse_dates=True,index_col=0)  # parse_dates=True try parsing the index
df['100ma']=df['Adj Close'].rolling(window=10,min_periods=0).mean()

# if we mention min_periods =0 we no need to drop NaNs because adjusted closing will be the moving average till 99th one
#df.dropna(inplace=True)
print(df.tail())
print(df.head())

ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)  # this means 6 rows and one column
ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1) 
ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['100ma'])
ax2.bar(df.index,df['Volume'])

plt.show()