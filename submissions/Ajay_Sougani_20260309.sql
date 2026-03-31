CREATE DATABASE employees_lab;

USE employees_lab;

CREATE TABLE employees_lab (
emp_id INT PRIMARY KEY AUTO_INCREMENT,
emp_name VARCHAR(50) NOT NULL,
department VARCHAR(50),
salary DECIMAL(10,2),
age INT,
joining_date DATE
);

INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES ('Ravi', 'IT', 50000, 25, '2022-01-10');

INSERT INTO employees_lab (emp_name, department, salary, age, joining_date) VALUES
('Raj','IT',65000,28,'2021-03-12'),
('Amit','HR',48000,26,'2022-05-10'),
('Sneha','Finance',72000,30,'2020-09-15'),
('Lokesh','Sales',45000,27,'2021-11-01'),
('Ramesh','Marketing',55000,29,'2023-01-20'),
('Kiran','IT',68000,31,'2019-07-22'),
('Neha','HR',52000,24,'2022-02-18'),
('Vikas','Finance',61000,33,'2018-12-05'),
('Rohit','Sales',47000,25,'2023-04-14'),
('Anita','Marketing',53000,28,'2020-06-30'),
('Rahul','IT',75000,35,'2017-08-12'),
('Pooja','HR',49000,27,'2021-09-21'),
('Manish','Finance',64000,32,'2019-10-10'),
('Suresh','Sales',46000,29,'2022-03-17'),
('Deepa','Marketing',58000,26,'2023-05-25'),
('Arjun','IT',70000,30,'2020-11-11'),
('Nisha','HR',51000,28,'2021-01-19'),
('Tarun','Finance',69000,34,'2018-04-09'),
('Priya','Sales',48000,25,'2022-07-07'),
('Ritu','Marketing',56000,27,'2023-02-16');

INSERT INTO employees_lab (emp_name, department)
VALUES ('Karthik', 'IT');

INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES (UPPER('harsha'), 'IT', ROUND(65432.789,2), 26, CURDATE());

SELECT * FROM employees_lab;

SELECT emp_name, salary FROM employees_lab;

SELECT * FROM employees_lab
WHERE salary > 60000;

SELECT * FROM employees_lab
WHERE age <= 30;

SELECT * FROM employees_lab
WHERE department = 'IT';

SELECT * FROM employees_lab
WHERE department IN ('IT','HR');

SELECT * FROM employees_lab
WHERE salary > 60000 AND department = 'IT';

SELECT DISTINCT department FROM employees_lab;

SELECT department, COUNT(*) AS total_employees
FROM employees_lab
GROUP BY department;

SELECT department, COUNT(*) AS total_employees
FROM employees_lab
GROUP BY department
HAVING COUNT(*) > 2;

SELECT * FROM employees_lab
ORDER BY salary DESC;

SELECT * FROM employees_lab
LIMIT 5;

SELECT * FROM employees_lab
LIMIT 5 OFFSET 5;

UPDATE employees_lab
SET salary = 75000
WHERE emp_name = 'Raj';

UPDATE employees_lab
SET salary = salary + 1000;

DELETE FROM employees_lab
WHERE emp_name = 'Lokesh';

REPLACE INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES (1, 'Ravi', 'IT', 60000, 26, '2022-01-10');

INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (2, 'Amit', 'HR', 50000, 27, '2022-05-10')
ON DUPLICATE KEY UPDATE salary = 50000;

INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (50, 'Sanjay', 'Finance', 62000, 29, '2024-01-01')
ON DUPLICATE KEY UPDATE salary = 62000;

INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (3, 'Sneha', 'Finance', 80000, 30, '2020-09-15')
ON DUPLICATE KEY UPDATE salary = 80000;

INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (4, 'Lokesh', 'Sales', 50000, 27, '2021-11-01')
ON DUPLICATE KEY UPDATE salary = VALUES(salary);

SELECT * FROM employees_lab
WHERE salary BETWEEN 50000 AND 70000;

SELECT * FROM employees_lab
WHERE emp_name LIKE 'R%';

SELECT * FROM employees_lab
WHERE department <> 'Finance';