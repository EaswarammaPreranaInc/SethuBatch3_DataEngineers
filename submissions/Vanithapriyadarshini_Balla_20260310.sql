create database demojoins;
use demojoins;
create table employees_demo(
emp_id int ,emp_name varchar(50),dept_id int);

INSERT INTO employees_demo VALUES
(1,'John',101),
(2,'Mary',102),
(3,'David',103),
(4,'Sophia',104),
(5,'Michael',105),
(6,'Emma',101),
(7,'Daniel',102),
(8,'Olivia',108),
(9,'James',109);
show errors;


create table department_demo(
dept_id int,dept_name varchar(50));

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


create table employees_selfjoin(
emp_id int, emp_name varchar(50),manager_id int);

select emp_name,dept_name from employees_demo e join department_demo d on e.dept_id = d.dept_id;

select emp_name,dept_name from employees_demo e left join department_demo d on e.dept_id=d.dept_id;

select emp_name,dept_name from employees_demo e right join department_demo d on e.dept_id=d.dept_id;

select emp_name,dept_id from employees_demo e  union select dept_id,dept_name from department_demo d;
select emp_name,dept_name from employees_demo join department_demo on dept_name='IT';
select emp_name,dept_name from employees_demo e join department_demo d on not (e.dept_id=d.dept_id);
