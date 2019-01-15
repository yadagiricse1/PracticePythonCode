import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

#C:/Users/yadag/Desktop/PythonProgrammingPractice/sampleText.txt
def animate(i):
    pullData=open('C:/Users/yadag/Desktop/PythonProgrammingPractice/sampleText.txt','r').read()
    dataArray=pullData.split('\n')
    xar=[]
    yar=[]
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y =eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear() #this method is not mandatory if we dont have this method a new line will be drawn on existing line again and again (we get different colors)       
    ax1.plot(xar,yar)



ani=animation.FuncAnimation(fig,animate,interval=1000)
plt.show()
    

  