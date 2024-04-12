import numpy as np
import matplotlib.pyplot as plt
import pandas as pds
import geopandas as gpd
import geodatasets

# import map(gsp) data file
node_gdf = gpd.read_file("map.gsp", layer='node')
# GeoDataFrame 읽기
gdf = gpd.read_file('path/to/shapefile.shp')

# 대화형 지도 출력
gdf.explore()
# import road network data file

# read in the data