CREATE DATABASE Emp;
USE Emp;
CREATE TABLE employees_lab (emp_id INT AUTO_INCREMENT PRIMARY KEY, emp_name VARCHAR(50) NOT NULL, department VARCHAR(50), salary DECIMAL(10,2), age INT, joining_date DATE);
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date) VALUES ('Ravi','IT',50000,25,'2022-01-10');
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date) VALUES
('Ravi','IT',50000,25,'2022-01-10'),
('Anil','HR',42000,28,'2021-05-12'),
('Kiran','Finance',60000,32,'2020-03-15'),
('Sai','Sales',45000,26,'2022-07-18'),
('Rahul','Marketing',48000,27,'2023-01-05'),
('Manoj','IT',55000,29,'2021-09-21'),
('Vikram','HR',40000,30,'2019-11-11'),
('Arjun','Finance',62000,34,'2018-06-25'),
('Suresh','Sales',47000,28,'2022-04-14'),
('Ramesh','Marketing',46000,31,'2020-10-30'),
('Deepak','IT',53000,27,'2021-08-19'),
('Ajay','HR',41000,26,'2023-02-17'),
('Mahesh','Finance',61000,33,'2019-12-09'),
('Naresh','Sales',44000,29,'2022-06-23'),
('Karthik','Marketing',49000,28,'2021-03-28'),
('Tarun','IT',52000,30,'2020-07-07'),
('Pavan','HR',43000,27,'2022-05-16'),
('Harish','Finance',64000,35,'2018-09-12'),
('Rohit','Sales',45500,26,'2023-04-01'),
('Nikhil','Marketing',47500,29,'2021-12-20');
SELECT * FROM employees_lab;
DELETE FROM employees_lab WHERE emp_id = 1;
SELECT * FROM employees_lab;
DELETE FROM employees_lab WHERE emp_id >= 22;
SELECT * FROM employees_lab;
INSERT INTO employees_lab (emp_name, department) VALUES ('Ramu','IT');
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date) VALUES (UPPER('Amit'),'Finance',ROUND(38765.45),27,CURDATE());
SELECT * FROM employees_lab;
SELECT emp_name, salary FROM employees_lab;
SELECT emp_name FROM employees_lab WHERE salary > 60000;
SELECT emp_name FROM employees_lab WHERE age <= 30;
SELECT emp_name FROM employees_lab WHERE department = 'IT';
SELECT * FROM employees_lab WHERE department = 'IT' OR department = 'HR';
SELECT emp_name FROM employees_lab WHERE salary > 60000 AND department LIKE 'IT';
SELECT DISTINCT department FROM employees_lab;
SELECT department, COUNT(*) AS total_employees FROM employees_lab GROUP BY department;
SELECT department, COUNT(*) AS total_employees FROM employees_lab GROUP BY department HAVING COUNT(*) > 2;
SELECT * FROM employees_lab ORDER BY salary DESC;
SELECT * FROM employees_lab LIMIT 5;
SELECT * FROM employees_lab LIMIT 5 OFFSET 5;
UPDATE employees_lab SET salary = 75000 WHERE emp_id = 20;
SET SQL_SAFE_UPDATES = 0;
UPDATE employees_lab SET salary = salary + 1000;
SELECT * FROM employees_lab;
DELETE FROM employees_lab WHERE emp_name = 'Pavan';
REPLACE INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date) VALUES (1,'Ravi','IT',52000,26,'2022-01-10');
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date) VALUES (21,'Aravind','IT',55000,27,'2023-05-10') ON DUPLICATE KEY UPDATE salary=55000;
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date) VALUES (22,'Pradeep','HR',48000,29,'2023-06-15') ON DUPLICATE KEY UPDATE salary=48000;
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date) VALUES (1,'Ravi','IT',75000,25,'2022-01-10') ON DUPLICATE KEY UPDATE salary=75000;
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date) VALUES (23,'Sanjay','Finance',60000,31,'2023-07-20') ON DUPLICATE KEY UPDATE salary=VALUES(salary);
SELECT * FROM employees_lab WHERE salary BETWEEN 50000 AND 70000;
SELECT * FROM employees_lab WHERE emp_name LIKE 'R%';
SELECT * FROM employees_lab WHERE department <> 'Finance';
