Create database joinsdb;
select database();
Use joinsdb;
CREATE TABLE employees_demo (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT
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
(106,'Admin'),
(107,'Operations'),
(108,'Support'),
(111,'Research'),
(112,'Training');
CREATE TABLE projects_demo (
project_id INT PRIMARY KEY,
project_name VARCHAR(50),
dept_id INT
);
INSERT INTO projects_demo VALUES
(201,'Payroll System',101),
(202,'Website Development',102),
(203,'Budget Analysis',103),
(204,'Ad Campaign',104),
(205,'CRM System',105),
(206,'Helpdesk Tool',108),
(207,'Security Audit',102),
(208,'Market Research',104),
(209,'Data Migration',103),
(210,'Sales Dashboard',105);
CREATE TABLE employees_selfjoin (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    manager_id INT
);
INSERT INTO employees_selfjoin  (emp_id, emp_name, manager_id) VALUES
(1, 'John', NULL),
(2, 'Mary', 1),
(3, 'David', 1),
(4, 'Sophia', 2),
(5, 'James', 2);
Select count(*) from employees_demo;
Select count(*) from departments_demo;
Select count(*) from projects_demo;
Select count(*) from employees_selfjoin ;

select * from employees_demo;
desc employees_demo;
ALTER TABLE employees_demo add column(salary decimal(10,2));
set sql_safe_updates=0;
update employees_demo set salary=25000;
set sql_safe_updates=0;
update employees_demo set salary=50000 where emp_id in (4,5,6);
update employees_demo set salary=100000 where emp_id in (7,8,9,10);
insert into employees_demo(emp_id,dept_id,salary) values(11,110,75000);
insert into employees_demo(emp_id,dept_id,salary) values(12,111,75000);
insert into employees_demo values(13,'****John****',111,75000);
select * from employees_demo;
SELECT IFNULL(emp_name,'Undetermined') AS emp_name, dept_id, salary 
FROM employees_demo;
SELECT REPLACE(emp_name,'a','@') AS modified_name 
FROM employees_demo;
SELECT TRIM(emp_name) AS clean_name 
FROM employees_demo;
SELECT TRIM('*' FROM '*John*') AS cleaned_name;
SELECT emp_name, salary,
CASE
WHEN salary < 40000 THEN 'Low Salary'
WHEN salary BETWEEN 40000 AND 80000 THEN 'Medium Salary'
WHEN salary > 80000 THEN 'High Salary'
ELSE 'Undetermined'
END AS salary_category
FROM employees_demo;
SELECT emp_name, SUBSTRING(emp_name,3) AS name_from_third
FROM employees_demo;
SELECT CONCAT(e.emp_name,' - ',d.dept_name) AS employee_department
FROM employees_demo e
JOIN departments_demo d
ON e.dept_id = d.dept_id;
SELECT emp_name, salary, POWER(salary,2) AS salary_square
FROM employees_demo;
SELECT d.dept_name
FROM departments_demo d
LEFT JOIN employees_demo e
ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;
SELECT * FROM employees_demo
WHERE dept_id > 103;
SELECT * FROM employees_demo
WHERE dept_id <> 101;
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM departments_demo d
LEFT JOIN employees_demo e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name;
SELECT dept_id, COUNT(*) AS total_employees
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(*) > 1;
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM departments_demo d
JOIN employees_demo e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name
LIMIT 2 OFFSET 2;
SELECT e.emp_name, p.project_name
FROM employees_demo e
JOIN projects_demo p
ON e.dept_id = p.dept_id;
SELECT e.emp_name, p.project_name
FROM employees_demo e
JOIN projects_demo p
ON e.dept_id = p.dept_id
JOIN departments_demo d
ON e.dept_id = d.dept_id
WHERE d.dept_name = 'IT';
SELECT p.project_name, COUNT(e.emp_id) AS total_employees
FROM employees_demo e
JOIN projects_demo p
ON e.dept_id = p.dept_id
GROUP BY p.project_name;
SELECT d.dept_name, e.emp_name, p.project_name
FROM departments_demo d
JOIN employees_demo e
ON d.dept_id = e.dept_id
JOIN projects_demo p
ON d.dept_id = p.dept_id;
SELECT DISTINCT d.dept_name
FROM departments_demo d
JOIN employees_demo e
ON d.dept_id = e.dept_id
LEFT JOIN projects_demo p
ON d.dept_id = p.dept_id
WHERE p.dept_id IS NULL;
SELECT e.emp_name,
CASE
WHEN d.dept_name = 'IT' THEN d.dept_name
ELSE NULL
END AS dept_name
FROM employees_demo e
LEFT JOIN departments_demo d
ON e.dept_id = d.dept_id;
SELECT e.emp_name, d.dept_name
FROM employees_demo e
JOIN departments_demo d
ON e.dept_id = d.dept_id
WHERE d.dept_name = 'IT';
