
CREATE TABLE employees_lab (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    age INT,
    joining_date DATE
);



-- Q2
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES ('Ravi','IT',50000,25,'2022-01-10');

-- Q3
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date) VALUES
('Raj','IT',65000,28,'2021-03-12'),
('Anita','HR',52000,26,'2020-07-15'),
('Kiran','Finance',70000,32,'2019-09-20'),
('Lokesh','Sales',48000,24,'2023-01-11'),
('Meena','Marketing',55000,29,'2022-05-10'),
('Arun','IT',72000,31,'2018-06-18'),
('Priya','HR',60000,27,'2021-02-14'),
('Rohit','Sales',53000,25,'2020-11-23'),
('Sneha','Finance',75000,34,'2017-08-30'),
('Vikas','Marketing',62000,30,'2019-04-09'),
('Neha','IT',58000,26,'2022-02-02'),
('Suresh','HR',64000,33,'2018-03-21'),
('Pooja','Sales',51000,28,'2021-07-19'),
('Ramesh','Finance',69000,35,'2016-10-10'),
('Divya','Marketing',56000,24,'2023-03-12'),
('Amit','IT',73000,29,'2019-12-01'),
('Kavya','HR',54000,27,'2022-06-06'),
('Rahul','Sales',47000,23,'2023-01-25'),
('Manoj','Finance',71000,36,'2017-05-05'),
('Deepa','Marketing',59000,28,'2020-09-09');

-- Q4
INSERT INTO employees_lab (emp_name, department)
VALUES ('Karthik','IT');

-- Q5
INSERT INTO employees_lab (emp_name, department, salary, age, joining_date)
VALUES (UPPER('naveen'),'IT',ROUND(65432.567,2),27,CURDATE());

-- Q6
SELECT * FROM employees_lab;

-- Q7
SELECT emp_name, salary FROM employees_lab;

-- Q8
SELECT * FROM employees_lab
WHERE salary > 60000;

-- Q9
SELECT * FROM employees_lab
WHERE age <= 30;

-- Q10
SELECT * FROM employees_lab
WHERE department = 'IT';

-- Q11
SELECT * FROM employees_lab
WHERE department IN ('IT','HR');

-- Q12
SELECT * FROM employees_lab
WHERE salary > 60000 AND department = 'IT';

-- Q13
SELECT DISTINCT department FROM employees_lab;

-- Q14
SELECT department, COUNT(*) 
FROM employees_lab
GROUP BY department;

-- Q15
SELECT department, COUNT(*) 
FROM employees_lab
GROUP BY department
HAVING COUNT(*) > 2;

-- Q16
SELECT * FROM employees_lab
ORDER BY salary DESC;

-- Q17
SELECT * FROM employees_lab
LIMIT 5;

-- Q18
SELECT * FROM employees_lab
LIMIT 5 OFFSET 5;

-- Q19
UPDATE employees_lab
SET salary = 75000
WHERE emp_name = 'Raj';

-- Q20
UPDATE employees_lab
SET salary = salary + 1000;

-- Part E – DELETE Operations

-- Q21
DELETE FROM employees_lab
WHERE emp_name = 'Lokesh';

-- Q22
DELETE FROM employees_lab;

-- Part F – MySQL Special Commands

-- Q23
REPLACE INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(1,'Ravi','IT',60000,25,'2022-01-10');

-- Q24
INSERT INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(2,'Raj','IT',65000,28,'2021-03-12')
ON DUPLICATE KEY UPDATE salary = 65000;

-- Q25
INSERT INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(30,'Nikhil','HR',55000,27,'2023-02-01')
ON DUPLICATE KEY UPDATE salary = VALUES(salary);

-- Q26
INSERT INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(1,'Ravi','IT',80000,25,'2022-01-10')
ON DUPLICATE KEY UPDATE salary = 80000;

-- Q27
INSERT INTO employees_lab
(emp_id, emp_name, department, salary, age, joining_date)
VALUES
(31,'Varun','Sales',62000,29,'2022-04-15')
ON DUPLICATE KEY UPDATE salary = VALUES(salary);


-- Q28
SELECT * FROM employees_lab
WHERE salary BETWEEN 50000 AND 70000;

-- Q29
SELECT * FROM employees_lab
WHERE emp_name LIKE 'R%';

-- Q30
SELECT * FROM employees_lab
WHERE department <> 'Finance';