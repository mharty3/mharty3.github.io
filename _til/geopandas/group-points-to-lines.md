---
Group Well Survey Points into Lines
---
# Group Well Survey Points into Lines (geopandas)
This is a useful snippet when working with well survey data. The points stored in the database as individual points, and commonly you want one LineString per well containing all the points for that well.

First groupby `WELL ID` or whatever unique field identifies each well and apply `shapely.geometry.LineString` to the list of points. Then convert the resulting dataframe back to a geodataframe. 

You may then want to join some or all of the columns from the original points dataframe back into final dataframe.

```python
import geopandas as gpd
from shapely.geometry import LineString

# convert survey points into lines grouped by well
survey_lines = survey_points.groupby('WELL_ID')['geometry'].apply(lambda x: LineString(x.tolist()))
survey_lines = gpd.GeoDataFrame(survey_lines, geometry='geometry') # turn back to geodataframe after groupby

# join columns from original data frame
cols = ['WELL_UWI', 'WELL_NAME_FREE']
survey_lines = survey_lines.join(survey_points.set_index('WELL_ID').drop_duplicates(subset=cols)[cols])
```

[Stack Overflow Post](https://stackoverflow.com/questions/51071365/convert-points-to-lines-geopandas)