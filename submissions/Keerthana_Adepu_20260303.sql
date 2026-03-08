##Part 1: Database Operations
#Q1. Display all available databases.
show databases;

#Q2. Create a database named StudentDB.
create database StudentDB;

#Q3. Select the StudentDB database.
use StudentDB;

#Q4. Display the currently selected database.
select database();

#Q5. Display the current date, current time, and current user.
select now();

##Part 2: Table Creation and Basic INSERT
#Q6. Create a table named student_info with the following columns:
#id → Integer
#name → VARCHAR(20)

create table student_info(
	id int,
    name varchar(50)
);

#Q7. Display the structure of the student_info table.
describe student_info;

#Q8. Insert the following records:
#(1, 'Ravi')
#(2, 'Priya')
insert into student_info values(1, 'Ravi');
insert into student_info values(2, 'Priya');

#Q9. Insert a record with only the name column ('Kiran').
insert into student_info(name) values('Kiran');

#Q10. Insert multiple records in a single query:
#(3, 'Anil')
#(4, 'Neha')
insert into student_info values
(3, 'Anil'),
(4, 'Neha');

#Q11. Display all records from the table.
select * from student_info;

##Part 3: AUTO_INCREMENT and PRIMARY KEY
#Q12. Create a table named employees with:
#emp_id → AUTO_INCREMENT, PRIMARY KEY
#emp_name → VARCHAR(100)
#salary → DECIMAL(10,2)
create table employees(
	emp_id int auto_increment primary key,
    emp_name varchar(100),
    salary decimal(10, 2)
);

#Q13. Insert 3 records without specifying emp_id.
insert into employees (emp_name, salary) values
('Ravi', 25000),
('Priya', 30000),
('Kiran', 35000);

#Q14. Insert one record with emp_id = 100.
insert into employees values (100, 'Anil', 40000);

#Q15. Display all employee records.
select * from employees;

##Part 4: AUTO_INCREMENT with Custom Starting Value
#Q16. Create a table named employee_auto with:
#emp_id → AUTO_INCREMENT, PRIMARY KEY
#emp_name → VARCHAR(50)
#Set AUTO_INCREMENT starting value to 500.
create table employee_auto (
    emp_id int auto_increment primary key,
    emp_name varchar(50)
) auto_increment = 500;

#Q17. Insert 2 records.
insert into employee_auto (emp_name) values
('Ravi'),
('Priya');

#Q18. Display all records.
select * from employee_auto;

##Part 5: DEFAULT Constraint
#Q19. Create a table named employee_default_test with:
#emp_id → PRIMARY KEY
#emp_name → VARCHAR(50)
#city → VARCHAR(50), default value should be 'Hyderabad'
create table employee_default_test (
    emp_id int primary key,
    emp_name varchar(50),
    city varchar(50) default 'Hyderabad'
);

#Q20. Insert one record with city specified.
insert into employee_default_test values
(1,'Ravi','Delhi');

#Q21. Insert one record without specifying city.
insert into employee_default_test(emp_id,emp_name)
values(2,'Priya');

#Q22. Display all records.
select * from employee_default_test;

##Part 6: UNIQUE Constraint
#Q23. Create a table named users_test with:
#user_id → PRIMARY KEY
#email → UNIQUE
#password → VARCHAR(50)
create table users_test(
user_id int primary key,
email varchar(100) unique,
password varchar(50)
);

#Q24. Insert 2 valid records.
insert into users_test
values
(1,'ravi@gmail.com','hi@123'),
(2,'priya@gmail.com','bye@789');

#Q25. Try inserting a duplicate email and observe the error.
insert into users_test
values
(3,'ravi@gmail.com','dup@456');

#Q26. Use SHOW ERRORS; to display the error.
show errors;

##Part 7: CHECK Constraint
#Q27. Create a table named student_age_test with:
#id → PRIMARY KEY
#name → VARCHAR(50)
#age → must be greater than or equal to 18
create table student_age_test(
id int primary key,
name varchar(50),
age int check(age >= 18)
);

#Q28. Insert one valid record.
insert into student_age_test
values(1,'Ravi',20);

#Q29. Try inserting one invalid record (age less than 18).
insert into student_age_test
values(2,'Anil',15);

#Q30. Display the error using SHOW ERRORS.
show errors;

