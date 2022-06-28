SELECT * FROM stores


SELECT store_id, city, count(*)
FROM stores
GROUP BY store_id, city
ORDER BY COUNT(*)


SELECT rowid, store_id, city FROM stores


DELETE FROM stores
WHERE rowid NOT IN (
SELECT MIN(rowid)
FROM stores
GROUP BY store_id, city
)


SELECT store_id, city, count(*) 
FROM stores
GROUP BY store_id, city
ORDER BY COUNT(*)


ALTER TABLE stores
ADD CONSTRAINT store_id_pk PRIMARY KEY (store_id)


CREATE UNIQUE INDEX store_id_idx -- such column list already indexed
ON stores (store_id)
COMPUTE STATISTICS


SELECT * FROM all_tables where rownum < 10


SELECT * FROM all_tables 
WHERE table_name = 'EMPLOYEES'
AND rownum < 10


SELECT * FROM all_tab_COLUMNS 
WHERE table_name = 'EMPLOYEES'
AND rownum < 10


SELECT * FROM all_tab_COLUMNS 
WHERE table_name = 'EMPLOYEES'


SELECT * FROM ALL_OBJECTS
WHERE object_type = 'TABLE'
AND ROWNUM < 50


SELECT * FROM ALL_OBJECTS
WHERE object_type = 'INDEX'
AND lower(object_name) = 'emp_name_idx'


SELECT * FROM user_tab_columns


CREATE PUBLIC SYNONYM emp_table -- insufficient privileges
FOR employees 


CREATE SYNONYM emp_table -- insufficient privileges
FOR employees 


SELECT * FROM emp_table


SELECT rownum, ename, sal from employees


