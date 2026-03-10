use sssdsql;
create table employees(emp_id int primary key auto_increment,emp_name varchar(50),department varchar(50),salary decimal(10,2),age int,joining_date date);
insert into employees(emp_name,department,salary,age,joining_date) values ('Ravi','IT',50000,25,'2022-01-10');
INSERT INTO employees (emp_name, department, salary, age, joining_date) VALUES 
('Amit Sharma', 'IT', 62000.00, 28, '2022-03-15'),
('Priya Singh', 'HR', 45000.00, 30, '2021-11-20'),
('Vikram Adani', 'Finance', 75000.00, 35, '2020-05-10'),
('Sanya Malhotra', 'Sales', 38000.00, 24, '2023-01-05'),
('Rahul Verma', 'Marketing', 52000.00, 27, '2022-08-12'),
('Anjali Gupta', 'IT', 58000.00, 26, '2022-06-30'),
('Karan Mehra', 'HR', 48000.00, 32, '2021-09-14'),
('Sneha Reddy', 'Finance', 71000.00, 29, '2021-04-22'),
('Rohan Das', 'Sales', 41000.00, 25, '2023-02-18'),
('Megha Iyer', 'Marketing', 55000.00, 31, '2020-12-01'),
('Aditya Roy', 'IT', 65000.00, 33, '2019-11-15'),
('Ishita Bhalla', 'HR', 46000.00, 27, '2022-10-10'),
('Arjun Kapoor', 'Finance', 82000.00, 40, '2018-07-05'),
('Kriti Sanon', 'Sales', 39000.00, 23, '2023-05-20'),
('Varun Dhawan', 'Marketing', 54000.00, 29, '2021-02-28'),
('Siddharth M', 'IT', 60000.00, 30, '2022-04-12'),
('Kiara Advani', 'HR', 47000.00, 28, '2022-01-25'),
('Ranbir R', 'Finance', 78000.00, 34, '2020-08-19'),
('Alia B', 'Sales', 42000.00, 26, '2022-12-05'),
('Deepika P', 'Marketing', 63000.00, 32, '2019-09-14');

insert into employees(emp_name,department) values ('KumaraSwamy','IT');

INSERT INTO employees (emp_name, department, salary, age, joining_date) VALUES 
(upper('rakesh'),'HR',round(55000.653),23,curdate());

select * from employees;


select emp_name,salary from employees;

select * from employees where salary > 60000;

select * from employees where age <= 30;


select * from employees where department = 'IT';

select * from employees where department = 'IT' or department = 'HR';

select * from employees where department = 'IT' and salary > 60000;


select distinct department from employees;

SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;


SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department having count(*) > 2;


select * from employees order by salary desc;



select * from employees limit 5;


select * from employees limit 5 offset 5;


insert into employees(emp_name,department,salary,age,joining_date) values ('Raj','IT',50000,25,'2022-01-10');

update employee set salary= 75000 where emp_name ='Raj';
set SQL_SAFE_UPDATES =0;      -- now allow deleting using emp_name
update employees set salary= 75000 where emp_name ='Raj';
set SQL_SAFE_UPDATES =1;     


UPDATE employees 
SET salary = salary + 1000;
set SQL_SAFE_UPDATES =0;      -- now allow deleting using emp_name
UPDATE employees 
SET salary = salary + 1000;

USE sssdsql;

DELETE FROM employees WHERE emp_name = 'Lokesh';

TRUNCATE TABLE employees; 

REPLACE INTO employees (emp_id, emp_name, department, salary, age, joining_date) 
VALUES (1, 'Ravi Kumar', 'IT', 75000.00, 25, '2022-01-10');

INSERT INTO employees (emp_id, emp_name, department, salary) 
VALUES (1, 'Ravi', 'IT', 60000.00) 
ON DUPLICATE KEY UPDATE salary = 60000.00;

INSERT INTO employees (emp_id, emp_name, department, salary, age, joining_date) 
VALUES (101, 'Aryan', 'Sales', 45000.00, 24, CURDATE()) 
ON DUPLICATE KEY UPDATE emp_name = VALUES(emp_name);

INSERT INTO employees (emp_id, salary) 
VALUES (1, 80000.00) 
ON DUPLICATE KEY UPDATE salary = 80000.00;

INSERT INTO employees (emp_id, emp_name, salary) 
VALUES (2, 'Priya', 55000.00) 
ON DUPLICATE KEY UPDATE salary = VALUES(salary), emp_name = VALUES(emp_name);

SELECT * FROM employees WHERE salary BETWEEN 50000 AND 70000;

SELECT * FROM employees WHERE emp_name LIKE 'R%';

SELECT * FROM employees WHERE department <> 'Finance';









