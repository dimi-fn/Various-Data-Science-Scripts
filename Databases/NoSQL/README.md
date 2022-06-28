# NoSQL

Contents
=======================
* [MongoDB](#mongodb)

------
# MongoDB

* [MongoDB commands - cheatsheet](https://www.mongodb.com/developer/quickstart/cheat-sheet/)

|Command|Description|
|--------|---------|
| **************** | **************** |
| `ls()` | ls|
| `cd('code')`| cd |
| `pwd()`| pwd |
| `load(filename.js)`| run JS file |
| **************** | **************** |
|  `show dbs` | display databases|
|`show collections`| display collections|
|`db.stats()`|display info about db|
| **************** | **************** |
| `db.createCollection(<colleciton-name>)`| |
|`use <db-name>`| switch database|
| **************** | **************** |
|`db.collectioName.insertOne({})`||
|`db.collectioName.insertMany({})`||
| **************** |**************** |
| `db.collectioName.find({})`| like selecting in SQL|
|`db.collectioName.find().sort({variable-name: -1})`| -1: descending order|
|`db.collectioName.find().sort({<variable-name>: 1})`| 1: ascending order|
| **************** |**************** |
| | `$lt`, `$gt` | less than, greater than|
| `$lookup`| like joins in SQL |
|  `$match`| it filters data |
| **************** |**************** |
