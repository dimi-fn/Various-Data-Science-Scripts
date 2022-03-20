# Databases

One of the main differences between SQL and NoSQL is that the former is a relational database architecture and it is in the form of tables, while the latter is in the form of key-value pairs with collections of documents (tables in SQL are collections in NoSQL)

Contents
=======================
* [SQL](#sql)
* [NoSQL](#nosql)
    * [MongoDB](#mongodb)

------

# SQL

* Tutorials
    * [The SQL Tutorial for Data Analysis by mode.com](https://mode.com/sql-tutorial/introduction-to-sql/)
    * [Entity Relationship Diagram (ERD)(https://www.youtube.com/watch?v=QpdhBUYk7Kk&ab_channel=Lucidchart)
* [e-books](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Databases/e-books)
* [Cheatsheets](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Databases/Cheatsheets)    
* [sqlite3](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Databases/sqlite3)
    * https://colab.research.google.com/drive/16kEVgvauogGKEC8PJr-J23SNtGItpVg1?usp=sharing
        * `Connect` | `Create` | `Insert` & `Commit` | `Read` | `Drop` | `Close`
        * Creating a `database interface` with `SQLlite`
* [Oracle SQL](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Databases/Oracle%20SQL) 


------

# NoSQL

## MongoDB

* [MongoDB commands - cheatsheet](https://www.mongodb.com/developer/quickstart/cheat-sheet/)

|Command|Description|
|--------|---------|
|  `show dbs` | display databases|
|`show collections`| display collections|
|`db.stats()`|display info about db|
|******** |********|
| `db.createCollection(<colleciton-name>)`| |
|`use <db-name>`| switch database|
|******** |********|
|`db.collectioName.insertOne({})`||
|`db.collectioName.insertMany({})`||
|******** |********|
| `db.collectioName.find({})`| like selecting in SQL|
|`db.collectioName.find().sort({variable-name: -1})`| -1: descending order|
|`db.collectioName.find().sort({<variable-name>: 1})`| 1: ascending order|
