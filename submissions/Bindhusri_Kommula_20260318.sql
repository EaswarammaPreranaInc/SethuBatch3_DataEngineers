1. Write a Query to display employees information whose name contains only 5 characters

select * emp where ename like '_____';

2. Write a query to display employees information whose names does not contains A.

select * emp where ename not like '%A%';

3. Write a query to display employees information who are all working as CLERK and their salary in range from 1000 to 2000.

select * emp where job='CLERK'
AND SAL BETWEEN 1000 AND 2000;


4. Write a query to display employees information who is not getting comm.

select * emp
where comm is null;

5. Write a query to display employees information whose annual salary is greater than 30000.

select * emp 
where sal*12>30000;

6. Create College Details as a parent table with the following details College Code, College Name, Principal Name, College_Address

create table college_details(
college_code varchar2(30),
college_name varchar2(30),
principal_namevarchar2(30),
college_address varchar2(30)
);

7. Create STUDENT details as a child table and link with Parent table college 
   with the following columns.
   
	SLNO NUMBER    --- Should have Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE,		-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES NUMBER   -- Should have CHECK Constraint  

    create table student(
    sino number constraint sino_pk primary key,
    sname varchar(20),
    DOB DATE,
    Fname varchar2(30),
    College_Code varchar2(30),
    Fees Number constraint fees_check check (fees>=5000)
    );

 8. query to get constraint details which are having in the table STUDENT. 

    select * from user_constraints
    where table_name='STUDENT';
    
9. Modify the data in the student table from NULL values to 100 in the SLNO column.
slno dont have null values as it is primary key

10. Difference between TRUNCATE, DELETE, DROP. 
  
Truncate: it remove only data but structure remains same
DELETE: It removes the data from the table
DROP: It removes the table structure along with data from database
    
    


