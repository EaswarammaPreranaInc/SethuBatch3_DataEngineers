-- PART A – TABLE CREATION --

-- Q1. Create a table named employees_lab
CREATE TABLE employees_lab (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    age INT,
    joining_date DATE
);

-- PART B – INSERT OPERATIONS --

-- Q2. Insert a single record into the table
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES ('Ravi', 'IT', 50000, 25, '2022-01-10');

-- Q3. Insert at least 20 employee records using a single INSERT statement
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date) VALUES
('Amit', 'IT', 65000, 28, '2021-03-15'),
('Priya', 'HR', 45000, 32, '2020-05-20'),
('Raj', 'Finance', 70000, 35, '2019-11-10'),
('Suman', 'Sales', 55000, 29, '2022-08-01'),
('Vikram', 'Marketing', 48000, 26, '2023-01-12'),
('Anjali', 'IT', 72000, 30, '2021-06-18'),
('Lokesh', 'HR', 42000, 24, '2023-04-05'),
('Kiran', 'Finance', 85000, 40, '2018-02-25'),
('Megha', 'Sales', 51000, 27, '2022-12-01'),
('Rohan', 'Marketing', 60000, 31, '2020-10-10'),
('Sneha', 'IT', 62000, 29, '2021-09-22'),
('Arjun', 'HR', 47000, 33, '2019-07-14'),
('Nitin', 'Finance', 68000, 34, '2020-01-30'),
('Pooja', 'Sales', 53000, 28, '2022-03-11'),
('Varun', 'Marketing', 59000, 32, '2021-11-05'),
('Deepa', 'IT', 75000, 36, '2017-05-15'),
('Suresh', 'HR', 44000, 25, '2023-06-20'),
('Kavita', 'Finance', 90000, 42, '2016-12-01'),
('Rahul', 'Sales', 56000, 30, '2021-08-19'),
('Neha', 'Marketing', 61000, 29, '2020-04-25');

-- Q4. Insert a record by specifying only selected columns
INSERT INTO employees_lab (emp_name, department)
VALUES ('Vijay', 'IT');

-- Q5. Insert a record using built-in functions (UPPER, ROUND, CURDATE)
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES (UPPER('Vyshnav'), 'Sales', ROUND(662000.78, 0), 26, CURDATE());

-- PART C – SELECT QUERIES --

-- Q6. Display all records from the table
SELECT * FROM employees_lab;

-- Q7. Display only employee names and salaries
SELECT emp_name, salary FROM employees_lab;

-- Q8. Display employees whose salary is greater than 60000
SELECT * FROM employees_lab WHERE salary > 60000;

-- Q9. Display employees whose age is less than or equal to 30
SELECT * FROM employees_lab WHERE age <= 30;

-- Q10. Display employees working in the IT department
SELECT * FROM employees_lab WHERE department = 'IT';

-- Q11. Display employees who belong to IT or HR department
SELECT * FROM employees_lab WHERE department IN ('IT', 'HR');

-- Q12. Display employees whose salary is greater than 60000 AND department is IT
SELECT * FROM employees_lab WHERE salary > 60000 AND department = 'IT';

-- Q13. Display distinct departments available in the table
SELECT DISTINCT department FROM employees_lab;

-- Q14. Display the number of employees in each department using GROUP BY
SELECT department, COUNT(*) as employee_count FROM employees_lab GROUP BY department;

-- Q15. Display departments having more than 2 employees using HAVING
SELECT department, COUNT(*) FROM employees_lab GROUP BY department HAVING COUNT(*) > 2;

-- Q16. Display employees sorted by salary in descending order
SELECT * FROM employees_lab ORDER BY salary DESC;

-- Q17. Display the first 5 employees using LIMIT
SELECT * FROM employees_lab LIMIT 5;

-- Q18. Display the next 5 employees using LIMIT and OFFSET
SELECT * FROM employees_lab LIMIT 5 OFFSET 5;

-- PART D – UPDATE OPERATIONS --

-- Q19. Update the salary of employee 'Raj' to 75000
UPDATE employees_lab SET salary = 75000 WHERE emp_name = 'Raj';

-- Q20. Increase salary of all employees by 1000
UPDATE employees_lab SET salary = salary + 1000;

-- PART E – DELETE OPERATIONS --

-- Q21. Delete the employee whose name is 'Lokesh'
DELETE FROM employees_lab WHERE emp_name = 'Lokesh';

-- Q22. Delete all records from the table
DELETE FROM employees_lab;

-- PART F – MYSQL SPECIAL COMMANDS --
-- (Note: Ensure records exist before running these if you just ran Q22)

-- Q23. Use REPLACE command to update the record with emp_id = 1
REPLACE INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (1, 'Ravi Kumar', 'IT', 55000, 26, '2022-01-10');

-- Q24. Perform UPSERT using INSERT ... ON DUPLICATE KEY UPDATE
INSERT INTO employees_lab (emp_id, emp_name, department, salary) 
VALUES (2, 'Amit', 'IT', 66000)
ON DUPLICATE KEY UPDATE salary = 66000;

-- Q25. Insert a new employee using UPSERT
INSERT INTO employees_lab (emp_id, emp_name, department, salary) 
VALUES (100, 'New User', 'HR', 40000)
ON DUPLICATE KEY UPDATE salary = 40000;

-- Q26. Try inserting a record with an existing emp_id and update the salary
INSERT INTO employees_lab (emp_id, emp_name, department, salary) 
VALUES (3, 'Priya', 'HR', 48000)
ON DUPLICATE KEY UPDATE salary = 48000;

-- Q27. Perform UPSERT using the VALUES() function
INSERT INTO employees_lab (emp_id, emp_name, salary) 
VALUES (4, 'Raj', 80000)
ON DUPLICATE KEY UPDATE salary = VALUES(salary);

-- PART G – ADDITIONAL SEARCH QUERIES --

-- Q28. Display employees whose salary is between 50000 and 70000
SELECT * FROM employees_lab WHERE salary BETWEEN 50000 AND 70000;

-- Q29. Display employees whose name starts with 'R'
SELECT * FROM employees_lab WHERE emp_name LIKE 'R%';

-- Q30. Display employees whose department is not 'Finance'
SELECT * FROM employees_lab WHERE department != 'Finance';