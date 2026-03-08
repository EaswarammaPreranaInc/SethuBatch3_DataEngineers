create database employees;
use employees;
select database();
create table employees_demo(
 emp_id INT PRIMARY KEY 
AUTO_INCREMENT,
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

1)select * from employees_demo;

2)select emp_name,salary from employees_demo;

3)select emp_name,department,joining_date from employees_demo;

4)select emp_name from employees_demo
WHERE department='HR';

5)select emp_name from employees_demo
WHERE department='IT';

6)select emp_name from employees_demo
where salary>50000;

7)select emp_name from employees_demo
where age>30;

8)select emp_name from employees_demo
where salary<40000;

9)select emp_name from employees_demo
where age<=28;

10)select emp_name from employees_demo
where joining_date<'2022-01-01';

11)select emp_name from employees_demo
where joining_date>'2022-01-01';

12)select emp_name from employees_demo
where department='Finance' and salary>45000;

13)select emp_name from employees_demo
where salary between 30000 and 60000;

14)select emp_name from employees_demo
where age between 25 and 30;

15)select emp_name from employees_demo
where department<>'HR';

16)select emp_name from employees_demo
order by salary asc;

17)select emp_name,salary from employees_demo
order by salary desc;

18)select emp_name,age from employees_demo
order by age asc;

19)select emp_name,joining_date from employees_demo
order by joining_date desc;

20)select emp_name,salary,department from employees_demo
order by department,salary asc;

21)select emp_name,salary,department from employees_demo
order by department,salary desc;

22)select emp_name,salary from employees_demo
order by salary desc
limit 3;

23)select emp_name,age from employees_demo
order by age desc
limit 2;

24)select *from employees_demo
limit 4;

25)select *from employees_demo
limit 3 offset 3;

26)select *from employees_demo
order by salary desc
limit 1;

27)select count(*) as total_employees
from employees_demo;

28)select count(*) as total_employees
from employees_demo
where department='HR';

29)select max(salary) as maxsalary
from employees_demo;

30)select min(salary) as minsalary
from employees_demo;

31)select avg(salary) as avgsalary
from employees_demo;

32)select sum(salary) as totalsalary
from employees_demo;

33)select avg(age) as average
from employees_demo;

34)select max(age) as highestage
from employees_demo;

35)select min(age) as lowestage
from employees_demo;

36)select count(emp_name) as noofemployees
from employees_demo
where joining_date>'2021-01-01';

37)select sum(salary) as totalsalary
from employees_demo
where department='IT';

38)select avg(salary) as avgsalary
from employees_demo
where department='Finance';

39)select  department,count(*) as departmentcount
from employees_demo
group by department;

40)select  department,avg(salary) as departmentavgsalary
from employees_demo
group by department;

41)select  department,max(salary) as departmentmaxsalary
from employees_demo
group by department;

42)select  department,sum(salary) as departmenttotalsalary
from employees_demo
group by department;

43)select  department, count(*) as departmentmorethan2employees
from employees_demo
group by department
having departmentmorethan2employees >2;

44)select  department, avg(salary) as avgsalary
from employees_demo
group by department
having avgsalary > 40000;

45)select  department, sum(salary) as totalsalary
from employees_demo
group by department
having totalsalary > 100000;

46)select  department, max(salary) as maxsalary
from employees_demo
group by department
having maxsalary>70000;

47)select  department, min(salary) as minsalary
from employees_demo
group by department
having minsalary<35000;

48)select  department, avg(salary) as avgsalary
from employees_demo
group by department;

49)select  department, avg(age) as avgage
from employees_demo
group by department
having avgage>28;

50)select  department, count(*) as employeelessthanthree
from employees_demo
group by department

having employeelessthanthree<3;
