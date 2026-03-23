create database joinsdb;
use joinsdb;
-- Tables Used
-- employees_demo
-- emp_id
-- emp_name
-- dept_id
CREATE TABLE employees_demo (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments_demo(dept_id)
);
CREATE TABLE employees_demo (
    emp_id INT,
    emp_name VARCHAR(50),
    dept_id INT
);

-- departments_demo
-- dept_id
-- dept_name
CREATE TABLE departments_demo (
    dept_id INT PRIMARY KEY,
    emp_name VARCHAR(50)
);
INSERT INTO employees_demo (emp_id, emp_name, dept_id) VALUES
(101, 'Ravi', 2),
(102, 'Divya', 1),
(103, 'Rahul', 3),
(104, 'Anil', NULL),
(105, 'Sita', 2);
-- employees_selfjoin
-- emp_id
-- emp_name
-- manager_id

INSERT INTO departments_demo (dept_id, dept_name) VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance'),
(4, 'Marketing');
-- Part 1 – Basic JOIN Queries
-- 1 Display employee name and department name using an INNER JOIN.
select emp_name,dept_name from employees_demo e  inner join departments_demo d ON e.dept_id= d.dept_id;
-- 2 Display all employees and their department names, even if the department does not exist.
-- (Hint: LEFT JOIN)
select emp_name,dept_name from employees_demo e  left join departments_demo d ON e.dept_id= d.dept_id;

-- 3 Display all departments and employees working in them. (Hint: RIGHT JOIN)
select emp_name,dept_name from employees_demo e  right join departments_demo d ON e.dept_id= d.dept_id;

-- 4 Display all employees and departments including unmatched rows from both tables. (Hint: FULL JOIN using UNION)
select e.*, d.* from employees_demo e  left join departments_demo d ON e.dept_id= d.dept_id
union
select  e.*, d.* from employees_demo e  right join departments_demo d ON e.dept_id= d.dept_id;

-- 5 Display employee id, employee name, and department name sorted by employee name.
select emp_id,emp_name,dept_name from employees_demo e  inner join departments_demo d ON e.dept_id= d.dept_id order by emp_name;

-- 6 Display employees who belong to the IT department.
select emp_id, emp_name, dept_name from employees_demo e  inner join departments_demo d ON e.dept_id= d.dept_id where dept_name = 'IT';

-- 7 Display employees who do not have a matching department. (Hint: NULL values)
select emp_name,e.dept_id from employees_demo e  left join departments_demo d ON e.dept_id= d.dept_id where e.dept_id is null;

-- 8 Display departments that do not have any employees.
select dept_name,d.dept_id from employees_demo e  right join departments_demo d ON e.dept_id= d.dept_id where emp_id is null;

-- Part 2 – CROSS JOIN
-- 9 Display all possible combinations of employee names and department names. (Hint: CROSS JOIN)
select emp_name,dept_name from employees_demo e  cross join departments_demo d;

-- 10Count how many rows are produced by the CROSS JOIN.(Hint: COUNT)
select count(*) from employees_demo e  cross join departments_demo d;

-- Part 3 – GROUP BY
-- 11Display department id and number of employees in each department.
select count(emp_id),d.dept_id from employees_demo e  inner join departments_demo d ON e.dept_id= d.dept_id group by d.dept_id;


-- 12Display department name and number of employees working in each department.(Hint: JOIN + GROUP BY)
select count(emp_id),d.dept_name from employees_demo e  inner join departments_demo d ON e.dept_id= d.dept_id group by d.dept_name;


-- 13Display departments with more than one employee.(Hint: HAVING)
select count(emp_id),d.dept_name from employees_demo e  inner join departments_demo d ON e.dept_id= d.dept_id group by d.dept_name having count(emp_id) > 1;

-- 14Display departments with exactly two employees.
select count(emp_id),d.dept_name from employees_demo e  inner join departments_demo d ON e.dept_id= d.dept_id group by d.dept_name having count(emp_id) = 2;


-- Part 4 – HAVING
-- 15 Display departments where employee count is greater than 1.
select count(emp_id),d.dept_name from employees_demo e  inner join departments_demo d ON e.dept_id= d.dept_id group by d.dept_name having count(emp_id) > 1;


-- 16 Display departments where employee count is less than 2.
select count(emp_id),d.dept_name from employees_demo e  inner join departments_demo d ON e.dept_id= d.dept_id group by d.dept_name having count(emp_id) < 2;


-- Part 5 – ORDER BY
-- 17 Display employees and departments ordered by department name.
select emp_name,dept_name from employees_demo e  inner join departments_demo d ON e.dept_id= d.dept_id order by dept_name ;

-- 18 Display employees ordered by department id descending.
select emp_name,dept_name,d.dept_id from employees_demo e  inner join departments_demo d ON e.dept_id= d.dept_id order by d.dept_id desc ;


-- 19 Display departments with employee count ordered by highest employee count first.
select count(emp_id),d.dept_name from employees_demo e  inner join departments_demo d ON e.dept_id= d.dept_id group by d.dept_name order by count(emp_id) desc;


-- Part 6 – LIMIT and OFFSET (Pagination)
-- 20 Display first 5 employees.
select * from employees_demo limit 5;

-- 21Display employees from row 6 to row 10. (Hint: LIMIT + OFFSET)
select * from employees_demo limit 5 offset 5;

-- 22Display 3 employees starting from the 4th row.
select * from employees_demo limit 3 offset 3;

-- 23Display department-wise employee list but show only first 3 rows.
SELECT d.dept_name, e.emp_name FROM employees_demo e JOIN departments_demo d ON e.dept_id = d.dept_id LIMIT 3;

-- Part 7 – SELF JOIN
-- Use table: employees_selfjoin

CREATE TABLE employees_selfjoin (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    manager_id INT
);

INSERT INTO employees_selfjoin VALUES
(1, 'John', NULL),
(2, 'Divya', 1),
(3, 'Rahul', 1),
(4, 'Anil', 2),
(5, 'Sita', 2);

-- 24Display employee name and their manager name.
select e.emp_name , m.emp_name as manager from employees_selfjoin e inner join employees_selfjoin m ON e.manager_id = m.emp_id;

-- 25Display employees who report to John.
select e.emp_name , m.emp_name as manager from employees_selfjoin e inner join employees_selfjoin m ON e.manager_id = m.emp_id where m.emp_name = 'John';

-- 26Display employees who do not have a manager.
select e.emp_name , m.emp_name as manager from employees_selfjoin e left join employees_selfjoin m ON e.manager_id = m.emp_id where m.emp_name is null;

-- 27Display manager name and number of employees reporting to them.(Hint: GROUP BY)
select  m.emp_name as manager, count(e.emp_id) from employees_selfjoin e right join employees_selfjoin m ON e.manager_id = m.emp_id group by m.emp_name ;

