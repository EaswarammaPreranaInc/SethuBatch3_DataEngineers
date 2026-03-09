show databases;
create database employees_lab;
use employees_lab;
create table employees_lab(
	emp_id INT PRIMARY KEY AUTO_INCREMENT,
	emp_name VARCHAR(50) NOT NULL,
	department VARCHAR(50), 
	salary DECIMAL(10,2),
	age INT,
	joining_date DATE 
    );
insert into employees_lab(emp_name,department,salary,age,joining_date)
values('Ravi','IT',50000,25,2022-01-10);
insert into employees_lab(emp_name,department,salary,age,joining_date)
values
('Ravi','IT',50000,25,'2022-01-10'),
('Sita','HR',42000,28,'2021-03-15'),
('Arjun','Finance',60000,30,'2020-07-21'),
('Kiran','Sales',48000,27,'2022-02-18'),
('Neha','Marketing',45000,26,'2021-11-05'),
('Rahul','IT',58000,29,'2020-09-12'),
('Priya','HR',40000,24,'2023-01-25'),
('Vikas','Finance',62000,31,'2019-06-14'),
('Anjali','Sales',47000,26,'2022-05-20'),
('Ramesh','Marketing',49000,28,'2021-08-10'),
('Sneha','IT',53000,27,'2022-03-17'),
('Deepak','HR',41000,30,'2019-12-01'),
('Pooja','Finance',61000,32,'2023-02-11'),
('Manoj','Sales',46000,29,'2020-04-08'),
('Divya','Marketing',44000,26,'2022-07-19'),
('Suresh','IT',57000,33,'2018-10-23'),
('Kavya','HR',43000,27,'2021-06-30'),
('Rohit','Finance',65000,34,'2020-01-16'),
('Nisha','Sales',45000,25,'2023-03-05'),
('Amit','Marketing',47000,31,'2018-05-09');
select * from employees_lab;
insert into employees_lab(emp_name,department)
values('soni','IT');
insert into employees_lab(emp_name,department,salary,age,joining_date)
values(upper('amith'),'Marketing',round(47000.789),31,current_date());
select * from employees_lab;
select emp_name,salary
from employees_lab;
select salary>60000
from employees_lab;
select * from employees_lab
where salary>60000;
select * from employees_lab
where age<=30;
select * from employees_lab
where department='IT';
select * from employees_lab
where department='IT' or department='HR';
select * from employees_lab
where salary>60000 and department='IT';
select distinct department from employees_lab;
select department,count(*)
from employees_lab
group by department;
select department, count(*) as number_of_employees
from employees_lab
group by department
having count(*) > 2;
select * 
from employees_lab
order by salary desc;
select * 
from employees_lab
limit 5;
select *
from employees_lab
limit 5 offset 5;
select emp_id 
from employees_lab
where emp_name='Amit';
update employees_lab
set salary=70000
where emp_name='Amit';
update employees_lab
set salary =salary+1000;
delete from employees_lab
where emp_name = 'Lokesh';
delete from employees_lab;
replace into employees_lab (emp_id, emp_name, department, salary, age, joining_date)
values (1, 'Ravi', 'IT', 60000, 28, '2022-01-10');
insert into employees_lab (emp_id, emp_name, department, salary, age, joining_date)
values (2, 'Sita', 'HR', 50000, 25, '2022-02-15')
on duplicate key update salary = 55000;
insert into employees_lab (emp_id, emp_name, department, salary, age, joining_date)
values (10, 'Neha', 'Marketing', 45000, 24, '2023-01-05')
on duplicate key update salary = VALUES(salary);
insert into employees_lab (emp_id, emp_name, department, salary, age, joining_date)
values (3, 'Raj', 'IT', 75000, 27, '2022-03-10')
on duplicate key update salary = 80000;
insert into employees_lab (emp_id, emp_name, department, salary, age, joining_date)
values (4, 'Kiran', 'Sales', 48000, 26, '2022-04-15')
on duplicate key update salary = VALUES(salary);
select * 
from employees_lab
where salary between 50000 and 70000;
select *
from employees_lab
where emp_name like 'R%';
select *
from employees_lab
where department != 'Finance';







