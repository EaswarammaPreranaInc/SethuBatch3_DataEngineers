use employees_info;
CREATE TABLE employees_demo (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT
);
CREATE TABLE departments_demo (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

INSERT INTO employees_demo VALUES
(1,'John',101),
(2,'Mary',102),
(3,'David',103),
(4,'Sophia',104),
(5,'Michael',105),
(6,'Emma',101),
(7,'Daniel',102),
(8,'Olivia',108),
(9,'James',109),
(10,'Isabella',110);

INSERT INTO departments_demo VALUES
(101,'HR'),
(102,'IT'),
(103,'Finance'),
(104,'Marketing'),
(105,'Sales'),
(106,'Admin'),
(107,'Operations'),
(108,'Support'),
(111,'Research'),
(112,'Training');
select*from departments_demo ;

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

SELECT e.emp_name, d.dept_name
FROM employees_demo e
LEFT JOIN departments_demo d
ON e.dept_id = d.dept_id

UNION

SELECT e.emp_name, d.dept_name
FROM employees_demo e
RIGHT JOIN departments_demo d
ON e.dept_id = d.dept_id;

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

SELECT dept_id, COUNT(*) AS employee_count
FROM employees_demo
GROUP BY dept_id;
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM departments_demo d
LEFT JOIN employees_demo e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name;


SELECT dept_id, COUNT(*) AS employee_count
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(*) > 1;

SELECT dept_id, COUNT(*) AS employee_count
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(*) = 2;

SELECT dept_id, COUNT(*) AS employee_count
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(*) > 1;

SELECT dept_id, COUNT(*) AS employee_count
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(*) < 2;
SELECT e.emp_name, d.dept_name
FROM employees_demo e
JOIN departments_demo d
ON e.dept_id = d.dept_id
ORDER BY d.dept_name;

SELECT emp_name, dept_id
FROM employees_demo
ORDER BY dept_id DESC;

SELECT dept_id, COUNT(*) AS employee_count
FROM employees_demo
GROUP BY dept_id
ORDER BY employee_count DESC;
SELECT *
FROM employees_demo
LIMIT 5;
SELECT *
FROM employees_demo
LIMIT 5 OFFSET 5;

SELECT *
FROM employees_demo
LIMIT 3 OFFSET 3;
SELECT e.emp_name, d.dept_name
FROM employees_demo e
JOIN departments_demo d
ON e.dept_id = d.dept_id
LIMIT 3;
SELECT e.emp_name AS employee, m.emp_name AS manager
FROM employees_selfjoin e
LEFT JOIN employees_selfjoin m
ON e.manager_id = m.emp_id;
SELECT e.emp_name AS employee, m.emp_name AS manager
FROM employees_selfjoin e
LEFT JOIN employees_selfjoin m
ON e.manager_id = m.emp_id;
SELECT emp_name
FROM employees_selfjoin
WHERE manager_id IS NULL;
SELECT m.emp_name AS manager, COUNT(e.emp_id) AS employee_count
FROM employees_selfjoin e
JOIN employees_selfjoin m
ON e.manager_id = m.emp_id
GROUP BY m.emp_name;