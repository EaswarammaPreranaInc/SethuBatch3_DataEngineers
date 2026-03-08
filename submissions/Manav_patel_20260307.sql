show databases;
create database StudentDB;
use StudentDB;
select database();
select current_date();
select current_time();
select current_user();
create table student_info(
   id INT,
   name VARCHAR(20));
desc student_info;
INSERT INTO student_info VALUES (1,'Ravi');
INSERT INTO student_info VALUES(2,'Priya');
INSERT INTO student_info(name) VALUES ('Kiran');
INSERT INTO student_info VALUES (3,'Anil'),(4,'Neha');
SELECT * FROM student_info;
CREATE TABLE employees(
  emp_id INT AUTO_INCREMENT PRIMARY KEY,
  emp_name VARCHAR(100),
  salary DECIMAL(10,2));
DESC employees;
INSERT INTO employees(emp_name,salary) VALUES ('Anil',25000),('Ram',50000),('Sam',13000);
INSERT INTO employees VALUES (101,'Amar',36000);
SELECT * FROM employees;
CREATE TABLE employee_auto(
emp_id INT PRIMARY KEY AUTO_INCREMENT,
emp_name VARCHAR(50))auto_increment=500;
INSERT INTO employee_auto(emp_name) VALUES ('Ram'),('Sai');
SELECT * FROM employee_auto;
CREATE TABLE employee_default_test(
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
city VARCHAR(50) DEFAULT 'Hyderabad');
INSERT INTO employee_default_test VALUES (1,'Sai','Vizag');
INSERT INTO employee_default_test(emp_id,emp_name) VALUES (2,'Raghu');
SELECT * FROM employee_default_test;
CREATE TABLE users_test(
user_id INT PRIMARY KEY,
email VARCHAR(50) UNIQUE,
password VARCHAR(50));
INSERT INTO users_test VALUES ( 1,'raghu@gmail.com','xyz'),(2,'abc@gmail.com','abc');
INSERT INTO users_test VALUES ( 3,'raghu@gmail.com','root');
SHOW ERRORS;
CREATE TABLE student_age_test(
id INT PRIMARY KEY,
name VARCHAR(50),
age INT CHECK(age>=18));
INSERT INTO student_age_test VALUES ( 1,'Sai',23);
INSERT INTO student_age_test VALUES ( 2,'Simran',15);
SHOW ERRORS;
create table company_employees(
emp_id INT PRIMARY KEY AUTO_INCREMENT,
emp_code INT NOT NULL UNIQUE,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NULL,
email VARCHAR(30) UNIQUE,
age INT CHECK(age>=18 and age<=60),
salary INT DEFAULT 30000 CHECK(salary>=0),
department VARCHAR(10) NOT NULL,
joining_date DATE DEFAULT (CURRENT_DATE),
is_active BOOL DEFAULT True);
INSERT INTO company_employees(emp_code,first_name,last_name,email,age,salary,department) VALUES (101,'Ram','Singh','ram@gmail.com',29,25000,'HR'),(102,'Reena','Sharma','reena@gmail.com',32,44000,'DevOps'),(103,'Ramya','Iyer','iyer@gmail.com',44,52000,'HR');
SELECT * FROM company_employees;
SELECT * FROM student_info;
SELECT first_name,last_name,salary FROM company_employees;
SELECT * FROM company_employees WHERE salary > 30000;
SELECT * FROM company_employees WHERE is_active = True;
select current_date();
select current_time();
select current_user();
select database();
create table temp_emp(
id INT PRIMARY KEY,
name VARCHAR(20) UNIQUE,
salary INT DEFAULT 25000,
age INT CHECK(age>=18));
INSERT INTO temp_emp VALUES(1,'Ram',50000,23);
INSERT INTO temp_emp(id,name,age) VALUES(2,'Raghava',21);
INSERT INTO temp_emp VALUES(3,'Sai chand',54000,35);
INSERT INTO temp_emp VALUES(4,'Varsha',53000,29);
INSERT INTO temp_emp VALUES(5,'Rama Rao',67000,24);
SELECT * FROM temp_emp;

create table product_orders(
order_id INT PRIMARY KEY AUTO_INCREMENT,
customer_name VARCHAR(100) NOT NULL,
product_name VARCHAR(100) NOT NULL,
quantity INT NOT NULL,
price DECIMAL(10,2) NOT NULL,
order_date DATE DEFAULT (CURRENT_DATE),
is_delivered BOOL DEFAULT FALSE);

insert into product_orders(customer_name,product_name,quantity,price) values('Rahul','Laptop',2,150000);
select * from product_orders;
select customer_name,product_name,price from product_orders;
select order_id,customer_name,product_name,quantity,price,order_date,is_delivered,(quantity*price) as total_amount from product_orders;
select * , (quantity * price) as total_amount from product_orders;



