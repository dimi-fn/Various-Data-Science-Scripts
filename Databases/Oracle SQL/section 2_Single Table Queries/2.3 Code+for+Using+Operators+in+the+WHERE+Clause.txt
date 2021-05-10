SELECT * FROM EMP
WHERE JOB != 'SALESMAN'


SELECT * FROM EMP
WHERE JOB = 'SALESMAN'
AND SAL = 1500


SELECT * FROM EMP
WHERE JOB != 'SALESMAN'
AND SAL < 2500


SELECT * FROM EMP
WHERE JOB != 'SALESMAN'
AND SAL < 3000


SELECT * FROM EMP
WHERE JOB != 'SALESMAN'
AND SAL <= 3000


SELECT * FROM EMP
WHERE JOB != 'SALESMAN'
AND SAL > 3000


-- Write a query that returns those employees who have a commission greater than their salary 
SELECT * FROM EMP
WHERE COMM > SAL


-- Get all employees that are not managers and have a salary greater than 2500 and also work in department no# 20 
SELECT * FROM EMP
WHERE JOB != 'MANAGER'
AND SAL > 2500
AND DEPTNO = 20

