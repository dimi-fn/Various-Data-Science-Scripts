-- 5 tables in total


-- SELECT data FROM all tables
SELECT * FROM employee;
SELECT * FROM branch;
SELECT * FROM client;
SELECT * FROM works_with;
SELECT * FROM branch_supplier;


-- Find all employees ordered by salary (with descending order)
SELECT * FROM employee 
ORDER BY salary;

-- Find all employees ordered by sex and then by name
select * from employee
ORDER BY sex, first_name, last_name;

-- Find the first 5 employees in the table of 'employees'
select * from employee
LIMIT 5;
