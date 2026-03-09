
CREATE TABLE employees_demo (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
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

#1
select * from employees_demo;

#2
select emp_name, salary from emplopyee_demo;

#3
select emp_name, department, joining_date from employees_demo;

#4
select * from employees_demo where department = 'hr';

#5
select * from employees_demo where department = 'it';

#6
select * from employees_demo where salary > 50000;

#7
select * from employees_demo where salary < 40000;

#8
select * from employees_demo
where age > 30;

#9
select * from employees_demo where age <= 28;

#10
select * from employees_demo where joining_date < '2021-01-01';

#11
select * from employees_demo where joining_date > '2022-01-01';

#12
select * from employees_demo where department = 'finance' and salary > 45000;

#13
select * from employees_demo where salary between 30000 and 60000;

#14
select * from employees_demo where age between 25 and 30;

#15
select * from employees_demo where department != 'hr';

#16
select * from employees_demo order by salary asc;

#17
select * from employees_demo order by salary desc;

#18
select * from employees_demo order by age asc;

#19
select * from employees_demo order by joining_date desc;

#20
select * from employees_demo order by department, salary;

#21
select * from employees_demo order by salary desc
limit 3;

#22
select * from employees_demo order by age asc
limit 2;

#23
select * from employees_demo
limit 4;

#24
select * from employees_demo
limit 3 offset 3;

#25
select * from employees_demo
order by salary desc
limit 1;

#26
select count(*) from employees_demo;

#27
select count(*) from employees_demo
where department = 'hr';

#28
select max(salary) from employees_demo;

#29
select min(salary) from employees_demo;

#30
select avg(salary) from employees_demo;

#31
select sum(salary) from employees_demo;

#32
select avg(age) from employees_demo;

#33
select max(age) from employees_demo;

#34
select min(age) from employees_demo;

#35
select count(*) from employees_demo
where joining_date > '2021-01-01';

#36
select sum(salary) from employees_demo
where department = 'it';

#37
select avg(salary) from employees_demo
where department = 'finance';

#38
select department, count(*)
from employees_demo
group by department;

#39
select department, avg(salary)
from employees_demo
group by department;

#40
select department, max(salary)
from employees_demo
group by department;

#41
select department, min(salary)
from employees_demo
group by department;

#42
select department, sum(salary)
from employees_demo
group by department;

#43
select department, count(*)
from employees_demo
group by department
having count(*) > 2;

#44
select department, avg(salary)
from employees_demo
group by department
having avg(salary) > 40000;

#45
select department, sum(salary)
from employees_demo
group by department
having sum(salary) > 100000;

#46
select department, max(salary)
from employees_demo
group by department
having max(salary) > 70000;

#47
select department, min(salary)
from employees_demo
group by department
having min(salary) < 35000;

#48
select department, avg(age)
from employees_demo
group by department;

#49
select department, avg(age)
from employees_demo
group by department
having avg(age) > 28;

#50
select department, count(*)
from employees_demo
group by department
having count(*) < 3;
