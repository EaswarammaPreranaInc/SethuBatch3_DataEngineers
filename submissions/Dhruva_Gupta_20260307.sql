StduentDB


-- 1) create database studentdb

-- 2) select now()
--     select user()
-- 3) use studentdb
-- 4) CREATE TABLE Students_Info (
--     id INT,
--     name VARCHAR(50)
-- );

-- 5) select * from students_info; or desc students_info

-- 6) INSERT INTO students_info (id, name)
-- VALUES 
-- (1, 'Ravi'),
-- (2, 'Priya');

-- 7)INSERT INTO students_info (name)
-- VALUES ('Kiran');



——————————————————————————————————————

-- 1)create table employees (
--     emp_id INT AUTO_INCREMENT PRIMARY KEY,
--     emp_name VARCHAR(100),
--     salary DECIMAL(10,2)
-- );

-- 2)insert into employees (emp_name, salary)
-- values
-- ('Ravi', 45000.00),
-- ('Priya', 52000.50),
-- ('Kiran', 39000.75);

-- 3) insert into employees (emp_id, emp_name, salary)
-- values (100, 'Anjali', 60000.00);

-- 4) select * from employees

———————————————————————————————————————

1)Create Table employee_auto (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(50)
) AUTO_INCREMENT = 500;

2)Insert Into employee_auto (emp_name)
Values 
('Ravi'),
(‘Priya');

————————————————————————————————————————

-- 1) CREATE TABLE employee_default_test (
--     emp_id INT PRIMARY KEY,
--     emp_name VARCHAR(50),
--     city VARCHAR(50) DEFAULT 'Hyderabad'
-- );

-- 2) INSERT INTO employee_default_test (emp_id, emp_name, city)
-- VALUES (1, 'Ravi', 'Mumbai');


-- Show errors;
——————————————————————————————————————————

Q27)
Create Table student_age_test (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    Check (age >= 18)
);

Q28)
Insert INTO student_age_test
Values (1, 'Rahul', 20);

Q30)
SHOW ERRORS;

Q31)
Create Table company_employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_code VARCHAR(10) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age BETWEEN 18 AND 60),
    salary DECIMAL(10,2) DEFAULT 30000 CHECK (salary >= 0),
    department VARCHAR(50) NOT NULL,
    joining_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE
);

Q32)
Insert into company_employees 
(emp_code, first_name, last_name, email, age, salary, department)
Values
('EMP101', 'Rahul', 'Sharma', 'rahul@company.com', 28, 45000, 'IT'),
('EMP102', 'Priya', 'Verma', 'priya@company.com', 32, 50000, 'HR'),
('EMP103', 'Amit', NULL, 'amit@company.com', 25, 35000, ‘Finance');

Q33)
Select * From company_employees;

Q34)
Select * 
From student_info;

Q35)
Select first_name, last_name, salary
From company_employees;

Q36)
Select *
From company_employees
Where salary > 30000;

Q37)
Select *
From company_employees
Where is_active = 1;

Q38)
Select CURDATE();

Q39)
Select CURTIME();

Q40)
Select CURRENT_USER();

Q41)
Select DATABASE();

Q42)
Create Table employee_bonus (
    emp_id INT PRIMARY KEY,
    emp_code VARCHAR(10) UNIQUE,
    name VARCHAR(50) NOT NULL,
    age INT CHECK (age >= 18),
    salary DECIMAL(10,2) DEFAULT 25000
);

Q43)
Insert onto employee_bonus VALUES
(1,'E101','Rahul',25,30000),
(2,'E102','Priya',28,35000),
(3,'E103','Amit',30,40000),
(4,'E104','Neha',26,28000),
(5,’E105','Karan',35,45000);

Q44)
Desc employee_bonus;

Q45)
Create Table product_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE,
    is_delivered BOOLEAN DEFAULT FALSE
);

Q46)
Insert into product_orders 
(customer_name, product_name, quantity, price)
Values
('Rahul','Laptop',1,65000),
('Priya','Mobile',2,20000),
('Amit','Headphones',3,1500),
('Neha','Keyboard',1,2500),
(‘Karan','Mouse',2,800);

Q47)
Insert into product_orders
(customer_name, product_name, quantity, price)
Values
(‘Rohit','Tablet',1,30000);

Q48)
Select * From product_orders;

Q49)
Select customer_name, product_name, price
From product_orders;

Q50)
Select *,
       quantity * price AS total_amount
From product_orders;