##Part 8: Table with Multiple Constraints
#Q31. Create a table named company_employees with the following constraints:
#emp_id → AUTO_INCREMENT, PRIMARY KEY
#emp_code → NOT NULL, UNIQUE
#first_name → NOT NULL
#last_name → NULL allowed
#email → UNIQUE
#age → between 18 and 60
#salary → DEFAULT 30000, must be >= 0
#department → NOT NULL
#joining_date → DEFAULT CURRENT_DATE
#is_active → DEFAULT TRUE
create table company_employees(
emp_id int auto_increment primary key,
emp_code varchar(20) not null unique,
first_name varchar(50) not null,
last_name varchar(50),
email varchar(100) unique,
age int check(age between 18 and 60),
salary decimal(10,2) default 30000 check(salary >= 0),
department varchar(50) not null,
joining_date date default now(),
is_active boolean default true
);

#Q32. Insert 3 valid employee records.
insert into company_employees
(emp_code,first_name,last_name,email,age,salary,department)
values
('E101','Ravi','Kumar','ravi@gmail.com',25,35000,'HR'),
('E102','Priya','Sharma','priya@gmail.com',28,40000,'IT'),
('E103','Anil','Reddy','anil@gmail.com',30,45000,'Finance');

#Q33. Display all records.
select * from company_employees;

##Part 9: SELECT Queries Practice
#Q34. Display all records from student_info.
select * from student_info;

#Q35. Display only employee names and salary.
select emp_name, salary
from employees;

#Q36. Display employees with salary greater than 30000.
select *
from employees
where salary > 30000;

#Q37. Display all active employees.
select *
from company_employees
where is_active = true;

##Part 10: System Functions
#Q38. Display the current date.
select current_date();

#Q39. Display the current time.
select current_time();

#Q40. Display the current user.
select current_user();

#Q41. Display current database name.
select database();

##Bonus Questions
#Q42. Create a table with:
#Primary Key
#Unique Key
#Default value
#Check constraint
create table bonus_table(
id int primary key,
email varchar(100) unique,
city varchar(50) default 'Hyderabad',
age int check(age >= 18)
);

#Q43. Insert minimum 5 records.
insert into bonus_table
values
(1,'siri@gmail.com','Delhi',20),
(2,'jesh@gmail.com','Mumbai',25),
(3,'fiya@gmail.com','Hyderabad',22),
(4,'shu@gmail.com','Chennai',30),
(5,'supriya@gmail.com','Pune',28);

#Q44. Display table structure and records.
describe bonus_table;

select * from bonus_table;

##Create Table(With all important Data Types)
#Q45. Create a table named product_orders with the following columns:
#• order_id → INT (PRIMARY KEY, AUTO_INCREMENT)
#• customer_name → VARCHAR(100) (NOT NULL)
#• product_name → VARCHAR(100) (NOT NULL)
#• quantity → INT (NOT NULL)
#• price → DECIMAL(10,2) (NOT NULL)
#• order_date → DATE (DEFAULT CURRENT_DATE)
#• is_delivered → BOOLEAN (DEFAULT FALSE)
create table product_orders(
order_id int auto_increment primary key,
customer_name varchar(100) not null,
product_name varchar(100) not null,
quantity int not null,
price decimal(10,2) not null,
order_date date default now(),
is_delivered boolean default false
);

#Q46. Insert 5 records into the product_orders table.
insert into product_orders
(customer_name,product_name,quantity,price)
values
('Ravi', 'Laptop' , 1, 60000),
('Priya', 'Mobile', 2, 20000),
('Anil', 'Tablet', 1, 15000),
('Neha', 'Headphones', 3, 2000),
('Kiran', 'Keyboard', 2, 1500);

#Q47. Insert one record by specifying only the following columns:
#• customer_name
#• product_name
#• quantity
#• price
insert into product_orders
(customer_name,product_name,quantity,price)
values
('Rahul', 'Monitor', 1, 12000);

#Q48. Display all records from the product_orders table.
select * from product_orders;

#Q49. Display only the following columns:
#• customer_name
#• product_name
#• price
select customer_name, product_name, price
from product_orders;

#Q50. Display all columns along with a calculated column:
#• total_amount → quantity * price
select *,
(quantity * price) as total_amount
from product_orders;