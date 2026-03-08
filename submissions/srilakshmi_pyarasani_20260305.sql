Create table employees_demo(emp_id int primary key Auto_Increment, emp_name Varchar(50), department Varchar(50),salary float, age int, joining_date);

INSERT
insert into employees_demo (emp_name, department, salary, age, joining_date) Values (('Rahul', 'HR', 30000, 25, '2022-01-10'),
('Sneha', 'HR', 35000, 28, '2021-03-15'),
('Amit', 'IT', 60000, 30, '2020-07-20'),
('Priya', 'IT', 75000, 32, '2019-05-18'),
('Kiran', 'Finance', 50000, 29, '2021-11-25'),
('Anjali', 'Finance', 45000, 27, '2022-02-14'),
('Vikram', 'IT', 80000, 35, '2018-09-10'),
('Meena', 'HR', 32000, 26, '2023-01-05'));

✅Section A – Basic SELECT & WHERE (1–15)
Display all records from the table.
Select * from employees_demo
Display only emp_name and salary.
Select emp_name, salary from employees_demo
Display only emp_name, department, and joining_date.
Select emp_name, department, joining_date from employees_demo
Display employees who belong to HR department.
select * from employees_demo
    Where department = "HR"	
Display employees who belong to IT department.
select * from employees_demo
    Where department = "IT"
Display employees whose salary is greater than 50000.
select * from employees_demo
    Where salary > 50000
Display employees whose salary is less than 40000.
select * from employees_demo
    Where salary < 40000
Display employees whose age is greater than 30.
select * from employees_demo
    Where age > 30
Display employees whose age is less than or equal to 28.
select * from employees_demo
    Where age <= 28
Display employees who joined before 2021-01-01.
select * from employees_demo
    where joining_date < '2021-01-01'
Display employees who joined after 2022-01-01.
select * from employees_demo
    where joining_date > '2022-01-01'
Display employees from Finance department with salary greater than 45000.
select * from employees_demo
    where department = "Finance" and salary > 45000
Display employees whose salary is between 30000 and 60000.
select * from employees_demo
    where salary between 30000 and 60000
Display employees whose age is between 25 and 30.
select * from employees_demo
    where age between 25 and 30
Display employees whose department is not HR.
select * from employees_demo
    where department!= "HR"

✅ Section B – ORDER BY & LIMIT (16–25)
Display all employees sorted by salary (Ascending).
select * from employees_demo
    order by salary 
Display all employees sorted by salary (Descending).
select * from employees_demo
    order by salary desc
Display employees sorted by age (Ascending).
select * from employees_demo
    order by age
Display employees sorted by joining date (Newest first).
select * from employees_demo
    order by joining_date desc
Display employees sorted by department and salary.
select * from employees_demo
    order by salary, department
Display top 3 highest paid employees.
select * from employees_demo
    order by salary desc limit 3
Display top 2 youngest employees.
select * from employees_demo
    order by age asc limit 2
Display first 4 records.
select * from employees_demo
    order by asc limit 4
Skip first 3 records and display next 3 records.
select * from employees_demo
    order by asc limit 3 offset 3
Display the employee with the highest salary.
select * from employees_demo
    order by salary desc limit 1

✅ Section C – Aggregate Functions (26–37)
Find total number of employees.
select count(emp_id) as count from employees_demo
Find total number of employees in HR department.
select count(department) as count from employees_demo
    where department - 'HR'
Find maximum salary.
select max(salary) as max from employees_demo
Find minimum salary.
select min(salary) as min from employees_demo
Find average salary.
select avg(salary) as average from employees_demo
Find total salary paid to all employees.
select sum(salary) as sum from employees_demo
Find average age of employees.
select avergae(age) average max from employees_demo
Find highest age among employees.
select max(age) as max from employees_demo
Find lowest age among employees.
select min(age) as min from employees_demo
Count number of employees who joined after 2021.
select count(Joining_date) as count from employees_demo
    where joining_date > 2021
Find total salary of IT department.
select sum(salary) as sum from employees_demo
    where department = 'IT'
Find average salary of Finance department.
select sum(salary) as sum from employees_demo
    where department = 'Finance'


✅ Section D – GROUP BY & HAVING (38–50)
Display department-wise employee count.
SELECT department, COUNT(*) AS count from employees_demo
    GROUP BY department;
Display department-wise average salary.
SELECT department, avg(salary) AS average from employees_demo
    GROUP BY department;
Display department-wise maximum salary.
SELECT department, max(salary) AS min from employees_demo
    GROUP BY department;
Display department-wise minimum salary.
SELECT department, min(salary) AS min from employees_demo
    GROUP BY department;
Display department-wise total salary.
SELECT department, sum(salary) AS sum from employees_demo
    GROUP BY department;
Display departments having more than 2 employees.
SELECT department, count(*)as count from employees_demo
    having count(*) > 2
Display departments having average salary greater than 40000.
SELECT department, avg(salary)as avg from employees_demo
    having avg(salary) > 40000
Display departments having total salary greater than 100000.
SELECT department, sum(salary)as sum from employees_demo
    having sum(salary) > 100000
Display departments where maximum salary is greater than 70000.
SELECT department, MAX(salary) AS max FROM Employee_demo
    GROUP BY department
    HAVING MAX(salary) > 70000;
Display departments where minimum salary is less than 35000.
SELECT department, Min(salary) AS min FROM Employee_demo
    GROUP BY department
    HAVING Min(salary) < 35000;
Display department-wise average age.
SELECT department, avg(age) as average FROM Employee_demo
    GROUP BY department
Display departments having average age greater than 28.
select department, avg(age) as average from employees_demo
    Group by department
    Having avg(age)>28
Display departments having employee count less than 3.
select department, count(*) as count from employee_demo
    Group by department
    Having count(*) < 3  