import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce_Rate':[65,67,78,65,45,52]}
             
df=pd.DataFrame(web_stats)
#print(df)
#print(df.head())
#print(df.tail())
#print(df.tail(2))

df.set_index('Day')
#print(df.set_index('Day'))
#df=df.set_index('Day')
'''
# this will set Day as index but after we try to print again it wont give results with day as index. 
we can get rid of this by asigning it again to df 
df=df.set_index('Day')  or
df.set_index('Day',inplace=True)  '''

df.set_index('Day',inplace=True)
#print(df)
# to reference specific column 
print(df['Visitors'])  # any of these 2 ways are fine
print(df.Visitors)
'''
it is good practice to give the  header values without spaces like Bounce_Rate instead of 'Bounce Rate' 
because whle getting o/p print(df['Bounce Rate']) will give proper output where as print(df.Bounce Rate) is not accepted'''
print(df['Bounce_Rate'])  # any of these 2 ways are fine
print(df.Bounce_Rate)
#print(df.Bounce Rate)
# to print more than one column we need to pass columns as a list
#print(df[['Visitors','Bounce_Rate']])

# to convert perticular column valuse to list
#print(df.Visitors.tolist())
#print(df[['Visitors','Bounce_Rate']].tolist()) # this will throw error

print(np.array(df[['Visitors','Bounce_Rate']]))

df2=pd.DataFrame(np.array(df[['Visitors','Bounce_Rate']]))
print(df2)

