DROP TABLE building_lease

CREATE TABLE building_lease (
	lease_number NUMBER,
	address VARCHAR2(50) NOT NULL,
	lease_expiring_in INTERVAL YEAR TO MONTH,
	PRIMARY KEY (lease_number)
);

INSERT INTO building_lease (
	lease_number,
	address,
	lease_expiring_in
	)
VALUES (
	110,
	'303 Remdel Ave New York, NY 07391',
	INTERVAL '10-2' YEAR TO MONTH
	);

INSERT INTO building_lease (
	lease_number,
	address,
	lease_expiring_in
	)
VALUES (
	120,
	'42 Cranburry Rd New York, NY 09652',
	INTERVAL '100' MONTH
	);