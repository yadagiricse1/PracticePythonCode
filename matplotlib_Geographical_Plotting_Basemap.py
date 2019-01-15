from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


# there are 30 types of map Porjections
m=Basemap(projection='mill',llcrnrlat=-60,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='c')
#m=Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='c') #we willge  whole map with this statement
# resolution types c-crude ,l-low,h-high

# llcrnrlat ll -lower Left crn- corner lat- latitude
#urcrnrlat  ur upper right crn- corner lat- latitude

m.drawcoastlines()
#m.drawcountries()
#m.drawstates()
#m.fillcontinents()
#m.drawrivers()

#m.fillcontinents(color='#04BAE3',lake_color='#FFFFFF' )
m.drawmapboundary(fill_color='#FFFFFF')
#m.bluemarble()  some how this operation is not working
plt.title('Quick basemap example')
plt.show()

# more detailed API methods https://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap