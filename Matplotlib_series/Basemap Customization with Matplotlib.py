from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


m = Basemap(projection='mill',
            llcrnrlat = 25,
            llcrnrlon = -130,
            urcrnrlat = 50,
            urcrnrlon = -60,
            resolution='l')

'''
c - crude
l - low
h - high
f - full
            '''
 #m.drawstates(color='b')

#m.drawcounties(color='darkred') #showing some error
#m.fillcontinents()
#m.etopo()

                      
m.drawcoastlines()
m.drawcountries(linewidth=2)
#m.drawstates(color='b')
m.bluemarble()

plt.show()