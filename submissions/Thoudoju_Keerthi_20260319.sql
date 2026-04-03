-- 1. Write a Query to display employees information whose name contains only 5 characters
select * from employees where name like '_____';

-- 2. Write a query to display employees information whose names does not contains A.
select * from employees where name not like '%A%';

-- 3. Write a query to display employees information who are all working as CLERK
   -- and their salary in range from 1000 to 2000.
   select * from employees where job = 'clerk' and salary between 1000 and 2000;
  
-- 4. Write a query to display employees information who is not getting comm.
 select * from employees where comm is null;


-- 5. Write a query to display employees information whose annual salary is 
   -- greater than 30000.
   select * from employees where salary*12 > 30000;
      
-- 6. Create College Details as a parent table with the following details 

	-- College Code, College Name, Principal Name, College_Address
    
    create table College_Details(
    college_code NUMBER CONSTRAINT clg_code PRIMARY KEY,
    college_name varchar2(50) ,
    principal_name varchar2(30),
    college_address varchar2(100)
    );
	
-- 7. Create STUDENT details as a child table and link with Parent table college 
   -- with the following columns.
   
	SLNO NUMBER    --- Should have Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE,		-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES NUMBER   -- Should have CHECK Constraint
    
    create table student_details(
    sl_no NUMBER CONSTRAINT slno PRIMARY KEY,
    sname varchar(30),
    dob DATE CONSTRAINT dob NOT NULL,
    fname varchar(30),
    college_code varchar(30),
    fees NUMBER CONSTRAINT fees_check check (fees > 10000),
    constraint clg_st FOREIGN KEY (college_code)
    REFERENCES College_Details(College_Code)
    );
   
-- 8. query to get constraint details which are having in the table STUDENT. 
select constraint_name, constraint_type from user_constraints where table_name = 'STUDENT';

-- 9. Modify the data in the student table from NULL values to 100 in the SLNO column.
update student_details
set sl_no = 100 where sl_no is null;

-- 10. Difference between TRUNCATE, DELETE, DROP. 

-- TRUNCATE                 										 DELETE                          								DROP
-- 1. DDL                     										 DML                              								DDL
-- 2. Deletes only data not structure							deletes data based on where condition                       deletes objects  from database
-- 3. Deletes all at once                                       deletes data row by row                                     deletes object permanently
-- 4.Faster                                                     slower  															faster
-- 5. Autocommited , data cannot be rolled back                 Data can be rolled back                                      Autocommit command 
--      
