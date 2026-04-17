CREATE TABLE employees_demo (
    emp_id INT AUTO_INCREMENT PRIMARY KEY, -- Good practice to have a unique ID
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    age INT,
    joining_date DATE
);

INSERT INTO employees_demo (emp_name, department, salary, age, joining_date) VALUES
('Chinu', 'HR', 30000, 25, '2025-01-10'),
('Sai', 'HR', 35000, 28, '2023-03-15'),
('Amit', 'IT', 60000, 30, '2018-07-20'),
('Pushpa', 'IT', 75000, 32, '2017-05-18'),
('Gita', 'Finance', 50000, 29, '2022-11-25'),
('Annaya', 'Finance', 45000, 27, '2026-02-14'),
('Viky', 'IT', 80000, 35, '2020-09-10'),
('Mita', 'HR', 32000, 26, '2023-01-05');

#Section A: Basic select and where
-- 1. Display all records from the table.
SELECT * FROM employees_demo;

-- 2. Display only emp_name and salary.
SELECT emp_name, salary FROM employees_demo;

-- 3. Display only emp_name, department, and joining_date.
SELECT emp_name, department, joining_date FROM employees_demo;

-- 4. Display employees who belong to HR department.
SELECT * FROM employees_demo WHERE department = 'HR';

-- 5. Display employees who belong to IT department.
SELECT * FROM employees_demo WHERE department = 'IT';

-- 6. Display employees whose salary is greater than 50000.
SELECT * FROM employees_demo WHERE salary > 50000;

-- 7. Display employees whose salary is less than 40000.
SELECT * FROM employees_demo WHERE salary < 40000;

-- 8. Display employees whose age is greater than 30.
SELECT * FROM employees_demo WHERE age > 30;

-- 9. Display employees whose age is less than or equal to 28.
SELECT * FROM employees_demo WHERE age <= 28;

-- 10. Display employees who joined before 2021-01-01.
SELECT * FROM employees_demo WHERE joining_date < '2021-01-01';

-- 11. Display employees who joined after 2022-01-01.
SELECT * FROM employees_demo WHERE joining_date > '2022-01-01';

-- 12. Display employees from Finance department with salary greater than 45000.
SELECT * FROM employees_demo WHERE department = 'Finance' AND salary > 45000;

-- 13. Display employees whose salary is between 30000 and 60000.
SELECT * FROM employees_demo WHERE salary BETWEEN 30000 AND 60000;

-- 14. Display employees whose age is between 25 and 30.
SELECT * FROM employees_demo WHERE age BETWEEN 25 AND 30;

-- 15. Display employees whose department is not HR.
SELECT * FROM employees_demo WHERE department <> 'HR';

#Section B: Order by and limit
-- 16. Display all employees sorted by salary (Ascending).
SELECT * FROM employees_demo ORDER BY salary ASC;

-- 17. Display all employees sorted by salary (Descending).
SELECT * FROM employees_demo ORDER BY salary DESC;

-- 18. Display employees sorted by age (Ascending).
SELECT * FROM employees_demo ORDER BY age ASC;

-- 19. Display employees sorted by joining date (Newest first).
SELECT * FROM employees_demo ORDER BY joining_date DESC;

-- 20. Display employees sorted by department and salary.
SELECT * FROM employees_demo ORDER BY department, salary;

-- 21. Display top 3 highest paid employees.
SELECT * FROM employees_demo ORDER BY salary DESC LIMIT 3;

-- 22. Display top 2 youngest employees.
SELECT * FROM employees_demo ORDER BY age ASC LIMIT 2;

-- 23. Display first 4 records.
SELECT * FROM employees_demo LIMIT 4;

-- 24. Skip first 3 records and display next 3 records.
SELECT * FROM employees_demo LIMIT 3 OFFSET 3;

-- 25. Display the employee with the highest salary.
SELECT * FROM employees_demo ORDER BY salary DESC LIMIT 1;

#Scetion C: Aggregate Functions
-- 26. Find total number of employees.
SELECT COUNT(*) FROM employees_demo;

-- 27. Find total number of employees in HR department.
SELECT COUNT(*) FROM employees_demo WHERE department = 'HR';

-- 28. Find maximum salary.
SELECT MAX(salary) FROM employees_demo;

-- 29. Find minimum salary.
SELECT MIN(salary) FROM employees_demo;

-- 30. Find average salary.
SELECT AVG(salary) FROM employees_demo;

-- 31. Find total salary paid to all employees.
SELECT SUM(salary) FROM employees_demo;

-- 32. Find average age of employees.
SELECT AVG(age) FROM employees_demo;

-- 33. Find highest age among employees.
SELECT MAX(age) FROM employees_demo;

-- 34. Find lowest age among employees.
SELECT MIN(age) FROM employees_demo;

-- 35. Count number of employees who joined after 2021.
SELECT COUNT(*) FROM employees_demo WHERE joining_date > '2021-12-31';

-- 36. Find total salary of IT department.
SELECT SUM(salary) FROM employees_demo WHERE department = 'IT';

-- 37. Find average salary of Finance department.
SELECT AVG(salary) FROM employees_demo WHERE department = 'Finance';

#Scetion D: Group by and having
-- 38. Display department-wise employee count.
SELECT department, COUNT(*) FROM employees_demo GROUP BY department;

-- 39. Display department-wise average salary.
SELECT department, AVG(salary) FROM employees_demo GROUP BY department;

-- 40. Display department-wise maximum salary.
SELECT department, MAX(salary) FROM employees_demo GROUP BY department;

-- 41. Display department-wise minimum salary.
SELECT department, MIN(salary) FROM employees_demo GROUP BY department;

-- 42. Display department-wise total salary.
SELECT department, SUM(salary) FROM employees_demo GROUP BY department;

-- 43. Display departments having more than 2 employees.
SELECT department FROM employees_demo GROUP BY department HAVING COUNT(*) > 2;

-- 44. Display departments having average salary greater than 40000.
SELECT department FROM employees_demo GROUP BY department HAVING AVG(salary) > 40000;

-- 45. Display departments having total salary greater than 100000.
SELECT department FROM employees_demo GROUP BY department HAVING SUM(salary) > 100000;

-- 46. Display departments where maximum salary is greater than 70000.
SELECT department FROM employees_demo GROUP BY department HAVING MAX(salary) > 70000;

-- 47. Display departments where minimum salary is less than 35000.
SELECT department FROM employees_demo GROUP BY department HAVING MIN(salary) < 35000;

-- 48. Display department-wise average age.
SELECT department, AVG(age) FROM employees_demo GROUP BY department;

-- 49. Display departments having average age greater than 28.
SELECT department FROM employees_demo GROUP BY department HAVING AVG(age) > 28;

-- 50. Display departments having employee count less than 3.
SELECT department FROM employees_demo GROUP BY department HAVING COUNT(*) < 3;