import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

# https://www.youtube.com/watch?v=8mnLZGNrAzM&feature=youtu.be&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-
bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}

df=pd.DataFrame(bridge_height)
df['STD']=pd.rolling_std(df['meters'],2)
#print(df)
df_std=df.describe()['meters']['std']  # std and STD is different here we are retirving std from describe() method of meters no STD. Please understand just by using describe() operation
print(df_std)

df=df[(df['STD']<df_std)]  # with this we can remove outliers using comparision operator . we can take benchmark of standard devaiation in our example and do.
print(df)
df['meters'].plot()
plt.show()

