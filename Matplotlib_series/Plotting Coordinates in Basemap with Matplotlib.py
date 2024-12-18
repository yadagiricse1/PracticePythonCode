from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill',
            llcrnrlat = 25,
            llcrnrlon = -130,
            urcrnrlat = 50,
            urcrnrlon = -60,
            resolution='l')

m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='b')
#m.bluemarble()

xs=[]
ys=[]

NYClat,NYClon=40.7127,-74.0059

xpt,ypt=m(NYClon,NYClat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt,ypt,'^',markersize=15) # for  triangle ^

LAlat, LAlon = 34.05, -118.25
xpt, ypt = m(LAlon, LAlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'g^', markersize=15)
m.plot(xs,ys,color='r',linewidth=1,label='Flight 98')
m.drawgreatcircle(NYClon,NYClat,LAlon, LAlat,color='c',linewidth=3,label='Arc')  # to get in the curved form

plt.legend(loc=4)
plt.show()