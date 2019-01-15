import matplotlib.pyplot as plt


days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]
# we cant directly have labels for each and every stack plot but we can acive indirectly now 

plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='g',label='playing',linewidth=5)
#plt.plot([],[],color='g',label='playing')
plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','g'])
plt.xlabel('x')
plt.ylabel('y')

plt.title('Interesting graph \n Check it out')
plt.legend()
plt.show()
