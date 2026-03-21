-- 1. Write a Query to display employees information whose name contains only 5 characters
SELECT * 
FROM emp
WHERE ename LIKE '_____';
-- 2. Write a query to display employees information whose names does not contains A.
SELECT *
FROM emp
WHERE ename NOT LIKE '%A%';
-- 3. Write a query to display employees information who are all working as CLERK
--    and their salary in range from 1000 to 2000.
SELECT *
FROM emp
WHERE job = 'CLERK' AND sal BETWEEN 1000 AND 2000;
  
-- 4. Write a query to display employees information who is not getting comm.
SELECT *
FROM emp
WHERE comm IS NULL;

-- 5. Write a query to display employees information whose annual salary is 
--    greater than 30000.
SELECT *
FROM emp
WHERE (sal*12) > 30000;
      
-- 6. Create College Details as a parent table with the following details 

-- 	College Code, College Name, Principal Name, College_Address
CREATE TABLE college_details(
college_code NUMBER ,
college_name VARCHAR2(20),
principal_name VARCHAR2(30),
college_address VARCHAR2(50),
CONSTRAINT college_pk PRIMARY KEY(college_code);

	
-- 7. Create STUDENT details as a child table and link with Parent table college 
--    with the following columns.
CREATE TABLE student(
	SLNO NUMBER CONSTRAINT student_pk PRIMARY KEY ,
	SNAME VARCHAR2(30),
	DOB DATE CONSTRAINT dob_nn NOT NULL,
	Fname VARCHAR2(30),
	college_code NUMBER,
	FEES NUMBER CONSTRAINT student_ck CHECK(FEES>=5000),
    CONSTRAINT student_fk FOREIGN KEY(college_code) 
    REFERENCES college_details(college_code)
);
   
-- 8. query to get constraint details which are having in the table STUDENT.
SELECT *
FROM user_constraints
WHERE table_name = 'STUDENT'; 

-- 9. Modify the data in the student table from NULL values to 100 in the SLNO column.
ALTER TABLE student disable constraint student_pk;
INSERT INTO student VALUES(NULL,'abc','12-Jan-2008','xyz',1234,6000);
UPDATE student
SET SLNO = 100
WHERE SLNO IS NULL;
ALTER TABLE student enable constraint student_pk;

-- 10. Difference between TRUNCATE, DELETE, DROP.   
TRUNCATE : It is a DDL(Data Defination Language) command . This command deletes all the records 
from the table but still the table structure exists. It cannot be rolled back.
DELETE :  It is a DML(Data Manipulation Language) command . This command deletes the specific record 
from the table based on the condition and this command can be rolled back .
DROP : It is a DDL(Data Defination Language) command . This command deletes the entire table 
from the database both the records and the table is deleted. It cannot be rolled back.