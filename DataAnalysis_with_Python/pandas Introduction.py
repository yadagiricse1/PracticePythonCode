import pandas as pd
import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style


style.use('fivethirtyeight')



start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = web.DataReader("XOM", "yahoo", start, end)

#print(df)
print(df.head())
df['Adj Close'].plot()
plt.show()