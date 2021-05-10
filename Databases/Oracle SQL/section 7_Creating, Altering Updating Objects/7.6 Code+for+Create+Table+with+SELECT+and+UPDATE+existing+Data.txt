CREATE TABLE employees AS
SELECT empno, ename, job, hiredate, sal, comm
FROM emp;


SELECT * from employees


DESCRIBE employees


DESCRIBE emp


ALTER TABLE employees
    ADD store_id number not null; -- gives error


ALTER TABLE employees
    ADD store_id number; -- works fine now


SELECT * from employees


UPDATE employees
SET store_id = 3
WHERE ename in ('KING', 'BLAKE', 'CLARK')


UPDATE employees
SET store_id = 2
WHERE job = 'SALESMAN'


UPDATE employees
SET store_id = 4
WHERE job = 'CLERK'



UPDATE employees
SET store_id = 4
WHERE job = 'ANALYST'


UPDATE employees
SET store_id = 3
WHERE ename = 'JONES'

-- Solution to Assignment
ALTER TABLE employees
    MODIFY store_id number not null;
