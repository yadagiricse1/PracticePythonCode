from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('fivethirtyeight')


fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')


x=[1,2,3,4,5,6,7,8,9,10]
y=[3,5,2,6,2,7,5,8,3,1]
z=[1,2,4,8,4,8,4,9,3,7]
#ax1.plot_wireframe(x,y,z)


x2=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2=[-3,-5,-2,-6,-2,-7,-5,-8,-3,-1]
z2=[1,2,4,8,4,8,4,9,3,7]

x3=[1,2,3,4,5,6,7,8,9,10]
y3=[3,5,2,6,2,7,5,8,3,0]
z3=np.zeros(10)


#ax1.scatter(x,y,z,c='g',marker='*')
#ax1.scatter(x2,y2,z2,c='r')

dx=np.ones(10)
dy=np.ones(10)
dz=[1,2,3,4,5,6,7,8,9,10]

ax1.bar3d(x3,y3,z3,dx,dy,dz)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.show()
