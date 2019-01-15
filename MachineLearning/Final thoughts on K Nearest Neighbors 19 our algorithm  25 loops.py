import numpy as np
from math import sqrt
import warnings
from collections import Counter
import random
import pandas as pd

def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups!')
    distances=[]
    for group in data:
        for features in data[group]:
            #euclidean_distance = sqrt( (features[0]-predict[0])**2 + (features[1]-predict[1])**2 )
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance,group])
   # print('distances',distances)
    #print('after sorting',sorted(distances)[:k])# this will give first 3 distances . in the below for loop it will take all the group names of the nearest ones
    votes = [i[1] for i in sorted(distances)[:k]]
    '''
    print('votes',votes)
    print('Counter(votes)',Counter(votes)) # it will group counts based on votes
    print('Counter(votes).most_common(1)',Counter(votes).most_common(1)) #
    '''
    vote_result = Counter(votes).most_common(1)[0][0]  # this will be more understandable if we have more groups. please remove comments fro prent statements above to get more understanding
    confidence = Counter(votes).most_common(1)[0][1]/k
    #print(vote_result,confidence)
    return vote_result,confidence
accuracies=[]
for i in range(25):
    
    df=pd.read_csv('C:/Users/yadag/Desktop/PythonProgrammingPractice/MachineLearning/breast-cancer-wisconsin.data.txt')
    
    df.replace('?',-99999,inplace=True)
    df.drop(['id'],1,inplace=True)
    full_data = df.astype(float).values.tolist() # to make sure that our data is with numbers. Try and check without writing float we might get data in the form of strings
    #full_data = df.values.tolist()
    random.shuffle(full_data) # no need of reasigning like full_data=random.shuffle(full_data)
    #print(20*'*')
    test_size=0.4
    train_set={2:[],4:[]}
    test_set={2:[],4:[]}
    train_data=full_data[:-int(test_size*len(full_data))]
    test_data=full_data[-int(test_size*len(full_data)):]
    
    for i in train_data:
        train_set[i[-1]].append(i[:-1])  # i[-1] indicates in cach row the last column . for us the class is a label(y) where as others are features(X)
    #print(Counter(Counter(train_set).most_common(1)[0][1]))
    for i in test_data:
        test_set[i[-1]].append(i[:-1])
    
    correct=0
    total=0
    
    for group in test_set:
        for data in test_set[group]:
            vote,confidence = k_nearest_neighbors(train_set, data, k=5)
            if group == vote:
                correct += 1
            total += 1
    #print('Accuracy:', correct/total)
    accuracies.append(correct/total)
    
print(sum(accuracies)/len(accuracies))

    
    
