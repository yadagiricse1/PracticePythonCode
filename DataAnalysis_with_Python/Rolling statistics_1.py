import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

     
fig=plt.figure()
ax1=plt.subplot2grid((2,1),(0,0))
ax2=plt.subplot2grid((2,1),(1,0),sharex=ax1)
HPI_data2=pd.read_pickle('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/fiddy_states3.pickle')     


HPI_data2['TX12MA']=pd.rolling_mean(HPI_data2['TX'],12) # here the moving average or rolling average will start with first 12 months
HPI_data2['TX12STD']=pd.rolling_std(HPI_data2['TX'],12)
print(HPI_data2[['TX','TX12MA','TX12STD']].head())




HPI_data2.dropna(inplace=True) # this will remove NANs for first 12 periods. First 12 period rows

print(HPI_data2[['TX','TX12MA','TX12STD']].head())


HPI_data2[['TX','TX12MA']].plot(ax=ax1)
HPI_data2[['TX12STD']].plot(ax=ax2)

plt.legend(loc=4)
plt.show()
     