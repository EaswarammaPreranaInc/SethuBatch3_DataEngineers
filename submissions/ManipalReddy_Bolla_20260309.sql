use employees;
create table employees_lab(
emp_id INT PRIMARY KEY	AUTO_INCREMENT,
emp_name VARCHAR(50) NOT NULL,
department VARCHAR(50),
salary DECIMAL(10,2),
age INT,
joining_date DATE);
insert into employees_lab(emp_name,department,salary,age,joining_date) VALUES ('Ravi','IT',50000,25,'2022-01-10');
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES 
    ('Sachin Tendulkar', 'IT', 95000, 50, '2020-01-15'),
    ('Virat Kohli', 'Marketing', 92000, 35, '2021-03-22'),
    ('MS Dhoni', 'Finance', 88000, 42, '2019-11-10'),
    ('Rohit Sharma', 'Sales', 85000, 36, '2020-06-05'),
    ('Kane Williamson', 'HR', 78000, 33, '2022-01-20'),
    ('Steve Smith', 'IT', 82000, 34, '2021-08-14'),
    ('Ben Stokes', 'Marketing', 80000, 32, '2022-05-12'),
    ('Pat Cummins', 'Finance', 84000, 30, '2022-09-30'),
    ('Jasprit Bumrah', 'IT', 79000, 30, '2021-12-01'),
    ('Joe Root', 'HR', 77000, 33, '2020-02-28'),
    ('Glenn Maxwell', 'Sales', 72000, 35, '2023-04-15'),
    ('Rashid Khan', 'IT', 71000, 25, '2023-01-10'),
    ('Quinton de Kock', 'Finance', 74000, 31, '2020-10-05'),
    ('Babar Azam', 'Marketing', 76000, 29, '2021-07-19'),
    ('Mitchell Starc', 'Sales', 81000, 34, '2022-03-11'),
    ('Rishabh Pant', 'IT', 68000, 26, '2023-06-25'),
    ('Hardik Pandya', 'Marketing', 75000, 30, '2022-11-02'),
    ('David Warner', 'Sales', 73000, 37, '2020-05-18'),
    ('Shubman Gill', 'HR', 65000, 24, '2024-01-05'),
    ('Ravindra Jadeja', 'Finance', 83000, 35, '2019-08-20');
insert into employees_lab(emp_name, department) VALUES (Pawan,Kabaddi);
INSERT INTO employees_lab(emp_name, department, salary, age, joining_date)VALUES (UPPER('Virat Kohli'),'Marketing', ROUND(95000.45, 0),35,CURDATE() );
select *from employees_lab;
select emp_name,salary from employees_lab;
select *from employees_lab
where salary > 60000;
select *from employees_lab
where age <=30;
select *from employees_lab
where department='IT';
select *from employees_lab
where department='IT' or department='HR';
select *from employees_lab
where salary > 60000 and department='IT';
select distinct department from employees_lab;
select department, count(emp_id) from employees_lab 
group by department;
select department, COUNT(emp_id) as total_emp from employees_lab
group by department
having total_emp > 2;
select emp_name,salary from employees_lab
order by salary desc;
select emp_id,emp_name from employees_lab
limit 5;
select emp_id,emp_name from employees_lab
limit 5 offset 5;
insert into employees_lab(emp_name,department,salary,age,joining_date) values ('Raj','IT',50000,28,'2020-01-10');
UPDATE employees_lab
SET salary = 75000
WHERE emp_name = 'Raj';
set SQL_SAFE_UPDATES =0;
UPDATE employees_lab
SET salary = 75000
WHERE emp_name = 'Raj';
UPDATE employees_lab
set salary=salary +1000;
delete from employees_lab
where emp_name='LOKESH';
select *from employees_lab;
truncate table employees_lab;
REPLACE INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (1, 'Virat Kohli', 'Marketing', 85000, 35, '2021-03-22');
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (18, 'Virat Kohli', 'Marketing', 95000, 35, '2021-03-22')
ON DUPLICATE KEY UPDATE 
salary = 95000,
department = 'Marketing';
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (10, 'Jasprit Bumrah', 'IT', 82000, 30, '2024-03-09')
ON DUPLICATE KEY UPDATE 
salary = 82000,
department = 'IT',
age = 30;
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (1, 'Virat Kohli', 'Marketing', 99000, 35, '2021-03-22')
ON DUPLICATE KEY UPDATE 
salary = 99000;
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (3, 'MS Dhoni', 'Finance', 95000, 42, '2019-11-10')
ON DUPLICATE KEY UPDATE 
salary = VALUES(salary),
department = VALUES(department);
INSERT INTO employees_lab (emp_id, emp_name, department, salary, age, joining_date)
VALUES (3, 'MS Dhoni', 'Finance', 67000, 42, '2019-11-10')
ON DUPLICATE KEY UPDATE 
salary = VALUES(salary),
department = VALUES(department);
insert into employees_lab values (8, 'Rohit sharma', 'Finance', 67000, 42, '2019-11-10');
select * from employees_lab
where salary between 50000 and 70000;
SELECT emp_name
FROM employees_lab
WHERE emp_name like 'R%';
select * from employees_lab
where department<>'Finance';

 