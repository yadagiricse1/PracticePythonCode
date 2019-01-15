import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


# we can get data from different Interenet APIs like yahoo,Google, Quandl

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    fig=plt.figure() # this figure() is by default called but when we want to change as per our requirement we have to call explicitly and modify
    ax1=plt.subplot2grid((1,1),(0,0)) # ax1 is a sub plot
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code=urllib.request.urlopen(stock_price_url).read().decode()
    stock_data=[]
    split_source=source_code.split('\n')
    for line in split_source[1:]:
        split_line=line.split(',')
        if len(split_line)==7:
            if 'values' not in line:
                stock_data.append(line)
    
    date,openp,highp,lowp,closep,Adj_colsep,volume=np.loadtxt(stock_data,
                                                              delimiter=',',
                                                              unpack=True,
                                                              # %Y =full year 2017
                                                              # %y=partial year 17
                                                              # %m= number month
                                                              # %d=number day
                                                              # %H=hours
                                                              # %M = minutes
                                                              # %S = seconds
                                                              # 12-06-2014 can be represented as %m-%d-%Y
                                                              converters={0: bytespdate2num('%Y-%m-%d')})
    ax1.plot_date(date,closep,'-',label='Price')
    ax1.plot([],[],linewidth=5,label='loss',color='r',alpha=0.5)
    ax1.plot([],[],linewidth=5,label='gain',color='g',alpha=0.5)
    #ax1.fill_between(date,closep,0)
    #ax1.fill_between(date,closep,0,alpha=0.3)
    ax1.fill_between(date,closep,closep[0],where=(closep>closep[0]),facecolor='g',alpha=0.3)
    ax1.fill_between(date,closep,closep[0],where=(closep<closep[0]),facecolor='r',alpha=0.3) # these 2 combinations are awesome green and red
    #ax1.fill_between(date,closep,closep[0],where=(closep>closep[0]),alpha=0.3)
    #ax1.fill_between(date,closep,100,alpha=0.3) # we can compare when you broght the stock . profits and losses in that time period
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45) # this will make all x lables ritated by 45 degrees
    ax1.grid(True)
    ax1.xaxis.label.set_color('r')
    ax1.yaxis.label.set_color('g')
    ax1.set_yticks([0,200,400,600,800])
    #ax1.grid(True,color='g',linestyle='-',linewidth=2)
    plt.xlabel('date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09,right=0.90,bottom=0.18,top=0.95,wspace=0.2,hspace=0) # this is used to set proper borders and spacing
    plt.show()
                                                              
graph_data('TSLA')                                                              