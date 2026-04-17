Q1. Display all available databases.
SHOW DATABASES;
#------------------------------------------
Q2. Create a database named StudentDB.
CREATE DATABASE StudentDB;
#------------------------------------------
Q3. Select the StudentDB database.
USE StudentDB;
#------------------------------------------
Q4. Display the currently selected database.
SELECT DATABASE();
#------------------------------------------
Q5. Display the current date, current time, and current user.
SELECT CURRENT_DATE(), CURRENT_TIME(), CURRENT_USER();
#------------------------------------------
Q6. Create a table named student_info.
CREATE TABLE student_info(
id INT,
name VARCHAR(20)
);
#------------------------------------------
Q7. Display the structure of the student_info table.
DESCRIBE student_info;
#------------------------------------------
Q8. Insert the records (1,'Ravi') and (2,'Priya').
INSERT INTO student_info VALUES
(1,'Ravi'),
(2,'Priya');
#------------------------------------------
Q9. Insert a record with only the name column ('Kiran').
INSERT INTO student_info(name) VALUES ('Kiran');
#------------------------------------------
Q10. Insert multiple records in a single query.
INSERT INTO student_info VALUES
(3,'Anil'),
(4,'Neha');
#------------------------------------------
Q11. Display all records from the table.
SELECT * FROM student_info;
#------------------------------------------
Q12. Create employees table with AUTO_INCREMENT and PRIMARY KEY.
CREATE TABLE employees(
emp_id INT AUTO_INCREMENT PRIMARY KEY,
emp_name VARCHAR(100),
salary DECIMAL(10,2)
);
#------------------------------------------
Q13. Insert 3 records without specifying emp_id.
INSERT INTO employees(emp_name,salary) VALUES
('Ravi',25000),
('Priya',35000),
('Kiran',40000);
#------------------------------------------
Q14. Insert one record with emp_id = 100.
INSERT INTO employees(emp_id,emp_name,salary)
VALUES (100,'Anil',50000);
#------------------------------------------
Q15. Display all employee records.
SELECT * FROM employees;
#------------------------------------------
Q16. Create employee_auto table with AUTO_INCREMENT starting at 500.
CREATE TABLE employee_auto(
emp_id INT AUTO_INCREMENT PRIMARY KEY,
emp_name VARCHAR(50)
) AUTO_INCREMENT=500;
#------------------------------------------
Q17. Insert 2 records.
INSERT INTO employee_auto(emp_name) VALUES
('Ravi'),
('Priya');
#------------------------------------------
Q18. Display all records.
SELECT * FROM employee_auto;
#------------------------------------------
Q19. Create employee_default_test table.
CREATE TABLE employee_default_test(
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
city VARCHAR(50) DEFAULT 'Hyderabad'
);
#------------------------------------------
Q20. Insert one record with city specified.
INSERT INTO employee_default_test VALUES
(1,'Ravi','Delhi');
#------------------------------------------
Q21. Insert one record without specifying city.
INSERT INTO employee_default_test(emp_id,emp_name)
VALUES (2,'Priya');
#------------------------------------------
Q22. Display all records.
SELECT * FROM employee_default_test;
#------------------------------------------
Q23. Create users_test table.
CREATE TABLE users_test(
user_id INT PRIMARY KEY,
email VARCHAR(100) UNIQUE,
password VARCHAR(50)
);
#------------------------------------------
Q24. Insert 2 valid records.
INSERT INTO users_test VALUES
(1,'[ravi@gmail.com](mailto:ravi@gmail.com)','pass123'),
(2,'[priya@gmail.com](mailto:priya@gmail.com)','pass456');
#------------------------------------------
Q25. Try inserting duplicate email.
INSERT INTO users_test VALUES
(3,'[ravi@gmail.com](mailto:ravi@gmail.com)','pass789');
#------------------------------------------
Q26. Display the error.
SHOW ERRORS;
#------------------------------------------
Q27. Create student_age_test table.
CREATE TABLE student_age_test(
id INT PRIMARY KEY,
name VARCHAR(50),
age INT CHECK(age >= 18)
);
#------------------------------------------
Q28. Insert one valid record.
INSERT INTO student_age_test VALUES
(1,'Ravi',20);
#------------------------------------------
Q29. Insert invalid record (age < 18).
INSERT INTO student_age_test VALUES
(2,'Kiran',16);
#------------------------------------------
Q30. Display error.
SHOW ERRORS;
#------------------------------------------
Q31. Create company_employees table with multiple constraints.
CREATE TABLE company_employees(
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
#------------------------------------------
Q32. Insert 3 valid records.
INSERT INTO company_employees(emp_code,first_name,last_name,email,age,salary,department)
VALUES
('E101','Ravi','Kumar','[ravi@company.com](mailto:ravi@company.com)',25,35000,'IT'),
('E102','Priya','Sharma','[priya@company.com](mailto:priya@company.com)',28,42000,'HR'),
('E103','Anil','Reddy','[anil@company.com](mailto:anil@company.com)',30,50000,'Finance');
#------------------------------------------
Q33. Display all records.
SELECT * FROM company_employees;
#------------------------------------------
Q34. Display all records from student_info.
SELECT * FROM student_info;
#------------------------------------------
Q35. Display only employee names and salary.
SELECT emp_name,salary FROM employees;
#------------------------------------------
Q36. Display employees with salary greater than 30000.
SELECT * FROM employees
WHERE salary > 30000;
#------------------------------------------
Q37. Display all active employees.
SELECT * FROM company_employees
WHERE is_active = TRUE;
#------------------------------------------
Q38. Display current date.
SELECT CURRENT_DATE();
#------------------------------------------
Q39. Display current time.
SELECT CURRENT_TIME();
#------------------------------------------
Q40. Display current user.
SELECT CURRENT_USER();
#------------------------------------------
Q41. Display current database name.
SELECT DATABASE();
#------------------------------------------
Q42. Create a table with Primary Key, Unique Key, Default, Check.
CREATE TABLE sample_table(
id INT PRIMARY KEY,
email VARCHAR(100) UNIQUE,
city VARCHAR(50) DEFAULT 'Hyderabad',
age INT CHECK(age >= 18)
);
#------------------------------------------
Q43. Insert 5 records.
INSERT INTO sample_table VALUES
(1,'[a@gmail.com](mailto:a@gmail.com)','Delhi',22),
(2,'[b@gmail.com](mailto:b@gmail.com)','Hyderabad',25),
(3,'[c@gmail.com](mailto:c@gmail.com)','Mumbai',30),
(4,'[d@gmail.com](mailto:d@gmail.com)','Chennai',28),
(5,'[e@gmail.com](mailto:e@gmail.com)','Pune',24);
#------------------------------------------
Q44. Display table structure and records.
DESCRIBE sample_table;
SELECT * FROM sample_table;
#------------------------------------------
Q45. Create product_orders table.
CREATE TABLE product_orders(
order_id INT PRIMARY KEY AUTO_INCREMENT,
customer_name VARCHAR(100) NOT NULL,
product_name VARCHAR(100) NOT NULL,
quantity INT NOT NULL,
price DECIMAL(10,2) NOT NULL,
order_date DATE DEFAULT CURRENT_DATE,
is_delivered BOOLEAN DEFAULT FALSE
);
#------------------------------------------
Q46. Insert 5 records.
INSERT INTO product_orders(customer_name,product_name,quantity,price)
VALUES
('Ravi','Laptop',1,55000),
('Priya','Mobile',2,20000),
('Kiran','Headphones',3,1500),
('Anil','Keyboard',2,1200),
('Neha','Mouse',4,500);
#------------------------------------------
Q47. Insert one record specifying only few columns.
INSERT INTO product_orders(customer_name,product_name,quantity,price)
VALUES ('Rahul','Monitor',1,15000);
#------------------------------------------
Q48. Display all records.
SELECT * FROM product_orders;
#------------------------------------------
Q49. Display only customer_name, product_name, price.
SELECT customer_name,product_name,price
FROM product_orders;
#------------------------------------------
Q50. Display all columns with calculated column total_amount.
SELECT *,
quantity * price AS total_amount
FROM product_orders;
