-- PART A – TABLE CREATION --

create database emp;
use emp;

-- Q1. Create a table named employees_lab
CREATE TABLE employees_lab (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    age INT,
    joining_date DATE
);
-----------------------------------------------------------
-- PART B – INSERT OPERATIONS --

-- Q2. Insert a single record
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES ('Ravi', 'IT', 50000, 25, '2022-01-10');

-- Q3. Insert 20 records using a single INSERT
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date) VALUES
('Charan', 'IT', 65000, 28, '2021-03-15'),
('Kanta', 'HR', 45000, 32, '2020-05-20'),
('Manvitha', 'Finance', 70000, 35, '2019-11-10'),
('Sai', 'Sales', 55000, 29, '2022-08-01'),
('Adarsh', 'Marketing', 48000, 26, '2023-01-12'),
('Maneesha', 'IT', 72000, 30, '2021-06-18'),
('Lucky', 'HR', 42000, 24, '2023-04-05'),
('Kiranmai', 'Finance', 85000, 40, '2018-02-25'),
('Meghana', 'Sales', 51000, 27, '2022-12-01'),
('Rohan', 'Marketing', 60000, 31, '2020-10-10'),
('Snehalatha', 'IT', 62000, 29, '2021-09-22'),
('Kabeer', 'HR', 47000, 33, '2019-07-14'),
('Nitin', 'Finance', 68000, 34, '2020-01-30'),
('Pooja', 'Sales', 53000, 28, '2022-03-11'),
('Varun Sandesh', 'Marketing', 59000, 32, '2021-11-05'),
('Deepa', 'IT', 75000, 36, '2017-05-15'),
('Suresh', 'HR', 44000, 25, '2023-06-20'),
('Kavita', 'Finance', 90000, 42, '2016-12-01'),
('Rahul Ravindran', 'Sales', 56000, 30, '2021-08-19'),
('Neeraj', 'Marketing', 61000, 29, '2020-04-25');

-- ---------------------------------------------------------

-- Q4. Insert using selected columns
INSERT INTO employees_lab (emp_name, department)
VALUES ('Vijay', 'IT');

-- ---------------------------------------------------------

-- Q5. Insert using built-in functions
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES (UPPER('Siddharth'), 'Finance', ROUND(65432.78,0), 28, CURDATE());

-- ---------------------------------------------------------

-- PART C – SELECT QUERIES --

-- Q6. Display all records
SELECT * FROM employees_lab;

-- Q7. Display employee names and salaries
SELECT emp_name, salary FROM employees_lab;

-- Q8. Employees with salary > 60000
SELECT * FROM employees_lab
WHERE salary > 60000;

-- Q9. Employees age <= 30
SELECT * FROM employees_lab
WHERE age <= 30;

-- Q10. Employees in IT department
SELECT * FROM employees_lab
WHERE department = 'IT';

-- Q11. Employees in IT or HR
SELECT * FROM employees_lab
WHERE department IN ('IT','HR');

-- Q12. Salary > 60000 AND department IT
SELECT * FROM employees_lab
WHERE salary > 60000 AND department = 'IT';

-- Q13. Distinct departments
SELECT DISTINCT department
FROM employees_lab;

-- Q14. Number of employees in each department
SELECT department, COUNT(*) AS employee_count
FROM employees_lab
GROUP BY department;

-- Q15. Departments with more than 2 employees
SELECT department, COUNT(*) AS employee_count
FROM employees_lab
GROUP BY department
HAVING COUNT(*) > 2;

-- Q16. Employees sorted by salary descending
SELECT * FROM employees_lab
ORDER BY salary DESC;

-- Q17. First 5 employees
SELECT * FROM employees_lab
LIMIT 5;

-- Q18. Next 5 employees
SELECT * FROM employees_lab
LIMIT 5 OFFSET 5;

-- ---------------------------------------------------------

-- PART D – UPDATE OPERATIONS --

-- Q19. Update Ravi salary
UPDATE employees_lab
SET salary = 75000
WHERE emp_name = 'Ravi';

-- Q20. Increase salary by 1000 (avoid NULL values)
UPDATE employees_lab
SET salary = salary + 1000
WHERE salary IS NOT NULL;

-- ---------------------------------------------------------

-- PART E – DELETE OPERATIONS --

-- Q21. Delete employee Lokesh
DELETE FROM employees_lab
WHERE emp_name = 'Lucky';

-- ---------------------------------------------------------

-- PART F – MYSQL SPECIAL COMMANDS --

-- Q22. REPLACE command
REPLACE INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (1, 'Ravi Kumar', 'IT', 55000, 26, '2022-01-10');

-- Q23. UPSERT example
INSERT INTO employees_lab (emp_id, emp_name, department, salary)
VALUES (2, 'Amit', 'IT', 66000)
ON DUPLICATE KEY UPDATE salary = 66000;

-- Q24. Insert new employee using UPSERT
INSERT INTO employees_lab (emp_id, emp_name, department, salary)
VALUES (100, 'New User', 'HR', 40000)
ON DUPLICATE KEY UPDATE salary = 40000;

-- Q25. Update salary if emp_id already exists
INSERT INTO employees_lab (emp_id, emp_name, department, salary)
VALUES (3, 'Priya', 'HR', 48000)
ON DUPLICATE KEY UPDATE salary = 48000;

-- Q26. UPSERT using VALUES()
INSERT INTO employees_lab (emp_id, emp_name, salary)
VALUES (4, 'Raj', 80000)
ON DUPLICATE KEY UPDATE salary = VALUES(salary);

-- ---------------------------------------------------------

-- PART G – ADDITIONAL SEARCH QUERIES --

-- Q27. Salary between 50000 and 70000
SELECT * FROM employees_lab
WHERE salary BETWEEN 50000 AND 70000;

-- Q28. Names starting with R
SELECT * FROM employees_lab
WHERE emp_name LIKE 'R%';

-- Q29. Employees not in Finance department
SELECT * FROM employees_lab
WHERE department <> 'Finance';

-- ---------------------------------------------------------

-- Q30. Delete all records (run only if needed)
DELETE FROM employees_lab;