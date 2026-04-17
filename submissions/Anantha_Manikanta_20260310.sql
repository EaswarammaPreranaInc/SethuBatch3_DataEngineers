CREATE DATABASE join_lab;
USE join_lab;
CREATE TABLE employees_demo (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
dept_id INT
);
CREATE TABLE departments_demo (
dept_id INT PRIMARY KEY,
dept_name VARCHAR(50)
);
CREATE TABLE employees_selfjoin (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
manager_id INT
);
INSERT INTO departments_demo VALUES
(101,'IT'),
(102,'HR'),
(103,'Finance'),
(104,'Sales'),
(105,'Marketing');
INSERT INTO employees_demo VALUES
(1,'Ravi',101),
(2,'Anil',102),
(3,'Kiran',101),
(4,'Suresh',103),
(5,'Rahul',104),
(6,'Pavan',NULL),
(7,'Arjun',102),
(8,'Vikram',101),
(9,'Ramesh',105),
(10,'Deepak',NULL);
INSERT INTO employees_selfjoin VALUES
(1,'John',NULL),
(2,'Ravi',1),
(3,'Anil',1),
(4,'Kiran',2),
(5,'Rahul',2),
(6,'Pavan',3),
(7,'Arjun',3);
SELECT e.emp_name, d.dept_name
FROM employees_demo e
JOIN departments_demo d
ON e.dept_id = d.dept_id;
SELECT e.emp_name, d.dept_name 
FROM employees_demo e 
LEFT JOIN departments_demo d 
ON e.dept_id = d.dept_id;
SELECT e.emp_name, d.dept_name 
FROM employees_demo e 
RIGHT JOIN departments_demo d 
ON e.dept_id = d.dept_id;
SELECT e.emp_name, d.dept_name 
FROM employees_demo e 
LEFT JOIN departments_demo d 
ON e.dept_id = d.dept_id
UNION
SELECT e.emp_name, d.dept_name 
FROM employees_demo e 
RIGHT JOIN departments_demo d 
ON e.dept_id = d.dept_id;
SELECT e.emp_name, d.dept_name 
FROM employees_demo e 
LEFT JOIN departments_demo d 
ON e.dept_id = d.dept_id
UNION
SELECT e.emp_name, d.dept_name 
FROM employees_demo e 
RIGHT JOIN departments_demo d 
ON e.dept_id = d.dept_id;
SELECT e.emp_id, e.emp_name, d.dept_name
FROM employees_demo e
JOIN departments_demo d
ON e.dept_id = d.dept_id
ORDER BY e.emp_name;
SELECT e.emp_name
FROM employees_demo e
JOIN departments_demo d
ON e.dept_id = d.dept_id
WHERE d.dept_name = 'IT';
SELECT e.emp_name
FROM employees_demo e
LEFT JOIN departments_demo d
ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;
SELECT d.dept_name
FROM departments_demo d
LEFT JOIN employees_demo e
ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;
SELECT e.emp_name, d.dept_name
FROM employees_demo e
CROSS JOIN departments_demo d;
SELECT COUNT(*)
FROM employees_demo e
CROSS JOIN departments_demo d;
SELECT dept_id, COUNT(*) AS total_employees
FROM employees_demo
GROUP BY dept_id;
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM departments_demo d
LEFT JOIN employees_demo e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name;
SELECT dept_id, COUNT(*) AS total_employees
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(*) > 1;
SELECT dept_id, COUNT(*) AS total_employees
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(*) = 2;
SELECT dept_id, COUNT(*) 
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(*) > 1;
SELECT dept_id, COUNT(*) 
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(*) < 2;
SELECT e.emp_name, d.dept_name
FROM employees_demo e
JOIN departments_demo d
ON e.dept_id = d.dept_id
ORDER BY d.dept_name;
SELECT * 
FROM employees_demo
ORDER BY dept_id DESC;
SELECT dept_id, COUNT(*) AS total_employees
FROM employees_demo
GROUP BY dept_id
ORDER BY total_employees DESC;
SELECT * FROM employees_demo LIMIT 5;
SELECT * FROM employees_demo LIMIT 5 OFFSET 5;
SELECT * FROM employees_demo LIMIT 3 OFFSET 3;
SELECT e.emp_name AS employee, m.emp_name AS manager
FROM employees_selfjoin e
LEFT JOIN employees_selfjoin m
ON e.manager_id = m.emp_id;
SELECT e.emp_name
FROM employees_selfjoin e
JOIN employees_selfjoin m
ON e.manager_id = m.emp_id
WHERE m.emp_name = 'John';
SELECT m.emp_name AS manager, COUNT(e.emp_id) AS employee_count
FROM employees_selfjoin e
JOIN employees_selfjoin m
ON e.manager_id = m.emp_id
GROUP BY m.emp_name;