1. create a student table and insert the records from 1st Jan to till data as 
   a joining date.( around 20 records with different dates).
Answer:
CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    course VARCHAR(50),
    joining_date DATE
);
#Insert Records (20 rows with different dates)
INSERT INTO student VALUES
(1, 'Ravi', 'CSE', '2026-01-01'),
(2, 'Sita', 'ECE', '2026-01-03'),
(3, 'Arjun', 'EEE', '2026-01-05'),
(4, 'Meena', 'CSE', '2026-01-08'),
(5, 'Kiran', 'IT', '2026-01-10'),
(6, 'Anu', 'CSE', '2026-01-12'),
(7, 'Rahul', 'ECE', '2026-01-15'),
(8, 'Divya', 'EEE', '2026-01-18'),
(9, 'Vikram', 'IT', '2026-01-20'),
(10, 'Sneha', 'CSE', '2026-01-22'),
(11, 'Ajay', 'ECE', '2026-01-25'),
(12, 'Pooja', 'EEE', '2026-01-28'),
(13, 'Nikhil', 'IT', '2026-02-01'),
(14, 'Lakshmi', 'CSE', '2026-02-05'),
(15, 'Teja', 'ECE', '2026-02-10'),
(16, 'Keerthi', 'EEE', '2026-02-15'),
(17, 'Manoj', 'IT', '2026-02-20'),
(18, 'Swathi', 'CSE', '2026-03-01'),
(19, 'Ramesh', 'ECE', '2026-03-10'),
(20, 'Geetha', 'IT', '2026-03-20');

SELECT * FROM student;

2. write a query to display students information who joined from last 30 days
Answer:
SELECT *
FROM student
WHERE joining_date >= SYSDATE - 30;

3. create a student table with the following columns 
	slno, name, mm , pm, cm 
Answer:
CREATE TABLE student (
    slno NUMBER PRIMARY KEY,
    name VARCHAR2(50),
    mm NUMBER,   
    pm NUMBER,   
    cm NUMBER    
);

4. insert the records in student table only into the following columns 
	slno, name, mm,pm,cm 
Answer:	
INSERT INTO student (slno, name, mm, pm, cm) VALUES (1, 'Ravi', 85, 78, 90);
INSERT INTO student (slno, name, mm, pm, cm) VALUES (2, 'Sita', 92, 88, 95);
INSERT INTO student (slno, name, mm, pm, cm) VALUES (3, 'Arjun', 75, 80, 70);
INSERT INTO student (slno, name, mm, pm, cm) VALUES (4, 'Meena', 88, 91, 84);
INSERT INTO student (slno, name, mm, pm, cm) VALUES (5, 'Kiran', 60, 65, 70);
INSERT INTO student (slno, name, mm, pm, cm) VALUES (6, 'Anu', 95, 89, 93);
INSERT INTO student (slno, name, mm, pm, cm) VALUES (7, 'Rahul', 70, 72, 68);
INSERT INTO student (slno, name, mm, pm, cm) VALUES (8, 'Divya', 85, 87, 90);
INSERT INTO student (slno, name, mm, pm, cm) VALUES (9, 'Vikram', 78, 75, 80);
INSERT INTO student (slno, name, mm, pm, cm) VALUES (10, 'Sneha', 90, 92, 94);

5. write a query to display student information along with tm, avgmarks,and result 
   of the student like Pass / Failed, 
   if pass then distinction / First class / Second Class / third class 
Answer:
SELECT 
    slno,
    name,
    mm,
    pm,
    cm,
    (mm + pm + cm) AS tm,
    ROUND((mm + pm + cm)/3, 2) AS avgmarks,
    CASE
        WHEN mm < 35 OR pm < 35 OR cm < 35 THEN 'Fail'
        WHEN (mm + pm + cm)/3 >= 75 THEN 'Pass - Distinction'
        WHEN (mm + pm + cm)/3 >= 60 THEN 'Pass - First Class'
        WHEN (mm + pm + cm)/3 >= 50 THEN 'Pass - Second Class'
        ELSE 'Pass - Third Class'
    END AS result
FROM student;