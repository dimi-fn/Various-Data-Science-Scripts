-- 5 tables in total

---------------------------------------------------------------
-- Basic queries
---------------------------------------------------------------

-- SELECT data FROM all tables
SELECT * FROM employee;
SELECT * FROM branch;
SELECT * FROM client;
SELECT * FROM works_with;
SELECT * FROM branch_supplier;


-- find all employees ordered by salary (with descending order)
SELECT * FROM employee 
ORDER BY salary;

-- find all employees ordered by sex and then by name
select * from employee
ORDER BY sex, first_name, last_name;

-- find the first 5 employees in the table of 'employees'
select * from employee
LIMIT 5;

-- find all unique genders
select DISTINCT sex
from employee;


---------------------------------------------------------------
-- SQL functions
---------------------------------------------------------------

-- find the total number of employees
select COUNT(emp_id) from employee;

-- find how many employees have supervisors
select COUNT(super_id) from employee;

--find the total number of unique supervisors
select COUNT(DISTINCT super_id) AS unique_supervisors from employee;

-- find the number of female employees born after 1970
select count(emp_id) from employee
where sex='F' AND birth_day>'1970-01-01';

-- find the average salary of male employees
select AVG(salary) from employee
WHERE sex='M';

-- find the sum of all employees' salary
select SUM(salary) from employee;

----------------- Aggregations -----------------

-- find how many of the employes are male and how many are female
select COUNT(sex), sex from employee
GROUP BY sex;

----- find the total sales for each salesman
-- table: works_with
select emp_id, sum(total_sales) from works_with
GROUP BY(emp_id);

-- find how much money each client spends with the branch
select client_id, sum(total_sales) from works_with
GROUP BY(client_id)
ORDER BY sum(total_sales) DESC;
