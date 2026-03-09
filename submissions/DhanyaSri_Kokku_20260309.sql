use employeedb;
create table employees_lab(
emp_id INT PRIMARY KEY AUTO_INCREMENT,
emp_name VARCHAR(50) NOT NULL,
department VARCHAR(50),
salary DECIMAL(10,2),
age INT,
joining_date DATE);
INSERT INTO employees_lab(emp_name,department,salary,age,joining_date) VALUES ('Ravi','IT',50000,25,'2022-01-10');
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date) VALUES
('Ramu','IT',60000,29,'2023-01-10'),
('Anita','HR',45000,28,'2021-03-15'),
('Kiran','Finance',55000,30,'2020-07-20'),
('Suresh','IT',60000,32,'2019-11-05'),
('Meena','Marketing',48000,27,'2021-06-12'),
('Arjun','IT',52000,26,'2022-09-01'),
('Divya','HR',47000,29,'2020-12-18'),
('Rahul','Finance',58000,31,'2018-04-10'),
('Sneha','Marketing',49000,24,'2023-02-14'),
('Vijay','IT',61000,33,'2019-08-22'),
('Priya','HR',46000,27,'2021-10-09'),
('Karthik','Finance',57000,30,'2020-01-17'),
('Lakshmi','Marketing',50000,28,'2022-05-11'),
('Naveen','IT',62000,34,'2017-09-30'),
('Pooja','HR',44000,26,'2023-01-05'),
('Ramesh','Finance',56000,29,'2019-03-21'),
('Anjali','Marketing',51000,27,'2021-07-08'),
('Manoj','IT',59000,31,'2018-12-13'),
('Deepa','HR',45500,28,'2022-04-19'),
('Sunil','Finance',57500,30,'2020-06-25');
INSERT INTO employees_lab(emp_name,department) VALUES ('Nikil','Finance');
INSERT INTO employees_lab(emp_name,department,salary,age,joining_date) VALUES (upper('Raghu'),'IT',round(70000.123),25,CURDATE());
SELECT * FROM employees_lab;
SELECT emp_name,salary from employees_lab;
SELECT * FROM employees_lab WHERE salary > 60000;
SELECT * FROM employees_lab WHERE age <= 30;
SELECT * FROM employees_lab WHERE department='IT';
SELECT * FROM employees_lab WHERE department in ('IT','HR');
SELECT * FROM employees_lab WHERE salary > 60000 and department='IT';
SELECT DISTINCT department FROM employees_lab;
SELECT department,count(*) FROM employees_lab GROUP BY department;
SELECT department,count(*) FROM employees_lab GROUP BY department having count(*) > 2;
SELECT * FROM employees_lab ORDER BY salary DESC;
SELECT * FROM employees_lab LIMIT 5;
SELECT * FROM employees_lab LIMIT 5 OFFSET 5;
SET SQL_SAFE_UPDATES=0;
UPDATE employees_lab SET salary =75000 where emp_name='Raj';
UPDATE employees_lab SET salary = salary+1000;
DELETE FROM employees_lab WHERE emp_name='Lokesh';
DELETE FROM employees_lab;
REPLACE INTO employees_lab(emp_id,emp_name,department,salary,age,joining_date) VALUES (1,'Ramesh','IT',53000,27,'2022-01-01');
INSERT INTO employees_lab(emp_id, emp_name, department, salary, age, joining_date)
VALUES (11, 'Ravi', 'IT', 70000, 32, '2022-01-10')ON DUPLICATE KEY UPDATE salary = 50000,department = 'IT';
INSERT INTO employees_lab(emp_id, emp_name, department, salary, age, joining_date) VALUES (12, 'Anita', 'HR', 45000, 28, '2021-03-15')ON DUPLICATE KEY UPDATE salary = 45000;
INSERT INTO employees_lab(emp_id, emp_name, department, salary, age, joining_date) VALUES (1, 'Ravi', 'IT', 60000, 25, '2022-01-10')ON DUPLICATE KEY UPDATE salary = 60000;
INSERT INTO employees_lab(emp_id, emp_name, department, salary, age, joining_date)
VALUES (13, 'Kiran', 'Finance', 55000, 30, '2020-07-20')ON DUPLICATE KEY UPDATE salary = VALUES(salary);
SELECT * FROM employees_lab WHERE salary BETWEEN 50000 and 70000;
SELECT * FROM employees_lab WHERE emp_name LIKE 'R%';
SELECT * FROM employees_lab WHERE department != 'Finance';