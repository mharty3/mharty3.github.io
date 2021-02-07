---
title: 'Using try-except to allow for optional imports in a module (python)'
---
I am writing a package to read and process data from a particular file format. One thing I want to do in the package is be able to take the data from the file and create an xarray data array. Not everyone using the package will need this functionality or want to install xarray in their environment. 

To get around this issue, you can import xarray inside of the function that needs it. By using a try and except statement, you can try importing xarray, if it is not available, it will send a useful message to the user telling them to install it.


```python
def function_that_needs_xarray():
    try:
        import xarray as xr
    except ImportError:
        raise ImportError(
            "Xarray package must be installed to convert to xarray data array."
        )
```