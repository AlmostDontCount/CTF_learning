#SQL injection tips
##strings
1.use select schema_name from information_schema.schemata to get all databases; or simply use select **,database() to get the current database().  

2.use select table_name from information_schema.tables where table_schema=’xxxxx’ to obtain database'xxxx''s tables ; simply using select table_name from information_schema.tables where table_schema=database(),we can get the tables of the current database.  

3.use Select column_name from information_schema.columns where table_name=’xxxxx’ to select all the columns of a table.  

4. use select *** from ***;
