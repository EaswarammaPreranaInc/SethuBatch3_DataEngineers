-- part 1
show databases;
create database studentdb;
use studentdb;
select database();
select current_date(), current_time(), current_user();

-- part 2
create table student_info(
id int,
name varchar(20)
);

desc student_info;

insert into student_info values (1,'ravi'),(2,'priya');
insert into student_info(name) values ('kiran');
insert into student_info values (3,'anil'),(4,'neha');

select * from student_info;

-- part 3
create table employees(
emp_id int auto_increment primary key,
emp_name varchar(100),
salary decimal(10,2)
);

insert into employees(emp_name,salary) values
('ravi',35000),
('priya',42000),
('anil',30000);

insert into employees(emp_id,emp_name,salary)
values(100,'kiran',50000);

select * from employees;

-- part 4
create table employee_auto(
emp_id int auto_increment primary key,
emp_name varchar(50)
) auto_increment=500;

insert into employee_auto(emp_name)
values ('ravi'),('priya');

select * from employee_auto;

-- part 5
create table employee_default_test(
emp_id int primary key,
emp_name varchar(50),
city varchar(50) default 'hyderabad'
);

insert into employee_default_test values (1,'ravi','delhi');
insert into employee_default_test(emp_id,emp_name) values (2,'priya');

select * from employee_default_test;

-- part 6
create table users_test(
user_id int primary key,
email varchar(100) unique,
password varchar(50)
);

insert into users_test values
(1,'ravi@gmail.com','123'),
(2,'priya@gmail.com','abc');

insert into users_test values
(3,'ravi@gmail.com','xyz');

show errors;

-- part 7
create table student_age_test(
id int primary key,
name varchar(50),
age int check(age>=18)
);

insert into student_age_test values (1,'ravi',20);
insert into student_age_test values (2,'anil',16);

show errors;

-- part 8
create table company_employees(
emp_id int auto_increment primary key,
emp_code varchar(20) not null unique,
first_name varchar(50) not null,
last_name varchar(50),
email varchar(100) unique,
age int check(age between 18 and 60),
salary decimal(10,2) default 30000 check(salary>=0),
department varchar(50) not null,
joining_date date default current_date,
is_active boolean default true
);

insert into company_employees
(emp_code,first_name,last_name,email,age,salary,department)
values
('e101','ravi','kumar','ravi@gmail.com',25,35000,'it'),
('e102','priya','sharma','priya@gmail.com',28,40000,'hr'),
('e103','anil','reddy','anil@gmail.com',30,45000,'finance');

select * from company_employees;

-- part 9
select * from student_info;
select emp_name,salary from employees;
select * from employees where salary>30000;
select * from company_employees where is_active=true;

-- part 10
select current_date();
select current_time();
select current_user();
select database();

-- bonus
create table bonus_table(
id int primary key,
email varchar(100) unique,
city varchar(50) default 'hyderabad',
age int check(age>=18)
);

insert into bonus_table values
(1,'anagha@gmail.com','delhi',25),
(2,'bhargavi@gmail.com','hyderabad',30),
(3,'chandana@gmail.com','chennai',22),
(4,'divya@gmail.com','mumbai',28),
(5,'eesha@gmail.com','hyderabad',35);

desc bonus_table;
select * from bonus_table;

-- product orders table
create table product_orders(
order_id int auto_increment primary key,
customer_name varchar(100) not null,
product_name varchar(100) not null,
quantity int not null,
price decimal(10,2) not null,
order_date date default current_date,
is_delivered boolean default false
);

insert into product_orders
(customer_name,product_name,quantity,price)
values
('ravi','laptop',1,60000),
('priya','mobile',2,20000),
('anil','keyboard',3,1500),
('neha','mouse',2,800),
('kiran','monitor',1,12000);

insert into product_orders
(customer_name,product_name,quantity,price)
values ('rahul','printer',1,7000);

select * from product_orders;

select customer_name,product_name,price
from product_orders;

select *, quantity*price as total_amount
from product_orders;