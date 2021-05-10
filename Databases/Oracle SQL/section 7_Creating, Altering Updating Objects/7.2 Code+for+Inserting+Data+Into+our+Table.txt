INSERT INTO stores(store_id, city) VALUES (1, 'San Francisco')


select * from stores -- You can see that one row has been inserted


INSERT INTO stores(store_id, city) VALUES (2, 'New York City')


select * from stores -- Both rows are now in our table


-- COMMIT; We don't need commit in APEX, statements are automatically committed. 


INSERT INTO stores(store_id, city) VALUES (3, 'Chicago')


-- Faster Way to insert into a table
INSERT ALL
    INTO stores (store_id, city) VALUES (4, 'Philadelphia')
    INTO stores (store_id, city) VALUES (5, 'Boston')
    INTO stores (store_id, city) VALUES (6, 'Seattle')
SELECT * FROM DUAL; 


SELECT store_id, count(*)
from stores
group by store_id


-- The code below does not work because we cannot insert NULL into store_id
INSERT ALL
    INTO stores (store_id, city) VALUES (NULL, 'Philadelphia')
    INTO stores (store_id, city) VALUES (NULL, 'Boston')
    INTO stores (store_id, city) VALUES (NULL, 'Seattle')
SELECT * FROM DUAL; 

