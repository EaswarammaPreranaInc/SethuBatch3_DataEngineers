-- PART A – TABLE CREATION --

CREATE TABLE employees_lab (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    age INT,
    joining_date DATE
);

-- PART B – INSERT OPERATIONS --

-- Single record
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES ('Chinmayee', 'IT', 50000, 22, '2022-01-10');

-- 20 records
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date) VALUES
('Kanhu', 'HR', 45000, 30, '2020-05-20'),
('Gita', 'Finance', 70000, 35, '2019-11-10'),
('Shiva', 'Sales', 55000, 27, '2022-08-01'),
('Vicky', 'Marketing', 48000, 26, '2023-01-12'),
('Amit', 'IT', 72000, 29, '2021-06-18'),
('Runu', 'HR', 42000, 24, '2023-04-05'),
('Rani', 'Finance', 85000, 40, '2018-02-25'),
('Pintu', 'Sales', 51000, 27, '2022-12-01'),
('Rakesh', 'Marketing', 60000, 31, '2020-10-10'),
('Sima', 'IT', 62000, 28, '2021-09-22'),
('Babu', 'HR', 47000, 33, '2019-07-14'),
('Kalia', 'Finance', 68000, 34, '2020-01-30'),
('Tina', 'Sales', 53000, 28, '2022-03-11'),
('Rohit', 'Marketing', 59000, 32, '2021-11-05'),
('Deepa', 'IT', 75000, 36, '2017-05-15'),
('Suresh', 'HR', 44000, 25, '2023-06-20'),
('Kavita', 'Finance', 90000, 42, '2016-12-01'),
('Rahul', 'Sales', 56000, 30, '2021-08-19'),
('Neha', 'Marketing', 61000, 29, '2020-04-25');

-- Insert selected columns
INSERT INTO employees_lab (emp_name, department)
VALUES ('Vicky', 'IT');

-- Insert using functions
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES (UPPER('Runu'), 'Finance', ROUND(65432.78,0), 24, CURDATE());

-- PART C – SELECT QUERIES --

SELECT * FROM employees_lab;

SELECT emp_name, salary FROM employees_lab;

SELECT * FROM employees_lab WHERE salary > 60000;

SELECT * FROM employees_lab WHERE age <= 30;

SELECT * FROM employees_lab WHERE department = 'IT';

SELECT * FROM employees_lab WHERE department IN ('IT','HR');

SELECT * FROM employees_lab WHERE salary > 60000 AND department = 'IT';

SELECT DISTINCT department FROM employees_lab;

SELECT department, COUNT(*) AS employee_count 
FROM employees_lab 
GROUP BY department;

SELECT department, COUNT(*) 
FROM employees_lab 
GROUP BY department 
HAVING COUNT(*) > 2;

SELECT * FROM employees_lab ORDER BY salary DESC;

SELECT * FROM employees_lab LIMIT 5;

SELECT * FROM employees_lab LIMIT 5 OFFSET 5;

-- PART D – UPDATE OPERATIONS --

UPDATE employees_lab 
SET salary = 75000 
WHERE emp_name = 'Gita';

UPDATE employees_lab 
SET salary = salary + 1000;

-- PART E – DELETE OPERATIONS --

DELETE FROM employees_lab 
WHERE emp_name = 'Runu';

DELETE FROM employees_lab;

-- PART F – MYSQL SPECIAL COMMANDS --

REPLACE INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (1, 'Chinmayee Sahoo', 'IT', 55000, 23, '2022-01-10');

INSERT INTO employees_lab (emp_id, emp_name, department, salary) 
VALUES (2, 'Kanhu', 'IT', 66000)
ON DUPLICATE KEY UPDATE salary = 66000;

INSERT INTO employees_lab (emp_id, emp_name, department, salary) 
VALUES (100, 'New User', 'HR', 40000)
ON DUPLICATE KEY UPDATE salary = 40000;

INSERT INTO employees_lab (emp_id, emp_name, department, salary) 
VALUES (3, 'Gita', 'HR', 48000)
ON DUPLICATE KEY UPDATE salary = 48000;

INSERT INTO employees_lab (emp_id, emp_name, salary) 
VALUES (4, 'Shiva', 80000)
ON DUPLICATE KEY UPDATE salary = VALUES(salary);

-- PART G – ADDITIONAL SEARCH QUERIES --

SELECT * FROM employees_lab 
WHERE salary BETWEEN 50000 AND 70000;

SELECT * FROM employees_lab 
WHERE emp_name LIKE 'C%';

SELECT * FROM employees_lab 
WHERE department != 'Finance';