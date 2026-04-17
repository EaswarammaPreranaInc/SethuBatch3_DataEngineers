
1. Write a query to display department details which  contains employees.
SELECT DISTINCT d.*
FROM departments_demo d
JOIN employees_demo e
ON d.dept_id = e.dept_id;
-- 2. Write a query to display employees information whose sal is greater than or equal to sum of sal of each department.
SELECT *
FROM employees_demo e
WHERE salary >= ALL (
    SELECT SUM(salary)
    FROM employees_demo
    GROUP BY dept_id
);
-- 3. write a query to display the department information which contains more than 3 employees.
SELECT dept_id, COUNT(*) AS total_employees
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(*) > 3;
-- 4. write a query to display the max sal who is working as clerks in 20 department.
SELECT MAX(salary) 
FROM employees_demo
WHERE job = 'CLERK' AND dept_id = 20;
-- 5. create a table emp_dtls with the below columns and insert multiple records for each country code.
	
/*	EMPNO,ENAME,JOB,COUNTRY_CODE
	
	101 , RAJ, IT     US
	102, RAM,  MED    US 
	103, RAKI  MECH   AUS
	104, ABC,  MECH   IND
	105, XYZ , IT     IND 
*/	
CREATE TABLE emp_dtls (
EMPNO INT,
ENAME VARCHAR(50),
JOB VARCHAR(50),
COUNTRY_CODE VARCHAR(10)
);
INSERT INTO emp_dtls VALUES
(101,'RAJ','IT','US'),
(102,'RAM','MED','US'),
(103,'RAKI','MECH','AUS'),
(104,'ABC','MECH','IND'),
(105,'XYZ','IT','IND');
-- 6. create a table country_details with the below columns 

/*	COUNTRY_CODE	COUNTRY_NAME	CODE
	US 				United States	01
	AUS 			Australia       61
	MAL             MALAYSIA        65 
*/	
CREATE TABLE country_details (
COUNTRY_CODE VARCHAR(10),
COUNTRY_NAME VARCHAR(50),
CODE INT
);
INSERT INTO country_details VALUES
('US','United States',01),
('AUS','Australia',61),
('MAL','Malaysia',65);
-- 7. Write a query to display employees information who are working as IT in INDIA and MECH from AUS. 
SELECT * 
FROM emp_dtls
WHERE (JOB='IT' AND COUNTRY_CODE='IND')
   OR (JOB='MECH' AND COUNTRY_CODE='AUS');
-- 8. the current existing query as below, in that add a new column to display country name 

/*	existing QUery:
	
	SELECT * from emp_dtls;
   */
   SELECT e.*, c.COUNTRY_NAME
FROM emp_dtls e
LEFT JOIN country_details c
ON e.COUNTRY_CODE = c.COUNTRY_CODE;


-- 1. create a student table and insert the records from 1st Jan to till data as 
--    a joining date.( around 20 records with different dates).
CREATE TABLE students_join (
slno INT PRIMARY KEY,
name VARCHAR(50),
joining_date DATE
);
INSERT INTO students_join VALUES
(1,'Ravi','2026-01-01'),
(2,'Anil','2026-01-05'),
(3,'Kiran','2026-01-10'),
(4,'Sai','2026-01-15'),
(5,'Rahul','2026-01-20'),
(6,'Arjun','2026-01-25'),
(7,'Pavan','2026-02-01'),
(8,'Ramesh','2026-02-05'),
(9,'Suresh','2026-02-10'),
(10,'Naresh','2026-02-15'),
(11,'Vikram','2026-02-20'),
(12,'Ajay','2026-02-25'),
(13,'Mahesh','2026-03-01'),
(14,'Tarun','2026-03-05'),
(15,'Deepak','2026-03-10'),
(16,'Nikhil','2026-03-12'),
(17,'Harish','2026-03-15'),
(18,'Karthik','2026-03-18'),
(19,'Rohit','2026-03-20'),
(20,'Manoj','2026-03-22');


 2. write a query to display students information who joined from last 30 days
SELECT * 
FROM students_join
WHERE joining_date >= CURDATE() - INTERVAL 30 DAY;

-- 3. create a student table with the following columns 
-- 	slno, name, mm , pm, cm 

CREATE TABLE students_marks (
slno INT PRIMARY KEY,
name VARCHAR(50),
mm INT,
pm INT,
cm INT
);

 4. insert the records in student table only into the following columns 
--	slno, name, mm,pm,cm 

INSERT INTO students_marks (slno, name, mm, pm, cm) VALUES
(1,'Ravi',80,70,60),
(2,'Anil',50,45,40),
(3,'Kiran',90,85,88),
(4,'Sai',30,35,25),
(5,'Rahul',60,55,50);
    
    
 5. write a query to display student information along with tm, avgmarks,and result 
--   of the student like Pass / Failed, 
 --  if pass then distinction / First class / Second Class / third class
 SELECT 
slno,
name,
mm, pm, cm,
(mm+pm+cm) AS total_marks,
(mm+pm+cm)/3 AS avg_marks,
CASE
WHEN mm<35 OR pm<35 OR cm<35 THEN 'Fail'
ELSE 'Pass'
END AS result,
CASE
WHEN mm<35 OR pm<35 OR cm<35 THEN 'No Class'
WHEN (mm+pm+cm)/3 >= 75 THEN 'Distinction'
WHEN (mm+pm+cm)/3 >= 60 THEN 'First Class'
WHEN (mm+pm+cm)/3 >= 50 THEN 'Second Class'
ELSE 'Third Class'
END AS class
FROM students_marks;

