1. Write a Query to display employees information whose name contains only 5 characters
select * from emp where ename like '____'

2. Write a query to display employees information whose names does not contains A.
select * from emp where ename not like '%A%'
3. Write a query to display employees information who are all working as CLERK
   and their salary in range from 1000 to 2000.
select * from emp where job  ='CLERK' and salary between 1000 and 2000
  
4. Write a query to display employees information who is not getting comm.

5. Write a query to display employees information whose annual salary is 
   greater than 30000.
select * from emp wehre sal>30000
      
6. Create College Details as a parent table with the following details 

	College Code, College Name, Principal Name, College_Address
CREATE TABLE college (
    college_code NUMBER ,
    college_name VARCHAR2(100),
    principal_name VARCHAR2(100),
    college_address VARCHAR2(200)
);
	
7. Create STUDENT details as a child table and link with Parent table college 
   with the following columns.
   CREATE TABLE student
	SLNO NUMBER primary key,   --- Should have Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE not null,		-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES NUMBER  check>1000  -- Should have CHECK Constraint 
   
8. query to get constraint details which are having in the table STUDENT. 
select * from student WHERE table_name = 'STUDENT';

9. Modify the data in the student table from NULL values to 100 in the SLNO column.
UPDATE student
SET slno = 100
WHERE slno IS NULL;

10. Difference between TRUNCATE, DELETE, DROP.   
DELETE is a DML (Data Manipulation Language) command used to remove specific rows from a table. It can be used with a WHERE clause to delete selected records. The operation can be rolled back before committing, and triggers will be fired. However, it is slower because it deletes rows one by one.

TRUNCATE is a DDL (Data Definition Language) command used to remove all rows from a table. It does not support a WHERE clause and cannot be rolled back. It is faster than DELETE because it removes data by deallocating storage rather than deleting row by row. Table structure remains intact, but triggers are not fired.

DROP is also a DDL command used to completely remove the table from the database. It deletes both the data and the table structure permanently. Once dropped, the table no longer exists and cannot be recovered. It is the fastest operation among the three.