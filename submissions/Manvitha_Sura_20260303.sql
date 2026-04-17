show databases;
create database StudentDB;
use StudentDB;
select database();
select current_date();
select current_time();
select user();
create table student_info(
id int,
name varchar(20));
desc student_info;
insert into student_info values(1,'Ravi'),(2,'Priya');
insert into student_info(name) values ('Kiran');
insert into student_info values(3,'Anil'),(4,'Neha');
select * from student_info;
create table employees(
emp_id  int PRIMARY KEY AUTO_INCREMENT,
emp_name VARCHAR(100),
salary DECIMAL(10,2));
insert into employees(emp_name,salary) values('Ram',20000),('Sam',40000);
insert into employees(emp_id) values (100);
select * from employees;
create table employee_auto(
emp_id int PRIMARY KEY AUTO_INCREMENT,
emp_name VARCHAR(50))AUTO_INCREMENT=500;
insert into employee_auto(emp_name) values ('RAMA'),('SITA');
select * from employee_auto;
create table employee_default_test(
emp_id  VARCHAR(50) PRIMARY KEY,
emp_name  VARCHAR(50),
city VARCHAR(50) default 'Hyderabad');
insert into employee_default_test(emp_id,emp_name) values (1,'Hari'),(2,'Ravi');
insert into employee_default_test values (5,'siri','hyderabad'),(10,'latha','bangalore');
select * from employee_default_test;
create table users_test(
user_id int PRIMARY KEY,
email varchar(50) UNIQUE,
password VARCHAR(50));
insert into users_test values(1,'abcd@gmail.com','hello@123'),(2,'efgh@gmail.com','hi@123');
insert into users_test values(3,'abcd@gmail.com','hello@123');
show errors;
create table student_age_test(
id int primary key,
name varchar(50),
age int check (age>=18));
insert into student_age_test values (1,'ravi',20);
insert into student_age_test values (2,'ravi',15);
show errors;
create table company_employees(
emp_id int PRIMARY KEY AUTO_INCREMENT ,
emp_code int NOT NULL UNIQUE,
first_name varchar(50) NOT NULL,
last_name varchar(50) ,
email varchar(50) UNIQUE,
age int check(age>=18 and age<=60),
salary decimal(10,2) DEFAULT 30000 check(salary>=0),
department varchar(50)NOT NULL,
joining_date date DEFAULT (current_date()),
is_active bool DEFAULT TRUE);
insert into company_employees(emp_id,emp_code, first_name, last_name, email, age, salary, department,is_active) values
(1,345,'ravi','kiran','abc@gmail.com',25,200000,'it',false),
(2,350,'raju','raghav','acf@gmail.com',28,450000,'finance',false),
(5,365,'ramu','kumar','bcd@gmail.com',45,250000,'hr',true);
SELECT * FROM company_employees;
SELECT * FROM student_info;
SELECT emp_name, salary FROM employees;
SELECT * FROM employees
WHERE salary > 30000;
SELECT * FROM company_employees
WHERE is_active = TRUE;
CREATE TABLE bonus_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(50) UNIQUE,
    age INT CHECK (age >= 18),
    city VARCHAR(50) DEFAULT 'Hyderabad'
);
INSERT INTO bonus_table (email, age,city) VALUES
('abc@gmail.com', 25,'Bangalore'),
('bcd@gmail.com', 27,'Warangal'),
('fg@gmail.com', 56,'Delhi'),
('hi@gmail.com', 45,'Mumbai'),
('hge@gmail.com', 34,'Chennai');
DESC bonus_table;
SELECT * FROM bonus_table;
CREATE TABLE product_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    order_date DATE DEFAULT (CURRENT_DATE),
    is_delivered BOOLEAN DEFAULT FALSE
);
INSERT INTO product_orders 
(customer_name, product_name, quantity, price, order_date, is_delivered)
VALUES
('priya', 'dress', 5, 550, '2025-02-17', TRUE),
('ramu', 'accessories', 3, 200, '2025-03-02', FALSE),
('Kamal', 'footwear', 3, 400, '2025-01-20', TRUE),
('Arun', 'mobile', 1, 20000, '2025-02-25', FALSE),
('Nitin', 'ring', 1, 150, '2025-12-18', TRUE);
INSERT INTO product_orders (customer_name, product_name, quantity, price)
VALUES ('Ravi', 'chain', 2, 300);
SELECT * FROM product_orders;
SELECT customer_name, product_name, price 
FROM product_orders;
SELECT *,(quantity * price) AS total_amount
FROM product_orders;


