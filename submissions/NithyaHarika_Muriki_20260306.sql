show databases;

create database StudentDB;

use StudentDB;
select database();
select user();
select now();

create table student_info(
id int ,
name varchar(50));
desc student_info;
insert into student_info values(1, 'Ravi'),(2, 'Priya');
insert into student_info(name) values('Kiran');
insert into student_info values(3, 'Anil'),(4, 'Neha');
select * from student_info;

create table employee(
emp_id int auto_increment primary key,
emp_name  VARCHAR(30),
SALARY decimal(10,2));


insert into employee(emp_name,SALARY) values 
('Nithya', 3000000),
('Shirisha', 400000),
('Vinay', 500000);

insert into employee(emp_id) values(100);

select * from employee;
#35
select emp_name,salary from employee;

#36
select emp_name from employee
where salary >= 300000;




create table employee_auto(
emp_id int auto_increment primary key,
emp_name varchar(50)) auto_increment= 500;


insert into employee_auto(emp_name) values('Shin'),('Chan');
select * from employee_auto;

create table emp_default_test(
emp_id int primary key,
emp_name varchar(50),
city varchar(50) default 'Hyderabad');

insert into emp_default_test values(1,'Varun','Banglore');
insert into emp_default_test(emp_id,emp_name) values(2,'Ajay');

select * from emp_default_test;

create table users_test(
user_id int primary key,
email varchar(50) unique,
password varchar(50));

insert into users_test values
(1, 'mnhvbnssdjpr@gmail.com', 'asdfgfg'),
(2, 'abcdefgh@gmail.com','abcdef');

insert into users_test values(3, 'abcdefgh@gmail.com', 'qwrert');
#Error Code: 1062. Duplicate entry 'abcdefgh@gmail.com' for key 'users_test.email'	0.015 sec  
select * from users_test;
show errors;

create table student_age_test(
id int primary key,
name varchar(50),
age int check (age >= 18));

insert into student_age_test values(1, 'Manipal',21);
insert into student_age_test values(2, 'Jasmine',12);
#Error Code: 3819. Check constraint 'student_age_test_chk_1' is violated.	0.000 sec

show errors;

create table com_employee(
emp_id int auto_increment primary key,
emp_code int not null unique key,
first_name varchar(50) not null,
last_name varchar(50) ,
email varchar(50) unique ,
age int check (age between 18  and 60),
salary int default 30000 check(salary >= 0),
joining_date date default (current_date()),
is_active boolean default TRUE
);

insert into com_employee(emp_code,first_name,last_name,email,age, salary,is_active) values 
(234, 'Mary','Khan','mnbvcxz@gmail.com',20,2002000,True),
(343, 'Mani','Sana','mnbvcxzasd@gmail.com',22,200000,true),
(555, 'Siri','Alexa', 'sirihaaa@gmail.com', 40,780000,false);

select * from com_employee; 
select first_name,last_name from com_employee
where salary >= 300000;

select first_name,last_name from com_employee
where is_active= true;


select current_date();
select current_time();
select current_user();
select database();

create table random_tabs(
id int auto_increment primary key,
city varchar(50) default 'Delhi',
ph_num bigint not null unique key,
age int check (age between 21 and 40)
);

insert into random_tabs(id,ph_num,age) values 
(1,345678900,22),
(2,234567321,34),
(3,565585558,24),
(4,548781258,39),
(5,99999999,32);


desc random_tabs;
select * from random_tabs;

create table product_orders(
order_id int auto_increment primary key,
cust_name varchar(100) not null,
product_name varchar(100) not null,
quantity int not null,
price  decimal(10,2) not null,
order_date date default (current_date()),
is_delivered boolean default false
);
use studentdb;
INSERT INTO product_orders 
(cust_name, product_name, quantity, price, order_date, is_delivered)
VALUES
('Ravi', 'Laptop', 1, 55000.00, '2025-03-01', TRUE),
('Priya', 'Mobile', 2, 20000.00, '2025-03-02', FALSE),
('Kiran', 'Headphones', 3, 1500.00, '2025-03-02', TRUE),
('Anil', 'Keyboard', 2, 1200.00, '2025-03-03', FALSE),
('Neha', 'Monitor', 1, 18000.00, '2025-03-03', TRUE);

insert into product_orders 
(cust_name, product_name, quantity, price)
VALUES
('Nithya','Telivision',2, 40000.00);

select * from product_orders;

select cust_name, product_name, price  from product_orders;

select *,(quatity*price) as total_amount from product_orders;