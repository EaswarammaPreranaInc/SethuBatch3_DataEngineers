show databases;

create database StudentDB;

use StudentDB;

select database();

select current_time(),current_date(),current_user();

create table student_info(
id int,
name varchar(50)
);

desc student_info;

insert into student_info values (1, 'Ravi'),
(2, 'Priya');

insert into student_info(name) values ('sai');

insert into student_info values (3, 'Anil'),
(4, 'Neha');

select * from student_info;

create table employees (
emp_id int auto_increment primary key,
emp_name varchar(100),
salary decimal(10,2)
);

insert into employees(emp_name,salary) values ('sai',10000),
('siva',20000),('rajesh',30000);

insert into employees values (100,'bhuvan',50000);

select * from employees;

create table employee_auto (
emp_id int auto_increment primary key,
emp_name varchar(100)
) auto_increment = 500;

insert into employee_auto(emp_name) values ('ganesh'),('pankaj');

select * from employee_auto;

create table employee_default_test(
emp_id int PRIMARY KEY,
emp_name VARCHAR(50),
city VARCHAR(50) default 'Hyderabad'
);

insert into employee_default_test values (100,'Harhsa','Secundearabd');

insert into employee_default_test(emp_id,emp_name) values (101,'Arun');

select * from employee_default_test;

create table users_test(
user_id int PRIMARY KEY,
email varchar(100) UNIQUE,
password VARCHAR(50)
);

insert into users_test values(1,'sure@gail.com','Sai@88899');

insert into users_test values(2,'sure@gail.com','Sai@8889');

show errors;

create table student_age_test (
id int PRIMARY KEY,
name  VARCHAR(50),
age int check(age>=18) 
);

insert into student_age_test values (100,'Sai',21);

insert into student_age_test values (101,'Siva',17);

show errors;

CREATE TABLE company_employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_code VARCHAR(10) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18 AND age <= 60),
    salary DECIMAL(10,2) DEFAULT 30000 CHECK (salary >= 0),
    department VARCHAR(50) NOT NULL,
    joining_date DATE DEFAULT (CURRENT_DATE),
    is_active BOOLEAN DEFAULT TRUE
);

insert into ompany_employees
(emp_code, first_name, last_name, email, age, salary, department)
values
('E001', 'Ram', 'Kumar', 'ram@gmail.com', 25, 35000, 'IT'),
('E002', 'Priya', 'Sharma', 'priya@gmail.com', 30, 40000, 'HR'),
('E003', 'John', 'David', 'john@gmail.com', 28, 45000, 'Finance');


select * from company_employees;

select * from student_info;

select emp_name, salary from employees;

select* from employees
where salary > 30000;

select * from company_employees
where is_active = true;

select current_date();

select current_time();

select user();

select database();

create table bonus_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    city VARCHAR(50) DEFAULT 'Bangalore'
);

insert into bonus_table (email, age) values
('a@gmail.com', 20),
('b@gmail.com', 22),
('c@gmail.com', 25),
('d@gmail.com', 30),
('e@gmail.com', 35);

desc bonus_table;

select* from bonus_table;

create table product_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    order_date DATE DEFAULT (CURRENT_DATE),
    is_delivered BOOLEAN DEFAULT FALSE
);

insert into  product_orders 
(customer_name, product_name, quantity, price, order_date, is_delivered)
values
('Ravi', 'Laptop', 1, 55000.00, '2025-03-01', TRUE),
('Priya', 'Mobile', 2, 20000.00, '2025-03-02', FALSE),
('Kiran', 'Headphones', 3, 1500.00, '2025-03-02', TRUE),
('Anil', 'Keyboard', 2, 1200.00, '2025-03-03', FALSE),
('Neha', 'Monitor', 1, 18000.00, '2025-03-03', TRUE);

insert into  product_orders 
(customer_name, product_name, quantity, price)
values
('Sita', 'Mouse', 4, 800.00);

select * from product_orders;

select customer_name, product_name, price from product_orders;

select *,(quantity * price) as total_amount from product_orders;







