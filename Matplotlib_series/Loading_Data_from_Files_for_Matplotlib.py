import matplotlib.pyplot as plt
import csv
import numpy as np

#part 1
#C:/Users/yadag/Desktop/PythonProgrammingPractice/Matplotlib_series/
'''
x=[]
y=[]

with open('C:/Users/yadag/Desktop/PythonProgrammingPractice/Matplotlib_series/example.txt','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        
plt.plot(x,y,label='Loaded from file')

plt.xlabel('x')
plt.ylabel('y')

plt.title('Interesting graph \n Check it out')
plt.legend()
plt.show()
'''
#the above method is messy and time consuming numpuy will help in getting the things faster

x,y,z=np.loadtxt('C:/Users/yadag/Desktop/PythonProgrammingPractice/Matplotlib_series/example.txt',delimiter=',',unpack=True)
# if we have less or more than expected variable it will throw error
plt.plot(x,y,label='Loaded from file')

plt.xlabel('x')
plt.ylabel('y')

plt.title('Interesting graph \n Check it out')
plt.legend()
plt.show()









