from numpy import zeros
from rasterio import open as rio_open
from rasterio.plot import show as rio_show
from matplotlib.pyplot import subplots, savefig
from matplotlib.colors import LinearSegmentedColormap
from skimage.draw import line
from skimage.draw import circle_perimeter
from numpy import column_stack
from sys import exit
# open the elevation data file
with rio_open("../../data/helvellyn/Helvellyn-50.tif") as dem:

    # read the data out of band 1 in the dataset
    dem_data =dem.read(1)

    # create a new 'band' of raster data the same size
    output = zeros(dem_data.shape)

# plot the dataset
fig, my_ax = subplots(1, 1, figsize=(16, 10))

# add the DEM
rio_show(
  dem_data,
  ax=my_ax,
  transform = dem.transform,
)
# add the drawing layer
rio_show(
    output,
    ax=my_ax,
    transform=dem.transform,
    cmap = LinearSegmentedColormap.from_list('binary_viewshed', [(0, 0, 0, 0), (1, 0, 0, 0.5)], N=2)
    )
savefig('./out/bresenham.png', bbox_inches='tight')
# Convert coordinate space (x, y) to image space (row, col)
def coords_2_img(x, y):
    row, col = dem.index(x, y)
    return row, col

# Convert the summit coordinates to image coordinates
row, col = coords_2_img(334170, 515165)

# Set the pixel at this location to 1 (red)
output[row, col] = 1
print(line(row, col, row, col+50))
print(column_stack(line(row, col, row, col+50)))
circle_perimeter(row, col, 50)
# set origin for viewshed
x0, y0 = 330000, 512500
# calculate the viewshed
output = viewshed(x0, y0, 20000, 1.8, 100, dem_data, dem.transform)
# make sure that we are within the dataset
	if not 0 <= r0 < dem_data.shape[0] or not 0 <= c0 < dem_data.shape[1]:
		print(f"Sorry, {x0, y0} is not within the elevation dataset.")
		exit()
        # convert the radius (m) to pixels
	radius_px = int(radius_m / transform[0])