CREATE TABLE products
(
    product_id number not null,
    name varchar(50),
    product_cost number(5,2),
    product_retail number(5,2),
    product_type varchar(10),
    store_id number not null,

    CONSTRAINT product_pk PRIMARY KEY (product_id)
)


select * from products -- no data yet


-- Solution to Assignment
INSERT INTO products (product_id, name, product_cost, product_retail, product_type, store_id )
    VALUES (1001, 'Colgate Toothpaste', 2.25, 5.47, 'hygiene', 2)

INSERT INTO products (product_id, name, product_cost, product_retail, product_type, store_id )
    VALUES (1002, 'Colgate Toothpaste', 2.25, 5.47, 'hygiene', 2)

INSERT INTO products (product_id, name, product_cost, product_retail, product_type, store_id )
    VALUES (1003, 'Listerine Mouthwash', 1.75, 4.81, 'hygiene', 3)


SELECT * from products


INSERT ALL
    INTO products (product_id, name, product_cost, product_retail, product_type, store_id )
        VALUES (1004, 'T-Shirt', 1.75, 7.77, 'Clothing', 2)
    INTO products (product_id, name, product_cost, product_retail, product_type, store_id )
        VALUES (1005, 'T-Shirt', 1.65, 7.85, 'Clothing', 2)
    INTO products (product_id, name, product_cost, product_retail, product_type, store_id )
        VALUES (1006, 'T-Shirt', 1.73, 7.80, 'Clothing', 3)
    INTO products (product_id, name, product_cost, product_retail, product_type, store_id )
        VALUES (1007, 'Shorts', 0.73, 5.60, 'Clothing', 3)
    INTO products (product_id, name, product_cost, product_retail, product_type, store_id )
        VALUES (1008, 'Dress Shoes', 17.85, 87.67, 'Clothing', 2)
    INTO products (product_id, name, product_cost, product_retail, product_type, store_id )
        VALUES (1009, 'Garden Chair', 12.01, 27.87, 'Home & Gar', 2)
    INTO products (product_id, name, product_cost, product_retail, product_type, store_id )
        VALUES (1010, 'Grass Fertilizer', 3.20, 8.70, 'Home & Gar', 2)
SELECT * FROM DUAL; 
