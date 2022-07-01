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

-- Find all employees ordered by sex 
