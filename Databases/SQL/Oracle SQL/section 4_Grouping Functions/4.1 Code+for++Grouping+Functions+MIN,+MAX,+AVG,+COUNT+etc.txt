select max(sal) from emp


select max(sal) as max_sal from emp


select min(sal) as min_sal from emp


select sum(sal) as sum_sal from emp


SELECT * from emp
where lower(job) like '%manager%'


SELECT max(sal) from emp
where lower(job) like '%manager%'


SELECT max(sal) from emp
where job = 'MANAGER'


SELECT avg(sal) as avg_sal from emp


SELECT count(ename) as count from emp


SELECT count(sal) as count from emp


SELECT count(*) as count from emp


SELECT count(comm) as count from emp


SELECT sum(sal) / count(*) as computed_avg, avg(sal) as native_avg from emp


SELECT sum(sal) + avg(sal) as computed from emp 


SELECT sum(sal) as sum, avg(sal) as avg, max(sal) as max, min(sal) as min, count(*)
from emp


SELECT avg(sal)
from emp
where job = 'SALESMAN'


SELECT avg(sal)
from emp
where job = 'CLERK'


SELECT avg(sal)
from emp
where job = 'MANAGER'

