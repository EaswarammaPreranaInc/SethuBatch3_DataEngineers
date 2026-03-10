use employeedb;
create table departments_demo(
dept_id INT PRIMARY KEY,
dept_name VARCHAR(50));
create table employees_demo(
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
dept_id INT);
create table employees_selfjoin(
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
manager_id INT);
INSERT INTO departments_demo (dept_id, dept_name) VALUES (101, 'IT'),(102, 'HR'),(103, 'Finance'),
(104, 'Marketing'),(105, 'Sales'),(106, 'Admin'),
(107, 'Operations'),(108, 'Support'),(109, 'Research'),(110, 'Training');
INSERT INTO employees_demo (emp_id, emp_name, dept_id) VALUES(1, 'Ravi', 101),(2, 'Anita', 102),(3, 'Kiran', 103),
(4, 'Sneha', 104),(5, 'Arjun', 101),(6, 'Divya', 105),
(7, 'Rahul', 106),(8, 'Pooja', 107),(9, 'Manoj', 108),(10, 'Deepa', 109);
INSERT INTO employees_selfjoin (emp_id, emp_name, manager_id) VALUES(1, 'Ravi', NULL),(2, 'Anita', 1),(3, 'Kiran', 1),(4, 'Sneha', 2),
(5, 'Arjun', 2),(6, 'Divya', 3),(7, 'Rahul', 3),(8, 'Pooja', 4),(9, 'Manoj', 5),(10, 'Deepa', 6);
SELECT e.emp_name, d.dept_name from employees_demo e 
inner join departments_demo d on e.dept_id=d.dept_id;
SELECT e.emp_name, d.dept_name from employees_demo e 
left join departments_demo d on e.dept_id=d.dept_id;
SELECT e.emp_name, d.dept_name from employees_demo e 
right join departments_demo d on e.dept_id=d.dept_id;
SELECT e.emp_name, d.dept_name from employees_demo e 
left join departments_demo d on e.dept_id=d.dept_id
union SELECT e.emp_name, d.dept_name from employees_demo e 
right join departments_demo d on e.dept_id=d.dept_id;
SELECT e.emp_id ,e.emp_name, d.dept_name from employees_demo e 
inner join departments_demo d 
on e.dept_id=d.dept_id order by e.emp_name;
SELECT e.emp_id ,e.emp_name, d.dept_name from employees_demo e 
inner join departments_demo d 
on e.dept_id=d.dept_id where d.dept_name = 'IT';
SELECT e.emp_id ,e.emp_name from employees_demo e 
left join departments_demo d 
on e.dept_id=d.dept_id where d.dept_name is NULL;
SELECT e.emp_name, d.dept_name from employees_demo e 
right join departments_demo d on e.dept_id=d.dept_id 
where e.emp_id is NULL;
SELECT e.emp_id,e.emp_name, d.dept_name from employees_demo e 
cross join departments_demo d;
SELECT count(*) from employees_demo e 
cross join departments_demo d ;
SELECT dept_id,count(*) FROM employees_demo group by dept_id;
SELECT d.dept_name, count(*) from employees_demo e 
inner join departments_demo d on e.dept_id=d.dept_id group by d.dept_name;
SELECT dept_id,count(*) FROM employees_demo group by dept_id having count(*) > 1;
SELECT dept_id,count(*) FROM employees_demo group by dept_id having count(*) = 2;
SELECT d.dept_name, count(*) from employees_demo e 
inner join departments_demo d on e.dept_id=d.dept_id group by d.dept_name having count(*) > 1;
SELECT d.dept_name, count(*) from employees_demo e 
inner join departments_demo d on e.dept_id=d.dept_id group by d.dept_name having count(*) < 2;
SELECT e.emp_name,d.dept_name from employees_demo e 
inner join departments_demo d on e.dept_id=d.dept_id order by d.dept_name;
SELECT * FROM employees_demo ORDER BY dept_id DESC;
SELECT d.dept_name,count(*) from employees_demo e 
inner join departments_demo d on e.dept_id=d.dept_id group by d.dept_name order by count(*) desc;
SELECT * FROM employees_demo LIMIT 5;
SELECT * FROM employees_demo LIMIT 5 OFFSET 5;
SELECT * FROM employees_demo LIMIT 3 OFFSET 3;
SELECT d.dept_name,e.emp_name from employees_demo e 
inner join departments_demo d on e.dept_id=d.dept_id limit 3;
update employees_selfjoin set emp_name = 'John' where emp_id =1;
SELECT e.emp_name, m.emp_name as manager_name 
FROM employees_selfjoin e join employees_selfjoin m 
on e.manager_id = m.emp_id; 
SELECT e.emp_name
FROM employees_selfjoin e join employees_selfjoin m 
on e.manager_id = m.emp_id where m.emp_name = 'John';
SELECT e.emp_name
FROM employees_selfjoin e left join employees_selfjoin m 
on e.manager_id = m.emp_id where m.emp_name is NULL;
SELECT m.emp_name as manager_name, count(*) as employee_count 
FROM employees_selfjoin e join employees_selfjoin m 
on e.manager_id = m.emp_id group by m.emp_name; 
