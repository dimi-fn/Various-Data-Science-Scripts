DESCRIBE emp -- get description of any table


CREATE table dest_tbl_1
(
    id number,
    name varchar2(50),
    date_of date
)


CREATE table dest_tbl_2
(
    id number,
    name varchar2(50),
    date_of date
)


CREATE table dest_tbl_3
(
    id number,
    name varchar2(50),
    date_of date
)


INSERT ALL
    INTO dest_tbl_1 (id, name, date_of) values (EMPNO, ENAME, HIREDATE)
    INTO dest_tbl_2 (id, name, date_of) values (EMPNO, ENAME, HIREDATE)
    INTO dest_tbl_3 (id, name, date_of) values (EMPNO, ENAME, HIREDATE)
SELECT empno, ename, hiredate
FROM emp


SELECT * FROM dest_tbl_1


INSERT ALL
WHEN sal <= 1500 THEN
    INTO dest_tbl_1 (id, name, date_of) values (EMPNO, ENAME, HIREDATE)
WHEN sal BETWEEN 1501 AND 2500 THEN 
    INTO dest_tbl_2 (id, name, date_of) values (EMPNO, ENAME, HIREDATE)
WHEN sal  > 2500 THEN
    INTO dest_tbl_3 (id, name, date_of) values (EMPNO, ENAME, HIREDATE)
SELECT empno, ename, hiredate, sal
FROM emp


SELECT * FROM dest_tbl_3


SELECT * FROM dest_tbl_3


SELECT * FROM dest_tbl_3
