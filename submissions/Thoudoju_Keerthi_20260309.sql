--  Create a table named employees_lab with the following columns:
-- Column Name
-- Data Type
-- Constraint
-- emp_id
-- INT
-- PRIMARY KEY, AUTO_INCREMENT
-- emp_name
-- VARCHAR(50)
-- NOT NULL
-- department
-- VARCHAR(50)
-- salary
-- DECIMAL(10,2)
-- age
-- INT
-- joining_date
-- DATE
set sql_safe_updates=0;
create database assignment3;
use assignment3;
create table employees_lab(emp_id INT PRIMARY KEY AUTO_INCREMENT,emp_name VARCHAR(50) NOT NULL,department VARCHAR(50), salary DECIMAL(10,2),age INT, joining_date DATE);
--  Insert a single record into the table.
-- Example:
-- emp_name
-- department
-- salary
-- age
-- joining_date
-- Ravi
-- IT
-- 50000
-- 25
-- 2022-01-10
-- insert single record
insert into employees_lab (emp_name, department, salary, age,joining_date) values('Ravi', 'IT',50000, 25,'2022-01-01');
-- insert 20 records
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date) VALUES
('Raj','IT',65000,28,'2021-02-10'),
('Lokesh','HR',45000,30,'2020-05-15'),
('Sneha','Finance',70000,32,'2019-08-20'),
('Arjun','Sales',55000,27,'2022-03-12'),
('Meena','Marketing',48000,29,'2021-11-01'),
('Kiran','IT',72000,31,'2018-06-25'),
('Divya','HR',46000,26,'2023-01-10'),
('Rahul','Finance',68000,35,'2017-04-19'),
('Anita','Sales',52000,28,'2020-07-22'),
('Vikram','Marketing',51000,33,'2019-09-17'),
('Rohit','IT',80000,36,'2016-12-05'),
('Suman','HR',43000,24,'2023-02-15'),
('Naveen','Finance',67000,34,'2018-10-30'),
('Pooja','Sales',56000,27,'2021-01-14'),
('Ramesh','Marketing',49000,29,'2020-03-03'),
('Keerthi','IT',62000,26,'2022-06-09'),
('Anil','HR',47000,31,'2019-04-27'),
('Swathi','Finance',69000,33,'2018-08-18'),
('Teja','Sales',53000,25,'2023-03-11'),
('Bhavya','Marketing',50000,28,'2021-12-20');

-- Insert using selected columns
INSERT INTO employees_lab (emp_name, department)
VALUES ('Ajay', 'IT');
-- Insert using functions upper , lower, curdate
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES (UPPER('rajesh'), 'Finance', ROUND(56789.456,2), 30, CURDATE());

-- Display all records
SELECT * FROM employees_lab;
-- Display employee names and salaries
SELECT emp_name, salary FROM employees_lab;
-- Salary > 60000
SELECT * FROM employees_lab WHERE salary > 60000;
-- Age ≤ 30
SELECT * FROM employees_lab WHERE age <= 30;
-- Employees in IT department
SELECT * FROM employees_lab WHERE department = 'IT';
-- Employees in IT or HR
SELECT * FROM employees_lab WHERE department = 'IT' OR department = 'HR';
-- Salary > 60000 AND department IT
SELECT * FROM employees_lab WHERE salary > 60000 AND department = 'IT';
-- Distinct departments
SELECT DISTINCT department FROM employees_lab;
-- Count employees in each department
SELECT department, COUNT(*) AS total_employees FROM employees_lab GROUP BY department;
-- Departments having more than 2 employees
SELECT department, COUNT(*) AS total FROM employees_lab GROUP BY department HAVING COUNT(*) > 2;
-- Sort by salary descending
SELECT * FROM employees_lab ORDER BY salary DESC;
-- First 5 employees
SELECT * FROM employees_lab LIMIT 5;
-- Next 5 employees
SELECT * FROM employees_lab LIMIT 5 OFFSET 5;
-- Update Raj salary
UPDATE employees_lab SET salary = 75000 WHERE emp_name = 'Raj';
-- Increase salary by 1000
UPDATE employees_lab SET salary = salary + 1000;
--  Delete Lokesh
DELETE FROM employees_lab WHERE emp_name = 'Lokesh';
-- Delete all records
DELETE FROM employees_lab;
TRUNCATE TABLE employees_lab;
-- REPLACE command
REPLACE INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date) VALUES (1,'Ravi','IT',60000,26,'2022-01-10');
-- UPSERT using ON DUPLICATE KEY UPDATE
INSERT INTO employees_lab (emp_id, emp_name, department, salary) VALUES (2,'Raj','IT',70000) ON DUPLICATE KEY UPDATE salary = 70000;
-- Insert new employee using UPSERT
INSERT INTO employees_lab (emp_id, emp_name, department, salary) VALUES (25,'Karthik','Sales',58000) ON DUPLICATE KEY UPDATE salary = VALUES(salary);
-- Insert existing emp_id and update salary
INSERT INTO employees_lab (emp_id, emp_name, department, salary) VALUES (3,'Sneha','Finance',72000) ON DUPLICATE KEY UPDATE salary = 72000;
-- UPSERT using VALUES()
INSERT INTO employees_lab (emp_id, emp_name, department, salary) VALUES (4,'Arjun','Sales',60000) ON DUPLICATE KEY UPDATE salary = VALUES(salary);
-- Salary between 50000 and 70000
SELECT * FROM employees_lab WHERE salary BETWEEN 50000 AND 70000;
-- Name starts with 'R'
SELECT * FROM employees_lab WHERE emp_name LIKE 'R%';
-- Department not Finance
SELECT * FROM employees_lab WHERE department <> 'Finance';


