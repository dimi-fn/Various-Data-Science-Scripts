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
SELECT * FROM employee
ORDER BY sex, first_name, last_name;

-- find the first 5 employees in the table of 'employees'
SELECT * FROM employee
LIMIT 5;

-- find all unique genders
SELECT DISTINCT sex
FROM employee;


---------------------------------------------------------------
-- SQL functions
---------------------------------------------------------------

-- find the total number of employees
SELECT COUNT(emp_id) FROM employee;

-- find how many employees have supervisors
SELECT COUNT(super_id) FROM employee;

--find the total number of unique supervisors
SELECT COUNT(DISTINCT super_id) AS unique_supervisors FROM employee;

-- find the number of female employees born after 1970
SELECT count(emp_id) FROM employee
where sex='F' AND birth_day>'1970-01-01';

-- find the average salary of male employees
SELECT AVG(salary) FROM employee
WHERE sex='M';

-- find the sum of all employees' salary
SELECT SUM(salary) FROM employee;

------------------------------ Aggregations ------------------------------

-- find how many of the employes are male and how many are female
SELECT COUNT(sex), sex FROM employee
GROUP BY sex;

----- find the total sales for each salesman
-- table: works_with
SELECT emp_id, sum(total_sales) FROM works_with
GROUP BY(emp_id);

-- find how much money each client spends with the branch
SELECT client_id, sum(total_sales) FROM works_with
GROUP BY(client_id)
ORDER BY sum(total_sales) DESC;


------------------------------ Wildcards (Like) ------------------------------

------ find any clients who are an LLC
-- '%': match with ANY number of characters in that attribute
-- '%LLC': any attribute containing 'LLC'
SELECT * FROM client WHERE client_name LIKE '%LLC';


------ find any employee born in October
--- '_' : match with ONE character in that attribute
-- in this case 4 underscores respesting the years, % for any number of character after the 10th month 
select * from employee WHERE birth_day LIKE '____-10%';
-- equivalent with:
select * from employee WHERE birth_day LIKE '____-10-____';

-- find any clients who are schools
select * from client where client_name LIKE '%school%';


------------------------------ Unions ------------------------------

------ Rules in unions with multiple select statements
------   * column names between the tables should be the same as well as
------   their respective data types

--- find a list of all money spent or earned by the company
-- tables: employee, works_with

select salary from employee
UNION 
select total_sales FROM works_with;


------------------------------ JOINS ------------------------------

------ find all branches and the names of their managers
------ tables: branch, employee (PS: manager IDs coincides with the employee IDs)
-- for the sake of the query:
INSERT INTO branch values(4,'Buffalo', NULL, NULL);

SELECT  branch.branch_id, employee.emp_id, employee.first_name, employee.last_name, branch.branch_name
FROM employee
JOIN branch --common column is branch_id, hence join will be made on this column
WHERE employee.emp_id = branch.mgr_id;



