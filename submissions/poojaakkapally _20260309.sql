create database employees_lab;
use employees_lab;
CREATE TABLE employees_labs (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50) not null,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    age INT,
    joining_date DATE
);
insert into employees_labs values(not null,'ravi','it',500000,25,'2022-01-10');
insert into employees_labs(emp_id,emp_name, department, salary, age, joining_date) values
(not null,'rani','it',500000,25,'2022-01-10'),
(not null,'killer','it',500000,25,'2022-01-10'),
(not null,'deepak','hr',500000,25,'2022-01-10'),
(not null,'dinesh','hr',500000,25,'2022-01-10'),
(not null,'pooja','finance',500000,25,'2022-01-10'),
(not null,'subbu','finance',500000,25,'2022-01-10'),
(not null,'uma','sales',500000,25,'2022-01-10'),
(not null,'subas','sales',500000,25,'2022-01-10'),
(not null,'shiva','marketing',500000,25,'2022-01-10'),
(not null,'suma','marketing',500000,25,'2022-01-10');
insert into employees_labs(emp_name, department)values('ghost','finance');
select upper('deeepak');
select round(12.8791,2);
select curdate();
select * from employees_labs;
select emp_name,salary
from employees_labs;
select salary
from employees_labs
where salary>=60000;
select age
from employees_labs
where age<=30;
select department
from employees_labs
where department='it';
select *
from employees_labs
where department='it' or department = 'hr';
select salary,department
from employees_labs
where salary>=60000 and department = 'it';
SELECT department, COUNT(*) AS total
FROM employees_labs
GROUP BY department;
SELECT department, COUNT(*) AS total
FROM employees_labs
GROUP BY department
HAVING COUNT(*) > 1;
SELECT *
FROM employees_labs
ORDER BY salary DESC;
SELECT *
FROM employees_labs
LIMIT 5;
SELECT *
FROM employees_labs
LIMIT 5 OFFSET 5;	
set sql_safe_updates=0;
update employees_lab set salary= 75000 where emp_name='viju';
show errors;
update employees_lab set salary= salary+1000;

delete from employees_lab where emp_name='Anitha';
delete from employees_lab;

replace into employees_lab(emp_id,emp_name,department,salary,age,joining_date) values  (1,'Sairam','HR',100000,111,curdate());
INSERT INTO employees_lab
(emp_id, emp_name, department, salary)
VALUES
(5, 'Chris', 'Marketing', 55000)
ON DUPLICATE KEY UPDATE
salary = 75000;
INSERT INTO employees_lab
(emp_id, emp_name, department, salary)
VALUES
(1, 'Shiva', 'IT', 75000)
ON DUPLICATE KEY UPDATE
salary=10000000;
select * from employees_lab;
select * from employees_lab where salary between 50000 and 70000;
select * from employees_lab where emp_name like 'R%';
select * from employees_lab where department<>'Finance';
show errors;

