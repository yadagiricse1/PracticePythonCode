import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean
from sklearn import svm, preprocessing, cross_validation

def create_labels(cur_hpi,fut_hpi):
    if fut_hpi>cur_hpi:
        return 1
    else:
        return 0
def moving_average(values):
    ma = mean(values)
    return ma

# the data which we have from HPI.pickle is not a valid data to test as  it was shown in the video
housing_data=pd.read_pickle('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/HPI.pickle')

housing_data=housing_data.pct_change()
print(housing_data.head())

# there will be some infinities   and negative infinities along with NaNs we have to replace them

housing_data.replace([np.inf,-np.inf],np.nan,inplace=True)

housing_data['US_HPI_future'] = housing_data['United States'].shift(-1)

housing_data.dropna(inplace=True)
print(housing_data[['US_HPI_future','United States']].head())
housing_data['label']=list(map(create_labels,housing_data['United States'],housing_data['US_HPI_future']))
print(housing_data.head())

# features(capital X) and labels(lower case y) 

X=np.array(housing_data.drop(['US_HPI_future','label'],1)) # because they are 100% percent coorelate as they are exact derived from others
X = preprocessing.scale(X)
y = np.array(housing_data['label'])

X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)

# from the Machine learning chart we choosed svm for this data
#http://scikit-learn.org/stable/tutorial/machine_learning_map/
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test)) # this will give how accurate is our data


