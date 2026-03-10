Part A – Table Creation
Q1. Create a table named employees_lab with the following columns:
Column Name                 Data Type                Constraint
emp_id                          INT            PRIMARY KEY, AUTO_INCREMENT
emp_name                    VARCHAR(50)                NOT NULL
department                  VARCHAR(50)
salary                      DECIMAL(10,2)
age                             INT
joining_date                    DATE

#Create table employees_lab(emp_id int primary key, emp_name varchar(50), department varachar(50), salary float, age int, joining_date date)

Part B – INSERT Operations
Q2. Insert a single record into the table.
Example:
emp_name    department   salary   age   joining_date
Ravi            IT       50000    25     2022-01-10

#Insert into employees_lab(emp_name, department, salary, age, joining_date)
values('Ravi', 'IT', 50000, 25, 2022-01-10)

Q3. Insert at least 20 employee records into the table using a single INSERT statement with multiple rows.
Departments may include:
IT
HR
Finance
Sales
Marketing

# Insert into employees_lab(emp_name, department, salary, age, joining_date)
values('Abc', 'HR', 34000, 23, 2021-07-6),('bcd', 'Finance', 23000, 20, 2022-01-01), ('efg', 'Sales', 62000, 34, 2022-03-12), ('edc', 'Marketing', 24000, 20, 2021-03-23),('Sam', 'Marketing', 30000, 19, 2021-08-9), ('Alex', 'IT', 60000, 20, 2021-02-22), ('Rose', 'HR', 76000, 22, 2021-03-30), ('Jack', 'Finance', 50000, 24, 2020-04-02),('Ben', 'Sales', 23000, 25, 2023-09-12), ('John', 'Marketing', 22000, 18, 2022-09-21), ('Pearson', 'Finance', 82000, 17, 2022-12-20), ('Bubble', 'HR', 48000, 16, 2022-05-12) 

Q4. Insert a record by specifying only selected columns (emp_name, department).

#Insert into employees_lab(emp_name, department)
Values('Mac', 'Finance')

Q5. Insert a record using built-in functions such as:
UPPER()
ROUND()
CURDATE()

#Insert into employees_lab(emp_name, salary, joining_date)
 Values(Upper('Spade'), Round(36450,56), curdate())


Part C – SELECT Queries
Q6. Display all records from the table.
#select * from employees_lab

Q7. Display only employee names and salaries.
#select emp_name, salary from employess_lab

Q8. Display employees whose salary is greater than 60000.
#select * from employees_lab
where salary > 60000

Q9. Display employees whose age is less than or equal to 30.
#select * from employees_lab
where age <= 30

Q10. Display employees working in the IT department.
#select * from employees_lab
where department = 'IT'

Q11. Display employees who belong to IT or HR department.
#select * from employees_lab
where department = 'IT' or 'HR'

Q12. Display employees whose salary is greater than 60000 AND department is IT.
#select * from employees_lab
where salary > 60000 and department = 'IT' 

Q13. Display distinct departments available in the table.
#select distinct department from employees_lab

Q14. Display the number of employees in each department using GROUP BY.
#select department, count(*) from employees_lab
 Group by department

Q15. Display departments having more than 2 employees using HAVING.
#select * from employees_lab
Group by department
Having count(department) > 2

Q16. Display employees sorted by salary in descending order.
#select * from employees_lab
Order by salary desc

Q17. Display the first 5 employees using LIMIT.
#select * from employees_lab 
Limit 5

Q18. Display the next 5 employees using LIMIT and OFFSET.
#select * from employees_lab 
Limit 5 Offset 5

Part D – UPDATE Operations
Q19. Update the salary of employee 'Raj' to 75000.
#Update employees_lab
set
salary = 75000
where emp_name = 'Raj'

Q20. Increase salary of all employees by 1000.
#Update employees_lab
set
salary = salary + 1000

Part E – DELETE Operations
Q21. Delete the employee whose name is 'Lokesh'.
#Delete employees_lab
where emp_name = 'Lokesh'

Q22. Delete all records from the table.
#Delete table employees_lab

Part F – MySQL Special Commands

Q23. Use REPLACE command to update the record with emp_id = 1.
#Replace into employees_lab (emp_id , emp_name, salary, department)
Values(1, 'Charm', 60000, 'IT')

Q24. Perform UPSERT using
INSERT ... ON DUPLICATE KEY UPDATE.
#Insert into employees_lab(emp_id, emp_name, salary, age, department)
Values(2, 'Dag', 75000, 27, 'Sales')
ON Duplicate Key Update
emp_name = 'Dag'
salary = 75000
age = 27
department = 'Sales'

Q25. Insert a new employee using UPSERT.
#Insert into employees_lab(emp_id, emp_name, salary, age, department)
Values(18, 'Kim', 45000, 23, 'Finance')
ON Duplicate Key Update
emp_name = 'Kim'
salary = 45000
age = 23
department = 'Finance'

Q26. Try inserting a record with an existing emp_id and update the salary using:
ON DUPLICATE KEY UPDATE
##Insert into employees_lab(emp_id, emp_name, salary, age, department)
Values(2, 'Dag', 75000, 27, 'Sales')
ON Duplicate Key Update
salary = 65000


Q27. Perform UPSERT using the VALUES() function.

Part G – Additional Search Queries
Q28. Display employees whose salary is between 50000 and 70000.
#select * from employees_lab
where salary between 50000 and 70000

Q29. Display employees whose name starts with 'R'.
#select * from employees_lab
where emp_name like R%

Q30. Display employees whose department is not 'Finance'.
#select * from employees_lab
where department is not 'Finance'
