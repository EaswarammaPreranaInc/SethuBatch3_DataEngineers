1. Write a Query to display employees information whose name contains only 5 characters
A: 
SELECT *
FROM emp
WHERE ename '_____';

2. Write a query to display employees information whose names does not contains A.
A:
SELECT *
FROM employees
WHERE ename NOT LIKE '%A%';

3. Write a query to display employees information who are all working as CLERK and their salary in range from 1000 to 2000.
A:
SELECT *
FROM employees
WHERE job = 'CLERK'
AND salary BETWEEN 1000 AND 2000;

4. Write a query to display employees information who is not getting comm.
A:
SELECT * 
FROM emp
WHERE COMM is NULL;

5. Write a query to display employees information whose annual salary is  greater than 30000.
A: 
SELECT *
FROM emp
WHERE sal * 12 > 30000;

6. Create College Details as a parent table with the following details 

	College Code, College Name, Principal Name, College_Address
A: 
CREATE TABLE College (
    College_Code VARCHAR2(30) PRIMARY KEY,
    College_Name VARCHAR2(50),
    Principal_Name VARCHAR2(50),
    College_Address VARCHAR2(100)
);

7. Create STUDENT details as a child table and link with Parent table college 
   with the following columns.
   
	SLNO NUMBER    --- Should have Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE,		-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES NUMBER   -- Should have CHECK Constraint 
A:
CREATE TABLE Student (
    SLNO NUMBER PRIMARY KEY,
    SNAME VARCHAR2(30),
    DOB DATE NOT NULL,
    Fname VARCHAR2(30),
    College_Code VARCHAR2(30),
    FEES NUMBER CHECK (FEES > 0),
    
    CONSTRAINT fk_college
    FOREIGN KEY (College_Code)
    REFERENCES College(College_Code)
);

8. query to get constraint details which are having in the table STUDENT. 
A:
SELECT constraint_name, constraint_type, search_condition
FROM user_constraints
WHERE table_name = 'STUDENT';

9. Modify the data in the student table from NULL values to 100 in the SLNO column.
A: SLNO can't be NULL values
'''
UPDATE Student
SET SLNO = 100
WHERE SLNO IS NULL;

10.  Difference between TRUNCATE, DELETE, DROP.   
A:
DELETE removes required data from the table,
TRUNCATE removes only data but structure remains same, 
DROP deletes the entire table structure and data permanently.