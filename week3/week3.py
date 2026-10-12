# THIS IMPORTS A SQUARE ROOT FUNCTION, WHICH IS A BIG HINT!!
from math import sqrt

def distance(x1, y1, x2, y2):
    """
    * Use Pythagoras' theorem to measure the distance. This is acceptable in this case because:
    *     - the CRS of the data is a local projection
    *     - the distances are short
    *  - computational efficiency is important (as we are making many measurements)
    """
    return sqrt((x1-x2)**2+(y1-y2)**2)# complete this line to return the distance between (x1,y1) and (x2,y2)
print (distance(345678,456789,445678,556789))

from geopandas import read_file
# read in shapefiles, ensure that they all have the same CRS
pop_points = read_file("../../../data/gulu/pop_points.shp")
water_points = read_file("../../../data/gulu/water_points.shp")
gulu_district = read_file("../../../data/gulu/district.shp")
 
print(water_points.estimate_utm_crs(datum_name='Arc 1960'))