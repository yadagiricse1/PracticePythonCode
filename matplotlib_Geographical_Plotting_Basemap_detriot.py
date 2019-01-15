from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


# there are 30 types of map Porjections
m=Basemap(projection='mill',llcrnrlat=20,urcrnrlat=50,llcrnrlon=-130,urcrnrlon=-60,resolution='c')


# llcrnrlat ll -lower Left crn- corner lat- latitude
#urcrnrlat  ur upper right crn- corner lat- latitude

m.drawcoastlines()
m.drawcountries()
m.drawstates()
#m.fillcontinents()
#m.drawrivers()

m.fillcontinents(color='#04BAE3',lake_color='#FFFFFF' )
m.drawmapboundary(fill_color='#FFFFFF')

lat,lon=42.3314,-83.0458  # detroit
x,y=m(lon,lat)
m.plot(x,y,'r*')


at,lon=41.8781,-87.6298
xpt,ypt = m(lon,lat)
m.plot(xpt,ypt, 'go') #chicago



#m.bluemarble()  some how this operation is not working
plt.title('Geo plotting')
plt.show()

# more detailed API methods https://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap