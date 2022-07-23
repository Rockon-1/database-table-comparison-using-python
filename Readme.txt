------------------------------------------------------------------
Overview of data comparison script from oracle database
-------------------------------------------------------------------
This script can be used to find out the differences of 2 tables exist in same database or different databases.
this script compare the structure of table , rows count and data also.

-------------------------------------------------------------------
dependencies
-------------------------------------------------------------------
script has dependency on 3 library which can be downloaded from python store by using 'pip' command.
1- cx_Oracle
This library used to connect with database.
2- pandas
This libray used to create numpy arrays
3- datacompy
This library used to compare data exist in source table and destination table.
datacompy also install pandas (if u skip installing pandsas library)

-------------------------------------------------------------------
Steps to use this script
-------------------------------------------------------------------
1- set parameters(like server, username and password) in conf.py for both source and destination database
2- Run main.py script