from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')


x=[1,2,3,4,5,6,7,8,9,10]
y=[3,5,2,6,2,7,5,8,3,0]
z=[1,2,4,8,4,8,4,9,3,7]
ax1.plot_wireframe(x,y,z)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.show()