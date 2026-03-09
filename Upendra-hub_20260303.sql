show databases;
create database StudentDB;
use StudentDB;
select Database();
select now();
select current_date();
select current_time();
select user();
create table Student_info(id int,name varchar(20));
desc Student_info;
insert into Student_info values(1,'Ravi'),(2,'Priya');
insert into Student_info(name) values('Kiran');
insert into Student_info values(3,'Anil'),(4,'Neha');
select * from Student_info;
create table employees(
emp_id  int Auto_increment primary key,
emp_name varchar(100),
salary decimal(10,2));
insert into employees(emp_name,salary) values('John',10000),('Dora',20000),('Jack',30000);
insert into employees values(101,'Ben',150000);
select * from employees;


create table employee_auto(
emp_id  int Auto_increment primary key,
emp_name varchar(100)) auto_increment=500;
insert into employee_auto(emp_name) values('Bean'),('Tom');
select * from employee_auto;


create table employee_default_test(
emp_id  int primary key,
emp_name varchar(50), 
city varchar(50) default "Hyderabad");
insert into employee_default_test(emp_id,emp_name) values(101,'Jill');
insert into employee_default_test values(102,'Jane',"Secunderabad");
select * from employee_default_test;


create table user_test(
user_id int primary key,
email varchar(50) unique,
password varchar(50));
insert into user_test values(101,'ben@gmail.com',1234),(102,'bean@gmail.com',2345);
insert into user_test values(103,'ben@gmail.com',23456);


create table student_age_test(
id int primary key,name varchar(50),
age int check(age>=18));
insert into student_age_test values(1,'Jerry',18);
insert into student_age_test values(2,'mack',17);
show errors;
use studentdb;


create table company_employees(
emp_id int auto_increment primary key,
emp_code int not null unique,
first_name varchar(50) not null,
last_name varchar(50)  ,
email varchar(100) unique,
age int check(age>=18 and age<=60),
salary bigint default 30000 check(salary>0),
department varchar(50) not null,
joining_date date default (current_date()),
is_active boolean default true);
show databases;


create database StudentDB;
use StudentDB;
select Database();
select now();
select current_date();
select current_time();
select user();


create table Student_info(id int,name varchar(20));
desc Student_info;
insert into Student_info values(1,'Ravi'),(2,'Priya');
insert into Student_info(name) values('Kiran');
insert into Student_info values(3,'Anil'),(4,'Neha');
select * from Student_info;


create table employees(emp_id  int Auto_increment primary key,emp_name varchar(100),salary decimal(10,2));
insert into employees(emp_name,salary) values('John',10000),('Dora',20000),('Jack',30000);
insert into employees values(101,'Ben',150000);
select * from employees;


create table employee_auto(emp_id  int Auto_increment primary key,emp_name varchar(100)) auto_increment=500;
insert into employee_auto(emp_name) values('Bean'),('Tom');
select * from employee_auto;
create table employee_default_test(emp_id  int primary key,emp_name varchar(50), city varchar(50) default "Hyderabad");
insert into employee_default_test(emp_id,emp_name) values(101,'Jill');
insert into employee_default_test values(102,'Jane',"Secunderabad");
select * from employee_default_test;


create table user_test(
user_id int primary key,
email varchar(50) unique,password varchar(50));
insert into user_test values(101,'ben@gmail.com',1234),(102,'bean@gmail.com',2345);
insert into user_test values(103,'ben@gmail.com',23456);


create table student_age_test(
id int primary key,name varchar(50),
age int check(age>=18));
insert into student_age_test values(1,'Jerry',18);
insert into student_age_test values(2,'mack',17);
show errors;
insert into company_employees(emp_code ,first_name,last_name,email,age,department,is_active)values
(21,'mary','khan','mary@gmail.com',19,'hr',true),
(22,'john','shen','john@gmail.com',23,'production',true),
(23,'ben','dell','ben@gmail.com',25,'developer',false);
select * from company_employees;
select first_name,last_name,salary from company_employees;
select * from company_employees where salary >30000;
select * from company_employees where is_active=true;
select current_date();
select current_time();

create table bonus_table(id int primary key, phno bigint unique,country varchar(50) default 'India',age int check(age>18));
insert into bonus_table(id,phno,age)values(1,234567,19),(2,1345678,21),(3,12345,22);
desc bonus_table;
select * from bonus_table;











