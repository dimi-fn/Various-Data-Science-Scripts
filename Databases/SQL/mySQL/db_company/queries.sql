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
WHERE sex='F' AND birth_day>'1970-01-01';

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
select * from client WHERE client_name LIKE '%school%';


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

----------------------------------------
---- https://www.w3schools.com/sql/sql_join.asp
-- * Join (inner join)
-- * left join
-- * right join
-- * full outer join
----------------------------------------

------ find all branches and the names of their managers
------ tables: branch, employee (PS: manager ID coincides with that of the employee ID)
-- for the sake of the query:
INSERT INTO branch values(4,'Buffalo', NULL, NULL);

SELECT  branch.branch_id, employee.emp_id, employee.first_name, employee.last_name, branch.branch_name
FROM employee
JOIN branch --common column is branch_id, hence join will be made on this column
ON employee.emp_id = branch.mgr_id;


------------------------------ Nested Queries ------------------------------

---- In SQL, nested queries are executed from the bottom-up, i.e. firstly the nested query will be executed

---- find all employee names that have sold over 30,000 to a single client
-- 1st way
select employee.emp_id, employee.first_name, employee.last_name, works_with.client_id, works_with.total_sales
FROM employee
JOIN works_with
ON employee.emp_id=works_with.emp_id
WHERE total_sales>30000;

-- However, the above does not give the unique employee names. If we want that then:
select DISTINCT(employee.emp_id), employee.first_name, employee.last_name, works_with.client_id, works_with.total_sales
FROM employee
JOIN works_with
ON employee.emp_id=works_with.emp_id
WHERE total_sales>30000
GROUP BY employee.emp_id;

-- 2nd way via nested query
select employee.emp_id, employee.first_name, employee.last_name
from employee
WHERE employee.emp_id IN (
     select works_with.emp_id
     from works_with
     WHERE works_with.total_sales>30000
);

-- find all clients who are handled by the branch that Michael Scott manages. Assume we know Michael's ID
select client.client_name
from client
WHERE client.branch_id=(
     select branch.branch_id
     from branch
     WHERE branch.mgr_id = 102
);

------------------------------ Triggers ------------------------------

-- create a trigget_test table for displaying a message everytime a new employee is created in the employee table
CREATE TABLE trigger_test(
     message VARCHAR(100)
);

-- this can only be executed from the terminal, i.e. and e.g. the mySQL command line client
DELIMETER $$ -- change the delimeter from ';' to something else, here it will be '$$'
               -- that is because of the code: INSERT INTO trigger_test VALUES('added new employee');
                    -- we want a loop there, however we need to change the delimeter otherwise it will only be executed one time

CREATE 
     TRIGGER my_trigger BEFORE INSERT
     ON employee
     FOR EACH ROW BEGIN 
     INSERT INTO trigger_test VALUES('added new employee');
     END$$ -- instead of END; --> END$$ 

DELIMETER ;   --change the delimeter back to the default ';'

