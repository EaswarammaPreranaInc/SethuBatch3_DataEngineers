-- SQL Assignment – Create Database, Tables, INSERT, and SELECT

-- Part 1: Database Operations

-- Q1. Display all available databases.
SHOW DATABASES;

-- Q2. Create a database named StudentDB.
CREATE DATABASE StudentDB;

-- Q3. Select the StudentDB database.
USE StudentDB;

-- Q4. Display the currently selected database.
SELECT DATABASE();

-- Q5. Display the current date, current time, and current user.
SELECT CURRENT_DATE();
SELECT CURRENT_TIME();
SELECT USER();

-- Part 2: Table Creation and Basic INSERT

-- Q6. Create a table named student_info with columns id and name.
CREATE TABLE student_info (
    id INT,
    name VARCHAR(20)
);

-- Q7. Display the structure of the student_info table.
DESC student_info;

-- Q8. Insert records (1,'Ravi') and (2,'Priya').
INSERT INTO student_info VALUES (1,'Ravi');
INSERT INTO student_info VALUES (2,'Priya');

-- Q9. Insert a record with only the name column.
INSERT INTO student_info (name) VALUES ('Kiran');

-- Q10. Insert multiple records in a single query.
INSERT INTO student_info VALUES
(3,'Anil'),
(4,'Neha');

-- Q11. Display all records from the table.
SELECT * FROM student_info;

-- Part 3: AUTO_INCREMENT and PRIMARY KEY

-- Q12. Create a table named employees.
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(100),
    salary DECIMAL(10,2)
);

-- Q13. Insert 3 records without specifying emp_id.
INSERT INTO employees (emp_name, salary) VALUES ('Ram',25000);
INSERT INTO employees (emp_name, salary) VALUES ('Priya',30000);
INSERT INTO employees (emp_name, salary) VALUES ('John',45000);

-- Q14. Insert one record with emp_id = 100.
INSERT INTO employees VALUES (100,'David',50000);

-- Q15. Display all employee records.
SELECT * FROM employees;

-- Part 4: AUTO_INCREMENT with Custom Starting Value

-- Q16. Create a table employee_auto starting from 500.
CREATE TABLE employee_auto (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(50)
) AUTO_INCREMENT = 500;

-- Q17. Insert 2 records.
INSERT INTO employee_auto (emp_name) VALUES ('Ravi');
INSERT INTO employee_auto (emp_name) VALUES ('Kiran');

-- Q18. Display all records.
SELECT * FROM employee_auto;

-- Part 5: DEFAULT Constraint

-- Q19. Create table employee_default_test.
CREATE TABLE employee_default_test (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    city VARCHAR(50) DEFAULT 'Hyderabad'
);

-- Q20. Insert record with city specified.
INSERT INTO employee_default_test VALUES (1,'Ram','Chennai');

-- Q21. Insert record without city.
INSERT INTO employee_default_test (emp_id,emp_name)
VALUES (2,'Priya');

-- Q22. Display all records.
SELECT * FROM employee_default_test;

-- Part 6: UNIQUE Constraint

-- Q23. Create users_test table.
CREATE TABLE users_test (
    user_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(50)
);

-- Q24. Insert valid records.
INSERT INTO users_test VALUES (1,'ram@gmail.com','abc');
INSERT INTO users_test VALUES (2,'priya@gmail.com','xyz');

-- Q25. Try inserting duplicate email.
INSERT INTO users_test VALUES (3,'ram@gmail.com','test');

-- Q26. Show error.
SHOW ERRORS;

-- Part 7: CHECK Constraint

-- Q27. Create student_age_test table.
CREATE TABLE student_age_test (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT CHECK(age >= 18)
);

-- Q28. Insert valid record.
INSERT INTO student_age_test VALUES (1,'Ravi',20);

-- Q29. Insert invalid record.
INSERT INTO student_age_test VALUES (2,'Kiran',15);

-- Q30. Show error.
SHOW ERRORS;

-- Part 8: Table with Multiple Constraints

-- Q31. Create company_employees table.
CREATE TABLE company_employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_code VARCHAR(10) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    age INT CHECK(age >= 18 AND age <= 60),
    salary DECIMAL(10,2) DEFAULT 30000 CHECK(salary >= 0),
    department VARCHAR(50) NOT NULL,
    joining_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE
);

-- Q32. Insert employee records.
INSERT INTO company_employees
(emp_code, first_name, last_name, email, age, salary, department)
VALUES
('E001','Ram','Kumar','ram@gmail.com',25,35000,'IT'),
('E002','Priya','Sharma','priya@gmail.com',30,40000,'HR'),
('E003','John','David','john@gmail.com',28,45000,'Finance');

-- Q33. Display all records.
SELECT * FROM company_employees;

-- Part 9: SELECT Queries Practice

-- Q34. Display all records from student_info.
SELECT * FROM student_info;

-- Q35. Display employee names and salary.
SELECT emp_name, salary FROM employees;

-- Q36. Display employees with salary > 30000.
SELECT * FROM employees WHERE salary > 30000;

-- Q37. Display active employees.
SELECT * FROM company_employees WHERE is_active = TRUE;

-- Part 10: System Functions

-- Q38. Display current date.
SELECT CURRENT_DATE();

-- Q39. Display current time.
SELECT CURRENT_TIME();

-- Q40. Display current user.
SELECT USER();

-- Q41. Display current database.
SELECT DATABASE();

-- Bonus

-- Q42. Create bonus_table.
CREATE TABLE bonus_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    age INT CHECK(age >= 18),
    city VARCHAR(50) DEFAULT 'Bangalore'
);

-- Q43. Insert records.
INSERT INTO bonus_table (email,age) VALUES
('a@gmail.com',20),
('b@gmail.com',22),
('c@gmail.com',25),
('d@gmail.com',30),
('e@gmail.com',35);

-- Q44. Display table structure and data.
DESC bonus_table;
SELECT * FROM bonus_table;

-- Q45. Create product_orders table.
CREATE TABLE product_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE,
    is_delivered BOOLEAN DEFAULT FALSE
);

-- Q46. Insert records.
INSERT INTO product_orders
(customer_name,product_name,quantity,price,order_date,is_delivered)
VALUES
('Ravi','Laptop',1,55000.00,'2025-03-01',TRUE),
('Priya','Mobile',2,20000.00,'2025-03-02',FALSE),
('Kiran','Headphones',3,1500.00,'2025-03-02',TRUE),
('Anil','Keyboard',2,1200.00,'2025-03-03',FALSE),
('Neha','Monitor',1,18000.00,'2025-03-03',TRUE);

-- Q47. Insert record specifying selected columns.
INSERT INTO product_orders
(customer_name,product_name,quantity,price)
VALUES
('Sita','Mouse',4,800.00);

-- Q48. Display all records.
SELECT * FROM product_orders;

-- Q49. Display selected columns.
SELECT customer_name, product_name, price FROM product_orders;

-- Q50. Display calculated column total_amount.
SELECT *, (quantity * price) AS total_amount
FROM product_orders;