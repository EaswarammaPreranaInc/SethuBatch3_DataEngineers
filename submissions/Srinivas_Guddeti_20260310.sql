Use Studentdb;
SHOW TABLES;
CREATE TABLE departments_demo (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);
INSERT INTO departments_demo VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance'),
(4, 'Sales'),
(5, 'Marketing');
ALTER TABLE employees_demo
ADD dept_id INT;
SELECT e.emp_name, d.dept_name
FROM employees_demo e
INNER JOIN departments_demo d
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
SELECT e.emp_id, e.emp_name, d.dept_name
FROM employees_demo e
INNER JOIN departments_demo d
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
SELECT dept_id, COUNT(*)
FROM employees_demo
GROUP BY dept_id;
SELECT d.dept_name, COUNT(e.emp_id)
FROM departments_demo d
LEFT JOIN employees_demo e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name;
SELECT dept_id, COUNT(*)
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(*) > 1;
SELECT dept_id, COUNT(*)
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
SELECT * FROM employees_demo
ORDER BY dept_id DESC;
SELECT dept_id, COUNT(*) AS emp_count
FROM employees_demo
GROUP BY dept_id
ORDER BY emp_count DESC;
SELECT * FROM employees_demo
LIMIT 5;
SELECT * FROM employees_demo
LIMIT 5 OFFSET 5;
SELECT * FROM employees_demo
LIMIT 3 OFFSET 3;
SELECT e.emp_name, d.dept_name
FROM employees_demo e
JOIN departments_demo d
ON e.dept_id = d.dept_id
LIMIT 3;
CREATE TABLE employees_selfjoin (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    manager_id INT
);
INSERT INTO employees_selfjoin VALUES
(1, 'John', NULL),
(2, 'Ravi', 1),
(3, 'Sneha', 1),
(4, 'Amit', 2),
(5, 'Priya', 2),
(6, 'Kiran', 3);
SELECT e.emp_name AS Employee,
       m.emp_name AS Manager
FROM employees_selfjoin e
LEFT JOIN employees_selfjoin m
ON e.manager_id = m.emp_id;
SELECT e.emp_name
FROM employees_selfjoin e
JOIN employees_selfjoin m
ON e.manager_id = m.emp_id
WHERE m.emp_name = 'John';
SELECT emp_name
FROM employees_selfjoin
WHERE manager_id IS NULL;
SELECT m.emp_name AS Manager,
       COUNT(e.emp_id) AS Employee_Count
FROM employees_selfjoin e
JOIN employees_selfjoin m
ON e.manager_id = m.emp_id
GROUP BY m.emp_name;