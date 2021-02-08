---
title: "Avoid nested for loops with itertools.product() (python)"
---
The Python itertools module contains many useful iterator functions. This entry will focus on the combinatoric iterators. 

Today I [solved](https://github.com/mharty3/advent_of_code/blob/main/2020/1.ipynb) the [advent of code puzzle](https://adventofcode.com/2020/day/1) using nested for loops to iterate over each item in an array twice:

```python
for i in data_list:
    for j in data_list:
        if i + j == 2020:
            print(i * j)
```

This nested for loop is finding the "cartesian product" of the the arrays it is looping over. It finds the set of all ordered pairs that can be constructed from the two arrays. The operation can be done more efficiently and succinctly by using 'itertools.product()'.

```python
for n in itertools.product(data_list, data_list): 
    if sum(n) == 2020: 
        print(np.product(n))
```

The itertools module also has functions for combinations and permutations as well:

<table class="docutils align-default">
<colgroup>
<col style="width: 36%">
<col style="width: 16%">
<col style="width: 48%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Iterator</p></th>
<th class="head"><p>Arguments</p></th>
<th class="head"><p>Results</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="#itertools.product" title="itertools.product"><code class="xref py py-func docutils literal notranslate"><span class="pre">product()</span></code></a></p></td>
<td><p>p, q, … [repeat=1]</p></td>
<td><p>cartesian product, equivalent to a nested for-loop</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#itertools.permutations" title="itertools.permutations"><code class="xref py py-func docutils literal notranslate"><span class="pre">permutations()</span></code></a></p></td>
<td><p>p[, r]</p></td>
<td><p>r-length tuples, all possible orderings, no repeated elements</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#itertools.combinations" title="itertools.combinations"><code class="xref py py-func docutils literal notranslate"><span class="pre">combinations()</span></code></a></p></td>
<td><p>p, r</p></td>
<td><p>r-length tuples, in sorted order, no repeated elements</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#itertools.combinations_with_replacement" title="itertools.combinations_with_replacement"><code class="xref py py-func docutils literal notranslate"><span class="pre">combinations_with_replacement()</span></code></a></p></td>
<td><p>p, r</p></td>
<td><p>r-length tuples, in sorted order, with repeated elements</p></td>
</tr>
</tbody>
</table>



<table class="docutils align-default">
<colgroup>
<col style="width: 43%">
<col style="width: 57%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Examples</p></th>
<th class="head"><p>Results</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">product('ABCD',</span> <span class="pre">repeat=2)</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">AA</span> <span class="pre">AB</span> <span class="pre">AC</span> <span class="pre">AD</span> <span class="pre">BA</span> <span class="pre">BB</span> <span class="pre">BC</span> <span class="pre">BD</span> <span class="pre">CA</span> <span class="pre">CB</span> <span class="pre">CC</span> <span class="pre">CD</span> <span class="pre">DA</span> <span class="pre">DB</span> <span class="pre">DC</span> <span class="pre">DD</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">permutations('ABCD',</span> <span class="pre">2)</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">AB</span> <span class="pre">AC</span> <span class="pre">AD</span> <span class="pre">BA</span> <span class="pre">BC</span> <span class="pre">BD</span> <span class="pre">CA</span> <span class="pre">CB</span> <span class="pre">CD</span> <span class="pre">DA</span> <span class="pre">DB</span> <span class="pre">DC</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">combinations('ABCD',</span> <span class="pre">2)</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">AB</span> <span class="pre">AC</span> <span class="pre">AD</span> <span class="pre">BC</span> <span class="pre">BD</span> <span class="pre">CD</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">combinations_with_replacement('ABCD',&nbsp;2)</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">AA</span> <span class="pre">AB</span> <span class="pre">AC</span> <span class="pre">AD</span> <span class="pre">BB</span> <span class="pre">BC</span> <span class="pre">BD</span> <span class="pre">CC</span> <span class="pre">CD</span> <span class="pre">DD</span></code></p></td>
</tr>
</tbody>
</table>

[Python itertools docs](https://docs.python.org/3/library/itertools.html)