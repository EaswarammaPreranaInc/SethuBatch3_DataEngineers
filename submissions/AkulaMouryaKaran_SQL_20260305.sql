create table employees(emp_id int primary key auto_increment,
emp_name varchar(100),salary decimal(10,2));
create table employee_auto(emp_id int primary key auto_increment,
emp_name varchar(50))auto_increment=500;
show tables;
select * from employee_auto;
insert into employee_auto(emp_id,emp_name) values (1,'Surya'),(2,'Mahesh');
select * from employee_auto;
create table employee_default_test(emp_id int auto_increment primary key,
emp_name varchar(50),city varchar(50) default 'Hyderabad');
insert into employee_default_test(emp_id,emp_name,city) values
(1,'Ramesh','Secunderabad');
insert into employee_default_test(emp_id,emp_name) values
(2,'Rajesh');
select * from employee_default_test;
create table users_test(user_id int primary key,email varchar(50) unique,
password varchar(50));
insert into users_test(user_id,email,password) values (101,'abc@gmail.com',12345678),(102,'123@gmail.com',87654321);
insert into users_test(user_id,email,password) values (103,'abc@gmail.com',00000000);
show errors;
show databases;
use studentdb;
select * from employees;
select * from employees where salary>=60000;
select * from employees where salary>=50000;
alter table employees add department varchar(50);
update employees set department='IT' where emp_id=1;
update employees set department='HR' where emp_id=2;
update employees set department='IT' where emp_id=3;
update employees set department='HR' where emp_id=100;
select * from employees;
select * from employees where salary between 50000 and 60000;
select * from employees where emp_name like 'S%';
select * from employees where emp_name like '%y%';
select * from employees where department in ('HR');
select * from employees where department in ('IT');
select * from employees where department in ('HR','IT');
update employees set emp_id=4 where emp_name='Suresh' limit 1;
select * from employees;
update employees set salary=90000 where emp_id=2;
select * from employees;
delete from employees where emp_id=4;
select * from employees;
create table studentabc(roll_no int auto_increment primary key,
name varchar(50) not null,marks int check (marks>=0),
email varchar(100) unique);
select count(*) from employees;
select max(salary) from employees;
select min(salary) from employees;
select avg(salary) from employees;
select sum(salary) from employees;
select department ,count(*) from employees group by department;
select department,count(*) from employees group by department having count(*)>1;
select * from employees order by salary asc;
select * from employees order by salary desc;
select * from employees order by salary desc limit 2;
select e.emp_name and d.department from employees e inner join department d on e.department=d.department;
use studentdb;
create table users(user_id int auto_increment primary key,
username varchar(50),marks int);
insert into users(username,marks) values ('Mourya',35),('Shourya',45);
select e.emp_name,d.name from employees e inner join department d on e.emp_id=d.id;
select * from employees where salary >(select avg(salary) from employees);
desc employees;
select * from employees;
alter table employees add hire_date date;
create table department(id int auto_increment primary key,
name varchar(50),marks int);
insert into department(name,marks) values ('Sairam',55),('John',45);
alter table employees modify salary bigint;
alter table employees drop hire_date;
show tables;
truncate table studentabc;
show tables;
drop table studentabc;












