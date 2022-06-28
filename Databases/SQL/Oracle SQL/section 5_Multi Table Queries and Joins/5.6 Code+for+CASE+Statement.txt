SELECT ename, job, (CASE job
 WHEN 'PRESIDENT' THEN 'big shot'
 WHEN 'MANAGER' THEN 'decides the pay'
 WHEN 'ANALYST' THEN 'good at pay'
 WHEN 'CLERK' THEN 'hard working'
 ELSE 'no comment'
 END) as 'COMMENT'
FROM emp;

-- Solution to Assignment

SELECT ename, sal, CASE
 WHEN sal >= 3000 THEN 'big shot'
 WHEN sal < 3000 THEN 'need more money'
 END as salary_comment
FROM emp;

