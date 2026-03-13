-- Create and use the database
CREATE DATABASE IF NOT EXISTS school_lab;
USE school_lab;

-- Create tables
CREATE TABLE IF NOT EXISTS departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50),
    dept_id INT,
    manager_id INT
);

CREATE TABLE IF NOT EXISTS projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    dept_id INT
);

-- Insert sample data
INSERT IGNORE INTO departments VALUES (101, 'IT'), (102, 'HR'), (103, 'Finance'), (104, 'Sales'), (105, 'Admin');
INSERT IGNORE INTO employees (emp_name, dept_id, manager_id) VALUES 
('John', 101, 3), ('Mary', 102, NULL), ('Ravi', 101, 3), ('Anika', 103, 2), ('Vijay', 104, 2), ('Jo', 101, 3);
INSERT IGNORE INTO projects VALUES (1, 'Cloud Sync', 101), (2, 'Hiring App', 102), (3, 'Tax Tool', 103);

-- 1. Display employee names in uppercase
SELECT UPPER(emp_name) FROM employees;

-- 2. Display employee names in lowercase
SELECT LOWER(emp_name) FROM employees;

-- 3. Display the length of each employee name
SELECT emp_name, LENGTH(emp_name) FROM employees;

-- 4. Display the first 3 characters of each employee name
SELECT LEFT(emp_name, 3) FROM employees;

-- 5. Display the last 2 characters of each employee name
SELECT RIGHT(emp_name, 2) FROM employees;

-- 6. Replace the letter 'o' with '0' in employee names
SELECT REPLACE(emp_name, 'o', '0') FROM employees;

-- 7. Display employee names with leading and trailing spaces removed
SELECT TRIM(emp_name) FROM employees;

-- 8. Concatenate employee name and emp_id
SELECT CONCAT(emp_name, '_', emp_id) FROM employees;

-- 9. Display employee names reversed
SELECT REVERSE(emp_name) FROM employees;

-- 10. Display employee names with the first letter capitalized
SELECT CONCAT(UPPER(LEFT(emp_name, 1)), LOWER(SUBSTRING(emp_name, 2))) FROM employees;


-- 11. Display dept_id multiplied by 10
SELECT dept_id, (dept_id * 10) FROM employees;

-- 12. Display dept_id rounded to nearest integer
SELECT ROUND(dept_id, 0) FROM employees;

-- 13. Display the absolute value of dept_id - 105
SELECT ABS(dept_id - 105) FROM employees;

-- 14. Display dept_id squared
SELECT POWER(dept_id, 2) FROM employees;

-- 15. Display square root of dept_id
SELECT SQRT(dept_id) FROM employees;

-- 16. Retrieve employees whose dept_id = 102
SELECT * FROM employees WHERE dept_id = 102;

-- 17. Retrieve employees whose dept_id > 104
SELECT * FROM employees WHERE dept_id > 104;

-- 18. Retrieve employees whose dept_id BETWEEN 101 AND 104
SELECT * FROM employees WHERE dept_id BETWEEN 101 AND 104;

-- 19. Retrieve employees whose name starts with 'J'
SELECT * FROM employees WHERE emp_name LIKE 'J%';

-- 20. Retrieve employees whose name ends with 'a'
SELECT * FROM employees WHERE emp_name LIKE '%a';

-- 21. Retrieve employees whose name contains 'vi'
SELECT * FROM employees WHERE emp_name LIKE '%vi%';

-- 22. Retrieve employees whose dept_id IN (101,102,103)
SELECT * FROM employees WHERE dept_id IN (101, 102, 103);

-- 23. Retrieve employees whose dept_id NOT IN (101,102)
SELECT * FROM employees WHERE dept_id NOT IN (101, 102);

-- 24. Retrieve employees whose dept_id is NULL
SELECT * FROM employees WHERE dept_id IS NULL;

-- 25. Retrieve employees whose name length > 5
SELECT * FROM employees WHERE LENGTH(emp_name) > 5;

-- Retrieve employees who work in the same department as John
SELECT emp_name FROM employees 
WHERE dept_id = (SELECT dept_id FROM employees WHERE emp_name = 'John');

-- Retrieve departments whose dept_id exists in employees table
SELECT dept_name FROM departments 
WHERE dept_id IN (SELECT DISTINCT dept_id FROM employees);

-- Retrieve employees working in departments that have projects
SELECT emp_name FROM employees 
WHERE dept_id IN (SELECT dept_id FROM projects);

-- Retrieve departments with maximum number of employees
SELECT dept_id FROM employees 
GROUP BY dept_id 
ORDER BY COUNT(*) DESC LIMIT 1;

-- Display employee names and their manager names
SELECT e.emp_name AS Employee, m.emp_name AS Manager 
FROM employees e 
INNER JOIN employees m ON e.manager_id = m.emp_id;

-- Display employees who do not have managers
SELECT emp_name FROM employees WHERE manager_id IS NULL;

-- Display employees who report to Mary
SELECT e.emp_name FROM employees e 
JOIN employees m ON e.manager_id = m.emp_id 
WHERE m.emp_name = 'Mary';