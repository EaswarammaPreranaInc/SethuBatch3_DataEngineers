Use Studentdb;
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
('Raj', 'IT', 65000, 28, '2021-03-10'),
('Sneha', 'HR', 45000, 26, '2022-02-15'),
('Amit', 'Finance', 70000, 32, '2020-08-20'),
('Priya', 'Sales', 55000, 27, '2021-11-05'),
('Kiran', 'Marketing', 60000, 29, '2019-07-12'),
('Anjali', 'HR', 48000, 25, '2022-01-19'),
('Vikram', 'IT', 75000, 35, '2018-09-10'),
('Meena', 'Finance', 62000, 30, '2021-04-23'),
('Lokesh', 'Sales', 53000, 31, '2020-12-15'),
('Deepak', 'Marketing', 57000, 28, '2022-06-01'),
('Rohit', 'IT', 80000, 33, '2019-10-10'),
('Ramesh', 'HR', 42000, 24, '2023-01-01'),
('Pooja', 'Finance', 61000, 29, '2021-05-05'),
('Arjun', 'Sales', 54000, 27, '2022-03-03'),
('Nikita', 'Marketing', 59000, 26, '2021-09-18'),
('Kavya', 'IT', 72000, 31, '2020-06-25'),
('Suresh', 'Finance', 66000, 34, '2019-02-17'),
('Harsha', 'Sales', 51000, 28, '2021-08-14'),
('Divya', 'HR', 47000, 25, '2022-12-12'),
('Tarun', 'Marketing', 63000, 30, '2020-05-05');
INSERT INTO employees_lab (emp_name, department)
VALUES ('Manoj', 'IT');
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES (UPPER('rahul'), 'Finance', ROUND(56789.45), 29, CURDATE());
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
SELECT department, COUNT(*) 
FROM employees_lab
GROUP BY department;
SELECT department, COUNT(*)
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
SET SQL_SAFE_UPDATES = 0;
UPDATE employees_lab
SET salary = salary + 1000;
DELETE FROM employees_lab
WHERE emp_name = 'Lokesh';
DELETE FROM employees_lab;
REPLACE INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES (1, 'Ravi', 'IT', 60000, 26, '2022-01-10');
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (2, 'Raj', 'IT', 70000, 28, '2021-03-10')
ON DUPLICATE KEY UPDATE salary = 70000;
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (21, 'Rahul', 'Finance', 65000, 30, '2023-02-10')
ON DUPLICATE KEY UPDATE salary = 65000;
INSERT INTO employees_lab (emp_id, emp_name, department, salary)
VALUES (3, 'Amit', 'Finance', 75000)
ON DUPLICATE KEY UPDATE salary = 75000;
INSERT INTO employees_lab (emp_id, emp_name, department, salary)
VALUES (4, 'Priya', 'Sales', 72000)
ON DUPLICATE KEY UPDATE salary = VALUES(salary);
INSERT INTO employees_lab (emp_id, emp_name, department, salary)
VALUES (4, 'Priya', 'Sales', 72000) AS new
ON DUPLICATE KEY UPDATE salary = new.salary;
SELECT * FROM employees_lab
WHERE salary BETWEEN 50000 AND 70000;
SELECT * FROM employees_lab
WHERE emp_name LIKE 'R%';
SELECT * FROM employees_lab
WHERE department != 'Finance';
