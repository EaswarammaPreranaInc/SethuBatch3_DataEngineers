--1. Write a Query to display employees information whose name contains only 5 characters
select * from emp where ename like '_____';

--2. Write a query to display employees information whose names does not contains A.
select * from emp where not upper(ename) like 'A%';

--3. Write a query to display employees information who are all working as CLERK
   --and their salary in range from 1000 to 2000.
select * from emp where upper(job)='CLERK' and sal in(1000,2000);
  
--4. Write a query to display employees information who is not getting comm.
select * from emp where comm is null;

--5. Write a query to display employees information whose annual salary is 
   --greater than 30000.
select *,sal*12 as annual_sal from emp where  (sal*12) > 30000;
      
--6. Create College Details as a parent table with the following details 
--College Code, College Name, Principal Name, College_Address
create table college_details(
ccode number,
cname varchar(20),
pname varchar(20),
caddress varchar(20),
constraint fk_slno foreign key(ccode) references student_details(slno)) ;
	
--7. Create STUDENT details as a child table and link with Parent table college 
   --with the following columns.
create table student_details(
	SLNO NUMBER primary key,    --- Should have Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE not null,		-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30),
	ccode VARCHAR2(30),
	FEES NUMBER check(fees > 5000) -- Should have CHECK Constraint 
   
--8. query to get constraint details which are having in the table STUDENT

SELECT constraint_name, constraint_type
FROM user_constraints
WHERE table_name = 'STUDENT';

--9. Modify the data in the student table from NULL values to 100 in the SLNO column.
update student_details set slno=100 where slno is null

--10. Difference between TRUNCATE, DELETE, DROP. 
-- truncate - is a DDL command which removes the data , but not table structure
-- delete - is a DML command which deletes the sepecified data from the table and without where cond, it deletes entire data
-- drop - drop is a DDL command which is used to remove the data along with table structure 

