create Table departments_demo(dept_id INT PRIMARY KEY,dept_name varchar(20));
create table employee(emp_id INT PRIMARY KEY auto_increment,emp_name varchar(50),dept_id int ,foreign key(dept_id) references 
departments_demo(dept_id));


INSERT INTO departments_demo (dept_id, dept_name) VALUES
(1,'HR'),
(2,'IT'),
(3,'Finance'),
(4,'Marketing');

INSERT INTO employee (emp_name, dept_id) VALUES
('Shankar',2),
('Alice',1),
('Bob',3),
('David',2),
('Chris',4);

INSERT INTO employee (emp_name, dept_id) VALUES
('Ravi', NULL),
('Kiran', NULL);

# inner join
select e.emp_name,d.dept_name
FROM employee as e
JOIN departments_demo as d
ON e.dept_id=d.dept_id;

#left join
select e.emp_name,d.dept_name
FROM employee as e
left join departments_demo as d
ON e.dept_id=d.dept_id;

# right join
select e.emp_name,d.dept_name
FROM employee as e
right join departments_demo as d

ON e.dept_id=d.dept_id;


# full join
select e.emp_name,d.dept_name
FROM employee as e
left JOIN departments_demo as d
ON e.dept_id=d.dept_id
union
select e.emp_name,d.dept_name
FROM employee as e
right join departments_demo as d
ON e.dept_id=d.dept_id;


select e.emp_id,e.emp_name,d.dept_name
FROM employee as e
JOIN departments_demo as d
ON e.dept_id=d.dept_id
order by e.emp_name desc;



select e.emp_name,d.dept_name
FROM employee as e
JOIN departments_demo as d
ON e.dept_id=d.dept_id
where d.dept_name='IT';

select e.emp_name,d.dept_name
FROM employee as e
LEFT JOIN departments_demo as d
ON e.dept_id=d.dept_id
where d.dept_name is null; 


select e.dept_id,count(e.emp_name)
FROM employee as e
JOIN departments_demo as d
ON e.dept_id=d.dept_id
group by e.dept_id;



select d.dept_name,count(e.emp_name)
FROM employee as e
JOIN departments_demo as d
ON e.dept_id=d.dept_id
group by d.dept_name;

select d.dept_name,count(e.emp_name)
FROM employee as e
JOIN departments_demo as d
ON e.dept_id=d.dept_id
group by d.dept_name
having count(e.emp_name)=2;
#Display departments where employee count is greater than 1.

select d.dept_name,count(e.emp_name)
FROM employee as e
JOIN departments_demo as d
ON e.dept_id=d.dept_id
group by d.dept_name
having count(e.emp_name)>1;

#Display departments where employee count is less than 2.


select d.dept_name,count(e.emp_name)
FROM employee as e
JOIN departments_demo as d
ON e.dept_id=d.dept_id
group by d.dept_name
having count(e.emp_name)<2;

#Display employees and departments ordered by department name.
select d.dept_name,e.emp_name
FROM employee as e
JOIN departments_demo as d
ON e.dept_id=d.dept_id
order by dept_name asc;

#Display employees ordered by department id descending.
select e.emp_name
FROM employee as e
JOIN departments_demo as d
ON e.dept_id=d.dept_id
order by e.dept_id desc;
