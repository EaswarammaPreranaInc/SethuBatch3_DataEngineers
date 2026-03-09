CREATE DATABASE employeedb;
USE employeedb;
CREATE TABLE employees_lab(
emp_id INT PRIMARY KEY
AUTO_INCREMENT,
emp_name VARCHAR(50) NOT NULL,
department VARCHAR(50),
salary DECIMAL(10 , 2),
age INT,
joining_date DATE
);
INSERT INTO employees_lab
(emp_name,department,salary,age,joining_date)
VALUES ('Ravi','IT',50000,25,'2022-01-10');
INSERT INTO employees_lab
(emp_name,department,salary,age,joining_date)
VALUES
('Alice','IT',65000,28,'2021-05-15'),
('Bob','HR',45000,32,'2020-11-01'),
('Charlie','Finance',70000,35,'2019-03-20'),
('David','sales',55000,29,'2022-08-12'),
('Eve','Marketing',48000,26,'2023-09-10'),
('Frank','IT',72000,31,'2018-09-10'),
('Grace','HR',52000,27,'2022-04-22'),
('Heidi','Finance',68000,40,'2017-12-12'),
('Ivan','sales',49000,24,'2023-06-01'),
('Judy','Marketing',61000,33,'2020-02-14'),
('Mallory','IT',75000,38,'2016-07-30'),
('Niaj','HR',43000,29,'2021-10-10'),
('Olivia','Finance',80000,45,'2015-05-20'),
('Peggy','sales',58000,30,'2022-03-15'),
('Quentin','Marketing',53000,27,'2021-11-25'),
('Rupert','IT',62000,29,'2020-09-09'),
('Sybil','HR',47000,31,'2019-04-18'),
('Trent','Finance',73000,36,'2018-08-08'),
('Victor','Marketing',59000,34,'2020-12-30');
INSERT INTO employees_lab
(emp_name,department)
VALUES ('Wendy','IT');
INSERT INTO employees_lab
(emp_name,department,salary,age,joining_date)
VALUES (UPPER('zara'),'sales',
ROUND(55000.756),28, CURDATE());
SELECT * FROM employees_lab;
SELECT emp_name, salary FROM employees_lab;
SELECT * FROM employees_lab WHERE salary>60000;
SELECT * FROM employees_lab WHERE age<=30;
SELECT * FROM employees_lab WHERE department IN ('IT','HR');
SELECT * FROM employees_lab WHERE salary>60000 AND department = 'IT';
SELECT DISTINCT department FROM employees_lab;
SELECT department,COUNT(*) FROM employees_lab GROUP BY department;
SELECT department,COUNT(*) FROM employees_lab
GROUP BY department
HAVING COUNT(*)>2;
SELECT * FROM employees_lab ORDER BY salary DESC;
SELECT * FROM employees_lab LIMIT 5;
SELECT * FROM employees_lab LIMIT 5 OFFSET 5;
UPDATE employees_lab SET salary = 75000 WHERE emp_name ='Raj';
UPDATE employees_lab SET salary = salary+1000;
DELETE FROM employees_lab WHERE emp_name='Lokesh';
DELETE FROM employees_lab;
REPLACE INTO employees_lab 
(emp_id,emp_name,joining_date)
VALUES (1,'NewName','IT',60000,30,'2024-01-01');
INSERT INTO employees_lab (emp_id,emp_name,department,salary,age,joining_date)
VALUES (1,'Ravi','IT',80000,26,'2022-01-10')
ON DUPLICATE KEY UPDATE salary = VALUES (salary);
SELECT * FROM employees_lab WHERE salary BETWEEN 50000 AND 70000;
SELECT * FROM employees_lab WHERE emp_name LIKE 'R%';
SELECT * FROM employees_lab WHERE department!='Finance';
 
 







