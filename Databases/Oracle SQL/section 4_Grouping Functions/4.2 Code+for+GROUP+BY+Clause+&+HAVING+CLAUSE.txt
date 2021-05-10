SELECT avg(sal), job
from emp
GROUP BY job


SELECT job
from emp
GROUP BY job


SELECT count(*), job
from emp
GROUP BY job


SELECT min(sal), job
from emp
GROUP BY job


SELECT distict job from emp


SELECT count(*), job
from emp
GROUP BY job
HAVING count(*) = 2


SELECT job
from emp
GROUP BY job
HAVING count(*) = 2


--1) SELECT job
--2) FROM emp
--3) WHERE
--4) GROUP BY JOB
--5) HAVING count(*) = 2
--6) ORDER BY


SELECT deptno
from emp
GROUP BY deptno
HAVING count(*) > 3


SELECT deptno, count(*)
from emp
GROUP BY deptno


SELECT deptno, count(*)
from emp
GROUP BY deptno
HAVING count(*) > 3
