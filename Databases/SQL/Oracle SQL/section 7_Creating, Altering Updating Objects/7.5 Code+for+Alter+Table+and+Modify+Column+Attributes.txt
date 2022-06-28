SELECT * FROM products


INSERT INTO PRODUCTS VALUES (1011, '', 4.00, 8.00, 'Clothing', 3)


DESCRIBE products


ALTER TABLE products
    MODIFY name varchar2(50) not null -- null values found


DELETE FROM products WHERE product_id = 1011


ALTER TABLE products
    MODIFY name varchar2(50) not null -- works now


INSERT INTO PRODUCTS VALUES (1011, '', 4.00, 8.00, 'Clothing', 3) -- won't work now because we cannot insert NULL values


DESCRIBE product_pk


DESCRIBE products


ALTER TABLE products
    MODIFY (product_cost number(5,2) not null,
            product_retail number(5,2) not null );


ALTER TABLE products
    RENAME COLUMN name to product_name;


SELECT * FROM products


