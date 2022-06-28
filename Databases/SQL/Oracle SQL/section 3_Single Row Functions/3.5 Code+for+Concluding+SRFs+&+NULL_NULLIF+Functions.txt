select ename, job, sal, comm
from emp
where empno in (7839, 7698, 7566, 7654)


select ename, job, sal, NVL(comm, 0)
from emp
where empno in (7839, 7698, 7566, 7654)

-- Solution to Assginment at 4:00 

select ename, job, sal, NVL(to_char(comm), 'No Data Found')
from emp
where empno in (7839, 7698, 7566, 7654)


select ename, length(ename) from emp


select ename, length(ename), NULLIF(length(ename), 5) from emp


select ename, length(ename), nvl(NULLIF(length(ename), 5), 'length is 5') from emp /* Gives "invalid number" error */


select ename, length(ename), nvl(NULLIF(to_char(length(ename)), to_char(5)), 'length is 5') from emp 


select ename, length(ename), nvl(NULLIF(to_char(length(ename)), to_char(5)), 'length is 5') as result, sal from emp 
where sal > 2000


