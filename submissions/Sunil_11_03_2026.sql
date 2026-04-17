Create database joinsdb;
Use joinsdb;
select database();

CREATE TABLE employees_demo (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT
);

INSERT INTO employees_demo VALUES
(1,'John',101),
(2,'Mary',102),
(3,'David',103),
(4,'Sophia',104),
(5,'Michael',105),
(6,'Emma',101),
(7,'Daniel',102),
(8,'Olivia',108),
(9,'James',109),
(10,'Isabella',110);


select * from employees_demo;

create table department_demo(
dept_id INT primary KEY,
dept_name VARCHAR(20)
);


INSERT INTO department_demo VALUES
(101,'HR'),
(102,'IT'),
(103,'Finance'),
(104,'Marketing'),
(105,'Sales'),
(106,'Admin'),
(107,'Operations'),
(108,'Support'),
(111,'Research'),
(112,'Training');


create table project_demo(
project_id INT primary KEY,
project_name varchar(50),
dept_id int
);


INSERT INTO project_demo VALUES

(201,'Payroll System',101),
(202,'Website Development',102),
(203,'Budget Analysis',103),
(204,'Ad Campaign',104),
(205,'CRM System',105),
(206,'Helpdesk Tool',108),
(207,'Security Audit',102),
(208,'Market Research',104),
(209,'Data Migration',103),
(210,'Sales Dashboard',105);




CREATE TABLE employees_selfjoin (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    manager_id INT
);



INSERT INTO employees_selfjoin  (emp_id, emp_name, manager_id) VALUES
(1, 'John', NULL),
(2, 'Mary', 1),
(3, 'David', 1),
(4, 'Sophia', 2),
(5, 'James', 2);


Select count(*) from employees_demo;
Select count(*) from departments_demo;
Select count(*) from projects_demo;
Select count(*) from employees_selfjoin ;
