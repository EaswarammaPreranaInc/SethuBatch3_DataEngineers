#03/03/2026
show databases;
create database studentdb;
use studentdb;
select database();
select now();select user();
create table student_info (
id int,
name varchar(20)
);
insert into student_info values(1,'ravi');
insert into student_info values(1,'Priya');
insert into student_info values(3,'Anil'),(4,'Neha');
select * from student_info;
create table employee(
emp_id int auto_increment primary key,
emp_name varchar(100),
salary decimal(10,2)
);
insert into employee(emp_name,salary) values('ravi',25800);
insert into employee(emp_name,salary) values('krishna',35800);
insert into employee(emp_name,salary) values('ram',45800);
insert into employee(emp_id,emp_name,salary) values(100,'lakshman',25800);
select * from employee;
create table employee_auto(
emp_id int auto_increment primary key,
emp_name varchar(50))auto_increment = 500;
insert into employee_auto(emp_name) values('ravi'),('kiran');
select * from employee_auto;
create table employee_default_test(
emp_id int primary key,
emp_name varchar(50),
city varchar(50) default'hyderabad'
);
insert into employee_default_test values(10,'Rama','Chennai');
insert into employee_default_test(emp_id,emp_name) values (11,'Ramu');		
Select * from employee_default_test;
create table users_test(
user_id int primary key,
email varchar(100) unique,
password varchar(100)
);
insert into users_test values (13,'ramu@gmail.com','RAMA');		
insert into users_test values (14,'rahul@gmail.com','RAHUl');	
show errors;
select * from users_test;
select count(*) users_test;
create table student_age_test(
id int primary key,
name varchar(50),
age int check(age>=18)
);
insert into student_age_test values(32,'Killer',29);
insert into student_age_test values(33,'ghost',09);
show errors;
create table company_employee(
emp_id int auto_increment primary key,
emp_code varchar(10) not null unique,
first_name varchar(50)not null,
last_name varchar(50),
email varchar(100) unique,
age int check(age>=18 and age<=60),
salary decimal(10,2)default 30000 check(salary>=0),
department varchar(50)not null,
joining_date date default(current_date),
is_active boolean default true
);
insert into company_employee(
emp_code,first_name,last_name,email,age,salary,department)
values
('E001','Rama','Rao','ramarao@gmail.com',29,30000,'it'),
('E002','killer','ghost','killergghost@gmail.com',28,44000,'hr'),
('E003','pooja','akkapally','pooja@gmail.com',25,40000,'finance'
);
show errors;
select * from company_employee;
select * from student_info;
select emp_name,salary from employee;
select * from employee
where salary>=30000;
select * from company_employee
where is_active = true;
select current_date();
select current_time();
select user();
select database();
create table bonus_table(
id int auto_increment primary key,
email varchar(100)unique,
age int check(age>=18),
city varchar(50)default 'bangalore'
);
insert into bonus_table(email,age)values
('a@gmail.com',20),
('b@gmail.com',30),
('c@gmail.com',40),
('d@gmail.com',50),
('e@gmail.com',45);
desc bonus_table;
select * from bonus_table;
create table product_orders(
order_id int auto_increment primary key,
customer_name varchar(100)not null,
product_name varchar(100)not null,
quantity int not null,
price decimal(10,2)not null,
order_date date default(current_date),
is_delivered boolean default false
);
insert into product_orders
(customer_name,product_name,quantity,price,order_date,is_delivered)values
('killer','laptop',1,20000.00,'2026-03-08',true),
('subbu','head set',1,30000.00,'2026-03-08',true),
('deepak','phone',1,40000.00,'2026-03-08',false),
('pooja','watch',2,50000.00,'2026-03-08',true),
('dinesh','bike',2,20000.00,'2026-03-08',false);
insert into product_orders
(customer_name,product_name,quantity,price)values
('kappa','laptop',1,20000.00);
select * from product_orders;
select customer_name ,product_name,price
from product_orders;


#05/03/2026
CREATE TABLE employees_demo (
    emp_id INT AUTO_INCREMENT PRIMARY KEY, -- Good practice to have a unique ID
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    age INT,
    joining_date DATE
);

INSERT INTO employees_demo (emp_name, department, salary, age, joining_date) VALUES
('Rahul', 'HR', 30000, 25, '2022-01-10'),
('Sneha', 'HR', 35000, 28, '2021-03-15'),
('Amit', 'IT', 60000, 30, '2020-07-20'),
('Priya', 'IT', 75000, 32, '2019-05-18'),
('Kiran', 'Finance', 50000, 29, '2021-11-25'),
('Anjali', 'Finance', 45000, 27, '2022-02-14'),
('Vikram', 'IT', 80000, 35, '2018-09-10'),
('Meena', 'HR', 32000, 26, '2023-01-05');

#Section A: Basic select and where
-- 1. Display all records from the table.
SELECT * FROM employees_demo;

-- 2. Display only emp_name and salary.
SELECT emp_name, salary FROM employees_demo;

-- 3. Display only emp_name, department, and joining_date.
SELECT emp_name, department, joining_date FROM employees_demo;

-- 4. Display employees who belong to HR department.
SELECT * FROM employees_demo WHERE department = 'HR';

-- 5. Display employees who belong to IT department.
SELECT * FROM employees_demo WHERE department = 'IT';

-- 6. Display employees whose salary is greater than 50000.
SELECT * FROM employees_demo WHERE salary > 50000;

-- 7. Display employees whose salary is less than 40000.
SELECT * FROM employees_demo WHERE salary < 40000;

-- 8. Display employees whose age is greater than 30.
SELECT * FROM employees_demo WHERE age > 30;

-- 9. Display employees whose age is less than or equal to 28.
SELECT * FROM employees_demo WHERE age <= 28;

-- 10. Display employees who joined before 2021-01-01.
SELECT * FROM employees_demo WHERE joining_date < '2021-01-01';

-- 11. Display employees who joined after 2022-01-01.
SELECT * FROM employees_demo WHERE joining_date > '2022-01-01';

-- 12. Display employees from Finance department with salary greater than 45000.
SELECT * FROM employees_demo WHERE department = 'Finance' AND salary > 45000;

-- 13. Display employees whose salary is between 30000 and 60000.
SELECT * FROM employees_demo WHERE salary BETWEEN 30000 AND 60000;

-- 14. Display employees whose age is between 25 and 30.
SELECT * FROM employees_demo WHERE age BETWEEN 25 AND 30;

-- 15. Display employees whose department is not HR.
SELECT * FROM employees_demo WHERE department <> 'HR';

#Section B: Order by and limit
-- 16. Display all employees sorted by salary (Ascending).
SELECT * FROM employees_demo ORDER BY salary ASC;

-- 17. Display all employees sorted by salary (Descending).
SELECT * FROM employees_demo ORDER BY salary DESC;

-- 18. Display employees sorted by age (Ascending).
SELECT * FROM employees_demo ORDER BY age ASC;

-- 19. Display employees sorted by joining date (Newest first).
SELECT * FROM employees_demo ORDER BY joining_date DESC;

-- 20. Display employees sorted by department and salary.
SELECT * FROM employees_demo ORDER BY department, salary;

-- 21. Display top 3 highest paid employees.
SELECT * FROM employees_demo ORDER BY salary DESC LIMIT 3;

-- 22. Display top 2 youngest employees.
SELECT * FROM employees_demo ORDER BY age ASC LIMIT 2;

-- 23. Display first 4 records.
SELECT * FROM employees_demo LIMIT 4;

-- 24. Skip first 3 records and display next 3 records.
SELECT * FROM employees_demo LIMIT 3 OFFSET 3;

-- 25. Display the employee with the highest salary.
SELECT * FROM employees_demo ORDER BY salary DESC LIMIT 1;

#Scetion C: Aggregate Functions
-- 26. Find total number of employees.
SELECT COUNT(*) FROM employees_demo;

-- 27. Find total number of employees in HR department.
SELECT COUNT(*) FROM employees_demo WHERE department = 'HR';

-- 28. Find maximum salary.
SELECT MAX(salary) FROM employees_demo;

-- 29. Find minimum salary.
SELECT MIN(salary) FROM employees_demo;

-- 30. Find average salary.
SELECT AVG(salary) FROM employees_demo;

-- 31. Find total salary paid to all employees.
SELECT SUM(salary) FROM employees_demo;

-- 32. Find average age of employees.
SELECT AVG(age) FROM employees_demo;

-- 33. Find highest age among employees.
SELECT MAX(age) FROM employees_demo;

-- 34. Find lowest age among employees.
SELECT MIN(age) FROM employees_demo;

-- 35. Count number of employees who joined after 2021.
SELECT COUNT(*) FROM employees_demo WHERE joining_date > '2021-12-31';

-- 36. Find total salary of IT department.
SELECT SUM(salary) FROM employees_demo WHERE department = 'IT';

-- 37. Find average salary of Finance department.
SELECT AVG(salary) FROM employees_demo WHERE department = 'Finance';

#Scetion D: Group by and having
-- 38. Display department-wise employee count.
SELECT department, COUNT(*) FROM employees_demo GROUP BY department;

-- 39. Display department-wise average salary.
SELECT department, AVG(salary) FROM employees_demo GROUP BY department;

-- 40. Display department-wise maximum salary.
SELECT department, MAX(salary) FROM employees_demo GROUP BY department;

-- 41. Display department-wise minimum salary.
SELECT department, MIN(salary) FROM employees_demo GROUP BY department;

-- 42. Display department-wise total salary.
SELECT department, SUM(salary) FROM employees_demo GROUP BY department;

-- 43. Display departments having more than 2 employees.
SELECT department FROM employees_demo GROUP BY department HAVING COUNT(*) > 2;

-- 44. Display departments having average salary greater than 40000.
SELECT department FROM employees_demo GROUP BY department HAVING AVG(salary) > 40000;

-- 45. Display departments having total salary greater than 100000.
SELECT department FROM employees_demo GROUP BY department HAVING SUM(salary) > 100000;

-- 46. Display departments where maximum salary is greater than 70000.
SELECT department FROM employees_demo GROUP BY department HAVING MAX(salary) > 70000;

-- 47. Display departments where minimum salary is less than 35000.
SELECT department FROM employees_demo GROUP BY department HAVING MIN(salary) < 35000;

-- 48. Display department-wise average age.
SELECT department, AVG(age) FROM employees_demo GROUP BY department;

-- 49. Display departments having average age greater than 28.
SELECT department FROM employees_demo GROUP BY department HAVING AVG(age) > 28;

-- 50. Display departments having employee count less than 3.
SELECT department FROM employees_demo GROUP BY department HAVING COUNT(*) < 3;
























































