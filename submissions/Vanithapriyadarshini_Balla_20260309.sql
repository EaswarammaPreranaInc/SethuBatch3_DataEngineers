use  demoforemployeedetails;
create table employees_lab(
emp_id int primary key auto_increment,
emp_name varchar(50) not null,
department varchar(50),
salary decimal(10,2),
age int,
joining_date date);

insert into employees_lab(emp_name,department,salary,age,joining_date) values('Ravi','IT',50000,25,'22-01-10');

insert into employees_lab(emp_name,department,salary,age,joining_date) values
('Shiva','IT',1000000,122,'21-01-10'),
('venkat','IT',1000000,121,'21-01-11'),
('varma','HR',40000,23,'22-11-10'),
('viju','Finance',70000,33,'19-01-10'),
('Brahma','Maeketing',95000,120,'22-01-18'),
('Ravi','IT',50000,25,'22-01-10'),
('Shiva','IT',1000000,122,'21-01-10'),
('Ravi','HR',650000,123,'20-03-15'),
('Anita','Finance',720000,124,'19-07-22'),
('Kiran','Marketing',580000,125,'22-02-18'),
('Suresh','Sales',610000,126,'21-11-09'),
('Priya','IT',950000,127,'20-06-30'),
('Rahul','HR',600000,128,'18-09-12'),
('Sneha','Finance',800000,129,'19-12-05'),
('Arjun','Marketing',550000,130,'23-01-14'),
('Meena','Sales',620000,131,'22-08-21'),
('Vikram','IT',1050000,132,'21-04-17'),
('Lakshmi','HR',670000,133,'20-10-10'),
('Rakesh','Finance',750000,134,'19-05-25'),
('Pooja','Marketing',590000,135,'22-03-11'),
('Deepak','Sales',640000,136,'23-06-19');

insert into employees_lab(emp_name,department) values ('Harish','HR');

insert into employees_lab(emp_name,department,salary,joining_date) values (upper('Harish'),'HR',round(50000),curdate());

select * from employees_lab;
select emp_name,salary from employees_lab;
select * from employees_lab where age<=30;
select * from employees_lab where department='IT';
select * from employees_lab where department= 'IT' or department='HR';
select * from employees_lab where salary>60000 and department='IT';
select distinct department from employees_lab;
select department,count(*) from employees_lab group by department;
select department,count(*) from employees_lab group by department having count(*)>2;
select * from employees_lab order by salary desc;
select * from employees_lab order by emp_id limit 5;
select * from employees_lab order by emp_id limit 5 offset 5;

set sql_safe_updates=0;
update employees_lab set salary= 75000 where emp_name='viju';
show errors;
update employees_lab set salary= salary+1000;

delete from employees_lab where emp_name='Anitha';
delete from employees_lab;

replace into employees_lab(emp_id,emp_name,department,salary,age,joining_date) values  (1,'Sairam','HR',100000,111,curdate());
INSERT INTO employees_lab
(emp_id, emp_name, department, salary)
VALUES
(5, 'Chris', 'Marketing', 55000)
ON DUPLICATE KEY UPDATE
salary = 75000;
INSERT INTO employees_lab
(emp_id, emp_name, department, salary)
VALUES
(1, 'Shiva', 'IT', 75000)
ON DUPLICATE KEY UPDATE
salary=10000000;
select * from employees_lab;


select * from employees_lab where salary between 50000 and 70000;
select * from employees_lab where emp_name like 'R%';
select * from employees_lab where department<>'Finance';
show errors;



