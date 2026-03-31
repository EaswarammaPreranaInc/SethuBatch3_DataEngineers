1. Write a Query to display employees information whose name contains only 5 characters
# SELECT * FROM emp
WHERE emp_name LIKE '_____';

2. Write a query to display employees information whose names does not contains A.
# SELECT * FROM emp
WHERE emp_name NOT LIKE '%A%';

3. Write a query to display employees information who are all working as CLERK and their salary in range from 1000 to 2000.
#SELECT * FROM emp
WHERE job = 'CLERK'
AND sal BETWEEN 1000 AND 2000;

4. Write a query to display employees information who is not getting comm.
#SELECT * FROM emp
WHERE comm IS NULL;

5. Write a query to display employees information whose annual salary is 
   greater than 30000.
#SELECT * FROM emp
WHERE sal*12 > 30000;

6. Create College Details as a parent table with the following details 

	College Code, College Name, Principal Name, College_Address
#CREATE TABLE college (
    college_code VARCHAR2(30) PRIMARY KEY,
    college_name VARCHAR2(50),
    principal_name VARCHAR2(50),
    college_address VARCHAR2(100)
);
	
7. Create STUDENT details as a child table and link with Parent table college 
   with the following columns.
   
	SLNO NUMBER    --- Should have Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE,		-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES NUMBER   -- Should have CHECK Constraint 
#CREATE TABLE student (
    slno NUMBER PRIMARY KEY,
    sname VARCHAR2(30),
    dob DATE NOT NULL,
    fname VARCHAR2(30),
    college_code VARCHAR2(30),
    fees NUMBER CHECK (fees > 0),
    FOREIGN KEY (college_code) REFERENCES college(college_code)
);  

8. query to get constraint details which are having in the table STUDENT. 
#SELECT constraint_name, constraint_type
FROM user_constraints
WHERE table_name = 'STUDENT';

9. Modify the data in the student table from NULL values to 100 in the SLNO column.
#UPDATE student
SET slno = 100
WHERE slno IS NULL;

10. Difference between TRUNCATE, DELETE, DROP. 
#Delete - 
- Used to remove specific rows from a table
- We can use WHERE condition
- Data can be rolled back 
- Table structure remains same
- It is slower compared to TRUNCATE

Truncate -
- Used to remove all rows from a table
- WHERE condition cannot be used
- Data cannot be rolled back
- Table structure remains, but data is erased
- It is faster than DELETE

Drop - 
- Used to delete the entire table
- Both data and structure are removed
- Cannot be rolled back
- Table will no longer exist






 