# code not working

'''
Sample data is located: http://sentdex.com/GBPUSD.zip
'''

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
#C:/Users/yadag/Desktop/PythonProgrammingPractice/GBPUSD/GBPUSD1d.txt


date,bid,ask = np.loadtxt('C:/Users/yadag/Desktop/PythonProgrammingPractice/GBPUSD/GBPUSD1d.txt', unpack=True,
                              delimiter=',',
                              converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})
                              
                              
def changeGranularity(x,y,divby):
    granX=x
    granY=y
    changedGranX=[]
    changedGranY=[]
    
    gX=len(x)
    while gX>divby:
        xList=granX[gX-divby:gX]
        xAvg=reduce(lambda x,y:x+y,xList)/float(len(xList))
        
        yList=granY[gX-divby:gX]
        yAvg=reduce(lambda x,y:x+y,yList)/float(len(yList))
        
        changedGranX.append(xAvg)
        changedGranY.append(yAvg)
        gX-=divby
    
    return changedGranX,changedGranY
        

                                  
def graphRawFX2():
    
    #changeGranularity(x,y,divby)
    bidGrandX,bidGrandY=changeGranularity(date,bid,5)
    askGrandX,askGrandY=changeGranularity(date,ask,5)
    
    
    
   

    fig=plt.figure(figsize=(10,7))

    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax1.plot(bidGrandX,bidGrandY)
    ax1.plot(askGrandX,askGrandY)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
    plt.subplots_adjust(bottom=.23)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    plt.grid(True)
    plt.show()
                                                                                                      
                                                                                                                                                                          
                              
def graphRawFX():
    date,bid,ask = np.loadtxt('C:/Users/yadag/Desktop/PythonProgrammingPractice/GBPUSD/GBPUSD1d.txt', unpack=True,
                              delimiter=',',
                              converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})

    fig=plt.figure(figsize=(10,7))

    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
    plt.subplots_adjust(bottom=.23)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    plt.grid(True)
    plt.show()
    

graphRawFX2()