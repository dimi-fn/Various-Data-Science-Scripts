SELECT * FROM employees


CREATE INDEX emp_name_idx
    ON employees (ename)


CREATE INDEX emp_name_job_date_idx
    ON employees (ename, job, hiredate)


--SELECT * FROM employees
--WHERE ename = 'John'
--AND hiredate = ''
--AND job = ''


CREATE UNIQUE INDEX emp_job_idx  -- cannot create UNIQUE INDEX
    ON employees (job)


CREATE INDEX emp_job_idx  -- this works
    ON employees (job)


DROP INDEX emp_job_idx


DROP INDEX emp_name_job_date_idx


CREATE INDEX emp_name_job_date_idx
ON employees (ename, job, hiredate)
COMPUTE STATISTICS;


ALTER INDEX emp_name_idx
REBUILD COMPUTE STATISTICS

