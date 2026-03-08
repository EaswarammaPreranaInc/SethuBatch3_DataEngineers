create database employees_demo;

use employees_demo;

create table employees_info(
	emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    age INT,
    joining_date DATE
);

select * from employees_info;

INSERT INTO employees_info (emp_name, department, salary, age, joining_date) VALUES
('Rahul', 'HR', 30000, 25, '2022-01-10'),
('Sneha', 'HR', 35000, 28, '2021-03-15'),
('Amit', 'IT', 60000, 30, '2020-07-20'),
('Priya', 'IT', 75000, 32, '2019-05-18'),
('Kiran', 'Finance', 50000, 29, '2021-11-25'),
('Anjali', 'Finance', 45000, 27, '2022-02-14'),
('Vikram', 'IT', 80000, 35, '2018-09-10'),
('Meena', 'HR', 32000, 26, '2023-01-05');

select * from employees_info;


-- 1.	Display all records from the table.
select * from employees_info;

-- 2.	Display only emp_name and salary.
select emp_name,salary 
from employees_info;

-- 3.	Display only emp_name, department, and joining_date.
select emp_name,department,joining_date
from employees_info;

-- 4.	Display employees who belong to HR department.
select emp_name 
from employees_info
where department='HR';

-- 5.	Display employees who belong to IT department.
select emp_name
from employees_info
where department='IT';

-- 6.	Display employees whose salary is greater than 50000.
select emp_name 
from employees_info
where salary>50000;

-- 7.	Display employees whose salary is less than 40000.
select emp_name 
from employees_info
where salary<40000;

-- 8.	Display employees whose age is greater than 30.
select emp_name 
from employees_info
where age>30;

-- 9.	Display employees whose age is less than or equal to 28.
select emp_name 
from employees_info
where age<=28;

-- 10.	Display employees who joined before 2021-01-01.
select emp_name
from employees_info
where joining_date<2021-01-01;

-- Section B – ORDER BY & LIMIT (16–25)

-- 16.	Display all employees sorted by salary (Ascending)
select emp_name
from employees_info
order by salary asc;

-- 17.	Display all employees sorted by salary (Descending).
select emp_name
from employees_info
order by salary desc;
-- 18.	Display employees sorted by age (Ascending).
select emp_name
from employees_info
order by age asc;
-- 19.	Display employees sorted by joining date (Newest first).
select emp_name
from employees_info
order by joining_date desc ;
-- 20.	Display employees sorted by department and salary.
select emp_name
from employees_info
order by department,salary asc;

-- 21.	Display top 3 highest paid employees.
select emp_name
from employees_info
order by salary desc
limit 3;
-- 22.	Display top 2 youngest employees.
select emp_name
from employees_info
order by age asc
limit 2;
-- 23.	Display first 4 records.
SELECT *
FROM employees_info
LIMIT 4;

-- 24.	Skip first 3 records and display next 3 records.
SELECT *
FROM employees_info
LIMIT 3 OFFSET 3;


--  25.	Display the employee with the highest salary.
SELECT *
FROM employees_info
ORDER BY salary DESC
LIMIT 1;

