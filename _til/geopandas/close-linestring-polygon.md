---
Convert a closed linestring to a polygon
---
# Convert a closed linestring to a polygon (geopandas)
Petrel often treats polygons as linestrings with the same starting and ending point. When they are exported as shapefiles or other spatial data formats, you may expect them to be polygons, but they aren't actually closed.

To fix this using geopandas, you can to convert the geometry of the geodataframe using `shapely.geometry.Polygon`.


```
import geopandas as gpd
from shapeley.geometry import Polygon

gdf = gpd.read_file('P://Shapefiles/NM_SebRegional_Poly.shp') # read the shapefile exported from Petrel
gdf.geometry = gdf.geometry.apply(lambda x: Polygon(x.coords))
```