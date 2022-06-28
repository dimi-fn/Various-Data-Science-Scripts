SELECT * FROM EMP
WHERE JOB = 'CLERK'
OR JOB = 'SALESMAN'


-- Get the names of those employees that are not managers nor salesmen and have a salary greater than or equal to 2000 
SELECT ENAME FROM EMP
WHERE JOB != 'MANAGER'
AND JOB != 'SALESMAN'
AND SAL >= 2000
