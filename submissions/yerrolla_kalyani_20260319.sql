1. Write a Query to display employees information whose name contains only 5 characters

#select * from employees where ename like '_____';

2. Write a query to display employees information whose names does not contains A.

#select * from employees where ename not like '%A%;

3. Write a query to display employees information who are all working as CLERK
   and their salary in range from 1000 to 2000.
   
# select * from employees where job='clerk' and salary between 1000 and 2000;
  
4. Write a query to display employees information who is not getting comm.

select * from employees where comm is 'null';

5. Write a query to display employees information whose annual salary is 
   greater than 30000.
   
   select * from employees where (12* salary)>30000;
      
6. Create College Details as a parent table with the following details 
	College Code, College Name, Principal Name, College_Address
    
	CREATE TABLE college (
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
    
    create  table student ( 
    SLNO NUMBER  Primary Key,
	SNAME VARCHAR2(30),
	DOB DATE not null,
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES NUMBER check(number>=5000),
    foreign key (college_code ) references college (college_code)
    );
    
   
8. query to get constraint details which are having in the table STUDENT. 
SELECT constraint_name, constraint_type
FROM user_constraints
WHERE table_name = 'STUDENT';
9. Modify the data in the student table from NULL values to 100 in the SLNO column.
#update student set slno = 100 where slno=null;
10. Difference between TRUNCATE, DELETE, DROP.
# TRUNCATE:it is a ddl command and it removes the data (records ) in the table  but structure remains.
# DELETE:it  is a dml command and it removes the record or  data (records ) based on condition .
 #DROP: it is a ddl command and it drops means it deletes the records and structure both.
   