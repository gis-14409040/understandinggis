from math import radians,sin,cos# IMPORT NECESSARY FUNCTIONS HERE
from pyproj import Geod
def compute_offset(origin, distance, direction):
    """
    Compute the location of a point at a given distance and direction from a specified location using trigonometry
    """
    offset_x = origin[0] + distance * cos(radians(direction))
    offset_y = origin[1] + distance * sin(radians(direction))
    return (offset_x, offset_y)

# this code tests whether your function works correctly
origin = (345678, 456789)
destination = compute_offset(origin, 1011, 123)	# move 1011m in a direction of 123 degrees 
print("CORRECT!!" if (int(destination[0]), int(destination[1])) == (345127, 457636) else f"INCORRECT!! Error: {(int(destination[0])-345127, int(destination[1])-457636)}")

import geopandas as gpd

world = gpd.read_file("../../data/natural-earth/ne_10m_admin_0_countries.shp")

iceland = world[world["ISO_A3"] == "ISL"]

land_cover = gpd.read_file("../../data/iceland/gis_osm_natural_a_free_1.shp")

ice = land_cover[land_cover["fclass"] == "glacier"]

minx, miny, maxx, maxy = iceland.total_bounds

print(minx, miny, maxx, maxy)

# set the geographical proj string and ellipsoid (should be the same)
geo_string = "+proj=longlat +datum=WGS84 +no_defs"
g = Geod(ellps='WGS84')
# create a list of dictionaries for the projected CRS' to evaluate for distortion
projections = [
    {'name':"Web Mercator", 'description':"Global Conformal",   'proj':""},
    {'name':"Eckert IV",    'description':"Global Equal Area",  'proj':""},
    {'name':"", 'description':"Local Equal Area",   'proj':""}
]