#https://www.quandl.com/api/v3/datasets/ZILLOW/Z77006_ZRIMFRR.csv?api_key=bNovya7KzxzgkVjpy1Ts

#C:\Users\yadag\Desktop\PythonProgrammingPractice\DataAnalysis_with_Python

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/ZILLOW-Z77006_ZRIMFRR.csv')

print(df.head())
df.set_index('Date',inplace=True)
#print(df.head())
df.to_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/New_CSV.csv')

df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/New_CSV.csv') 

print(df.head()) # this wont consider the dat as index column . if we want date to be index column we can mention while reading the file

df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/New_CSV.csv',index_col=0)
# to rename the column from value to Austin_HPI  (Austin house price index)
df.columns=['Austin_HPI'] # to change the every single column we have to write all the new column names in list form
print(df.head())
#df.plot()
#plt.show()

df.to_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/New_CSV2.csv')
df.to_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/New_CSV3.csv',header=False) # to ignore the header

# while reading data if there are no headers and we want to asign headers and index while reading data

df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/New_CSV3.csv',names=['Date','Austin_HPI'],index_col=0)
print(df.head())
df.to_html('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/New_CSV4.html')

# how to rename column after loading data in to data frame

df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/New_CSV3.csv',names=['Date','Austin_HPI'])
df.rename(columns={'Austin_HPI':'77006_HPI'},inplace=True)
print(df.head())




 



