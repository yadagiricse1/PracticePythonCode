import pandas as pd
import quandl,math
import numpy as np
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import pickle

style.use('ggplot')
df=quandl.get('WIKI/GOOGL')
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT']=(df['Adj. High']-df['Adj. Low'])/df['Adj. Close']*100.0
df['PCT_change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]


forecast_col='Adj. Close'

df.fillna('-9999',inplace=True)
forecast_out=int(math.ceil(0.01*len(df)))  # it is going to predict 10 perecnt of data ex if we have 100 records in df then we are planning to predict 10 future values
#print(len(df))
#print(forecast_out)
df['label']=df[forecast_col].shift(-forecast_out)

#print(df.head())

X=np.array(df.drop(['label'],1))


X=preprocessing.scale(X)
X_lately=X[-forecast_out:]
X=X[:-forecast_out]

df.dropna(inplace=True)
y=np.array(df['label'])
#y=np.array(df['label'])
#print(len(X),len(y))


X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)
clf=LinearRegression(n_jobs=-1)
#clf=LinearRegression()
#clf=LinearRegression(n_jobs=10 ) # if n_jobs=-1 then it will run many times
#clf=svm.SVR()
#clf=svm.SVR(kernel='poly')  # kernel possible values'linear','poly','rbf','sigmoid'

clf.fit(X_train,y_train)

# training every time is going to take a tedious time . so we can train the classifier and save load and use the classifier when you want


with open('C:/Users/yadag/Desktop/PythonProgrammingPractice/MachineLearning/linearregression.pickle','wb') as f:
    pickle.dump(clf, f)
pickle_in = open('C:/Users/yadag/Desktop/PythonProgrammingPractice/MachineLearning/linearregression.pickle','rb')
clf = pickle.load(pickle_in)
    
accuracy=clf.score(X_test,y_test)
#print(accuracy)
forecast_set=clf.predict(X_lately)
print(forecast_set,accuracy,forecast_out)

df['Forecast']=np.nan
last_date=df.iloc[-1].name
last_unix=last_date.timestamp()
one_day=86400 # number of seconds in a day
next_unix=last_unix+one_day

print('len',len(df.columns))
for i in forecast_set:
    next_date=datetime.datetime.fromtimestamp(next_unix)
    next_unix+=one_day
    df.loc[next_date]=[np.nan for _ in range(len(df.columns)-1)]+[i]
#print('df.loc[next_date]',df['Forecast'].loc[next_date])
#print(df.tail())
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()