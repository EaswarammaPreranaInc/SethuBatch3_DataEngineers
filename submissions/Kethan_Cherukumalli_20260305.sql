CREATE TABLE employees_demo (
    emp_id INT AUTO_INCREMENT PRIMARY KEY, -- Good practice to have a unique ID
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    age INT,
    joining_date DATE
);

INSERT INTO employees_demo (emp_name, department, salary, age, joining_date) VALUES
('Rahul', 'HR', 30000, 25, '2022-01-10'),
('Sneha', 'HR', 35000, 28, '2021-03-15'),
('Amit', 'IT', 60000, 30, '2020-07-20'),
('Priya', 'IT', 75000, 32, '2019-05-18'),
('Kiran', 'Finance', 50000, 29, '2021-11-25'),
('Anjali', 'Finance', 45000, 27, '2022-02-14'),
('Vikram', 'IT', 80000, 35, '2018-09-10'),
('Meena', 'HR', 32000, 26, '2023-01-05');

SELECT * FROM employees_demo;

SELECT emp_name, salary FROM employees_demo;

SELECT emp_name, department, joining_date FROM employees_demo;

SELECT * FROM employees_demo WHERE department = 'HR';

SELECT * FROM employees_demo WHERE department = 'IT';

SELECT * FROM employees_demo WHERE salary > 50000;

SELECT * FROM employees_demo WHERE salary < 40000;

SELECT * FROM employees_demo WHERE age > 30;

SELECT * FROM employees_demo WHERE age <= 28;

SELECT * FROM employees_demo WHERE joining_date < '2021-01-01';

SELECT * FROM employees_demo WHERE joining_date > '2022-01-01';

SELECT * FROM employees_demo WHERE department = 'Finance' AND salary > 45000;

SELECT * FROM employees_demo WHERE salary BETWEEN 30000 AND 60000;

SELECT * FROM employees_demo WHERE age BETWEEN 25 AND 30;

SELECT * FROM employees_demo WHERE department <> 'HR';

SELECT * FROM employees_demo ORDER BY salary ASC;

SELECT * FROM employees_demo ORDER BY salary DESC;

SELECT * FROM employees_demo ORDER BY age ASC;

SELECT * FROM employees_demo ORDER BY joining_date DESC;

SELECT * FROM employees_demo ORDER BY department, salary;

SELECT * FROM employees_demo ORDER BY salary DESC LIMIT 3;

SELECT * FROM employees_demo ORDER BY age ASC LIMIT 2;

SELECT * FROM employees_demo LIMIT 4;

SELECT * FROM employees_demo LIMIT 3 OFFSET 3;

SELECT * FROM employees_demo ORDER BY salary DESC LIMIT 1;

SELECT COUNT(*) FROM employees_demo;

SELECT COUNT(*) FROM employees_demo WHERE department = 'HR';

SELECT MAX(salary) FROM employees_demo;

SELECT MIN(salary) FROM employees_demo;

SELECT AVG(salary) FROM employees_demo;

SELECT SUM(salary) FROM employees_demo;

SELECT AVG(age) FROM employees_demo;

SELECT MAX(age) FROM employees_demo;

SELECT MIN(age) FROM employees_demo;

SELECT COUNT(*) FROM employees_demo WHERE joining_date > '2021-12-31';

SELECT SUM(salary) FROM employees_demo WHERE department = 'IT';

SELECT AVG(salary) FROM employees_demo WHERE department = 'Finance';

SELECT department, COUNT(*) FROM employees_demo GROUP BY department;

SELECT department, AVG(salary) FROM employees_demo GROUP BY department;

SELECT department, MAX(salary) FROM employees_demo GROUP BY department;

SELECT department, MIN(salary) FROM employees_demo GROUP BY department;

SELECT department, SUM(salary) FROM employees_demo GROUP BY department;

SELECT department FROM employees_demo GROUP BY department HAVING COUNT(*) > 2;

SELECT department FROM employees_demo GROUP BY department HAVING AVG(salary) > 40000;

SELECT department FROM employees_demo GROUP BY department HAVING SUM(salary) > 100000;

SELECT department FROM employees_demo GROUP BY department HAVING MAX(salary) > 70000;

SELECT department FROM employees_demo GROUP BY department HAVING MIN(salary) < 35000;

SELECT department, AVG(age) FROM employees_demo GROUP BY department;

SELECT department FROM employees_demo GROUP BY department HAVING AVG(age) > 28;

SELECT department FROM employees_demo GROUP BY department HAVING COUNT(*) < 3;