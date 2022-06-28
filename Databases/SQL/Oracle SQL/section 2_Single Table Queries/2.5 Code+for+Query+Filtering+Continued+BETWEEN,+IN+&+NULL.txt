-- Solution to problem from Lecture 7 
SELECT ename, hiredate FROM EMP
WHERE DEPTNO  = 20 
OR DEPTNO = 30


SELECT ename, hiredate FROM EMP
WHERE DEPTNO IN (20,30)


SELECT ename, hiredate FROM EMP
WHERE ENAME IN ('FORD', 'SMITH', 'ALLEN', 'WARD', 'MARTIN')


SELECT ename, hiredate FROM EMP
WHERE ENAME NOT IN ('FORD', 'SMITH', 'ALLEN', 'WARD', 'MARTIN')


SELECT * from emp
where hiredate between '05/01/1981' and '12/09/1982'


SELECT * from emp
where SAL between 1000 AND 2000


SELECT * from emp
where SAL NOT BETWEEN 950 AND 1600

SELECT * FROM EMP
WHERE COMM IS NOT NULL;


SELECT * FROM EMP WHERE MGR IS NULL

