import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import ShuffleSplit
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
num_folds=5
kfold = KFold(n_splits=num_folds)
model=svm.SVC()
results =cross_val_score(model,X,y,cv=kfold)

print("K fold Results",results)  
print("K fold Mean Result",results.mean())  
loocv=LeaveOneOut()
model_loo=svm.SVC()
results =cross_val_score(model_loo,X,y,cv=loocv)
#print("LeaveOneOut Results",results)  # it give the results equivalent to number of records
print("LeaveOneOut Mean Result",results.mean())  

n_splits=10
test_size=0.3
seed=7
ssplit=ShuffleSplit(n_splits=n_splits,test_size=test_size,random_state=seed)
model_Ssplit=svm.SVC()
results =cross_val_score(model_Ssplit,X,y,cv=ssplit)
#print("LeaveOneOut Results",results)  # it give the results equivalent to number of records
print("ShuffleSplit Mean Result",results.mean()) 




