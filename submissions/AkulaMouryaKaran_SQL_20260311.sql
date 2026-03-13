USE joinsdb;
SELECT DATABASE();

CREATE TABLE employees_demo(
	emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT
);

INSERT INTO employees_demo VALUES
	(1,'John',101),
	(2,'Mary',102),
	(3,'David',103),
	(4,'Sophia',104),
	(5,'Micheal',105)
;
CREATE TABLE departments_demo(
	dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);



