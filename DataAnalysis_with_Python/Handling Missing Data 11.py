import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

     
fig=plt.figure()
ax1=plt.subplot2grid((1,1),(0,0))
HPI_data2=pd.read_pickle('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/fiddy_states3.pickle')     

#TX1yr=HPI_data2['TX'].resample('A',how='mean') # by default  how is asigned as mean   
HPI_data2['TX1']=HPI_data2['TX'].resample('A',how='mean')
print(HPI_data2[['TX','TX1']].head())

#HPI_data2.dropna(inplace=True) # removes the data that is not a number NAN
#HPI_data2.dropna(how='all'inplace=True)  # in this case if a row contains all NAN not a number then it will drop that row

#HPI_data2.dropna(thresh=2)  # Drop row if it does not have at least two values that are **not** NaN .that means if a row has 2 or more NAN's then delete them

#HPI_data2.fillna(method='ffill',inplace=True)  # this will fill the previous Number in NAN . ex if  at index 5 has value of 8.99 and index 6 is NaN then Nan will be replaced with 8.99
#HPI_data2.fillna(method='bfill',inplace=True) #  similar to ffill but it fulls future value in current position
HPI_data2.fillna(value=-99999,inplace=True)  # fills vaule with given value
#HPI_data2.fillna(value=-99999,limit=10,inplace=True)  # it limits number(10) of NaNs to be replaced by -99999 and remaining will be NaNs


print(HPI_data2[['TX','TX1']].head())
#print(HPI_data2.isnull().values.sum())# this will give how many are nulls (NaNs)  tested this line with limit option of fillna

HPI_data2[['TX','TX1']].plot(ax=ax1,label='Mothly TX HPI')

plt.legend(loc=4)
plt.show()
     