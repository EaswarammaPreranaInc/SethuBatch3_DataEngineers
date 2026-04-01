use employee_db;
#1. Remove column from an existing table.
alter table employees drop column comm;

CREATE TABLE dept (
    deptno INT PRIMARY KEY,
    dname VARCHAR(20),
    loc VARCHAR(20)
);
INSERT INTO dept (deptno, dname, loc) VALUES
(10, 'ACCOUNTING', 'NEW YORK'),
(20, 'RESEARCH', 'DALLAS'),
(30, 'SALES', 'CHICAGO'),
(40, 'OPERATIONS', 'BOSTON'),
(50, 'HR', 'HYDERABAD'),
(60, 'IT', 'BANGALORE'),
(70, 'FINANCE', 'MUMBAI'),
(80, 'MARKETING', 'DELHI'),
(90, 'SUPPORT', 'PUNE');

#2. write a query to display the deptno which does not contains the employees.
SELECT deptno
FROM dept
WHERE deptno NOT IN (SELECT DISTINCT deptno FROM employee);

#3. write a query to display the given employee details irrespective of case sensitive.
select * from employees where lower(emp_name)=lower('scott');

#4. Write a query to display employees information who are all working as MANAGER in department 20
select * from employees,dept where job='MANAGER' and deptno=20;

#5. Modify the employee names from lower case to upper case from the emp table.
update employees set emp_name=upper(emp_name) where emp_id>0;

#6. delete the employees whose name starts with J.
select * from employees where emp_name like 'j%';



