import matplotlib.pyplot as plt
'''
# barchart

x=[1,3,5,7,9]
y=[6,3,2,4,4]
x2=[2,4,6,8,10]
y2=[6,3,2,4,4]
#plt.bar(x,y,label='Bars1') # this will give default color
#plt.bar(x2,y2,label='Bars2')
plt.bar(x,y,label='Bars1',color='r') 
plt.bar(x2,y2,label='Bars2',color='g')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph \n Check it out') # to get sub title \n XXXXX
plt.legend()
plt.show()
'''
# histogram

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
#plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph \n Check it out')
# if we dont have any labels  we will get warning
#ids=[x for x in range(len(population_ages))]
# plt.bar(ids,population_ages)  #this wont give a proper arrangement of data in plot histgram is better and we no longer need of using IDs
plt.legend()
plt.show()


