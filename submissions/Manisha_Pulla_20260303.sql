show databases;
create database studentDB;
use studentDB;
select database();
select now();
select user();

create table student_info(id int, name varchar(20));
desc student_info;
insert into student_info values(1,'Ravi'),(2,'Priya');
insert into student_info(name) values('Kiran');
insert into student_info values(3,'Anil'),(4,'Neha');
select * from student_info;

create table employees(
emp_id int auto_increment primary key,
emp_name varchar(100),
salary decimal(10,2));
insert into employees(emp_name,salary) values
('Jyothi',500000), ('Harika',600000), ('Sarika',800000);
insert into employees(emp_id) values(100);
select * from employees;

create table employee_auto(
emp_id int auto_increment primary key,
emp_name varchar(50))auto_increment=500;
insert into employee_auto (emp_name) values('Manisha'),('vijetha');
select * from employee_auto;

create table employee_default_test(
empl_id int primary key,
emp_name varchar(50),
city varchar(50) default 'Hyderabad');

insert into employee_default_test values(1,'Sai','Warangal');
insert into employee_default_test (empl_id,emp_name)  values(2,'Manoj');
select * from employee_default_test;

create table users_id(
user_id int primary key,
email  varchar(50) unique,
password varchar(50));
insert into users_id values(1,'abcd@gmail.com','Abc12'),
(2,'mani@gmail.com','Mani12');
insert into users_id values(3,'mani@gmail.com','Sai12');#Error Code: 1062. Duplicate entry 'mani@gmail.com' for key 'users_id.email'
select * from users_id;
show errors;

create table student_age_test(
id int primary key,
name varchar(50),
age int check(age>=18));
insert into student_age_test values(1,'Keerthi',20);
insert into student_age_test values(2,'Mani',17);#Error Code: 3819. Check constraint 'student_age_test_chk_1' is violated.
show errors;

create table comp_employees(
emp_id int auto_increment primary key,
emp_code varchar(50) not null unique,
first_name varchar(50) not null,
last_name varchar(50) ,
email varchar(50) unique,
age int check(age>=18 and age<=60),
salary int default 30000 check(salary>=0),
department varchar(100) not null,
joining_date date default (current_date()),
is_active boolean default true);
insert into comp_employees (emp_code,first_name,last_name,email,age,salary,department,is_active)values
('111','Manisha','Pulla','mani@gmail.com',25,25000,'HR Department',true),
('133','Sarika','punna','sarika@gamil.com',30,30000,'Tech department',false),
('122','Nithya','harika','nithya@gmail.com',45,50000,'Technical',true);
select * from comp_employees;

select first_name,last_name,salary from comp_employees;
select * from comp_employees where salary>30000;
select * from comp_employees where is_active=true;

select current_date();
select current_time();
select current_user();
select database();

 create table bonus_table(
 student_id int primary key,
 ph_no bigint unique key,
 country varchar(50) default 'India',
 age int check(age>=18));
 insert into bonus_table(student_id,ph_no,age) values
 (1,1234,18),(2,56789,19),(3,9876,18),(4,54321,20),(5,101010,19);
 desc bonus_table;
 select * from bonus_table;
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
('Ravi', 'Laptop', 1, 55000.00, '2025-03-01', TRUE),
('Priya', 'Mobile', 2, 20000.00, '2025-03-02', FALSE),
('Kiran', 'Headphones', 3, 1500.00, '2025-03-02', TRUE),
('Anil', 'Keyboard', 2, 1200.00, '2025-03-03', FALSE),
('Neha', 'Monitor', 1, 18000.00, '2025-03-03', TRUE);
INSERT INTO product_orders 
(customer_name, product_name, quantity, price)
VALUES
('Sita', 'Mouse', 4, 800.00);

SELECT * FROM product_orders;
SELECT customer_name, product_name, price 
FROM product_orders;
SELECT *,
       (quantity * price) AS total_amount
FROM product_orders;
 










