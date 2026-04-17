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

INSERT INTO employees_selfjoin (emp_id, emp_name, manager_id) VALUES
(1, 'John', NULL),
(2, 'Mary', 1),
(3, 'David', 1),
(4, 'Sophia', 2),
(5, 'James', 2);

SELECT e.emp_name, d.dept_name FROM employees_demo e INNER JOIN departments_demo d ON e.dept_id = d.dept_id;
SELECT e.emp_name, d.dept_name FROM employees_demo e LEFT JOIN departments_demo d ON e.dept_id = d.dept_id;
SELECT e.emp_name, d.dept_name FROM employees_demo e RIGHT JOIN departments_demo d ON e.dept_id = d.dept_id;
SELECT e.emp_name, d.dept_name FROM employees_demo e LEFT JOIN departments_demo d ON e.dept_id = d.dept_id 
SELECT e.emp_name, d.dept_name FROM employees_demo e RIGHT JOIN departments_demo d ON e.dept_id = d.dept_id;
SELECT e.emp_id, e.emp_name, d.dept_name FROM employees_demo e JOIN departments_demo d ON e.dept_id = d.dept_id ORDER BY e.emp_name;
SELECT e.emp_name, d.dept_name FROM employees_demo e JOIN departments_demo d ON e.dept_id = d.dept_id WHERE d.dept_name = 'IT';
SELECT e.emp_name, e.dept_id FROM employees_demo e LEFT JOIN departments_demo d ON e.dept_id = d.dept_id WHERE d.dept_id IS NULL;
SELECT d.dept_name FROM employees_demo e RIGHT JOIN departments_demo d ON e.dept_id = d.dept_id WHERE e.emp_id IS NULL;
SELECT e.emp_name, d.dept_name FROM employees_demo e CROSS JOIN departments_demo d;
SELECT COUNT(*) FROM employees_demo CROSS JOIN departments_demo;
SELECT dept_id, COUNT(*) AS total_employees FROM employees_demo GROUP BY dept_id;
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees FROM employees_demo e JOIN departments_demo d ON e.dept_id = d.dept_id GROUP BY d.dept_name;
SELECT dept_id, COUNT(*) FROM employees_demo GROUP BY dept_id HAVING COUNT(*) > 1;
SELECT dept_id, COUNT(*) FROM employees_demo GROUP BY dept_id HAVING COUNT(*) = 2;
SELECT d.dept_name, COUNT(e.emp_id) FROM employees_demo e JOIN departments_demo d ON e.dept_id = d.dept_id GROUP BY d.dept_name HAVING COUNT(e.emp_id) > 1;
SELECT d.dept_name, COUNT(e.emp_id) FROM employees_demo e JOIN departments_demo d ON e.dept_id = d.dept_id GROUP BY d.dept_name HAVING COUNT(e.emp_id) < 2;
SELECT e.emp_name, d.dept_name FROM employees_demo e JOIN departments_demo d ON e.dept_id = d.dept_id ORDER BY d.dept_name;
SELECT * FROM employees_demo ORDER BY dept_id DESC;
SELECT d.dept_name, COUNT(e.emp_id) AS total FROM employees_demo e JOIN departments_demo d ON e.dept_id = d.dept_id GROUP BY d.dept_name ORDER BY total DESC;
SELECT * FROM employees_demo LIMIT 5;
SELECT * FROM employees_demo LIMIT 5 OFFSET 5;
SELECT * FROM employees_demo LIMIT 3 OFFSET 3;
SELECT d.dept_name, e.emp_name FROM employees_demo e JOIN departments_demo d ON e.dept_id = d.dept_id LIMIT 3;
SELECT e.emp_name AS employee, m.emp_name AS manager FROM employees_selfjoin e LEFT JOIN employees_selfjoin m ON e.manager_id = m.emp_id;
SELECT e.emp_name FROM employees_selfjoin e JOIN employees_selfjoin m ON e.manager_id = m.emp_id WHERE m.emp_name = 'John';
SELECT emp_name FROM employees_selfjoin WHERE manager_id IS NULL;
SELECT m.emp_name AS manager, COUNT(e.emp_id) AS reportees FROM employees_selfjoin e JOIN employees_selfjoin m ON e.manager_id = m.emp_id GROUP BY m.emp_name;