---
title: "Get the value counts of a column in SQL (SQL)"
---
This will return a table containing the number of times each unique value in a given column occurs in a table. `DESC` is optional. If it is not included, the result will be in ascending order.

```
SELECT column, COUNT(*) 
FROM table 
GROUP BY column 
ORDER BY 2 DESC;
```