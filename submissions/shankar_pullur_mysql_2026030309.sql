use practise;
create table employee_demo(emp_id INT  PRIMARY KEY,emp_name varchar(50),department varchar(50)
,salary DECIMAL(10,2),age INT, joining_date date);
 
 ALTER TABLE employee_demo MODIFY emp_id INT auto_increment;

INSERT INTO employee_demo (emp_name, department, salary, age, joining_date) VALUES
('Rahul', 'HR', 30000, 25, '2022-01-10'),
('Sneha', 'HR', 35000, 28, '2021-03-15'),
('Amit', 'IT', 60000, 30, '2020-07-20'),
('Priya', 'IT', 75000, 32, '2019-05-18'),
('Kiran', 'Finance', 50000, 29, '2021-11-25'),
('Anjali', 'Finance', 45000, 27, '2022-02-14'),
('Vikram', 'IT', 80000, 35, '2018-09-10'),
('Meena', 'HR', 32000, 26, '2023-01-05');



SELECT schema_name,default_collation_name
FROM information_schema.schemata
WHERE schema_name='practise';


ALTER DATABASE practise
CHARACTER SET utf8mb4
COLLATE utf8mb4_bin;

SHOW TABLE STATUS
WHERE Name = 'employee_demo';



INSERT INTO employee_demo
VALUES (NULL, 'SSK', 'HR', 45000, 30, '2023-01-10');

INSERT INTO employee_demo
(emp_name, department, salary, age, joining_date)
VALUES('O''brien','Sales',48000,33,'2026--02-10');
select * from employee_demo;

REPLACE INTO employee_demo
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(1, 'John', 'HR', 80000, 31, '2023-01-10');


INSERT INTO employee_demo
(emp_id, emp_name, department, salary)
VALUES
(11, 'Chris', 'Marketing', 55000) as new
ON DUPLICATE KEY UPDATE
salary = VALUES(salary);