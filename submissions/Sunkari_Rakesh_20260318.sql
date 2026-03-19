1. Write a Query to display employees information whose name contains only 5 characters

--> select * from employees 
    where name is 5_;

2. Write a query to display employees information whose names does not contains A.

--> select * from employees
    where name not like %A%


3. Write a query to display employees information who are all working as CLERK
   and their salary in range from 1000 to 2000.

--> select clerk from employees 
    where salary is 1000>=2000;  


4. Write a query to display employees information who is not getting comm.

--> select * from employees where comm is null;



5. Write a query to display employees information whose annual salary is 
   greater than 30000.

--> select * from employees where salary > 30000;


      
6. Create College Details as a parent table with the following details 

	College Code, College Name, Principal Name, College_Address

--> create table college_details (college_code number primary key, college_name varchar2(50), Principal_Name varchar2(50), college_address varchar (100))


	
7. Create STUDENT details as a child table and link with Parent table college 
   with the following columns.
   
	SLNO NUMBER    --- Should have Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE,		-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES NUMBER   -- Should have CHECK Constraint 
 
--> create table student_details (slno number primarykey, 
					sname varchar(30), 
					DOB date, 
					fname varchar(30), 
					college_code number(30), 
					fees number check not null, 
					foreign key(college_code), references college_details(colllege_code));


8. query to get constraint details which are having in the table STUDENT. 

--> select * from table user constraints;

9. Modify the data in the student table from NULL values to 100 in the SLNO column.

--> update table student 
    set SLNO=100
    where SLNO is null;


10. Difference between TRUNCATE, DELETE, DROP.  

-->
Truncate : Removes all rows from the table faster

Delete : we can delete the selected rows, we can roll back if it is not committed

Drop :  deletes the entire table with rows and columns (also deletes the structure of table)