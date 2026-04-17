create database demoforemployeedetails;
use demoforemployeedetails;
create table employee_details(
emp_id int primary key auto_increment,
emp_name varchar(50),
department varchar(50),
salary decimal(10,2),
age int,
joining_date date);

INSERT INTO employee_details(emp_name, department, salary, age, joining_date) VALUES
('Rahul', 'HR', 30000, 25, '2022-01-10'),
('Sneha', 'HR', 35000, 28, '2021-03-15'),
('Amit', 'IT', 60000, 30, '2020-07-20'),
('Priya', 'IT', 75000, 32, '2019-05-18'),
('Kiran', 'Finance', 50000, 29, '2021-11-25'),
('Anjali', 'Finance', 45000, 27, '2022-02-14'),
('Vikram', 'IT', 80000, 35, '2018-09-10'),
('Meena', 'HR', 32000, 26, '2023-01-05');

select * from employee_details;
select emp_name,salary from employee_details;
select emp_name,department,joining_date from employee_details;
select * from employee_details where department='HR';
select * from employee_details where department='IT';
select * from employee_details where salary>50000;
select * from employee_details where salary<40000;
select * from employee_details where age>30;
select * from employee_details where age<=28;
select * from employee_details where joining_date<'2021-01-01';
select * from employee_details where joining_date>'2022-01-01';
select * from employee_details where department='finance' and salary>45000;
select * from employee_details where salary between 30000 and 60000;
select * from employee_details where not department='HR';
select * from employee_details order by salary;
select * from employee_details order by salary desc;
select * from employee_details order by age;
select * from employee_details order by joining_date desc;
select * from employee_details order by department,salary;
select * from employee_details order by salary desc limit 3;
select * from employee_details order by age limit 2;
select * from employee_details limit 4;
select * from employee_details  limit 3 offset 3;
select * from employee_details order by salary desc limit 1;





