SHOW DATABASES;
CREATE DATABASE Student;
USE Student;
SELECT DATABASE();
SELECT CURRENT_DATE();
SELECT CURRENT_TIME();
SELECT USER();
CREATE TABLE student_info (
    id INT,
    name VARCHAR(20)
);
DESC student_info;
INSERT INTO student_info VALUES (1, 'Manisha');
INSERT INTO student_info VALUES (2, 'Surya');
INSERT INTO student_info (name) VALUES ('Bunny');
INSERT INTO student_info VALUES
(3, 'Raja'),
(4, 'Suma');
SELECT * FROM student_info;
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(100),
    salary DECIMAL(10,2)
);
INSERT INTO employees (emp_name, salary) VALUES ('Abhishek', 25000);
INSERT INTO employees (emp_name, salary) VALUES ('Nithish', 30000);
INSERT INTO employees (emp_name, salary) VALUES ('kohli', 45000);
INSERT INTO employees VALUES (100, 'Nisha', 50000);
select * from employees;
CREATE TABLE employee_auto (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(50)
) AUTO_INCREMENT = 500;
INSERT INTO employee_auto (emp_name) VALUES ('Dube');
INSERT INTO employee_auto (emp_name) VALUES ('pat cummins');
SELECT * FROM employee_auto;
CREATE TABLE employee_default_test (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    city VARCHAR(50) DEFAULT 'Hyderabad'
);
INSERT INTO employee_default_test VALUES (1, 'Rohit', 'Andhra');
INSERT INTO employee_default_test (emp_id, emp_name)
VALUES (2, 'Kavya');
SELECT * FROM employee_default_test;
CREATE TABLE users_test (
    user_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(50)
);
INSERT INTO users_test VALUES (1, 'raju@gmail.com', 'abc');
INSERT INTO users_test VALUES (2, 'kavya@gmail.com', 'xyz');
INSERT INTO users_test VALUES (3, 'nisha@gmail.com', 'test');
SHOW ERRORS;
CREATE TABLE student_age_test (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT CHECK (age >= 18)
);
INSERT INTO student_age_test VALUES (1, 'Manisha', 20);
INSERT INTO student_age_test VALUES (2, 'Surya', 25);
SHOW ERRORS;
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
('E001', 'Raju', 'Kumar', 'raju@gmail.com', 25, 35000, 'IT'),
('E002', 'Isha', 'Sharma', 'Isha@gmail.com', 30, 40000, 'HR'),
('E003', 'Surya', 'Prakash', 'Surya@gmail.com', 28, 45000, 'Finance');
SELECT * FROM company_employees;
SELECT * FROM student_info;
SELECT emp_name, salary FROM employees;
SELECT * FROM employees
WHERE salary > 30000;
SELECT * FROM company_employees
WHERE is_active = TRUE;
SELECT CURRENT_DATE();
SELECT CURRENT_TIME();
SELECT USER();
SELECT DATABASE();
CREATE TABLE bonus_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    city VARCHAR(50) DEFAULT 'Bangalore'
);
INSERT INTO bonus_table (email, age) VALUES
('nisha@gmail.com', 20),
('isha@gmail.com', 22),
('prakash@gmail.com', 25),
('abhishek@gmail.com', 30),
('dube@gmail.com', 35);
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


