-- 1. Write a query to display the employees information who has more than 30 years of exp.
SELECT * FROM employees_demo WHERE exp > 30;
-- 2. Write a query to divide the below string as first name, middle name, last name.
-- Raja Ram Mohan
SELECT SUBSTRING_INDEX('Raja Ram Mohan',' ',1) AS first_name,SUBSTRING_INDEX(SUBSTRING_INDEX('Raja Ram Mohan',' ',2),' ',-1) AS middle_name,SUBSTRING_INDEX('Raja Ram Mohan',' ',-1) AS last_name;
-- 3. Write a query to display the employees information with their salary with the below format.
--	ex: Salary is 5000 then output would be XXX5000
--		Salary is 800 then output would be XXXX800
SELECT emp_name, CONCAT(REPEAT('X',4 - LENGTH(salary)), salary) AS formatted_salary FROM employees_demo;		
-- 4. Write a query to display the output as below 
/*
	like employee name is working as job 
	Ex: 
	KING is working as President
	BLAKE is working as CLERK
*/
SELECT CONCAT(emp_name,' is working as ', job) AS result FROM employees_demo;

date : 20/3/26
-- Create the Database
CREATE DATABASE CompanyDB;

-- Use the database (Specific to MySQL/SQL Server)
-- USE CompanyDB; 

-- Creating the EMP table with common columns
CREATE TABLE EMP (
    EMPNO NUMBER PRIMARY KEY,
    ENAME VARCHAR2(50),
    JOB VARCHAR2(50),
    MGR NUMBER,
    HIREDATE DATE,
    SAL NUMBER,
    COMM NUMBER,
    DEPTNO NUMBER
);

Creating a DEPT table for reference
CREATE TABLE DEPT (
    DEPTNO NUMBER PRIMARY KEY,
    DNAME VARCHAR2(50),
    LOC VARCHAR2(50)
);

 1. Remove column from an existing table.
ALTER TABLE EMP DROP COLUMN MGR;

 2. Write a query to display the deptno which does not contains the employees.
 This selects departments from the DEPT table that have no matching records in EMP.
SELECT DEPTNO 
FROM DEPT 
WHERE DEPTNO NOT IN (SELECT DISTINCT DEPTNO FROM EMP WHERE DEPTNO IS NOT NULL);
 3. Write a query to display the given employee details irrespective of case sensitive.
 Using UPPER ensures that 'scott', 'SCOTT', or 'Scott' all match correctly.
SELECT * FROM EMP 
WHERE UPPER(ENAME) = UPPER('scott');
 4. Write a query to display employees information who are all working as MANAGER in department 20.
SELECT * FROM EMP 
WHERE JOB = 'MANAGER' 
AND DEPTNO = 20;
 5. Modify the employee names from lower case to upper case from the emp table.
UPDATE EMP 
SET ENAME = UPPER(ENAME);
 6. Delete the employees whose name starts with J.
 The '%' is a wildcard representing any characters following 'J'.
DELETE FROM EMP 
WHERE ENAME LIKE 'J%';

 1. Write a Query to display employees information whose name contains only 5 characters

		select *
        from emp
        where ename like '_____';

 2. Write a query to display employees information whose names does not contains A.

		select *
		from emp
		where ename not like '%A%';
			
 3. Write a query to display employees information who are all working as CLERK and their salary in range from 1000 to 2000.
		select *
		from emp
		where job='CLERK'
        AND (sal>=1000 AND sal<=2000);
		
  
 4. Write a query to display employees information who is not getting comm.

		select *
		from emp
		where comm = 0;

 5. Write a query to display employees information whose annual salary is greater than 30000.
   
		select *
		from emp
		where sal*12 > 30000;
      
 6. Create College Details as a parent table with the following details College Code, College Name, Principal Name, College_Address
    
			create table college_details ( College_Code number constraint College_Code_PK primary key, 
			  College_Name VARCHAR2(50), 
              Principal_Name VARCHAR2(50),
              College_Address VARCHAR2(50)             
            );
 7. Create STUDENT details as a child table and link with Parent table college with the following columns.
   
	SLNO NUMBER    --- Should have Primary Key 
	SNAME VARCHAR2(30),
	DOB DATE,		-- Should have NOT NULL Constraint 
	Fname VARCHAR2(30)
	College_Code VARCHAR2(30),	FEES NUMBER   -- Should have CHECK Constraint 
    
		create table student_details
        ( SLNO NUMBER constraint SLNO_PK primary key,
          SNAME VARCHAR2(30),
          DOB DATE constraint DOB_NN not null,
          Fname VARCHAR2(30),
          College_Code number constraint College_Code_FK references college_details (College_Code),
          FEES NUMBER constraint FEES_chk check (FEES >=54321)
        );
   
   
 8. query to get constraint details which are having in the table STUDENT. 

		select * from user_constraints where table = upper('student');

 9. Modify the data in the student table from NULL values to 100 in the SLNO column.

		update student
        set SLNO = 100
        where SLNO is NULL;



 10. Difference between TRUNCATE, DELETE, DROP.   

	#- To clear data and keep the structure of the table, use TRUNCATE.
    # To delete specific row of the table, use DELETE.
	#- To erase the entire table (data and structure) from db, use drop.
    