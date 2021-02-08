---
title: "Query for Table and Column Names in a Database (SQL)"
---
When working in a new database or one with a complicated schema, it is useful to be able to query for table names and column names in the database. For each flavor of SQL, it is slightly different.

## MSSQL

### Get all tables
```SQL
SELECT * FROM information_schema.tables ORDER BY table_type
```

### Search for a table
```SQL
SELECT * FROM information_schema.tables t WHERE t.table_name LIKE '%{search}%' ORDER BY table_type
```

### Get all columns in a table
```SQL
SELECT * FROM information_schema.columns c WHERE c.table_name = '{table_name}'
```

### Search for columns across tables
```SQL
SELECT * FROM information_schema.columns c WHERE c.column_name LIKE '%{search}%'
```

## Oracle
### Get all tables
```SQL
SELECT DISTINCT table_name 
  FROM all_tab_columns 
 WHERE owner = '{schema_name}' 
 ORDER BY table_name
 ```

 
### Search for a table
```SQL
SELECT DISTINCT table_name
FROM all_tab_columns 
WHERE owner = '{schema_name}' 
  AND table_name LIKE '%{search_string}%'
ORDER BY table_name
```

### Get all columns in a table
```SQL
SELECT * FROM all_tab_columns WHERE table_name = '{table_name}'
```

### Search for columns across tables
```SQL
SELECT table_name, column_name
  FROM all_tab_columns 
 WHERE owner = '{schema_name}' 
   AND column_name LIKE '%{search}%'
 ORDER BY table_name, column_name
```