---
title: 'Accessing the parts of a file path with Pathlib (python)'
---
Pathlib is the module in Python (>3.4) for working with filesystem paths. It has a lot of useful methods. One useful set of methods are those to access the various parts of a path. It's much easier and more reliable than trying to split strings on forward slashes or back slashes. Don't forget that Windows uses backslashes and Unix systems use forward slashes to separate parts of paths. This can cause things to get tricky when working across platforms. 

See the relevant documentation [here](https://docs.python.org/3/library/pathlib.html#accessing-individual-parts). There are more examples there.

| Method        | Description                                                                           | Example
| ---           | ---                                                                                   | ---     |
|path.parts()   | A tuple giving access to the path’s various components                                | ('c:\\', 'Program Files', 'PSF')
|path.drive()   | A string representing the drive letter or name, if any                                | 'c:'
|path.root()    | A string representing the (local or global) root, if any                              | '/'
|path.anchor()  | The concatenation of the drive and root                                               | 'c:\\'
|path.name()    | A string representing the final path component, excluding the drive and root, if any  | 'setup.py'
|path.suffix()  | The file extension of the final component, if any                                     | '.py'
|path.suffixes()| A list of the path’s file extensions                                                  | ['.tar', '.gz']
|path.stem()    | The final path component, without its suffix                                          | 'setup'
|