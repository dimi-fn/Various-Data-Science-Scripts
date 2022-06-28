-- Write a query that returns those employees that don't make any commision and have a salary greater than 1100
-- but less than 5000. Exclude those employees that have a salary equal to 3000
SELECT * FROM EMP WHERE ( COMM IS NULL
AND SAL > 1100 AND SAL < 5000
AND SAL <> 3000 )
OR COMM = 0


SELECT * FROM EMP
WHERE ( COMM IS NULL or COMM = 0)
AND SAL > 1100 AND SAL < 5000
AND SAL <> 3000


-- Returns those employees that are salesman and that make either 300 dollars in commission
--or greater than 1100 follars in collission
SELECT * FROM EMP
WHERE JOB = 'SALESMAN'
AND (COMM = 300 OR COMM > 1100)


SELECT * FROM EMP 
WHERE JOB LIKE 'S%'


SELECT * FROM EMP 
WHERE JOB LIKE '%GER'


