SELECT * from emp


Select job, count(*)
from emp
group by job


Select job, count(*)
from emp
group by job, deptno


SELECT job, deptno
from emp


SELECT job, deptno
from emp
group by job, deptno


SELECT job, deptno, count(*)
from emp
group by job, deptno

