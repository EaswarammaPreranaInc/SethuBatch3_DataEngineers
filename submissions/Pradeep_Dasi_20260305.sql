-- creating a database named as StudentDB
show databases;
create database StudentDB;
use StudentDB;

-- creating a table StudentDB in the database StudentDB
create table StudentDB(
id int primary key auto_increment,
name varchar(50)
);

insert into StudentDB(name) values
('Anil'),
('neha');

select * from StudentDB;

select current_date from StudentDB;
select current_time from StudentDB;
select current_user from StudentDB;

create table employees(
emp_id int primary key auto_increment,
emp_name varchar(50),
emp_salary decimal(10,2)
);
insert into employees(emp_name, emp_salary) values
('Pradeep', 30000),
('Pranay', 50000),
('Ajay', 80000);
select * from employees;

create table employee_auto(
emp_id int primary key auto_increment,
emp_name varchar(50)
) auto_increment 500;

insert into employee_auto(emp_name) values
('Pradeep'),
('Ajay'),
('Pranay'),
('Kushal');
select * from employee_auto;

create table employee_table(
emp_id int primary key,
emp_name varchar(80),
city varchar(50) default 'Hyderabad'
);
insert into employee_table values
(1,'Pradeep','Hanamkonda'),
(2,'Ajay', 'Karimnagar'),
(3,'Pranay', 'Mulugu'),
(4,'Kushal', 'AP');
select * from employee_table;

insert into employee_table(emp_id, emp_name) values
(11,'Pradeep'),
(12,'Ajay'),
(13,'Pranay'),
(14,'Kushal');

delete from employee_table where emp_id > 10;

drop database StudentDB;