---
Binning data with cut and qcut
---
# Binning data with cut and qcut (pandas)
When working with continuous numerical data, it can often be helpful to split it into buckets or bins based on some cutoffs. There are two useful pandas methods for this: [pd.cut](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html) and [pd.qcut](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.qcut.html). 

The key difference to remember between these two methods is that `qcut`, which is a quantile-based discretization function, splits the data into buckets of equal distribution. Each bucket will contain approximately the same number of data points. On the other hand, `cut` will divide the data into intervals of equal width. `cut` also can divide the data into discrete bins of nonuniform width if it is provided with a sequence of scalars representing the interval boundaries.

Both functions accept a `labels` argument to specify the names of the resulting bins. It must be an array of the same length as the number of resulting bins. 

For an excellent description of how to use these methods, see this Practical Business Python [blog post](https://pbpython.com/pandas-qcut-cut.html).