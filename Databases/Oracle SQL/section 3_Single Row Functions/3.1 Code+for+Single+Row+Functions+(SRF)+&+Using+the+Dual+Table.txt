SELECT 'my name is ' || ename
FROM EMP


SELECT concat('my name is ', ename)
FROM EMP


SELECT upper('hello')
from emp

SELECT 'hello'
from emp
where deptno = 20


select upper('hello')
from DUAL


select lower('hello')
from DUAL 


SELECT 'pizza' as FOOD, 'fanta' as drink, concat('hello', ' John') from dual


SELECT 'pizza' as FOOD, 'fanta' as drink, concat('hello', ' John') as "This is a func" from dual


SELECT concat(lower(ename), ' is the name') from emp


SELECT concat(lower(ename), upper(' is the name')) from emp
where deptno = 20

-- Solution to assignment 
SELECT concat(concat(lower(ename), upper(' is the name')), concat(' and their job is: ', job)) as "function call" from emp
where deptno = 20


