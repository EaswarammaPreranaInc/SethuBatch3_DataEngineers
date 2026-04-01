1. Write a Query to display employees information whose name contains only 5 characters
Ans:
select * from emp 
where length(ename)=5;

2. Write a query to display employees information whose names does not contains A.
Ans:
select * from emp
where ename not like '%A%';

3. Write a query to display employees information who are all working as CLERK
   and their salary in range from 1000 to 2000.
Ans:
select * from emp
where job='CLERK'
and sal between 1000 and 2000;

4. Write a query to display employees information who is not getting comm.
Ans:
select * from emp
where comm is null;

5. Write a query to display employees information whose annual salary is 
   greater than 30000.
Ans:
select * from emp
where sal>30000;

6. Create College Details as a parent table with the following details 
College Code, College Name, Principal Name, College_Address
Ans:
create table college(
	college_code varchar2(30) primary key,
	college_name varchar2(30),
	principal_name varchar2(50),
	college_address varchar2(100)
);

7. Create STUDENT details as a child table and link with Parent table college 
   with the following columns.
   
	SLNO NUMBER    --- Should have Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE,		-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),
	FEES NUMBER   -- Should have CHECK Constraint 
Ans:
create table student(
	slno number primary key,
	sname varchar2(30),
	dob date not null,
	fname varchar2(30),
	college_code varchar2(30),
	fees number check(fees>0),
	constraint fk_college foreign key(college_code)
	references college(college_code)
);

8. query to get constraint details which are having in the table STUDENT. 
Ans:
select * from user_constraints
where fk_college='college_code';
(or)
select * from user_constraints
where table_name='student';

9. Modify the data in the student table from NULL values to 100 in the SLNO column.
Ans:
update student
set slno=100
where slno is null;

10. Difference between TRUNCATE, DELETE, DROP.   
Ans:
	TRUNCATE 		DELETE			DROP
i.           removes all rows 	        removes selected rows               removes entire table
         but structure remains                   only required data from              along with structure.
           the same(unchanged).                          the table.               
ii.           It is a DDL type.                        It is a DML type.                         It is a DDl type.
iii.        rollback is not possible.               rollback is possible.                   rollback is not possible.