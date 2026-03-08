create database employeedb;
use employeedb;
create table employeedb_demo(
emp_id INT  PRIMARY KEY AUTO_INCREMENT,
emp_name VARCHAR(50),
department VARCHAR(50),
salary DECIMAL(10,2),
age INT,
joining_date  DATE );
use employeedb;
create table employees_demo(
emp_id INT  PRIMARY KEY AUTO_INCREMENT,
emp_name VARCHAR(50),
department VARCHAR(50),
salary DECIMAL(10,2),
age INT,
joining_date  DATE );
INSERT INTO employees_demo (emp_name, department, salary, age, joining_date) VALUES
('Rahul', 'HR', 30000, 25, '2022-01-10'),
('Sneha', 'HR', 35000, 28, '2021-03-15'),
('Amit', 'IT', 60000, 30, '2020-07-20'),
('Priya', 'IT', 75000, 32, '2019-05-18'),
('Kiran', 'Finance', 50000, 29, '2021-11-25'),
('Anjali', 'Finance', 45000, 27, '2022-02-14'),
('Vikram', 'IT', 80000, 35, '2018-09-10'),
('Meena', 'HR', 32000, 26, '2023-01-05');
select *from employees_demo;
select emp_name ,salary from employees_demo;
SELECT emp_name, department, joining_date FROM employees_demo;
 SELECT * FROM employees_demo WHERE department = 'HR';
-- Display employees who belong to IT department.
SELECT * FROM employees_demo WHERE department = 'IT';
-- Display employees whose salary is greater than 50000.
SELECT * FROM employees_demo WHERE salary > 50000;
-- Display employees whose salary is less than 40000.
SELECT * FROM employees_demo WHERE salary < 40000;
-- Display employees whose age is greater than 30.
SELECT * FROM employees_demo WHERE age > 30;
-- Display employees whose age is less than or equal to 28.
SELECT * FROM employees_demo WHERE age <= 28;
-- Display employees who joined before 2021-01-01.
SELECT * FROM employees_demo WHERE joining_date < '2021-01-01';
-- Display employees who joined after 2022-01-01.
SELECT * FROM employees_demo WHERE joining_date > '2022-01-01';
-- Display employees whose salary is between 30000 and 60000.
SELECT * FROM employees_demo WHERE salary BETWEEN 30000 AND 60000;
-- Display employees whose age is between 25 and 30.
SELECT * FROM employees_demo WHERE age BETWEEN 25 AND 30;
-- Display employees whose department is not HR.
SELECT * FROM employees_demo WHERE department <> 'HR';
--  Display all employees sorted by salary (Ascending).
SELECT * FROM employees_demo ORDER BY salary ASC;
-- Display all employees sorted by salary (Descending).
SELECT * FROM employees_demo ORDER BY salary DESC;
-- Display employees sorted by age (Ascending).
SELECT * FROM employees_demo ORDER BY age ASC;
-- Display employees sorted by joining date (Newest first).
SELECT * FROM employees_demo ORDER BY joining_date DESC;
-- Display employees sorted by department and salary.
SELECT * FROM employees_demo ORDER BY department ASC, salary ASC;
-- Display top 3 highest paid employees.
SELECT * FROM employees_demo ORDER BY salary DESC LIMIT 3;
-- Display top 2 youngest employees.
SELECT * FROM employees_demo ORDER BY age ASC LIMIT 2;
-- Display first 4 records.
SELECT * FROM employees_demo LIMIT 4;
-- Skip first 3 records and display next 3 records.
SELECT * FROM employees_demo LIMIT 3 OFFSET 3;
-- Display the employee with the highest salary.
SELECT * FROM employees_demo ORDER BY salary DESC LIMIT 1;
-- Find total number of employees.
SELECT COUNT(*) AS total_employees FROM employees_demo;
-- Find total number of employees in HR department.

