SELECT * FROM employees
WHERE job = 'MANAGER'


CREATE VIEW managers_v 
AS SELECT * FROM employees
WHERE job = 'MANAGER'


SELECT * FROM managers_v


SELECT * FROM user_objects
WHERE object_type = 'VIEW'


SELECT * FROM all_objects 
WHERE OWNER = 'SQL_TRAINING'
and object_type = 'TABLE'


SELECT * FROM all_objects
where object_type = 'VIEW'
and rownum < 10 


SELECT * FROM sys.V_$VerSION


SELECT * FROM employees


CREATE VIEW super_employees AS

SELECT store_id, MAX(sal) sal
FROM employees
GROUP BY store_id


SELECT * FROM
EMPLOYEES e1
INNER JOIN
    (SELECT store_id, MAX(sal) sal
    FROM employees
    GROUP BY store_id) e2
ON e1.store_id = e2.store_id
AND e1.sal = e2.sal


SELECT * FROM
EMPLOYEES e1
INNER JOIN
    (SELECT store_id, MAX(sal) sal
    FROM employees
    GROUP BY store_id) e2
ON e1.store_id = e2.store_id
AND e1.sal = e2.sal
WHERE ename != 'FORD'


CREATE VIEW super_employees AS
SELECT e1.* FROM
EMPLOYEES e1
INNER JOIN
    (SELECT store_id, MAX(sal) sal
    FROM employees
    GROUP BY store_id) e2
ON e1.store_id = e2.store_id
AND e1.sal = e2.sal
WHERE ename != 'FORD'


SELECT * from super_employees


SELECT * from super_employees
UNION
SELECT * FROM employees


SELECT * FROM super_employees
UNION ALL
SELECT * FROM employees


SELECT * FROM super_employees
MINUS
SELECT * FROM employees where job = 'SALESMAN'


CREATE or replace VIEW super_employees AS
SELECT e1.*
FROM EMPLOYEES e1
INNER JOIN
    (SELECT store_id, MAX(sal) sal
    FROM employees
    GROUP BY store_id) e2
ON e1.store_id = e2.store_id
AND e1.sal = e2.sal
WHERE ename != 'FORD'


drop view super_employees
