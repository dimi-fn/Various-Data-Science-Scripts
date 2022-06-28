SELECT * FROM DEPT


SELECT * FROM DEPT WHERE deptno = 40


DELETE FROM DEPT WHERE deptno = 40


DELETE FROM DEPT WHERE dname IN ('ACCOUNTING') -- I don't run this


ALTER TABLE emp
DROP CONSTRAINT EMP_DEPT_FK -- Use the FK that you see


SELECT * FROM emp


DROP TABLE dept


TRUNCATE TABLE emp


SELECT * FROM emp -- no date found


SELECT * FROM dept -- table no longer exists


DROP TABLE emp
