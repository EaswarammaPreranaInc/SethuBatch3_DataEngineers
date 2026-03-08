show databases;
 
create database StudentDB;

use StudentDB;

select database();

select current_date();
select current_time();
select user();

create table student_info(id integer primary key ,name varchar(20));

desc student_info;

insert into student_info values(1,'ravi');
insert into student_info values(2,'rajesh');

insert into student_info values(3,'Anil'),(4,'Neha');

select * from student_info;

# auto-increment

create table employees(emp_id int auto_increment primary key,emp_name varchar(100), salary decimal(10,2));
insert into employees(emp_name,salary) values('ravi',15676.98),('neha',87878.77);
insert into employees(emp_name,salary) values('rajesh',98676.98);
insert into employees values(100,'yash',1000676.98);
select * from employees;


create table employees_auto(emp_id int auto_increment primary key,emp_name varchar(50));
insert into employees_auto values(500,'ravi');
insert into employees_auto(emp_name) values('ravi');
select * from employees_auto;

Create table employee_default_test(emp_id integer primary key, emp_name varchar(55), city Varchar(50) default 'Hyderabad');
insert into  employee_default_test values(1,'ravi','Secunderabad');
insert into  employee_default_test(emp_id,emp_name) values(2,'ravi');
select * from employee_default_test;

create table users_test(id integer KEy,email varchar(100) unique, password varchar(50));
insert into users_test values(35,'123@gmail.com','haha'),(36,'456@gmail.com','hehe');
insert into users_test values(37,'123@gmail.com','huu');

show errors;

create table student_age_test(id integer KEy,name varchar(100), age integer check (age>=18));
insert into student_age_test values(35,'mani',22);--
insert into student_age_test values(25,'hari',12);   # error

show errors;

create table company_employees(emp_id int auto_increment primary key, emp_code int not null unique, 
firstname varchar(70) not null,last_name varchar(60), email varchar(50) unique,age int check (18<age<60), 
salary decimal(10,2) default 30000 check (salary>=0), department varchar(60) not null,
joining_date Date Default (current_date()),is_active boolean default true);

insert into company_employees(emp_id , emp_code , 
firstname ,last_name, email ,age , 
salary , department) values(100, 200,'gurusupriya', 'peruri', 'guru@gmail.com', 22, 100000,'ds');

insert into company_employees(emp_code , 
firstname ,last_name, email ,age , 
salary , department) values(201,'sumanjali', 'seetha', 'suma@gmail.com', 22, 100000,'ds');

insert into company_employees(emp_code , 
firstname ,last_name, email ,age , 
salary , department) values(202,'sowmya', 'nidigonda', 'sowmya@gmail.com', 22, 100000,'ds');




