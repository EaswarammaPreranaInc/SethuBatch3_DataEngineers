SELECT *
FROM employees
WHERE first_name LIKE '_____';

SELECT * 
FROM employees
WHERE first_name NOT LIKE '%A%'
    AND first_name NOT LIKE '%a%';
    
SELECT * 
FROM employees
WHERE job_id = 'IT_PROG'
AND salary BETWEEN 4000 AND 6000;

SELECT *
FROM employees
WHERE commission_pct IS NULL;

SELECT *
FROM employees
WHERE salary * 12 > 75000;

CREATE TABLE college_details(
    college_code VARCHAR2(10) PRIMARY KEY,
    college_name VARCHAR2(50),
    principal_name VARCHAR2(50),
    college_address VARCHAR2(100)
);

CREATE TABLE student (
    slno NUMBER PRIMARY KEY,
    sname VARCHAR2(30),
    dob DATE NOT NULL,
    fname VARCHAR2(30),
    college_code VARCHAR2(10),
    fees NUMBER CHECK (fees > 0),
    CONSTRAINT fk_college
    FOREIGN KEY (college_code)
    REFERENCES college_details(college_code)
);

SELECT constraint_name, constraint_type
FROM user_constraints
WHERE table_name = 'STUDENT';

UPDATE student
SET slno = 100
WHERE slno IS NULL;

DELETE FROM student WHERE slno = 1;
TRUNCATE TABLE student;
DROP TABLE student;
