#https://pythonprogramming.net/static/downloads/machine-learning-data/titanic.xls
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
style.use('ggplot')

'''
Pclass Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
survival Survival (0 = No; 1 = Yes)
name Name
sex Sex
age Age
sibsp Number of Siblings/Spouses Aboard
parch Number of Parents/Children Aboard
ticket Ticket Number
fare Passenger Fare (British pound)
cabin Cabin
embarked Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
boat Lifeboat
body Body Identification Number
home.dest Home/Destination
'''
df=pd.read_excel('C:/Users/yadag/Desktop/PythonProgrammingPractice/MachineLearning/titanic.xls')
df.drop(['name','body'],1,inplace=True)
print(df.head())
df.convert_objects(convert_numeric=True)
df.fillna(0,inplace=True)
def handle_non_numerical_data(df):
    columns = df.columns.values
    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1
            df[column] = list(map(convert_to_int, df[column]))

    return df
df = handle_non_numerical_data(df)  

#df.drop(['ticket'],1,inplace=True)    
df.drop(['sex','boat'], 1, inplace=True)
X=np.array(df.drop(['survived'],1).astype(float))
X=preprocessing.scale(X)
y=np.array(df['survived'])

clf=KMeans(n_clusters=2)
clf.fit(X)
correct=0
for i in range(len(X)):
    predict_me=np.array(X[i].astype(float))
    predict_me=predict_me.reshape(-1,len(predict_me))
    prediction=clf.predict(predict_me)
    if prediction==y[i]:
        correct+=1
        
print(correct/len(X))


