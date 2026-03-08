
# PART 1 : DATABASE OPERATIONS


SHOW DATABASES;

CREATE DATABASE StudentDB;

USE StudentDB;

SELECT DATABASE();

SELECT CURRENT_DATE(), CURRENT_TIME(), CURRENT_USER();



#   PART 2 : TABLE CREATION & INSERT


CREATE TABLE student_info(
id INT,
name VARCHAR(20)
);

DESCRIBE student_info;

INSERT INTO student_info VALUES (1,'Ravi');
INSERT INTO student_info VALUES (2,'Priya');

INSERT INTO student_info(name) VALUES ('Kiran');

INSERT INTO student_info VALUES
(3,'Anil'),
(4,'Neha');

SELECT * FROM student_info;



#   PART 3 : AUTO_INCREMENT & PK


CREATE TABLE employees(
emp_id INT AUTO_INCREMENT PRIMARY KEY,
emp_name VARCHAR(100),
salary DECIMAL(10,2)
);

INSERT INTO employees(emp_name,salary) VALUES
('Ravi',25000),
('Priya',35000),
('Anil',40000);

INSERT INTO employees(emp_id,emp_name,salary)
VALUES (100,'Kiran',50000);

SELECT * FROM employees;



# PART 4 : AUTO_INCREMENT START


CREATE TABLE employee_auto(
emp_id INT AUTO_INCREMENT PRIMARY KEY,
emp_name VARCHAR(50)
) AUTO_INCREMENT = 500;

INSERT INTO employee_auto(emp_name) VALUES
('Ravi'),
('Priya');

SELECT * FROM employee_auto;



#   PART 5 : DEFAULT CONSTRAINT


CREATE TABLE employee_default_test(
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
city VARCHAR(50) DEFAULT 'Hyderabad'
);

INSERT INTO employee_default_test VALUES
(1,'Ravi','Delhi');

INSERT INTO employee_default_test(emp_id,emp_name)
VALUES (2,'Priya');

SELECT * FROM employee_default_test;


#   PART 6 : UNIQUE CONSTRAINT


CREATE TABLE users_test(
user_id INT PRIMARY KEY,
email VARCHAR(100) UNIQUE,
password VARCHAR(50)
);

INSERT INTO users_test VALUES
(1,'ravi@gmail.com','123'),
(2,'priya@gmail.com','456');


INSERT INTO users_test VALUES
(3,'ravii@gmail.com','789');
SHOW ERRORS;



#PART 7 : CHECK CONSTRAINT


CREATE TABLE student_age_test(
id INT PRIMARY KEY,
name VARCHAR(50),
age INT CHECK(age >= 18)
);

INSERT INTO student_age_test VALUES
(1,'Ravi',20);

INSERT INTO student_age_test VALUES
(2,'Anil',21);

SHOW ERRORS;



# PART 8 : MULTIPLE CONSTRAINTS


CREATE TABLE company_employees(
emp_id INT AUTO_INCREMENT PRIMARY KEY,
emp_code VARCHAR(20) NOT NULL UNIQUE,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50),
email VARCHAR(100) UNIQUE,
age INT CHECK(age BETWEEN 18 AND 60),
salary DECIMAL(10,2) DEFAULT 30000 CHECK(salary >=0),
department VARCHAR(50) NOT NULL,
joining_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
is_active BOOLEAN DEFAULT TRUE
);

INSERT INTO company_employees
(emp_code,first_name,last_name,email,age,salary,department)
VALUES
('E101','Ravi','Kumar','ravi@gmail.com',25,35000,'IT'),
('E102','Priya','Sharma','priya@gmail.com',30,40000,'HR'),
('E103','Anil','Reddy','anil@gmail.com',28,32000,'Finance');

SELECT * FROM company_employees;



#   PART 9 : SELECT PRACTICE

SELECT * FROM student_info;

SELECT emp_name,salary FROM employees;

SELECT * FROM employees
WHERE salary > 30000;

SELECT * FROM company_employees
WHERE is_active = TRUE;



#   PART 10 : SYSTEM FUNCTIONS


SELECT CURRENT_DATE();

SELECT CURRENT_TIME();

SELECT CURRENT_USER();

SELECT DATABASE();



#   BONUS QUESTIONS


CREATE TABLE bonus_table(
id INT PRIMARY KEY,
email VARCHAR(100) UNIQUE,
city VARCHAR(50) DEFAULT 'Hyderabad',
age INT CHECK(age >=18)
);

INSERT INTO bonus_table VALUES
(1,'a@gmail.com','Delhi',25),
(2,'b@gmail.com','Hyderabad',22),
(3,'c@gmail.com','Chennai',30),
(4,'d@gmail.com','Mumbai',27),
(5,'e@gmail.com','Pune',35);

DESCRIBE bonus_table;

SELECT * FROM bonus_table;



#   PRODUCT ORDERS TABLE


CREATE TABLE product_orders(
order_id INT PRIMARY KEY AUTO_INCREMENT,
customer_name VARCHAR(100) NOT NULL,
product_name VARCHAR(100) NOT NULL,
quantity INT NOT NULL,
price DECIMAL(10,2) NOT NULL,
order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
is_delivered BOOLEAN DEFAULT FALSE
);

INSERT INTO product_orders
(customer_name,product_name,quantity,price)
VALUES
('Ravi','Laptop',1,50000),
('Priya','Mobile',2,20000),
('Anil','Tablet',1,15000),
('Neha','Headphones',3,2000),
('Kiran','Monitor',1,12000);

INSERT INTO product_orders
(customer_name,product_name,quantity,price)
VALUES
('Rahul','Keyboard',2,1500);

SELECT * FROM product_orders;

SELECT customer_name,product_name,price
FROM product_orders;

SELECT *,
quantity * price AS total_amount
FROM product_orders;