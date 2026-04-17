create database demo;
use demo;
create table employees_demo(
emp_id int primary key auto_increment,
emp_name varchar(50),
department varchar(50),
salary decimal(10,2),
age int,
joining_date date);
insert into employees_demo(emp_name,department,salary,age,joining_date) values
('Rahul', 'HR', 30000, 25, '2022-01-10'),
('Sneha', 'HR', 35000, 28, '2021-03-15'),
('Amit', 'IT', 60000, 30, '2020-07-20'),
('Priya', 'IT', 75000, 32, '2019-05-18'),
('Kiran', 'Finance', 50000, 29, '2021-11-25'),
('Anjali', 'Finance', 45000, 27, '2022-02-14'),
('Vikram', 'IT', 80000, 35, '2018-09-10'),
('Meena', 'HR', 32000, 26, '2023-01-05');
select * from employees_demo;
select emp_name,salary from employees_demo;
select emp_name,department,joining_date from employees_demo;
select * from employees_demo where department='HR';
select * from employees_demo where department='IT';
select * from employees_demo where salary>50000;
select * from employees_demo where salary<40000;
select * from employees_demo where age>30;
select * from employees_demo where age<=28;
select * from employees_demo where joining_date<'2021-01-01';
select * from employees_demo where joining_date>'2022-01-01';
select * from employees_demo where department='Finance' and salary>45000;
select * from employees_demo where salary between 30000 and 60000;
select * from employees_demo where age between 25 and 30;
select * from employees_demo where department<>'HR';
select * from employees_demo order by salary;
select * from employees_demo order by salary desc;
select * from employees_demo order by age;
select * from employees_demo order by joining_date;
select * from employees_demo order by department,salary;
select * from employees_demo order by salary desc limit 3;
select * from employees_demo order by age limit 2;
select * from employees_demo limit 4;
select * from employees_demo limit 3 offset 3;
select * from employees_demo order by salary desc limit 1;
select count(*) from employees_demo;
select count(*) from employees_demo where department='HR';
select max(salary) from employees_demo;
select min(salary) from employees_demo;
select avg(salary) from employees_demo;
select sum(salary) from employees_demo;
select avg(age) from employees_demo;
select max(age) from employees_demo;
select min(age) from employees_demo;
select count(*) from employees_demo where joining_date<'2021-01-01';
select sum(salary) from employees_demo where department='IT';
select avg(salary) from employees_demo where department='Finance';
select department,count(*) from employees_demo group by department;
select department,avg(salary) from employees_demo group by department;
select department,max(salary) from employees_demo group by department;
select department,min(salary) from employees_demo group by department;
select department from employees_demo group by department having count(*)>2;
select department from employees_demo group by department having avg(salary)>40000;
select department from employees_demo group by department having sum(salary)>100000;
select department from employees_demo group by department having max(salary)>70000;
select department,avg(age) from employees_demo group by department ;
select department from employees_demo group by department having avg(age)>28;
select department from employees_demo group by department having count(*)>3;





