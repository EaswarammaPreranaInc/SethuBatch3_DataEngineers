#Part A – Table Creation
#Q1. Create a table named employees_lab with the following columns:
CREATE TABLE employees_lab (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    age INT,
    joining_date DATE
);
#Part B – INSERT Operations
#Q2. Insert a single record into the table.
'''
Example:
emp_name
department
salary
age
joining_date
Ravi
IT
50000
25
2022-01-10
'''
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES ('Ravi', 'IT', 50000, 25, '2022-01-10');

#Q3. Insert at least 20 employee records into the table using a single INSERT statement with multiple rows.
'''
Departments may include:
IT
HR
Finance
Sales
Marketing
'''
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date) VALUES
('Raj','IT',65000,28,'2021-03-12'),
('Amit','HR',48000,30,'2020-05-10'),
('Sneha','Finance',72000,32,'2019-07-19'),
('Kiran','Sales',55000,26,'2022-08-11'),
('Lokesh','Marketing',47000,29,'2021-06-22'),
('Ramesh','IT',80000,35,'2018-02-15'),
('Priya','HR',52000,27,'2023-01-12'),
('Arjun','Finance',69000,31,'2020-09-09'),
('Meena','Sales',60000,24,'2022-04-14'),
('Vikas','Marketing',51000,28,'2021-12-01'),
('Rahul','IT',90000,33,'2017-11-18'),
('Anita','HR',45000,26,'2023-02-21'),
('Suresh','Finance',73000,36,'2016-10-30'),
('Deepa','Sales',58000,29,'2022-07-17'),
('Neha','Marketing',54000,27,'2021-09-23'),
('Ritu','IT',61000,28,'2020-08-05'),
('Ajay','HR',47000,31,'2019-12-12'),
('Sunil','Finance',68000,34,'2018-03-25'),
('Pooja','Sales',56000,25,'2022-05-15'),
('Varun','Marketing',52000,30,'2021-01-10');

#Q4. Insert a record by specifying only selected columns (emp_name, department).
INSERT INTO employees_lab (emp_name, department)
VALUES ('Kavya', 'IT');

#Q5. Insert a record using built-in functions such as:
'''
UPPER()
ROUND()
CURDATE()
'''
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES (UPPER('rohit'), 'Sales', ROUND(45678.567,2), 29, CURDATE());

#Part C – SELECT Queries
#Q6. Display all records from the table.
SELECT * FROM employees_lab;
#Q7. Display only employee names and salaries.
SELECT emp_name, salary FROM employees_lab;
#Q8. Display employees whose salary is greater than 60000.
SELECT * FROM employees_lab
WHERE salary > 60000;
#Q9. Display employees whose age is less than or equal to 30.
SELECT * FROM employees_lab
WHERE age <= 30;
#Q10. Display employees working in the IT department.
SELECT * FROM employees_lab
WHERE department = 'IT';
#Q11. Display employees who belong to IT or HR department.
SELECT * FROM employees_lab
WHERE department IN ('IT','HR');
#Q12. Display employees whose salary is greater than 60000 AND department is IT.
SELECT * FROM employees_lab
WHERE salary > 60000 AND department = 'IT';
#Q13. Display distinct departments available in the table.
SELECT DISTINCT department FROM employees_lab;
#Q14. Display the number of employees in each department using GROUP BY.
SELECT department, COUNT(*) AS total_employees
FROM employees_lab
GROUP BY department;
#Q15. Display departments having more than 2 employees using HAVING.
SELECT department, COUNT(*) AS total
FROM employees_lab
GROUP BY department
HAVING COUNT(*) > 2;
#Q16. Display employees sorted by salary in descending order.
SELECT * FROM employees_lab
ORDER BY salary DESC;
#Q17. Display the first 5 employees using LIMIT.
SELECT * FROM employees_lab
LIMIT 5;
#Q18. Display the next 5 employees using LIMIT and OFFSET.
SELECT * FROM employees_lab
LIMIT 5 OFFSET 5;

#Part D – UPDATE Operations
#Q19. Update the salary of employee 'Raj' to 75000.
UPDATE employees_lab
SET salary = 75000
WHERE emp_name = 'Raj';
#Q20. Increase salary of all employees by 1000.
UPDATE employees_lab
SET salary = salary + 1000;

#Part E – DELETE Operations
#Q21. Delete the employee whose name is 'Lokesh'.
DELETE FROM employees_lab
WHERE emp_name = 'Lokesh';
#Q22. Delete all records from the table.
DELETE FROM employees_lab;

#Part F – MySQL Special Commands
#Q23. Use REPLACE command to update the record with emp_id = 1.
REPLACE INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES (1, 'Ravi', 'IT', 60000, 26, '2022-01-10');
#Q24. Perform UPSERT using
#INSERT ... ON DUPLICATE KEY UPDATE.
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (2,'Amit','HR',50000,30,'2021-05-10')
ON DUPLICATE KEY UPDATE
salary = 52000;
#Q25. Insert a new employee using UPSERT.
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (30,'Manoj','IT',62000,29,'2024-01-15')
ON DUPLICATE KEY UPDATE
salary = VALUES(salary);
#Q26. Try inserting a record with an existing emp_id and update the salary using:
#ON DUPLICATE KEY UPDATE
INSERT INTO employees_lab (emp_id, emp_name, department, salary)
VALUES (3,'Sneha','Finance',75000)
ON DUPLICATE KEY UPDATE
salary = 75000;
#Q27. Perform UPSERT using the VALUES() function.
INSERT INTO employees_lab (emp_id, emp_name, department, salary)
VALUES (4,'Kiran','Sales',65000)
ON DUPLICATE KEY UPDATE
salary = VALUES(salary);

#Part G – Additional Search Queries
#Q28. Display employees whose salary is between 50000 and 70000.
SELECT * FROM employees_lab
WHERE salary BETWEEN 50000 AND 70000;
#Q29. Display employees whose name starts with 'R'.
SELECT * FROM employees_lab
WHERE emp_name LIKE 'R%';
#Q30. Display employees whose department is not 'Finance'.
SELECT * FROM employees_lab
WHERE department <> 'Finance';