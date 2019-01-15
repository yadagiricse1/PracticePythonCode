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

TX_AK_Corr=pd.rolling_corr(HPI_data2['TX'],HPI_data2['AK'],12)


HPI_data2['TX'].plot(ax=ax1,label='TX HPI')
HPI_data2['AK'].plot(ax=ax1,label='AK HPI')
TX_AK_Corr.plot(ax=ax2,label='TX_AK_Corr')

plt.legend(loc=4)
plt.show()
     