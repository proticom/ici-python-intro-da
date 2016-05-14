'''
Created on May 14, 2016

@author: Edward

1. Create a map of the United States just like we did in the class lectures. 
2. use the scatter method to plot dots over Chicago, New York, and Los Angeles
'''


def makeMap():
    # imports
    import matplotlib
    matplotlib.use("TkAgg")
    import matplotlib.pyplot as plt
    from mpl_toolkits.basemap import Basemap
    
    # define values
    minLon = -130
    minLat = 25
    maxLon = -60
    maxLat = 50
    figW = 15
    figH = 7

    latitudes = [41.50, 40.47, 34.30]
    longitudes = [-87.37, -73.58, -118.15]
    labels = ['Chicago', 'New York', 'Los Angeles']
    
    lOffsetY = -1.00
    lOffsetX = 0.45
    
    # put code here to make map 
    plt.figure(1, figsize=(figW, figH))
    usaMap = Basemap(minLon, minLat, maxLon, maxLat, projection='cyl', resolution='i')
    usaMap.drawcoastlines()
    usaMap.drawstates(linewidth=1)
    usaMap.drawcountries(linewidth=1)
    
    # put code here to plot scatter data 
    usaMap.scatter(longitudes, latitudes, latlon=True, c='green', s=100)
    X, Y = usaMap(longitudes, latitudes)
    for x, y, label in zip(X,Y,labels):
        plt.text(x + lOffsetX, y + lOffsetY, label)

    plt.show()    
    
    return