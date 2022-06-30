# SQL

Contents
=======================
* [e-books](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Databases/SQL/e-books)
* [Cheatsheets](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Databases/SQL/Cheatsheets)
* [Tutorials](#tutorials)
* [Oracle SQL](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Databases/SQL/Oracle%20SQL)
* [sqlite3](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Databases/SQL/sqlite3)
* [PostgreSQL](#postgresql)
* [mySQL](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Databases/SQL/mySQL)
* [SQL - Basics & Miscellaneous](#sql---basics--miscellaneous)
    * [General](#general)
    * [Data Types](#data-types)
    * [Keys](#keys)
    * [Foreign Keys Constraints](#foreign-keys-constraints)


-------------------------

# Tutorials

* [The SQL Tutorial for Data Analysis by mode.com](https://mode.com/sql-tutorial/introduction-to-sql/)
* [Entity Relationship Diagram (ERD)](https://www.youtube.com/watch?v=QpdhBUYk7Kk&ab_channel=Lucidchart)
* [Oracle SQL](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Databases/SQL/Oracle%20SQL)


-----------------

# PostgreSQL

After entering postgreSQL database with docker:

|Command|Description|
|--------|---------|
| `\i code/<filename.sql>` ->| to execute code |
| `\dt`| show tables|

-----------------

# SQL - Basics & Miscellaneous

# General
    
* In Relational Database Management Systems you can use SQL to
    * proceed to CRUD operations
    * create and manage databases
    * design & create database tables
    * implement administrative tasks (e.g. user management, security, etc)

<br>

* SQL
    * Data Query Language (DQL)    
        * query the db (database)
    * Data Definition Language (DDL)        
        * define db schemas
    * Data Control Language (DCL)
        * control who has access to the db
        * manage permissions
    * Data Manipulation Language (DML)
        * allows CRUD operations in the db
  

-------

# Data Types
    
* Main SQL data types:
    * `INT`
    * `DECIMAL`(length of number, length of decimal point)
    * `VARCHAR`()
    * `BLOB` (binary large number)
    * `DATE`
    * `TIMESTAMP`

# Keys   

|What|Description|
|--------|---------|
| `primary key`| an attribute which uniquely identifies the row in a database |
|`surrogate key`|a key that has no mapping to anything in the real world (e.g. a random employee number assigned to a company's employees)|
| `natural key`|e.g. social security number that can be used as a primary key (it has a mapping to something in the real world) |
| `foreigh key`| * a foreigh key stores the primary key of a row in another database table<br>* a table can have more than one foreign key |
|`composite (compound) key` | * a primary key consisted of two attributes (columns)<br>* there are cases when only two keys combined together can uniquely identify each row in the table |  
| | |

-------

# Foreign Keys Constraints

| ON UPDATE or ON DELETE | What it does | 
|-----------------------|---------------|
| `NO ACTION`|The update or delete operations in the parent table will fail with an error |
| `CASCADE`| The same action performed on the referenced values of the parent table will be reflected to the related values in the child table. For example, if the referenced value is deleted in the parent table, all related rows in the child table are also deleted|
|`SET NULL`| All related values in the child table are set to NULL value|
| `SET DEFAULT`| The related values in the child table with FOREIGN KEY columns will be set to its default value |


-------

# Useful Sources

* https://www.sqlshack.com/commonly-used-sql-server-constraints-foreign-key-check-default/
