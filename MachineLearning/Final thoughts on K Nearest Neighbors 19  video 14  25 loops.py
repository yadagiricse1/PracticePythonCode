import pandas as pd
import numpy as np
from sklearn import preprocessing,cross_validation,neighbors

accuracies=[]
for i in range(25):
    df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/MachineLearning/breast-cancer-wisconsin.data.txt')
    
    df.replace('?',-99999,inplace=True)
    df.drop(['id'],1,inplace=True) # id is not used for classification and if we dont drop it we wont gett proper results
    #print(len(df))
    
    X=np.array(df.drop(['class'],1))
    y=np.array(df['class'])
    
    X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)
    
    clf=neighbors.KNeighborsClassifier()
    clf.fit(X_train,y_train)
    
    accuracy=clf.score(X_test,y_test)
    
    #print('accuracy',accuracy)
    accuracies.append(accuracy)
    
print(sum(accuracies)/len(accuracies))
    
    