CREATE DIRECTORY data_dir AS 'C:\data';

CREATE TABLE emp_ext
      (employee_number      CHAR(5),
       employee_dob         CHAR(20),
       employee_last_name   CHAR(20),
       employee_first_name  CHAR(15),
       employee_middle_name CHAR(15),
       employee_hire_date   DATE)
    ORGANIZATION EXTERNAL
      (TYPE ORACLE_LOADER
      DEFAULT DIRECTORY data_dir
      ACCESS PARAMETERS
        (RECORDS DELIMITED BY NEWLINE
        -- skip 1 (uncomment this line if you have a column header) 
        FIELDS (employee_number      CHAR(2),
                 employee_dob         CHAR(20),
                 employee_last_name   CHAR(18),
                 employee_first_name  CHAR(11),
                employee_middle_name CHAR(11),
                 employee_hire_date   CHAR(10) date_format DATE mask "mm/dd/yyyy"
                )
        )
      LOCATION ('my_data_new.txt')
     );

select * from emp_ext