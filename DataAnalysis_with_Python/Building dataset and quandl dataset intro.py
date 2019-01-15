import quandl
import pandas as pd

api_key=open('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/quandlapikey.txt','r').read() 
# the above key we can get it from quandl website .after login click account settings and click API KEY
#print(api_key)

df=quandl.get("FMAC/HPI_AK", authtoken=api_key)

df.rename(columns={'Value':'HPI_AK'},inplace=True)

fifty_stats=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')



print(df.head())
print(fifty_stats[0][0][1:])

for abbv in fifty_stats[0][0][1:]:
    #print(abbv)
    print("FMAC/HPI_"+str(abbv))