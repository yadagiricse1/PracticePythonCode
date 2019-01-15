from matplotlib  import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

X=[1,2,3,4,5,6,7,8,9,10]
Y=[5,6,2,5,7,2,7,4,7,8]
Z=[2,3,4,1,3,4,6,3,3,3]

ax.scatter(X,Y,Z,c='b',marker='o')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()



