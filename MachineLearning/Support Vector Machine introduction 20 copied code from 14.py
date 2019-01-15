import pandas as pd
import numpy as np
from sklearn import preprocessing,cross_validation,neighbors ,svm

df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/MachineLearning/breast-cancer-wisconsin.data.txt')

df.replace('?',-99999,inplace=True)
df.drop(['id'],1,inplace=True) # id is not used for classification and if we dont drop it we wont gett proper results
#print(len(df))

X=np.array(df.drop(['class'],1))
y=np.array(df['class'])

X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)

clf=svm.SVC()
clf.fit(X_train,y_train)

accuracy=clf.score(X_test,y_test)

print('accuracy',accuracy)

#example_measure=np.array([4,2,1,1,1,2,3,2,1]) #used reshape method as it was suggested in DeprecationWarning while executing code.for clarification run without reshape
#example_measure=np.array([4,2,1,1,1,2,3,2,1]).reshape(1, -1)
example_measure=np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,1,1,2,3,2,1]])
example_measure=example_measure.reshape(len(example_measure), -1)# if we have 2 samples we have to use (2,-1) instead of (1,-1) or use its size
example_measure1=np.array([3,1,1,1,2,1,2,1,1])

prediction=clf.predict(example_measure) 
print(prediction)