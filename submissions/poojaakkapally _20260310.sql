create database employees_demo;
use employees_demo;
CREATE TABLE employees_demo (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT
);

INSERT INTO employees_demo VALUES
(1,'Ganga',101),
(2,'Killer',102),
(3,'subbu',103),
(4,'deepak',104),
(5,'dinesh',105),
(6,'pooja',101);

CREATE TABLE departments_demo (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

INSERT INTO departments_demo VALUES
(101,'HR'),
(102,'IT'),
(103,'Finance'),
(104,'Marketing'),
(105,'Sales'),
(106,'Admin');

SELECT e.emp_name, d.dept_name 
FROM employees_demo e INNER JOIN departments_demo d ON e.dept_id = d.dept_id;
SELECT e.emp_name, d.dept_name
FROM employees_demo e LEFT JOIN departments_demo d ON e.dept_id = d.dept_id;
SELECT d.dept_name, e.emp_name
FROM employees_demo e RIGHT JOIN departments_demo d ON e.dept_id = d.dept_id;
SELECT e.emp_name, d.dept_name 
FROM employees_demo e LEFT JOIN departments_demo d ON e.dept_id = d.dept_id UNION SELECT e.emp_name, d.dept_name FROM employees_demo e RIGHT JOIN departments_demo d ON e.dept_id = d.dept_id;
SELECT e.emp_id, e.emp_name, d.dept_name
FROM employees_demo e INNER JOIN departments_demo d ON e.dept_id = d.dept_id ORDER BY e.emp_name;
SELECT e.emp_name 
FROM employees_demo e JOIN departments_demo d ON e.dept_id = d.dept_id WHERE d.dept_name = 'IT';
SELECT emp_name 
FROM employees_demo WHERE dept_id IS NULL;
SELECT d.dept_name 
FROM departments_demo d LEFT JOIN employees_demo e ON d.dept_id = e.dept_id WHERE e.emp_id IS NULL;
SELECT e.emp_name, d.dept_name 
FROM employees_demo e CROSS JOIN departments_demo d;
SELECT COUNT(*) 
FROM employees_demo CROSS JOIN departments_demo;
SELECT dept_id, COUNT(emp_id) 
FROM employees_demo GROUP BY dept_id;
SELECT d.dept_name, COUNT(e.emp_id) 
FROM departments_demo d LEFT JOIN employees_demo e ON d.dept_id = e.dept_id GROUP BY d.dept_name;
SELECT dept_id 
FROM employees_demo GROUP BY dept_id HAVING COUNT(emp_id) > 1;
SELECT dept_id 
FROM employees_demo GROUP BY dept_id HAVING COUNT(emp_id) = 2;
SELECT dept_id 
FROM employees_demo GROUP BY dept_id HAVING COUNT(emp_id) > 1;
SELECT dept_id 
FROM employees_demo GROUP BY dept_id HAVING COUNT(emp_id) < 2;
SELECT e.emp_name, d.dept_name 
FROM employees_demo e JOIN departments_demo d ON e.dept_id = d.dept_id ORDER BY d.dept_name;
SELECT * FROM employees_demo 
ORDER BY dept_id DESC;
SELECT dept_id, COUNT(emp_id) AS emp_count 
FROM employees_demo GROUP BY dept_id ORDER BY emp_count DESC;
SELECT * FROM employees_demo LIMIT 5;
SELECT * FROM employees_demo LIMIT 5 OFFSET 5;
SELECT * FROM employees_demo LIMIT 3 OFFSET 3;
SELECT e.emp_name, d.dept_name 
FROM employees_demo e JOIN departments_demo d ON e.dept_id = d.dept_id LIMIT 3;
SELECT e.emp_name AS Employee, m.emp_name AS Manager 
FROM employees_selfjoin e JOIN employees_selfjoin m ON e.manager_id = m.emp_id;
SELECT e.emp_name 
FROM employees_selfjoin e JOIN employees_selfjoin m ON e.manager_id = m.emp_id WHERE m.emp_name = 'John';
SELECT emp_name 
FROM employees_selfjoin WHERE manager_id IS NULL;
SELECT m.emp_name AS Manager, COUNT(e.emp_id) AS Reportees 
FROM employees_selfjoin e JOIN employees_selfjoin m ON e.manager_id = m.emp_id GROUP BY m.emp_name;

show errors;






