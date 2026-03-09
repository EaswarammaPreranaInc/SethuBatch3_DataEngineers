show databases;
create database studentDB;
use studentDB;
create table student_details(sno int, name varchar(15));
show tables;
insert into student_details values (10,'Ramesh'),(11,'rahul'),(12,'Hyd');
select * from student_details;
create table employees(Emp_id int auto_increment primary key,Emp_name varchar(20),salary decimal (10,2));
insert into employees (emp_name,salary)values ('Ramesh',10000);
select * from employees;
insert into employees values('kedhar',12000);
insert into employees values('pavan',11000);
insert into employees values (100,'Ram',10000);
select * from employees;

create table employee_autoINR ( emp_id int auto_increment primary key,Emp_name varchar(20)) ;
#auto increment = 500;
insert into employee_autoINR (emp_name) values ('Ramesh');
insert into employee_autoINR (emp_name) values ('Sitara');
select * from employee_autoINR;
show tables;
select database ();
create table employee_default_test (user_id int primary key,emp_name varchar(50),city varchar(20) default 'Hyderabad');
insert into employee_default_test values (101,'Rajesh','Bengaluru');
insert into employee_default_test values (102,'Anish');
select * from employee_default_test;
create table user_test(user_id int primary key,email varchar(30) unique,password varchar(50));
insert into user_test values(10,'rajesh11@gmail.com','Rajesh1122@');
insert into user_test values(20,'anish1010@gmail.com','anish000%');
insert into user_test values(30,'rahul1010@gmail.com','Human08081');
show errors;
create table student_age_test(id int primary key,name varchar (50),age int check(age>=18));
insert into student_age_test values(10,'Laxman',20);
insert into student_age_test values(20,'Raghu',16);
show errors;
create table company_employees (emp_id int auto_increment primary key,emp_code int not null unique,
firstname varchar(20) Not null,lastname varchar(20),email varchar(30) unique,age int check (age >=18 and age <=60),salary int default 30000 check (salary >0),
department varchar(20) not null,joining_date date);
insert into company_employees values (1122,'Ranga','reddy','rangareddy@gamail.com',20,'HR',current_date);
insert into company_employees values (2233,'Ranga','naidu','ranganaidu@gamail.com',25,'Accounts',35000,current_date);
insert into company_employees values (3344,'Ranga','rao','rangarao@gamail.com',30,'Management',current_date);
select * from company_employees;
select * from student_details;
select first_name,last_name,salry from company_employees;
select * from company_employees where salary > 30000;
select now();
select current_date();
select current_time();
select user();
create table product_orders (order_id int auto_increment primary key,customer_name varchar(50) not null,product_name varchar(50) not null,
quantity int not null,price decimal not null,order_date date default 'current_date',is_delivered bool default False);
select * from product_orders ;
select customer_name,product_name,price from product_orders;
select * from product_name where total_amount(quantit * price);


