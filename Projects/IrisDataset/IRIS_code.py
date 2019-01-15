from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
#C:\Users\yadag\AppData\Local\Enthought\Canopy\edm\envs\User\Lib\site-packages\sklearn\datasets\data
# Iris data is present here and we are importing from there
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/Projects/IrisDataset/iris.txt',names=names)

#print(dataset.shape)
#print(dataset.head())
#print(dataset.describe())
#print(dataset.groupby('class').size())
print(dataset['class'].value_counts())
unique_class_list=dataset['class'].unique()
dict_class={}
original_dataset=dataset.copy()
for i in range(len(unique_class_list)):
    dict_class[unique_class_list[i]]=i
print('dictionary',dict_class)
cleanup_values={'class':dict_class}
dataset.replace(cleanup_values,inplace=True)
# shuffling data
dataset = dataset.reindex(np.random.permutation(dataset.index))
#print("after shuffling")
dataset.reset_index(drop=True,inplace=True)
print(dataset.head(5))
array=dataset.values
X=array[:,0:4]
y=array[:,4]
preprocessing.StandardScaler (X)
model=svm.SVC()
train_X,test_X,train_y,test_y=train_test_split(X,y,test_size=0.3)
model.fit(train_X,train_y)
print(model.predict(test_X.reshape(-1, 4)),test_y)


print(classification_report(test_y, model.predict(test_X.reshape(-1, 4))))
print(model.score(test_X,test_y))  #print(accuracy_score(test_y, model.predict(test_X.reshape(-1, 4))))








