-- 1. Write a Query to display employees information whose name contains only 5 characters
select * from emp where name like '_____';

-- 2. Write a query to display employees information whose names does not contains A.
select * from emp where name not like 'A%';

-- 3. Write a query to display employees information who are all working as CLERK
   -- and their salary in range from 1000 to 2000.
select * from emp where job='CLERK' and salary between 1000 and 2000;

-- 4. Write a query to display employees information who is not getting comm.
select * from emp where comm=0;

-- 5. Write a query to display employees information whose annual salary is greater than 30000.
    select * from emp where salary*12 = 30000;  
    
-- 6. Create College Details as a parent table with the following details 
-- College Code, College Name, Principal Name, College_Address
	create table  College(College_Code Integer , College_Name varchar(50), Principal_Name varchar(50), College_Address varchar(100));
    
7. Create STUDENT details as a child table and link with Parent table college 
   with the following columns.
   
	SLNO NUMBER    --- Should have Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE,		-- Should have NOT// NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES NUMBER   -- Should have CHECK Constraint 
     
	create table Student (SLNO_NUMBER Integer Constraint pk_slno Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE Constraint dob_nn NOT NULL,		-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES_NUMBER Constraint ck_fees Decimal(10,2) check(FEES_NUMBER>0)
    foreign key College_Code references college(College_Code))
    
8. query to get constraint details which are having in the table STUDENT. 
select user_constraints  from table student

9. Modify the data in the student table from NULL values to 100 in the SLNO column.
there cannot be nulls in the slno column because of primary key constraint

10. Difference between TRUNCATE, DELETE, DROP.  
truncate deletes all the rows in the table 
delete deletes the specified rows
drop deletes all the rows and table too 