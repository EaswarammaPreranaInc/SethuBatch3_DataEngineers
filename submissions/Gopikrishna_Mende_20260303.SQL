1.
show databases;
2.
create database studentdb;
3.
use studentdb;
4.
select database();
5.
select current_time();
select current_date();
select user();
6.
create table student_info(
id int,
name varchar(50)
);

7.
DESC student_info;
8.
insert into student_info values(1,'Gopi');
insert into student_info values(2,'Ram');
9.
INSERT INTO student_info (name) VALUES ('Kiran');
10.
INSERT INTO student_info VALUES
(3, 'Anil'),
(4, 'Neha');
11.
select * from student_info;
-------------------------------------------
12.
create table employees(
  emp_id INT auto_increment primary key,
  emp_name varchar(100),
  salary decimal(10,2)
  );
  13.
  
insert into employees (emp_name, salary) values('Ram', 250000);
insert into employees (emp_name, salary) values('Priya', 30000);
insert into employees (emp_name, salary) values('John', 45000);
14.

insert into employees values(100, 'David', 500000);

15.
select * from employees;

16.
create table employee_auto(
 emp_id int  auto_increment primary key,
 emp_name varchar(50)
 )auto_increment = 500;
 17.
 insert into employeee_auto(emp_name) values ('Ravi');
 insert into employeee_auto(emp_name) values ('Kiran');
 18.
 select * from employee_auto;
 
 19.
 create table employee_default_test (
     emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    city VARCHAR(50) DEFAULT 'Hyderabad'
);
20.
insert into employee_default_test values (1, 'Ram', 'Chennai');
21.
insert into employee_default_test (emp_id, emp_name) values( 2, 'Priya');
 22.
select * from employee_default_test;

23.
create table users_test(
  user_id int primary key,
  email varchar(100) unique,
  password varchar(50)
);

24.
insert into users_test values(1, 'ram@gmail.com', 'abc');
insert into users_test values(2, 'priya@gmail.com', 'dca');

25.
insert into users_test values(3, 'gopi@gmail.com','xyz');

26.
show errors;

27.
create table student_age_test (
  id int primary key,
  name varchar(50),
  age int check(age>=18)
);

28.
insert into student_age_test values(1, 'Ravi', 20);
29.
insert into student_age_test values(2, 'ram', 17);
30.
show errors;
31.
create table  company_employees (
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

32.
INSERT INTO company_employees
(emp_code, first_name, last_name, email, age, salary, department)
VALUES
('E001', 'Ram', 'Kumar', 'ram@gmail.com', 25, 35000, 'IT'),
('E002', 'Priya', 'Sharma', 'priya@gmail.com', 30, 40000, 'HR'),
('E003', 'John', 'David', 'john@gmail.com', 28, 45000, 'Finance');

33.
select * from company_empoyees;

34.
select * from student_info;

35.
select emp_name, salary from employees;

36.
select * from employees
where salary > 30000;
37.
select * from company_employees
where is_active = True;

38.
select current_date();

39.
select current_time();

40.
select user();

41.
select database();

42.
create  table  bonus_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    city VARCHAR(50) DEFAULT 'Khammam'
);

43.
INSERT INTO bonus_table (email, age) VALUES
('a@gmail.com', 20),
('b@gmail.com', 22),
('c@gmail.com', 25),
('d@gmail.com', 30),
('e@gmail.com', 35);

44.
select * from bonus_table;

45.
CREATE TABLE product_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    order_date DATE DEFAULT (CURRENT_DATE),
    is_delivered BOOLEAN DEFAULT FALSE
);

46.
INSERT INTO product_orders 
(customer_name, product_name, quantity, price, order_date, is_delivered)
VALUES
('Ravi', 'Laptop', 1, 55000.00, '2025-03-01', TRUE),
('Ram', 'Mobile', 2, 20000.00, '2025-03-02', FALSE),
('Raj', 'Headphones', 3, 1500.00, '2025-03-02', TRUE),
('Anil', 'Keyboard', 2, 1200.00, '2025-03-03', FALSE),
('Neha', 'Monitor', 1, 18000.00, '2025-03-03', TRUE);


47.
INSERT INTO product_orders 
(customer_name, product_name, quantity, price)
VALUES
('Sita', 'Mouse', 4, 800.00);

48.
SELECT * FROM product_orders;
49.
SELECT customer_name, product_name, price 
FROM product_orders;

50.
SELECT customer_name, product_name, price 
FROM product_orders;