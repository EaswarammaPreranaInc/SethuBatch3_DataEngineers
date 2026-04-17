##Part A – Table Creation
#Q1. Create a table named employees_lab with the following columns:
#Column Name
#Data Type
#Constraint
#emp_id
#INT
#PRIMARY KEY, AUTO_INCREMENT
#emp_name
#VARCHAR(50)
#NOT NULL
#department
#VARCHAR(50)


#salary
#DECIMAL(10,2)


#age
#INT


#joining_date
#DATE

create table employees_lab (
    emp_id int primary key auto_increment,
    emp_name varchar(50) not null,
    department varchar(50),
    salary decimal(10,2),
    age int,
    joining_date date
);

#Part B – INSERT Operations
#Q2. Insert a single record into the table.
#Example:
#emp_name
#department
#salary
#age
#joining_date
#Ravi
#IT
#50000
#25
#2022-01-10
insert into employees_lab (emp_name, department, salary, age, joining_date)
values ('Ravi', 'IT', 50000, 25, '2022-01-10');

#Q3. Insert at least 20 employee records into the table using a single INSERT statement with multiple rows.
#Departments may include:
#IT
#HR
#Finance
#Sales
#Marketing
insert into employees_lab (emp_name, department, salary, age, joining_date) values
('Raj', 'IT', 65000, 28, '2021-05-10'),
('Anita', 'HR', 52000, 30, '2020-03-15'),
('Karan', 'Finance', 70000, 35, '2019-07-22'),
('Meena', 'Sales', 48000, 27, '2022-02-11'),
('Lokesh', 'Marketing', 55000, 29, '2021-08-01'),
('Rohan', 'IT', 72000, 32, '2018-09-18'),
('Sneha', 'HR', 51000, 26, '2023-01-12'),
('Arjun', 'Finance', 68000, 33, '2020-11-05'),
('Priya', 'Sales', 46000, 24, '2022-04-19'),
('Vikas', 'Marketing', 59000, 31, '2021-06-23'),
('Ritu', 'IT', 64000, 28, '2020-02-14'),
('Nikhil', 'Finance', 71000, 34, '2019-10-10'),
('Pooja', 'HR', 53000, 29, '2021-12-01'),
('Amit', 'Sales', 47000, 25, '2022-06-21'),
('Deepa', 'Marketing', 60000, 30, '2020-08-17'),
('Rahul', 'IT', 75000, 36, '2018-03-03'),
('Sanjay', 'Finance', 67000, 32, '2019-09-09'),
('Neha', 'HR', 52000, 27, '2022-05-05'),
('Varun', 'Sales', 49000, 26, '2023-02-15'),
('Kavya', 'Marketing', 58000, 28, '2021-07-30');

#Q4. Insert a record by specifying only selected columns (emp_name, department).
insert into employees_lab (emp_name, department)
values ('Ramesh', 'IT');

#Q5. Insert a record using built-in functions such as:
#UPPER()
#ROUND()
#CURDATE()
insert into employees_lab (emp_name, department, salary, age, joining_date)
values (upper('suresh'), 'Finance', round(45678.678,2), 29, curdate());

#Part C – SELECT Queries
#Q6. Display all records from the table.
select * from employees_lab;

#Q7. Display only employee names and salaries.
select emp_name, salary from employees_lab;

#Q8. Display employees whose salary is greater than 60000.
select * from employees_lab
where salary > 60000;

#Q9. Display employees whose age is less than or equal to 30.
select * from employees_lab
where age <= 30;

#Q10. Display employees working in the IT department.
select * from employees_lab
where department = 'IT';

#Q11. Display employees who belong to IT or HR department.
select * from employees_lab
where department in ('IT','HR');

#Q12. Display employees whose salary is greater than 60000 AND department is IT.
select * from employees_lab
where salary > 60000 and department = 'IT';

#Q13. Display distinct departments available in the table.
select distinct department from employees_lab;

#Q14. Display the number of employees in each department using GROUP BY.
select department, count(*) as total_employees
from employees_lab
group by department;

#Q15. Display departments having more than 2 employees using HAVING.
select department, count(*) as total_employees
from employees_lab
group by department
having count(*) > 2;

#Q16. Display employees sorted by salary in descending order.
select * from employees_lab
order by salary desc;

#Q17. Display the first 5 employees using LIMIT.
select * from employees_lab
limit 5;

#Q18. Display the next 5 employees using LIMIT and OFFSET.
select * from employees_lab
limit 5 offset 5;

##Part D – UPDATE Operations
#Q19. Update the salary of employee 'Raj' to 75000.
update employees_lab
set salary = 75000
where emp_name = 'Raj';

#Q20. Increase salary of all employees by 1000.
update employees_lab
set salary = salary + 1000;

##Part E – DELETE Operations
#Q21. Delete the employee whose name is 'Lokesh'.
delete from employees_lab
where emp_name = 'Lokesh';

#Q22. Delete all records from the table.
delete from employees_lab;

##Part F – MySQL Special Commands
#Q23. Use REPLACE command to update the record with emp_id = 1.
replace into employees_lab (emp_id, emp_name, department, salary, age, joining_date)
values (1, 'Ravi', 'IT', 60000, 26, '2022-01-10');

#Q24. Perform UPSERT using
#INSERT ... ON DUPLICATE KEY UPDATE.
insert into employees_lab (emp_id, emp_name, department, salary)
values (2, 'Amit', 'Sales', 50000)
on duplicate key update salary = 50000;

#Q25. Insert a new employee using UPSERT.
insert into employees_lab (emp_id, emp_name, department, salary)
values (30, 'Teja', 'IT', 62000)
on duplicate key update salary = 62000;

#Q26. Try inserting a record with an existing emp_id and update the salary using:
#ON DUPLICATE KEY UPDATE
insert into employees_lab (emp_id, emp_name, department, salary)
values (3, 'Karan', 'Finance', 80000)
on duplicate key update salary = 80000;

#Q27. Perform UPSERT using the VALUES() function.
insert into employees_lab (emp_id, emp_name, department, salary)
values (4, 'Meena', 'Sales', 55000)
on duplicate key update salary = values(salary);

##Part G – Additional Search Queries
#Q28. Display employees whose salary is between 50000 and 70000.
select * from employees_lab
where salary between 50000 and 70000;

#Q29. Display employees whose name starts with 'R'.
select * from employees_lab
where emp_name like 'R%';

#Q30. Display employees whose department is not 'Finance'.
select * from employees_lab
where department != 'Finance';

