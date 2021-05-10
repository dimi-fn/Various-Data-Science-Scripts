SELECT * from dept


SELECT * from dept
where deptno = 30


SELECT * from dept
where deptno = ( select deptno from dept where deptno = 30)


SELECT * from dept
where deptno < ( select deptno from dept where deptno = 30)


SELECT * from dept
where deptno < ( select deptno from dept where deptno = 30)
and dname = 'ACCOUNTING'


SELECT * from dept
where deptno < 30
and dname = 'ACCOUNTING'


SELECT * from ( select * from dept)


SELECT * from ( select * from emp)


SELECT * from emp where deptno = (select deptno from dept where loc = 'CHICAGO')


SELECT * from emp where deptno in (select deptno from dept where deptno in (10,20))


SELECT * from emp where deptno in (select deptno, loc, dname from dept where deptno in (10,20)) --too many values


SELECT job, ename, (select job from emp)
from emp  -- single-row subquery returns more than one row


SELECT job, ename, (select job from emp where ename = 'KING')
from emp 


SELECT job, ename, (select 'Hello' from emp)
from emp -- single-row subquery returns more than one row


SELECT job, ename, (select * from dual)
from emp


SELECT job, ename, (select 'Hello there' from dual)
from emp


SELECT job, ename, (select 'Hello there' from dual)
from emp
where job = (select job from emp where job = 'PRESIDENT')

