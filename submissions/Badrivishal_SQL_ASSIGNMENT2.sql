1. Write a Query to display employees information whose name contains only 5 characters

select * 
fromn employees 
where length(ename)=5;

2. Write a query to display employees information whose names does not contains A.
select  *
from employees
where ename not like '%a%';

3. Write a query to display employees information who are all working as CLERK
   and their salary in range from 1000 to 2000.
select * 
from employees
where designation='CLERK'
and salary in between 1000 & 2000;





5. Write a query to display employees information whose annual salary is 
   greater than 30000.
      
select * 
from employees
where salary *12 > 30000;

6. Create College Details as a parent table with the following details 

	College Code, College Name, Principal Name, College_Address

create table college_details (
	College Code int primary key not null,
	College Name varchar(50),
	Principal Name varchar(50),
	College_Address varchar(100);
	
7. Create STUDENT details as a child table and link with Parent table college 
   with the following columns.
   SLNO NUMBER    --- Should have Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE,		-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES NUMBER   -- Should have CHECK Constraint 
   
CREATE TABLE student (
    slno NUMBER PRIMARY KEY,
    sname VARCHAR2(30),
    dob DATE NOT NULL,
    fname VARCHAR2(30),
    college_code VARCHAR2(30),
    fees NUMBER CHECK (fees > 0),
    CONSTRAINT fk_college
    FOREIGN KEY (college_code)
    REFERENCES college(college_code)
);
8. query to get constraint details which are having in the table STUDENT. 

SELECT constraint_name, constraint_type
FROM user_constraints
WHERE table_name = 'STUDENT';


9. Modify the data in the student table from NULL values to 100 in the SLNO column.
UPDATE student
SET slno = 100
WHERE slno IS NULL;

10. Difference between TRUNCATE, DELETE, DROP.   


truncate 
---------
ddl command
removes all rows
stucture of table remains

drop
-----
ddl command
removes entire table


delete
------
dml command 
removes specific rows
