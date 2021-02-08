---
title: "Raster affine transforms in Python (GIS)"
---
[Very helpful blog from perrygeo](https://www.perrygeo.com/python-affine-transforms.html)

>The typical geospatial coordinate reference system is defined on a cartesian plane with the 0,0 origin in the bottom left and X and Y increasing as you go up and to the right. But raster data, coming from its image processing origins, uses a different referencing system to access pixels. We refer to rows and columns with the 0,0 origin in the upper left and rows increase and you move down while the columns increase as you go right. Still a cartesian plane but not the same one. 

![raster cartesian plane](raster-cartesian.png)

The six elements of the affine transform in `rasterio` and the Python `affine` library are:

* a = width of a pixel
* b = row rotation (typically zero)
* c = x-coordinate of the upper-left corner of the upper-left pixel
* d = column rotation (typically zero)
* e = height of a pixel (typically negative)
* f = y-coordinate of the of the upper-left corner of the upper-left pixel


## Using `rasterio.transform.Affine`

[Writing Data with Rasterio](https://rasterio.readthedocs.io/en/latest/quickstart.html#opening-a-dataset-in-writing-mode)

```python
>>> from rasterio.transform import Affine
>>> res = (x[-1] - x[0]) / 240.0  # last x minus first x divided by the number of x's
>>> transform = Affine.translation(x[0] - res / 2, y[0] - res / 2) * Affine.scale(res, res)
>>> transform
Affine(0.033333333333333333, 0.0, -4.0166666666666666,
       0.0, 0.033333333333333333, -3.0166666666666666)
```