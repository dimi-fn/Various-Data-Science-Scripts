SELECT ENAME "EMPLOYEE NAME", SAL SALARY, COMM COMMISSION
FROM EMP;


SELECT 'hello my name is ' || ename as "concatenated value"
FROM EMP
WHERE job = 'MANAGER'

-- Create Query that looks like:
-- King makes $5000 per month 
-- Blake makes $2850 per month 
-- Clark makes $2450 per month 
SELECT ename || ' makes $' || sal || ' per month' as "employee income"
FROM EMP


-- ORDER BY 
SELECT *
FROM emp
ORDER BY ENAME


SELECT *
FROM emp
ORDER BY SAL


-- ORDER BY descending order
SELECT *
FROM emp
ORDER BY SAL DESC


-- ORDER BY ascending order
SELECT *
FROM emp
ORDER BY SAL ASC


SELECT DEPTNO, SAL, ENAME
FROM EMP
ORDER BY DEPTNO, SAL


SELECT *
FROM EMP
ORDER BY DEPTNO, SAL

