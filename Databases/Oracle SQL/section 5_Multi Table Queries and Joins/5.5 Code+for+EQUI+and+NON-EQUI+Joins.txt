CREATE TABLE job_grade
   (Grade_level varchar(2) not null,
    lowest_sal number not null,
    highest_sal number not null);


INSERT ALL
    INTO job_grade
    VALUES ('A', 0, 1000)
    INTO job_grade
    VALUES ('B', 1001, 2000)
    INTO job_grade
    VALUES ('C', 2001, 3000)
    INTO job_grade
    VALUES ('D', 3001, 4000)
    INTO job_grade
    VALUES ('E', 4001, 5000)
SELECT * FROM DUAL;