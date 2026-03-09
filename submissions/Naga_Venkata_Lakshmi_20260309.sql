show databases;
create table employees_lab (
emp_id INT PRIMARY KEY AUTO_INCREMENT,
emp_name VARCHAR(50) NOT NULL,
department VARCHAR(50),
salary DECIMAL(10,2),
age INT,
joining_date DATE

);
INSERT INTO employees_lab(emp_name, department, salary, age, joining_date)
VALUES ('Ravi' , 'IT' , 50000 , 25 , '2022-01-10');
INSERT INTO employees_lab(emp_name, department, salary, age,joining_date)
VALUES ('Amit' , 'IT' , 55000 , 26 , '2021-05-01'),
('Sita' , 'HR' , 52000 , 27 , '2020-03-15'),
('Rahul' , 'Finance' , 60000 , 30 , '2019-07-20'),
('Priya' , 'Sales' , 48000 , 24 , '2022-02-10'),
('Vikram' , 'Marketing' , 53000 , 29 , '2021-09-05'),
('Neha' , 'IT' , 58000 , 28 , '2020-11-12'),
('Raj' , 'HR' , 51000 , 25 , '2022-01-05'),
('Kiran' , 'Finance' , 62000 , 31 , '2018-04-18'),
('Anita' , 'Sales' , 49000 , 23 , '2023-03-01'),
('Manish' , 'Marketing' ,  54000 , 27 , '2021-06-22'),
('Lakshmi' , 'IT' , 57000 , 29 , '2020-08-15'),
('Sachin' , 'HR' , 50000 , 24 , '2022-04-10'),
('Deepa' , 'Finance' , 61000 , 30 , '2019-02-14'),
('Arun' , 'Sales' , 47000 , 22 , '2023-05-05'),
('Pooja' , 'Marketing' , 52000 , 26 , '2021-07-19'),
('Ramesh' , 'IT' , 59000 , 28 , '2020-10-08'),
('Sunita' , 'HR' , 53000 , 27 , '2021-04-12'),
('Vivek' , 'Finance' , 63000 , 32 , '2018-06-21'),
('Geeta' , 'Sales' , 50000 , 25 , '2022-03-15'),
('Nithin' , 'Marketing' , 55000 , 29 , '2021-08-25');
INSERT INTO employees_lab (emp_name, department)
VALUES ('Kumar' , 'IT');
INSERT INTO employees_lab (emp_name, department, salary , age , joining_date)
VALUES  (UPPER('test'), 'IT' , ROUND(50000.5678, 2), 25, CURDATE());
SELECT * FROM employees_lab;
SELECT emp_name, salary FROM employees_lab;
SELECT * FROM employees_lab WHERE salary > 60000;
SELECT * FROM employees_lab WHERE age <= 30;
SELECT * FROM employees_lab WHERE department = 'IT';
SELECT * FROM employees_lab WHERE department IN ('IT' , 'HR');
SELECT DISTINCT department FROM employees_lab;
SELECT department, COUNT(*) AS num_employees FROM employees_lab GROUP BY department;
SELECT * FROM employees_lab ORDER BY salary DESC;
SELECT * FROM employees_lab LIMIT 5;
SELECT * FROM employees_lab LIMIT 5 OFFSET 5;
UPDATE employees_lab SET salary = 75000 WHERE emp_name = 'Raj';
UPDATE employees_lab SET salary = salary + 1000;
DELETE FROM employees_lab WHERE emp_name = 'Lokesh'
DELETE FROM employees_lab;
REPLACE INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (1, 'NewName' , 'IT' , 60000 , 30 , '2022-01-01');
INSERT INTO employees_lab (emp_id, emp_name, department, salary)
VALUES (1, 'ExistingName' , 'IT' ,  70000)
ON DUPLICATE KEY UPDATE emp_name = 'ExistingName' , salary = 70000;
INSERT INTO  employees_lab (emp_id, emp_name, department, salary)
VALUES (99, 'NewEmp' , 'HR' , 50000)
ON DUPLICATE KEY UPDATE emp_name = 'NewEmp'
INSERT INTO employees_lab (emp_id, emp_name, department, salary)
VALUES (1, 'OldEmp' , 'Finance' , 80000)
ON DUPLICATE KEY UPDATE salary = 80000;
INSERT INTO employees_lab (emp_id, emp_name, department, salary)
VALUES (1 , 'Test', 'IT' , 90000) ON DUPLICATE KEY UPDATE salary = VALUES(salary);
SELECT * FROM employees_lab WHERE salary BETWEEN 50000 AND 70000;
SELECT * FROM employees_lab WHERE emp_name LIKE 'R%';
SELECT * FROM employees_lab WHERE department != 'Finance';













