# Logs Analysis Project
---------------------------

# Questions
-----------------
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
 
## Requirements
---------------
* Python 3.5.3
* psycopg2
* Postgresql 9.6

## How to run
--------------------
* load the data onto the database
```sql
psql -d news -f newsdata.sql
```
* connect to the database
```sql
psql -d news

##Create Views
------------------
Create the Following Views before running the logsanalysis.py file

CREATE VIEW erroredlog_count AS
 SELECT to_char(log.time, 'MM_DD_YYYY') as date, count(log.id) as error_count
     FROM log
 WHERE status = '404 NOT FOUND'
     GROUP BY 1;
     

CREATE VIEW requestlog_count AS
SELECT to_char(log.time, 'MM_DD_YYYY') as date , count(log.id) as request_count
    FROM log
    GROUP BY 1;
    
	
## Running the Script
---------------------
after creating the views run the logsanalysis.py
