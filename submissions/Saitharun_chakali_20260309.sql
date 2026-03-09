SQL Assignment – Questions with Queries

Q1. Display all available databases.
Query:
SHOW DATABASES;


Q2. Create a database named StudentDB.
Query:
CREATE DATABASE StudentDB;


Q3. Select the StudentDB database.
Query:
USE StudentDB;


Q4. Display the currently selected database.
Query:
SELECT
    DATABASE();


Q5. Display the current date, current time, and current user.
Query:
SELECT
    CURRENT_DATE(),
    CURRENT_TIME(),
    CURRENT_USER();


Q6. Create a table named student_info with columns id and name.
Query:
CREATE TABLE student_info
(
    id INT,
    name VARCHAR(20)
);


Q7. Display the structure of the student_info table.
Query:
DESCRIBE student_info;


Q8. Insert the records (1,'Ravi') and (2,'Priya').
Query:
INSERT INTO student_info
VALUES
    (1,'Ravi'),
    (2,'Priya');


Q9. Insert a record with only the name column 'Kiran'.
Query:
INSERT INTO student_info(name)
VALUES ('Kiran');


Q10. Insert multiple records (3,'Anil') and (4,'Neha').
Query:
INSERT INTO student_info
VALUES
    (3,'Anil'),
    (4,'Neha');


Q11. Display all records from student_info.
Query:
SELECT * FROM student_info;


Q12. Create table employees.
Query:
CREATE TABLE employees
(
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(100),
    salary DECIMAL(10,2)
);


Q13. Insert 3 records without specifying emp_id.
Query:
INSERT INTO employees(emp_name, salary)
VALUES
    ('Ravi',25000),
    ('Priya',32000),
    ('Anil',28000);


Q14. Insert one record with emp_id = 100.
Query:
INSERT INTO employees VALUES (100,'Neha',45000);


Q15. Display all employee records.
Query:
SELECT * FROM employees;


Q16. Create table employee_auto with AUTO_INCREMENT starting from 500.
Query:
CREATE TABLE employee_auto
(
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(50)
) AUTO_INCREMENT = 500;


Q17. Insert two records.
Query:
INSERT INTO employee_auto(emp_name)
VALUES
    ('Ravi'),
    ('Priya');


Q18. Display all records.
Query:
SELECT  * FROM employee_auto;


Q19. Create table employee_default_test with default city 'Hyderabad'.
Query:
CREATE TABLE employee_default_test
(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    city VARCHAR(50) DEFAULT 'Hyderabad'
);


Q20. Insert a record with city specified.
Query:
INSERT INTO employee_default_test VALUES  (1,'Ravi','Delhi');


Q21. Insert a record without specifying city.
Query:
INSERT INTO employee_default_test(emp_id, emp_name)
VALUES (2,'Priya');


Q22. Display all records.
Query:
SELECT * FROM employee_default_test;


Q23. Create table users_test with UNIQUE email.
Query:
CREATE TABLE users_test
(
    user_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(50)
);



Q24. Insert two valid records.
Query:
INSERT INTO users_test
VALUES
    (1,'ravi@gmail.com','1234'),
    (2,'priya@gmail.com','abcd');


Q25. Insert duplicate email.
Query:
INSERT INTO users_test
VALUES
    (3,'ravi@gmail.com','5678');


Q26. Display the error.
Query:
SHOW ERRORS;


Q27. Create table student_age_test with age >= 18 constraint.
Query:
CREATE TABLE student_age_test
(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT CHECK(age >= 18)
);


Q28. Insert valid record.
Query:
INSERT INTO student_age_test
VALUES (1,'Ravi',20);


Q29. Insert invalid record.
Query:
INSERT INTO student_age_test
VALUES (2,'Priya',15);


Q30. Display error.
Query:
SHOW ERRORS;


Q31. Create table company_employees with multiple constraints.
Query:
CREATE TABLE company_employees
(
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_code VARCHAR(20) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    age INT CHECK(age BETWEEN 18 AND 60),
    salary DECIMAL(10,2) DEFAULT 30000 CHECK(salary >= 0),
    department VARCHAR(50) NOT NULL,
    joining_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE
);


Q32. Insert three valid employee records.
Query:
INSERT INTO company_employees (emp_code, first_name, last_name, email, age, salary, department)
VALUES
    ('EMP101','Ravi','Kumar','ravi@gmail.com',25,35000,'IT'),
    ('EMP102','Priya','Sharma','priya@gmail.com',30,40000,'HR'),
    ('EMP103','Anil','Reddy','anil@gmail.com',28,30000,'Finance');


Q33. Display all records.
Query:
SELECT * FROM company_employees;


Q34. Display all records from student_info.
Query:
SELECT * FROM student_info;


Q35. Display only employee names and salary.
Query:
SELECT emp_name, salary
FROM employees;


Q36. Display employees with salary greater than 30000.
Query:
SELECT * FROM employees
WHERE salary > 30000;


Q37. Display all active employees.
Query:
SELECT * FROM company_employees
WHERE is_active = TRUE;


Q38. Display current date.
Query:
SELECT CURRENT_DATE();


Q39. Display current time.
Query:
SELECT CURRENT_TIME();


Q40. Display current user.
Query:
SELECT CURRENT_USER();


Q41. Display current database name.
Query:
SELECT DATABASE();


Q42. Create table with Primary Key, Unique, Default, Check constraint.
Query:
CREATE TABLE bonus_table
(
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    salary INT DEFAULT 20000,
    age INT CHECK(age >= 18)
);


Q43. Insert five records.
Query:
INSERT INTO bonus_table
VALUES
    (1,'a@gmail.com',25000,25),
    (2,'b@gmail.com',20000,22),
    (3,'c@gmail.com',30000,30),
    (4,'d@gmail.com',20000,28),
    (5,'e@gmail.com',35000,35);


Q44. Display structure and records.
Query:
DESCRIBE bonus_table;

SELECT * FROM bonus_table;


Q45. Create table product_orders.
Query:
CREATE TABLE product_orders
(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE,
    is_delivered BOOLEAN DEFAULT FALSE
);


Q46. Insert five records.
Query:
INSERT INTO product_orders (customer_name, product_name, quantity, price)
VALUES
    ('Ravi','Laptop',1,55000),
    ('Priya','Mobile',2,20000),
    ('Anil','Headphones',3,1500),
    ('Neha','Keyboard',1,1200),
    ('Kiran','Mouse',2,700);


Q47. Insert one record specifying selected columns.
Query:
INSERT INTO product_orders (customer_name, product_name, quantity, price)
VALUES ('Arjun','Monitor',1,12000);


Q48. Display all records.
Query:
SELECT * FROM product_orders;


Q49. Display customer_name, product_name and price.
Query:
SELECT customer_name, product_name, price
FROM product_orders;


Q50. Display calculated column total_amount.
Query:
SELECT *, quantity * price AS total_amount
FROM product_orders;