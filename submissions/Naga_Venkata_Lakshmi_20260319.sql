Select * from employees where ename like '_____%';
Select * from employees where ename not like '%A%';
Select * from employees where job = 'CLERK' and  Salary between 1000 and 2000;
Select * from employees where comm is null or comm = 0;
Select * from employees where (Salary*12) > 30000;
create table college(
College_Code INT,
College_Name Varchar(255),
Principal_Name Varchar(255),
College_Address varchar(255),
CONSTRAINT PK_CollegeCode PRIMARY KEY (College_Code)
);
Create table STUDENT(
SLNO NUMBER CONSTRAINT SLNO_PK PRIMARY KEY,
SNAME varchar(30),
DOB DATE CONSTRAINT DOB_NN NOT NULL,
Fname varchar2(30),
College_Code Varchar2(30),
FEES NUMBER CONSTRAINT chk check(FEES >= 5000)
CONSTRAINT fk_CollegeCode FOREIGN KEY(College_Code) REFERENCES College(College_Code)
);
Select * from USER_CONSTRAINTS
where CONSTRAINT_NAME = 'fk_CollegeCode';
UPDATE STUDENT 
SET SLNO = 100
where SLNO IS NULL;
DELETE : It removes the required data from the table.It removes one record.
delete from STUDENT
where SLNO = 1;
TRUNCATE: It deletes all the records from table and table structure remains same.
DROP : It removes the table structure along with data from database.
Drop table STUDENT;














