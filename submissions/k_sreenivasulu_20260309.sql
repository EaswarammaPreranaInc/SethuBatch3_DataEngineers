# PART A create table
create database Employeedb;

use Employeedb;

create table employees_lab (
emp_id int primary key auto_increment,
emp_name varchar(50) not null,
department varchar(50),
salary decimal(10,2),
age int,
joining_date date
)

 

# PART B insert records

insert into employees_lab(emp_name , department , salary , age , joining_date)
values('Ravi' , 'IT' , 50000 , 25 , '2022-01-10');

insert into employees_lab (emp_name, department, salary, age, joining_date) values
('Rahul','IT',65000,28,'2021-03-10'),
('Anita','HR',55000,30,'2020-06-15'),
('Kiran','Finance',70000,35,'2019-02-20'),
('Sneha','Sales',48000,26,'2022-08-11'),
('Vikram','Marketing',52000,29,'2021-11-01'),
('Arjun','IT',75000,32,'2018-05-18'),
('Pooja','HR',46000,24,'2023-01-05'),
('Neha','Finance',68000,31,'2019-09-09'),
('Ramesh','Sales',51000,27,'2022-02-14'),
('Suresh','Marketing',59000,33,'2020-12-30'),
('Divya','IT',72000,34,'2017-07-07'),
('Meena','HR',54000,28,'2021-04-16'),
('Ajay','Finance',66000,36,'2018-10-10'),
('Priya','Sales',47000,25,'2023-03-03'),
('Naveen','Marketing',61000,30,'2020-01-19'),
('Teja','IT',80000,38,'2016-06-06'),
('Lakshmi','HR',53000,27,'2021-09-09'),
('Karthik','Finance',71000,35,'2019-12-12'),
('Varun','Sales',49000,26,'2022-05-05'),
('Deepa','Marketing',60000,31,'2020-08-08');


insert into employees_lab(emp_name , department) values
('sanjay', 'it');

insert into employees_lab (emp_name , department , salary , age , joining_date) values
(upper('mohan'), 'IT' , round(45678.45) , 29, curdate());

# PART C SELECT Queries
select * from employees_lab;

select emp_name , salary from employees_lab;

select * from employees_lab
where salary > 60000;

select * from employees_lab
where age <= 30;

select * from employees_lab
where department = 'IT';

select * from employees_lab
where department IN ('IT', 'HR');

select * from employees_lab
where salary > 60000 and department = 'IT';

select distinct department from employees_lab;

select department, count(*) AS total_employees
from employees_lab
group by department;

select department, COUNT(*) AS total_employees
from employees_lab
group by department
having COUNT(*) > 2;

select *
from employees_lab
order by salary DESC;

select * from employees_lab
limit 5;

select * from employees_lab
limit 5 offset 5;

# Part D – UPDATE Operations

update employees_lab
set salary = 75000
where emp_name = 'Raj';

UPDATE employees_lab
SET salary = salary + 1000;

# Part E – DELETE Operations
delete from employees_lab
where emp_name = 'Lokesh';


delete from employees_lab;

#Part F – MySQL Special Commands
REPLACE INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(1, 'Ravi', 'IT', 70000, 26, '2022-01-10');


INSERT INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(2, 'Rahul', 'IT', 65000, 28, '2021-03-10')
ON DUPLICATE KEY UPDATE
salary = 65000;


INSERT INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(30, 'Manoj', 'Sales', 52000, 27, '2024-02-10')
ON DUPLICATE KEY UPDATE
salary = 52000;


INSERT INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(1, 'Ravi', 'IT', 80000, 26, '2022-01-10')
ON DUPLICATE KEY UPDATE
salary = 80000;


INSERT INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(3, 'Kiran', 'Finance', 72000, 35, '2020-05-20')
ON DUPLICATE KEY UPDATE
salary = VALUES(salary);

#Part G – Additional Search Queries
SELECT *
FROM employees_lab
WHERE salary BETWEEN 50000 AND 70000;


SELECT *
FROM employees_lab
WHERE emp_name LIKE 'R%';


SELECT *
FROM employees_lab
WHERE department != 'Finance';






