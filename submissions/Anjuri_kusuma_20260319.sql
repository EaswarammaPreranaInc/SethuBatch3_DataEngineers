create database employee_db;
use employee_db;
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    job VARCHAR(20),
    salary INT,
    comm INT
);
INSERT INTO employees VALUES (7, 'KING', 'PRESIDENT', 5000, NULL);
INSERT INTO employees VALUES (8, 'WARD', 'SALESMAN', 1250, 500);
INSERT INTO employees VALUES (9, 'TURNER', 'SALESMAN', 1500, 0);
INSERT INTO employees VALUES (10, 'JAMES', 'CLERK', 950, NULL);
INSERT INTO employees VALUES (11, 'FORD', 'ANALYST', 3000, NULL);
INSERT INTO employees VALUES (12, 'MILLER', 'CLERK', 1300, NULL);
INSERT INTO employees VALUES (13, 'CLARK', 'MANAGER', 2450, NULL);
INSERT INTO employees VALUES (14, 'SCOTTY', 'CLERK', 1600, NULL);
INSERT INTO employees VALUES (15, 'ADAM', 'SALESMAN', 1400, 200);
INSERT INTO employees VALUES (16, 'BRIAN', 'CLERK', 1700, NULL);
INSERT INTO employees VALUES (17, 'STEVE', 'ANALYST', 2800, NULL);
INSERT INTO employees VALUES (18, 'DAVID', 'MANAGER', 2600, 300);
INSERT INTO employees VALUES (19, 'JOHN', 'CLERK', 1000, NULL);
INSERT INTO employees VALUES (20, 'MIKE', 'SALESMAN', 1900, 400);

#1. Write a Query to display employees information whose name contains only 5 characters
select * from employees where length(emp_name)=5;

#2. Write a query to display employees information whose names does not contains A.
select*from employees where emp_name not like '%A%';

#3. Write a query to display employees information who are all working as CLERK
  # and their salary in range from 1000 to 2000.
  select * from employees where job='CLERK' and salary between 1000 and 2000;
  
 #4. Write a query to display employees information who is not getting comm. 
 select * from employees where comm is null;
 
 #5. Write a query to display employees information whose annual salary is 
  # greater than 30000.
  select * from employees where salary*12>30000;
  
 # 6. Create College Details as a parent table with the following details 
	#College Code, College Name, Principal Name, College_Address
    CREATE TABLE COLLEGE (
    college_code VARCHAR(30) PRIMARY KEY,
    college_name VARCHAR(50),
    principal_name VARCHAR(50),
    college_address VARCHAR(100)
);

#7. Create STUDENT details as a child table and link with Parent table college 
   #with the following columns.
  # SLNO NUMBER    --- Should have Primary Key 
	#SNAME VARCHAR2(30),
	#DOB DATE,		-- Should have NOT NULL Constraint 
	#Fname VARCHAR2(30)
	#College_Code VARCHAR2(30),
	#FEES NUMBER   -- Should have CHECK Constraint 
   CREATE TABLE STUDENT (
    slno int PRIMARY KEY,
    sname VARCHAR(30),
    dob DATE NOT NULL,
    fname VARCHAR(30),
    college_code VARCHAR(30),
    fees int CHECK (FEES > 0),

    FOREIGN KEY (college_code)
    REFERENCES COLLEGE(college_code)
);

#8. query to get constraint details which are having in the table STUDENT. 
#select constraint_name,constraint_type from users_constraints where table_name='STUDENT';

#9. Modify the data in the student table from NULL values to 100 in the SLNO column.  ---->error

#10. Difference between TRUNCATE, DELETE, DROP. 
#Truncate:Removes data but not the structure
#Delete:Removes the specified data
#Drop:Removes whole data and the structure

   


    