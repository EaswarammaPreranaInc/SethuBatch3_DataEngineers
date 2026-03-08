show databases;
create database studentDb;
use studentDb;
select database();
select current_date(),current_time(),current_user();
create table student_info(id int,name varchar(20));
desc student_info;
insert into student_info values(1,'Ravi');
insert into student_info values(2,'Priya');
insert into student_info (name) values('kiran');
insert into student_info values(3,'Anil');
insert into student_info values(4,'Neha');
select *from student_info;
   
 create table employees(emp_id int auto_increment primary key,emp_ename varchar(100),salary decimal(10,2));  
 insert into employees(emp_ename,salary) values('Sree',25000.00),('Ram',300000.00),('Sai',400000.00);
 insert into employees(emp_id,emp_ename,salary) values(100,'Jai',450000.00);
 select *from employees;
 
 
 create table employee_auto(emp_id int auto_increment primary key,emp_name varchar(50))auto_increment=500;
 insert into employee_auto(emp_name) values('sneha'),('kavya');
 select *from employee_auto;
 
 create table employee_default_test(emp_id int primary key,emp_name varchar(50),city varchar(50) default 'Hyderabad');
 insert into employee_default_test values(1,'Arjun','chennai');
  insert into employee_default_test (emp_id,emp_name)values(2,'Arjun');
  select *from employee_default_test;
  
  Create table users_test(user_id int primary key,email varchar(100) unique,password varchar(50));
  insert into users_test values(1,'user1@gmail.com','pass123'),(2,'user2@gmail.com','pass1234');
  insert into users_test values(3,'user1@gmail.com','pass12345');
  show Errors;
  
  create table syudent_age_test(id int primary key,name varchar(50),age int check(age>=18));
  insert into syudent_age_test values(1,'ranvith',20);
  insert into syudent_age_test values(1,'nivansh',17);
  show errors;
  

select current_date();
select current_time();
select current_user();
select database();  

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

INSERT INTO company_employees
(emp_code, first_name, last_name, email, age, salary, department)
VALUES
('A01', 'Nithya', 'harika', 'niha@gmail.com', 25, 35000, 'IT'),
('A02', 'Priya', 'Sharma', 'priya@gmail.com', 30, 40000, 'HR'),
('A03', 'John', 'David', 'john@gmail.com', 28, 45000, 'Finance');

select *from company_employees;


select *from student_info;
select emp_ename,salary from employees;
select *from employees where salary>30000; 
select *from company_employees where is_active=true;


create table bonus(stuid int primary key,email varchar(100) unique,city varchar(50) default 'Hyderabad',age int check(age>=18));
insert into bonus values(101,'user1@gmail.com','chennai',20),(102,'user2@gmail.com','tamilnadu',23),(103,'user3@gmail.com','delhi',22),(104,'user4@gmail.com','tamilnadu',23),(105,'user5@gmail.com','chennai',23);
desc bonus;
select *from bonus;


create table product_order(order_id int auto_increment primary key,customer_name varchar(100) not null,product_name varchar(100) not null,quantity int not null,
price decimal(10,2) not null,order_date date default (current_date),is_delivered boolean default false); 


insert into product_order(customer_name,product_name,quantity,price,order_date,is_delivered)
values
('Rahul','Laptop',1,55000.00,'2026-03-01',true),
('Anitha','Mobile',2,20000.00,'2026-03-02',false),
('Arun','Headphones',3,1500.00,'2026-03-03',true),
('Priyanka','Keyboard',1,1200.00,'2026-03-04',false),
('Vikram','Mouse',2,800.00,'2026-03-05',true);


insert into product_order(customer_name,product_name,quantity,price)
values ('Sneha','Monitor',1,12000.00);

select * from product_order;

select *, quantity * price as total_amount
from product_order;

