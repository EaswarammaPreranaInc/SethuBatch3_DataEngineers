-- 1. Write a Query to display employees information whose name contains only 5 characters



-- 2. Write a query to display employees information whose names does not contains A.



-- 3. Write a query to display employees information who are all working as CLERK

--    and their salary in range from 1000 to 2000.

  

-- 4. Write a query to display employees information who is not getting comm.



-- 5. Write a query to display employees information whose annual salary is 

--    greater than 30000.

      

-- 6. Create College Details as a parent table with the following details 



-- 	College Code, College Name, Principal Name, College_Address

	

-- 7. Create STUDENT details as a child table and link with Parent table college 

--    with the following columns.

   

-- 	SLNO NUMBER    --- Should have Primary Key 

-- 	SNAME VARCHAR2(30),

-- 	DOB DATE,		-- Should have NOT NULL Constraint 

-- 	Fname VARCHAR2(30)

-- 	College_Code VARCHAR2(30),

-- 	FEES NUMBER   -- Should have CHECK Constraint 

   

-- 8. query to get constraint details which are having in the table STUDENT. 



-- 9. Modify the data in the student table from NULL values to 100 in the SLNO column.



-- 10. Difference between TRUNCATE, DELETE, DROP.   



-- 1. Employees with exactly 5 character names

SELECT * FROM employees WHERE LENGTH(name) = 5;



-- 2. Employees whose names don't contain 'A'

SELECT * FROM employees WHERE name NOT LIKE '%A%';



-- 3. Clerks with salary between 1000 and 2000

SELECT * FROM employees WHERE job = 'CLERK' AND salary BETWEEN 1000 AND 2000;



-- 4. Employees not receiving commission

SELECT * FROM employees WHERE comm IS NULL OR comm = 0;



-- 5. Employees with annual salary > 30000

SELECT * FROM employees WHERE salary * 12 > 30000;



-- 6. Create College parent table

CREATE TABLE College_Details (

	College_Code VARCHAR2(30) PRIMARY KEY,

	College_Name VARCHAR2(50),

	Principal_Name VARCHAR2(30),

	College_Address VARCHAR2(100)

);



-- 7. Create STUDENT child table

CREATE TABLE STUDENT (

	SLNO NUMBER PRIMARY KEY,

	SNAME VARCHAR2(30),

	DOB DATE NOT NULL,

	Fname VARCHAR2(30),

	College_Code VARCHAR2(30),

	FEES NUMBER CHECK(FEES > 0),

	FOREIGN KEY(College_Code) REFERENCES College_Details(College_Code)

);



-- 8. Get constraints on STUDENT table

SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE FROM USER_CONSTRAINTS WHERE TABLE_NAME = 'STUDENT';



-- 9. Update NULL values in SLNO to 100

UPDATE STUDENT SET SLNO = 100 WHERE SLNO IS NULL;



-- 10. TRUNCATE vs DELETE vs DROP:

-- TRUNCATE: Removes all rows, resets identity, faster, cannot be rolled back

-- DELETE: Removes specific/all rows, slower, can be rolled back with transaction

-- DROP: Removes entire table structure and data, cannot be rolled back easi
