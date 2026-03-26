-- 1. create a student table and insert the records from 1st Jan to till data as 
--    a joining date.( around 20 records with different dates).
CREATE TABLE students_join (
slno INT PRIMARY KEY,
name VARCHAR(50),
joining_date DATE
);
INSERT INTO students_join VALUES
(1,'Ravi','2026-01-01'),
(2,'Anil','2026-01-05'),
(3,'Kiran','2026-01-10'),
(4,'Sai','2026-01-15'),
(5,'Rahul','2026-01-20'),
(6,'Arjun','2026-01-25'),
(7,'Pavan','2026-02-01'),
(8,'Ramesh','2026-02-05'),
(9,'Suresh','2026-02-10'),
(10,'Naresh','2026-02-15'),
(11,'Vikram','2026-02-20'),
(12,'Ajay','2026-02-25'),
(13,'Mahesh','2026-03-01'),
(14,'Tarun','2026-03-05'),
(15,'Deepak','2026-03-10'),
(16,'Nikhil','2026-03-12'),
(17,'Harish','2026-03-15'),
(18,'Karthik','2026-03-18'),
(19,'Rohit','2026-03-20'),
(20,'Manoj','2026-03-22');


-- 2. write a query to display students information who joined from last 30 days
SELECT * 
FROM students_join
WHERE joining_date >= CURDATE() - INTERVAL 30 DAY;

-- 3. create a student table with the following columns 
-- 	slno, name, mm , pm, cm 

CREATE TABLE students_marks (
slno INT PRIMARY KEY,
name VARCHAR(50),
mm INT,
pm INT,
cm INT
);


-- 4. insert the records in student table only into the following columns 
--	slno, name, mm,pm,cm 

INSERT INTO students_marks (slno, name, mm, pm, cm) VALUES
(1,'Ravi',80,70,60),
(2,'Anil',50,45,40),
(3,'Kiran',90,85,88),
(4,'Sai',30,35,25),
(5,'Rahul',60,55,50);
    
    
-- 5. write a query to display student information along with tm, avgmarks,and result 
--   of the student like Pass / Failed, 
 --  if pass then distinction / First class / Second Class / third class
 SELECT 
slno,
name,
mm, pm, cm,
(mm+pm+cm) AS total_marks,
(mm+pm+cm)/3 AS avg_marks,
CASE
WHEN mm<35 OR pm<35 OR cm<35 THEN 'Fail'
ELSE 'Pass'
END AS result,
CASE
WHEN mm<35 OR pm<35 OR cm<35 THEN 'No Class'
WHEN (mm+pm+cm)/3 >= 75 THEN 'Distinction'
WHEN (mm+pm+cm)/3 >= 60 THEN 'First Class'
WHEN (mm+pm+cm)/3 >= 50 THEN 'Second Class'
ELSE 'Third Class'
END AS class
FROM students_marks;