
use test;
create table employees_demo(
emp_id int primary key,
emp_name varchar(50),
dept_id int
);
create table departments_demo(
dept_id int primary key,
dept_name varchar(50)
);
create table employees_selfjoin(
emp_id int,
emp_name varchar(50),
manager_id int
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

select e.emp_name,d.dept_name from  employees_demo e
inner join departments_demo d where e.dept_id=d.dept_id;
SELECT e.emp_id, e.emp_name, d.dept_name
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
JOIN departments_demo d
ON e.dept_id = d.dept_id
ORDER BY e.emp_name;
SELECT *
FROM employees_demo e
JOIN departments_demo d
ON e.dept_id = d.dept_id
WHERE d.dept_name = 'IT';
SELECT *
FROM employees_demo e
LEFT JOIN departments_demo d
ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;
SELECT *
FROM departments_demo d
LEFT JOIN employees_demo e
ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;
SELECT *
FROM employees_demo e
CROSS JOIN departments_demo d;
SELECT COUNT(*)
FROM employees_demo e
CROSS JOIN departments_demo d;
SELECT dept_id, COUNT(emp_id) AS number_of_employees
FROM employees_demo
GROUP BY dept_id;
SELECT d.dept_name, COUNT(e.emp_id) AS number_of_employees
FROM departments_demo d
JOIN employees_demo e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name;
SELECT d.dept_id
FROM departments_demo d
JOIN employees_demo e
ON d.dept_id = e.dept_id
GROUP BY d.dept_id
HAVING COUNT(e.emp_id) > 1;
SELECT d.dept_id
FROM departments_demo d
JOIN employees_demo e
ON d.dept_id = e.dept_id
GROUP BY d.dept_id
HAVING COUNT(e.emp_id) = 2;
SELECT dept_id
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(emp_id) > 1;
SELECT dept_id
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(emp_id) <2;
SELECT *
FROM employees_demo e
JOIN departments_demo d
ON e.dept_id = d.dept_id
ORDER BY d.dept_name;
SELECT *
FROM employees_demo
ORDER BY dept_id DESC;
SELECT d.dept_id, d.dept_name, COUNT(e.emp_id) AS employee_count
FROM departments_demo d
JOIN employees_demo e
ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
ORDER BY employee_count DESC;
select * from employees_demo limit 5;
select * from employees_demo limit 5 offset 5;
select * from employees_demo limit 3 offset 3;
SELECT d.dept_name, e.emp_name
FROM departments_demo d
JOIN employees_demo e
ON d.dept_id = e.dept_id
ORDER BY d.dept_name
LIMIT 3;




