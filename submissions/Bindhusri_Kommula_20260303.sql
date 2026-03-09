show databases;
create database EmployeeDB;
use employeeDB;
select database();
select current_date();
select current_time();
select user();
create table student_info(
id INT,
name VARCHAR(15)
);
desc student_info;
insert into student_info values(1,'Ravi'),(2,'Priya');
insert into student_info(name) values('Kiran');
insert into student_info values(3,'Anil'),(4,'Neha');
select * from student_info;
create table employees(
emp_id int AUTO_INCREMENT PRIMARY KEY,
emp_name VARCHAR(100),
salary decimal(10,2)
);
insert into employees(emp_name,salary) values('bindhu',10000),('sreeja',20000),('bhavishya',300000);
insert into employees(emp_id) values(100);
select * from employees;
create table employee_auto(
emp_id int auto_increment primary key,
emp_name VARCHAR(50)
) auto_increment=500;
insert into employee_auto(emp_name) values('ram');
select * from employee_auto;
create table employee_default(
emp_id int primary key,
emp_name varchar(50),
city varchar(50) default 'Hyderabad'
);
insert into employee_default values(1,'ramu','sec');
insert into employee_default(emp_id,emp_name) values(2,'latha');
show errors;
select * from employee_default;
create table users_test(
user_id int primary key,
email varchar(100) unique,
password varchar(50)
);
insert into users_test(user_id,email,password) values(101,'abc@gmail.com','abc'),(102,'xyz@gmail.com','xyz');
#insert into users_test values(103,'abc@gmail.com','aaa');
create table student_age_test(
id int primary key,
name varchar(50),
age int check (age>=18)
);
insert into student_age_test values(1,'vardhini',30);
#insert into student_age_test values(1,'vardhini',10); 
show errors;
create table company_employees(
emp_id int auto_increment primary key,
emp_code varchar(10) not null unique,
first_name varchar(15) not null,
last_name varchar(15) null,
email varchar(50) unique,
age int check(age>=18 and age<=30),
salary decimal(10,2) default 30000.00 check(salary>=0),
department varchar(20) not null,
joining_date DATE default (current_date),
is_active BOOLEAN default TRUE
);
insert into company_employees(emp_id,emp_code,first_name,last_name,email,age,salary,department,joining_date,is_active)
 values(1000,242,'bindhu','kommula','bindhu@gmail.com',30,30000,'HR','2026-03-03',TRUE);
 select * from company_employees;
 select * from student_info;
 select emp_name,salary from employees;
 select * from employees where salary>30000;
 select * from company_employees where is_active=TRUE;
 select current_Date();
 select current_time();
 select user();
 
 select database();
create database temp;
show errors;
use temp;
create table bonus_table(
id int auto_increment primary key,
email varchar(100) unique,
age int check(age>=18),
city varchar(50) default 'bangalore'
);
insert into bonus_table(email,age) values
('a@gmail.com', 20),
('b@gmail.com', 22),
('c@gmail.com', 25),
('d@gmail.com', 30),
('e@gmail.com', 35);
DESC bonus_table;
SELECT * FROM bonus_table;

create table product_orders(
order_id int auto_increment primary key,
customer_name varchar(100) not null,
product_name varchar(100) not null,
quantity int not null,
price decimal(10,2) not null,
order_date date default(current_date),
is_delivered boolean default FALSE
);
select * from product_orders;
INSERT INTO product_orders 
(customer_name, product_name, quantity, price, order_date, is_delivered)
VALUES
('Ravi', 'Laptop', 1, 55000.00, '2025-03-01', TRUE),
('Priya', 'Mobile', 2, 20000.00, '2025-03-02', FALSE),
('Kiran', 'Headphones', 3, 1500.00, '2025-03-02', TRUE),
('Anil', 'Keyboard', 2, 1200.00, '2025-03-03', FALSE),
('Neha', 'Monitor', 1, 18000.00, '2025-03-03', TRUE);
INSERT INTO product_orders 
(customer_name, product_name, quantity, price)
VALUES
('Sita', 'Mouse', 4, 800.00);


select customer_name from product_orders;
select product_name from product_orders;
select price from product_orders;
select (quantity*price) as total_amount from product_orders;












 


