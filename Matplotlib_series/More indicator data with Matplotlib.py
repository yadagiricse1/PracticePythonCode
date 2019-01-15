import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib import style
import numpy as np
import urllib



# we can get data from different Interenet APIs like yahoo,Google, Quandl

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
#style.use('ggplot')

style.use('seaborn-notebook') # classic  ,dark_background
print(plt.style.available) # we will get all available styles
#print(plt.__file__)# this will give the location of my matplotlib(plt/pyplot)

#If you want to change any of the styles provided or create any new styles based on existing styles
#we can modify them  ex:C:\Users\yadag\AppData\Local\Enthought\Canopy\edm\envs\User\Lib\site-packages\matplotlib\mpl-data\stylelib
#in this location we have all the styles defined like fivethirtyeight in file fivethirtyeight.mplstyle

def moving_average(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas
    
def high_minus_low(highs, lows):
    return highs-lows
    
    
MA1 = 10
MA2 = 30

def graph_data(stock):
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    fig=plt.figure() # this figure() is by default called but when we want to change as per our requirement we have to call explicitly and modify
    ax1=plt.subplot2grid((6,1),(0,0),rowspan=1,colspan=1)
    plt.title(stock)
    ax2=plt.subplot2grid((6,1),(1,0),rowspan=4,colspan=1)
    plt.xlabel('date')
    plt.ylabel('Price')
    ax3=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1)
    
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
    x=0
    y=len(date)/250  # choosed only very less data to get view of candlesticks
    ohlc=[]
    
    while x<y:
        append_me=date[x],openp[x],highp[x],lowp[x],closep[x],volume[x]
        ohlc.append(append_me)
        x+=1
    
    candlestick_ohlc(ax2,ohlc,width=0.4,colorup='g',colordown='b')
    #ax1.plot(date,closep)
    #ax1.plot(date,openp)
    
    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)
        
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax2.xaxis.set_major_locator(mticker.MaxNLocator(10)) # for the date labels it woll select max N locators and display. other dates are not displayed
    ax2.grid(True)
    '''
    # annotated examplet with arrow
    ax2.annotate('Bad News!',(date[9],highp[9]),
                 xytext=(0.8, 0.9), textcoords='axes fraction',
                 arrowprops = dict(facecolor='grey',color='grey'))
    
    #font dict example
    font_dict={'family':'serif','color':'darkred','size':15}
    #Hard coded text
    ax2.text(date[10],closep[1],'Text Example',fontdict=font_dict)   # to display some text in the graph  
    
    '''
    
    ma1 = moving_average(closep,MA1)
    ma2 = moving_average(closep,MA2)
    start = len(date[MA2-1:])
    h_l = list(map(high_minus_low, highp, lowp))

    ax1.plot_date(date,h_l,'-')
    
    ax3.plot(date[-start:], ma1[-start:])
    ax3.plot(date[-start:], ma2[-start:])
    
    
    
    plt.legend()
    plt.subplots_adjust(left=0.09,right=0.90,bottom=0.18,top=0.95,wspace=0.2,hspace=0) # this is used to set proper borders and spacing
    plt.show()
                                                              
graph_data('TSLA')                                                              