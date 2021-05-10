-- Solution to Assignment from previous video
SELECT empno, ename, job, mgr, hiredate, sal, comm, e.deptno as deptno, d.deptno as deptno, dname, loc
from (select * from dept) d LEFT OUTER JOIN (select * from emp where job = 'SALESMAN') e
ON e.deptno = d.deptno


SELECT e.*, d.*
from (select * from dept) d LEFT OUTER JOIN (select * from emp where job = 'SALESMAN') e
ON e.deptno = d.deptno -- Further Simplified Version


SELECT * 
from emp
WHERE EXISTS (select 'random' from dual)


SELECT * 
from emp
WHERE NOT EXISTS (select 'random' from dual)


SELECT * 
from emp
WHERE EXISTS (select null from dual)


SELECT * 
from emp
WHERE NOT EXISTS (select * from emp where job = 'PROGRAMMER')


SELECT d.*
FROM dept d
WHERE EXISTS (SELECT * FROM emp WHERE d.deptno = emp.deptno)


SELECT d.*
FROM dept d
WHERE NOT EXISTS (SELECT * FROM emp WHERE d.deptno = emp.deptno)
AND LOC = 'CHICAGO' -- no data found


SELECT d.*
FROM dept d
WHERE NOT EXISTS (SELECT * FROM emp WHERE d.deptno = emp.deptno)
AND LOC = 'BOSTON' -- no data found


SELECT d.*
FROM dept d
WHERE NOT EXISTS (SELECT * FROM emp WHERE d.deptno = emp.deptno)
OR LOC = 'CHICAGO'
