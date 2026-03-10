show databases;
create database employees_info;
use employees_info;
create table employees_lab(
emp_id INT PRIMARY KEY AUTO_INCREMENT,
emp_name VARCHAR(50) NOT NULL,
department VARCHAR(50),
salary DECIMAL(10,2),
age INT ,
joining_date DATE);
INSERT INTO employees_lab(emp_name,department ,salary ,age ,joining_date)
values('Ravi','IT', 50000,25,'2022-01-10');
INSERT INTO  employees_lab(emp_name,department ,salary ,age ,joining_date) values
('Ravi','Sales', 40000,25,'2021-06-10'),
('kiran','HR', 50000,23,'2024-01-10'),
('vamsi','Marketing', 54000,25,'2020-01-10'),
('anil','IT', 50000,26,'2022-01-10'),
('Ravi','Finance', 70000,30,'2023-01-10'),
('uma','Finance', 50000,24,'2026-01-10'),
('arun','Finance', 60000,28,'2024-01-10'),
('kiran','Sales', 60000,27,'2023-01-10'),
('priya','IT', 50000,25,'2022-06-10'),
('pavan','Finance', 80000,25,'2022-01-10'),
('anil','Sales', 50000,29,'2022-08-10'),
('jitesh','Marketing', 100000,28,'2022-01-10'),
('chandu','IT', 40000,28,'2022-07-10'),
('krishna','HR', 80000,23,'2022-06-10'),
('Ramu','Marketing', 70000,25,'2022-05-10'),
('laxman','Finance', 65000,27,'2022-04-10'),
('manish','Sales', 75000,29,'2023-01-10'),
('sai','Sales', 50000,30,'2026-01-10'),
('srinu','Finance', 50000,25,'2022-01-10'),
('shiva','Sales', 50000,25,'2022-01-10');
insert into employees_lab (emp_name, department) values('hari','HR');
insert into employees_lab(emp_name,salary,joining_date)values
(upper('sonu'),round(50000.087,0),curdate());
select*from employees_lab;
-- Q7. Display only employee names and salaries. 
select emp_name,salary from employees_lab;
 -- Display employees whose salary is greater than 60000.--
 select * from employees_lab where salary> 60000;
 --  Display employees whose age is less than or equal to 30.-- 
 select * from employees_lab where age<= 30;
-- 10. Display employees working in the IT department.
 select * from employees_lab where department='IT';
--  Q12. Display employees whose salary is greater than 60000 AND department is IT.
SELECT * FROM  employees_lab where salary>60000 and department='IT';
-- Q13. Display distinct departments available in the table.
select  distinct  department  from   employees_lab;
-- Q14. Display the number of employees in each department using GROUP BY.
select department, count(*) from employees_lab group by department ;
select * from employees_lab where department='NULL';
-- Q15. Display departments having more than 2 employees using HAVING.
select department,count(*) from employees_lab  group by (department ) having count(*)>2 ;
-- Q16. Display employees sorted by salary in descending order.
select *from employees_lab order by(salary) desc;
-- Q17. Display the first 5 employees using LIMIT.
select * from employees_lab  limit 5;
-- Q19. Update the salary of employee 'Raj' to 75000.
SET SQL_SAFE_UPDATES=0;
update employees_lab SET salary = 75000 where emp_name='Raj';
SET SQL_SAFE_UPDATES=1;
-- Q20. Increase salary of all employees by 1000.
SET SQL_SAFE_UPDATES=0;
 update employees_lab SET salary = salary +1000 ;
 SET SQL_SAFE_UPDATES=1;
-- Q18. Display the next 5 employees using LIMIT and OFFSET.
SELECT * FROM employees_lab LIMIT 5 OFFSET 5;
-- 11. Display employees who belong to IT or HR department.
select* from employees_lab where department ='HR' or department=' IT';
-- Delete the employee whose name is 'Lokesh'.
SET SQL_SAFE_UPDATES=0;
delete from employees_lab where emp_name ='lokesh';
SET SQL_SAFE_UPDATES=1;
-- Q22. Delete all records from the table.
SET SQL_SAFE_UPDATES=0;
delete  from employees_lab ;
SET SQL_SAFE_UPDATES=1;
-- Q23. Use REPLACE command to update the record with emp_id = 1.
REPLACE INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(1,'Ravi','IT',55000,25,'2022-01-10');
-- Q24. Perform UPSERT using
-- INSERT ... ON DUPLICATE KEY UPDATE.
INSERT INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES (2,'Kiran','HR',60000,23,'2024-01-10') ON DUPLICATE KEY UPDATE
salary = 60000;
-- Q25. Insert a new employee using UPSERT.
INSERT INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date) VALUES (25,'Lokesh','IT',65000,26,'2024-02-10') ON DUPLICATE KEY UPDATE salary = 65000;
-- Q26. Try inserting a record with an existing emp_id and update the salary using:
-- ON DUPLICATE KEY UPDATE
INSERT INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date) VALUES (1,'Ravi','IT',90000,25,'2022-01-10') ON DUPLICATE KEY UPDATE salary = 90000;

-- Q27. Perform UPSERT using the VALUES() function.
INSERT INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(3,'Kiran','HR',70000,23,'2024-01-10')
ON DUPLICATE KEY UPDATE
salary = VALUES(salary);
-- Q28. Display employees whose salary is between 50000 and 70000.
SELECT *
FROM employees_lab
WHERE salary BETWEEN 50000 AND 70000;
-- Q29. Display employees whose name starts with 'R'.
-- Display employees whose name starts with 'R'
SELECT *
FROM employees_lab
WHERE emp_name LIKE 'R%';
-- Q30. Display employees whose department is not 'Finance'.
SELECT *
FROM employees_lab
WHERE department <> 'Finance';