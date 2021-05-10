SELECT lower(ename) from emp;


SELECT *
FROM emp
WHERE JOB = lower('MANAGER')


SELECT *
FROM emp
WHERE JOB = upper('MANAGER')


SELECT *
FROM emp
WHERE JOB = upper('manager')


SELECT initcap('hello my name is Imtiaz') as sentence
from dual


SELECT length('hello my name is Imtiaz') as length
from dual


SELECT length(ename) as length
from emp


SELECT ename, length(ename) as length
from emp


SELECT ename, length(ename) as length
from emp
where length(ename) = 6


select substr('hello', 2, 2)
from dual


select 'hello', substr('hello', 2, 2)
from dual


select 'hello', substr('hello', 2)
from dual


select 'Hello my name is', substr('Hello my name is', 10)
from dual


select 'Hello my name is', substr('Hello my name is', 10, 5)
from dual


select 'Hello my name is', length(substr('Hello my name is', 10, 5))
from dual


select LPAD('hello', 10, '&')
from dual


select LPAD('hello', 100, '&')
from dual


select RPAD('hello', 100, '&')
from dual


select LTRIM('hello', 'h')
from dual


select RTRIM('hhhhhellohhhhh', 'h')
from dual

