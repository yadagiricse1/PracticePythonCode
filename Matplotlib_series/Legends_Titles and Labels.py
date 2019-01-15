import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,7,4]
x2=[1,2,3]
y2=[10,15,12]
# if we want any thing to display in the plot we should call every thing before plt.show()
plt.plot(x,y,label='First Line')
plt.plot(x2,y2,label='second Line')
plt.xlabel('Plot Number')
plt.ylabel('Implortan Var')
plt.title('Interesting graph \n Check it out') # to get sub title \n XXXXX
plt.legend()
plt.show()