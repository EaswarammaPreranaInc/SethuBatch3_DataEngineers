1. Write a Query to display employees information whose name contains only 5 characters

2. Write a query to display employees information whose names does not contains A.

3. Write a query to display employees information who are all working as CLERK
   and their salary in range from 1000 to 2000.
  
4. Write a query to display employees information who is not getting comm.

5. Write a query to display employees information whose annual salary is 
   greater than 30000.
      
6. Create College Details as a parent table with the following details 

	College Code, College Name, Principal Name, College_Address
	
7. Create STUDENT details as a child table and link with Parent table college 
   with the following columns.
   
	SLNO NUMBER    --- Should have Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE,		-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES NUMBER   -- Should have CHECK Constraint 
   
8. query to get constraint details which are having in the table STUDENT. 

9. Modify the data in the student table from NULL values to 100 in the SLNO column.

10. Difference between TRUNCATE, DELETE, DROP.   


select * from empolyees where length(employee_name) = 5;

select * from empolyees where name not like '%A%'

select * from employees where job = clerk and salary between 1000 and 2000;

select * from employees where comm is NUll or comm = 0;

select * from employees where (salary*2) > 30000;


create table college_details(
	college_code number constraint prim_k primary key
	college_name varchar(50),
	prici_name varchar(20),
	col_add varchar(50) 
);

create table STUDENT_details(
	SLNO NUMBER constraint pk primary key
	SNAME VARCHAR2(30),
	DOB DATE constraint nn not null	-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES NUMBER CHECK (FEES > 30000)
	foreign key (College_Code) references college_code (college_details)

);

select * from user_constraints
where table_name = STUDENT;

update student set slno = 100 where slno is null

truncate removes the data not the structure

drop is used to drop the structure of table
delete is used to delete specific employees