SELECT *
from emp, dept
WHERE emp.deptno = dept.deptno


SELECT *
from emp INNER JOIN dept
ON emp.deptno = dept.deptno


SELECT *
from emp RIGHT JOIN dept
ON emp.deptno = dept.deptno


SELECT *
from emp LEFT JOIN dept
ON emp.deptno = dept.deptno


SELECT *
from dept LEFT JOIN emp
ON emp.deptno = dept.deptno


SELECT *
from dept RIGHT JOIN emp
ON emp.deptno = dept.deptno


SELECT *
from emp RIGHT OUTER JOIN dept
ON emp.deptno = dept.deptno


SELECT *
from emp LEFT OUTER JOIN dept
ON emp.deptno = dept.deptno


SELECT *
from emp, dept
WHERE emp.deptno(+) = dept.deptno --RIGHT OUTER JOIN


SELECT *
from emp, dept
WHERE emp.deptno = dept.deptno(+) --LEFT OUTER JOIN


SELECT *
from emp FULL OUTER JOIN dept
ON emp.deptno = dept.deptno


SELECT *
from (select * from emp) emp FULL OUTER JOIN dept
ON emp.deptno = dept.deptno


SELECT *
from (select * from emp) e FULL OUTER JOIN dept
ON e.deptno = dept.deptno


SELECT *
from (select * from emp) e FULL OUTER JOIN (select * from dept) d
ON e.deptno = d.deptno


SELECT *
from (select * from emp) e, (select * from dept) d
WHERE e.deptno = d.deptno


SELECT *
from (select * from emp where job = 'SALESMAN') e FULL OUTER JOIN (select * from dept) d
ON e.deptno = d.deptno

