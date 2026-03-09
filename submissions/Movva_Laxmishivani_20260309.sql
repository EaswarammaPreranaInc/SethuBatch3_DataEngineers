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
INSERT INTO employees_lab(emp_name, department, salary, age, joining_date)
VALUES ('Ravi', 'IT', 50000, 25, '2022-01-10');
#Q3. Insert at least 20 employee records into the table using a single INSERT statement with multiple rows.
INSERT INTO employees_lab(emp_name, department, salary, age, joining_date) VALUES
('Raj','IT',65000,28,'2021-02-15'),
('Anita','HR',48000,26,'2020-05-10'),
('Lokesh','Finance',55000,30,'2019-07-21'),
('Sneha','Sales',60000,27,'2022-03-12'),
('Kiran','Marketing',52000,24,'2023-01-10'),
('Arjun','IT',72000,31,'2020-11-05'),
('Priya','HR',51000,29,'2021-06-19'),
('Rahul','Finance',68000,34,'2018-09-25'),
('Meena','Sales',47000,25,'2023-04-14'),
('Suresh','Marketing',59000,33,'2022-08-30'),
('Ramesh','IT',61000,28,'2021-09-17'),
('Divya','HR',53000,27,'2020-10-11'),
('Manoj','Finance',70000,36,'2017-12-01'),
('Pooja','Sales',45000,23,'2024-02-10'),
('Vikram','Marketing',64000,32,'2019-03-28'),
('Neha','IT',75000,35,'2018-04-05'),
('Ajay','HR',52000,30,'2021-01-20'),
('Deepak','Finance',67000,34,'2019-06-13'),
('Ritu','Sales',58000,28,'2022-12-07'),
('Varun','Marketing',62000,29,'2023-03-15');
#Q4. Insert a record by specifying only selected columns (emp_name, department).
INSERT INTO employees_lab(emp_name, department)
VALUES ('Kavya','IT');
#Q5. Insert a record using built-in functions such as:
INSERT INTO employees_lab(emp_name, department, salary, age, joining_date)
VALUES (UPPER('arun'), 'IT', ROUND(45678.567,2), 26, CURDATE());

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
WHERE department = 'IT' OR department = 'HR';
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
SELECT department, COUNT(*) AS total_employees
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
REPLACE INTO employees_lab(emp_id, emp_name, department, salary, age, joining_date)
VALUES (1,'Ravi','IT',60000,26,'2022-01-10');
#Q24. Perform UPSERT using
INSERT ... ON DUPLICATE KEY UPDATE.
INSERT INTO employees_lab(emp_id, emp_name, department, salary)
VALUES (2,'Anil','HR',55000)
ON DUPLICATE KEY UPDATE salary = 55000;
#Q25. Insert a new employee using UPSERT.
INSERT INTO employees_lab(emp_id, emp_name, department, salary)
VALUES (30,'Teja','IT',50000)
ON DUPLICATE KEY UPDATE salary = 50000;
#Q26. Try inserting a record with an existing emp_id and update the salary using:
ON DUPLICATE KEY UPDATE
INSERT INTO employees_lab(emp_id, emp_name, department, salary)
VALUES (3,'Raj','IT',80000)
ON DUPLICATE KEY UPDATE salary = 80000;
#Q27. Perform UPSERT using the VALUES() function.
INSERT INTO employees_lab(emp_id, emp_name, department, salary)
VALUES (4,'Arun','Finance',65000)
ON DUPLICATE KEY UPDATE salary = VALUES(salary);

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