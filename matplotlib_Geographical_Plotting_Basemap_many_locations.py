from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


# there are 30 types of map Porjections
m=Basemap(projection='mill',llcrnrlat=20,urcrnrlat=50,llcrnrlon=-130,urcrnrlon=-60,resolution='c')


# llcrnrlat ll -lower Left crn- corner lat- latitude
#urcrnrlat  ur upper right crn- corner lat- latitude

m.drawcoastlines()
m.drawcountries()
m.drawstates()


m.fillcontinents(color='#04BAE3',lake_color='#FFFFFF' )
m.drawmapboundary(fill_color='#FFFFFF')
lat = 30,31,34,33,32
lon = -103,-110,-107,-111,-115


lat2 = 40,33,44,31,30
lon2 = -113,-100,-102,-111,-112

x,y = m(lon,lat)
m.plot(x,y,'ro',markersize=20,alpha=.5)

x,y = m(lon2,lat2)
m.plot(x,y,'go',markersize=20,alpha=.5)


# the above type of feature is helpfull to diffferenciate  things like employed vs unemploed etc.
#m.bluemarble()  some how this operation is not working
plt.title('Geo plotting')
plt.show()

# more detailed API methods https://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap