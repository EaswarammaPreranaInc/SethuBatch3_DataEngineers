-- show databases;
-- use studentdb;
-- show tables;
-- create table student_details(id int primary key auto_increment,name varchar(50),phone_number int);
-- desc student_details;
-- insert into student_details values (0,'manav',789); 
-- insert into student_details values ( 9,'vivek',89),(6,'sai',89);


-- Autoincrement table
-- create table employee_auto1 (id int primary key auto_increment,name varchar (200))auto_increment=200;
-- desc employee_auto1;
-- insert into employee_auto1 values (500,'manav);
-- show databases;
-- use studentdb;
-- create table employees_lab(emp_id int primary key auto_increment,emp_name varchar(50) Not NULL,department varchar(50),salary decimal(10,2),age int,joining_date date);
-- desc employees_lab;
-- insert into employees_lab (emp_name,department,salary,age,joining_date) Values('ravi','it',50000,25,'2022-01-10');
-- INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
-- VALUES
-- ('Ravi', 'IT', 50000, 25, '2022-01-10'),
-- ('Amit', 'HR', 45000, 28, '2021-05-15'),
-- ('Neha', 'Finance', 60000, 30, '2020-08-20'),
-- ('Rahul', 'Sales', 42000, 26, '2023-02-12'),
-- ('Priya', 'Marketing', 47000, 27, '2022-07-18'),
-- ('Karan', 'IT', 55000, 29, '2021-11-05'),
-- ('Sneha', 'HR', 43000, 24, '2023-03-10'),
-- ('Vikas', 'Finance', 62000, 32, '2019-09-25'),
-- ('Anjali', 'Sales', 41000, 23, '2022-04-14'),
-- ('Rohit', 'Marketing', 48000, 28, '2021-06-30'),
-- ('Suresh', 'IT', 53000, 31, '2020-12-11'),
-- ('Pooja', 'HR', 44000, 26, '2023-01-19'),
-- ('Deepak', 'Finance', 61000, 33, '2018-10-09'),
-- ('Meena', 'Sales', 40000, 24, '2022-09-21'),
-- ('Arjun', 'Marketing', 49000, 27, '2021-03-17'),
-- ('Nikhil', 'IT', 56000, 29, '2020-05-13'),
-- ('Kavita', 'HR', 45000, 28, '2022-11-07'),
-- ('Manish', 'Finance', 63000, 34, '2019-01-28'),
-- ('Divya', 'Sales', 42000, 25, '2023-06-16'),
-- ('Tarun', 'Marketing', 50000, 30, '2020-07-22');

-- insert into employees_lab (emp_name, department) values('vivek','Finance');

-- insert into employees_lab(emp_name, department, salary, age, joining_date) values(upper('Rashwin'),'IT',round(50000.25,1),23,curdate());
-- select * from employees_lab;
-- select emp_name,salary from employees_lab;

-- select * from employees_lab 
-- where salary>6000;
-- select * from employees_lab
-- where age<=30;

-- select * from employees_lab
-- where department='IT';

-- select * from employees_lab
-- where department='IT' or department='Hr';

-- select * from employees_lab
-- where department='IT' and salary>6000;
-- select distinct(department) from employees_lab;

-- select department, count(*) as dept_employees from employees_lab 
-- group by department;

-- select department, count(*) as dept_employees from employees_lab 
-- group by department
-- having dept_employees>2;
-- select * from employees_lab
-- order by salary desc;

-- select * from employees_lab
-- limit 5;
-- select * from employees_lab
-- limit 5 offset 5;

-- SET SQL_SAFE_UPDATES = 0;
-- UPDATE employees_lab
-- SET salary = 75000
-- WHERE emp_name = 'ravi';

-- update employees_lab
-- set salary=salary+1000;

-- delete from employees_lab
-- where emp_name='ravi';
-- delete from employees_lab;
-- select * from employees_lab;



-- INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
-- VALUES
-- ('Ravi', 'IT', 50000, 25, '2022-01-10'),
-- ('Amit', 'HR', 45000, 28, '2021-05-15'),
-- ('Neha', 'Finance', 60000, 30, '2020-08-20'),
-- ('Rahul', 'Sales', 42000, 26, '2023-02-12'),
-- ('Priya', 'Marketing', 47000, 27, '2022-07-18'),
-- ('Karan', 'IT', 55000, 29, '2021-11-05'),
-- ('Sneha', 'HR', 43000, 24, '2023-03-10'),
-- ('Vikas', 'Finance', 62000, 32, '2019-09-25'),
-- ('Anjali', 'Sales', 41000, 23, '2022-04-14'),
-- ('Rohit', 'Marketing', 48000, 28, '2021-06-30'),
-- ('Suresh', 'IT', 53000, 31, '2020-12-11'),
-- ('Pooja', 'HR', 44000, 26, '2023-01-19'),
-- ('Deepak', 'Finance', 61000, 33, '2018-10-09'),
-- ('Meena', 'Sales', 40000, 24, '2022-09-21'),
-- ('Arjun', 'Marketing', 49000, 27, '2021-03-17'),
-- ('Nikhil', 'IT', 56000, 29, '2020-05-13'),
-- ('Kavita', 'HR', 45000, 28, '2022-11-07'),
-- ('Manish', 'Finance', 63000, 34, '2019-01-28'),
-- ('Divya', 'Sales', 42000, 25, '2023-06-16'),
-- ('Tarun', 'Marketing', 50000, 30, '2020-07-22');

-- replace into employees_lab (emp_id, emp_name, department, salary, age, joining_date)
-- values(1,'sai','IT',45000,40,curdate());

-- insert into employees_lab (emp_id,emp_name, department, salary, age, joining_date) values (1,'sai','IT',45000,40,curdate())
-- on duplicate key update
-- salary=9000;

-- insert into employees_lab (emp_id,emp_name, department, salary, age, joining_date) values (100,'sai','IT',45000,40,curdate())
-- on duplicate key update
-- salary=9000;

-- insert into employees_lab (emp_id,emp_name, department, salary, age, joining_date) values (1,'sai','IT',45000,40,curdate())
-- on duplicate key update
-- salary=9000;

-- INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
-- VALUES (22, 'Rohan', 'Sales', 148000, 28, CURDATE())
-- ON DUPLICATE KEY UPDATE
-- salary = VALUES(salary),
-- age = VALUES(age);

-- select * from employees_lab
-- where salary>50000 and  salary<70000;

-- select * from employees_lab
-- where emp_name like 'r%';

select * from employees_lab where departmentd!= 'Finance';





-- select * from employees_lab;



