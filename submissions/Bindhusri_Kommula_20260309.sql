create database labdb;
use labdb;
create table employees_lab(
emp_id int primary key auto_increment,
emp_name varchar(50) not null,
department varchar(50),
salary decimal(10,2),
age int,
joining_date date
);
insert into employees_lab(emp_name,department,salary,age,joining_date) values('Ravi','IT',50000,25,'2022-01-10');
insert into employees_lab(emp_name,department,salary,age,joining_date)
values
('Rama','IT',60000,35,'2022-01-10'),
('Sita','HR',70000,30,'2021-01-10'),
('Neha','Marketing',40000,21,'2020-01-10'),
('kiran','Sales',30000,31,'2018-02-11'),
('Anitha','HR',20000,22,'2021-11-10'),
('Rajesh','Marketing',60000,28,'2020-12-20'),
('Divya','Sales',40000,31,'2021-07-10'),
('Arjun','IT',90000,25,'2023-02-10'),
('Pooja','HR',55000,30,'2022-01-10'),
('Manoj','Finance',25000,27,'2021-12-15'),
('Kavya','Finance',66000,32,'2022-03-10'),
('Nikhi','IT',41000,35,'2018-01-11'),
('Priya','IT',77000,39,'2019-11-14'),
('Ramya','Finance',34000,23,'2023-01-10'),
('suresh','HR',67000,32,'2018-02-10'),
('sneha','IT',22000,29,'2021-09-16'),
('Bindhu','Marketing',34000,28,'2022-02-18'),
('vikram','IT',88000,37,'2022-03-19'),
('meena','HR',63000,31,'2021-04-11');
insert into employees_lab(emp_name,department) values('sam','IT');
insert into employees_lab(emp_name,department,salary,age,joining_date)
values(UPPER('raju'),'Finance',Round(45000.67),23,curdate());
select * from employees_lab;
select emp_name,salary from employees_lab;
select * from employees_lab where salary>60000;
select * from employees_lab where age<=30;
select * from employees_lab where department='IT';
select * from employees_lab where department IN ('IT','HR');
select * from employees_lab where salary>60000 and department='IT';
select distinct department from employees_lab;
select department,count(*) from employees_lab group by department;
select department from employees_lab group by department having count(*)>2;
select * from employees_lab order by salary desc;
select * from employees_lab limit 5;
select * from employees_lab limit 5 offset 5;
set sql_safe_updates=0;
update employees_lab
set salary=75000
where emp_name='RAJU';
update employees_lab
set salary=salary+1000;
delete from employees_lab where emp_name='Lokesh';
delete from employees_lab;
replace into employees_lab (emp_id,emp_name,department,salary,age,joining_date) values(1,'Raj','IT',75000,30,'2022-01-01');
insert into employees_lab
(emp_id,emp_name,department,salary)
values(5,'Chris','Marketing',55000) 
on duplicate key update
salary=100000;
insert into employees_lab
(emp_id,emp_name,department,salary)
values(5,'Anil','IT',59000) 
on duplicate key update
salary=60000;
insert into employees_lab
(emp_id,emp_name,department,salary)
values(1,'Raj','Marketing',55000) 
on duplicate key update
salary=70000;
insert into employees_lab
(emp_id,emp_name,department,salary)
values(3,'Kiran','Finance',55000) 
on duplicate key update
salary=VALUES(salary);
select * from employees_lab where salary between 50000 and 70000;
select * from employees_lab where emp_name like 'R%';
select * from employees_lab where department<>'Finance';





