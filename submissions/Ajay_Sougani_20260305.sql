-- creating a database named StudentDB
show databases;
create database StudentDB;
use StudentDB;

-- creating a table StudentDB in the database StudentDB
create table StudentDB(
id int primary key auto_increment,
name varchar(50)
);

insert into StudentDB(name) values
('Ajay'),
('Vijay');

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
('Ajay', 40000),
('Vijay', 50000),
('Sanjay', 60000);
select * from employees;

create table employee_auto(
emp_id int primary key auto_increment,
emp_name varchar(50)
) auto_increment 500;

insert into employee_auto(emp_name) values
('Saketh'),
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
(1,'Saketh','Jagtial'),
(2,'Ajay', 'Karimnagar'),
(3,'Pranay', 'Siddipet'),
(4,'Kushal', 'AndraPradesh');
select * from employee_table;

insert into employee_table(emp_id, emp_name) values
(11,'Sakesh'),
(12,'Ajay'),
(13,'Pradeep'),
(14,'Kushal');

delete from employee_table where emp_id > 10;

drop database StudentDB;