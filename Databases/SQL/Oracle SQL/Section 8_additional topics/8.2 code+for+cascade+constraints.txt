
CREATE TABLE supplier
( supplier_id numeric(10) not null,
  supplier_name varchar2(50) not null,
  contact_name varchar2(50),
  CONSTRAINT supplier_pk PRIMARY KEY (supplier_id)
);

CREATE TABLE products
( product_id numeric(10) not null,
  supplier_id numeric(10) not null,
  CONSTRAINT fk_supplier
    FOREIGN KEY (supplier_id)
    REFERENCES supplier(supplier_id)
);

BEGIN

INSERT INTO supplier values(10, '1st Supplier', 'John Dollan');
INSERT INTO supplier values(20, '2nd Supplier', 'Steve Reeves');
INSERT INTO supplier values(30, '3rd Supplier', 'Peter Marcello');

INSERT INTO products values(1, 10);
INSERT INTO products values(2, 10);
INSERT INTO products values(3, 10);
INSERT INTO products values(4, 20);
INSERT INTO products values(5, 20);
INSERT INTO products values(6, 30);

END;
/