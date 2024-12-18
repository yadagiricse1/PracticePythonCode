from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('fivethirtyeight')


fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')


x,y,z=axes3d.get_test_data()
print(axes3d.__file__) # this will give tou the location of the axes3d source code
#ax1.plot_wireframe(x,y,z)
ax1.plot_wireframe(x,y,z,rstride=5,cstride=5)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.show()


# we can learn many things from matplotlib.org click examples  tutorials. There is also library called seaborn similar to matplotlib