-- 1. create a student table and insert the records from 1st Jan to till data as 
--    a joining date.( around 20 records with different dates).
CREATE TABLE student1 (
    slno NUMBER,
    name VARCHAR2(30),
    join_date DATE
);
INSERT INTO student1 VALUES (1, 'Amit', DATE '2026-01-01');
INSERT INTO student1 VALUES (2, 'Ravi', DATE '2026-01-02');
INSERT INTO student1 VALUES (3, 'Sita', DATE '2026-01-03');
INSERT INTO student1 VALUES (4, 'John', DATE '2026-01-04');
INSERT INTO student1 VALUES (5, 'Neha', DATE '2026-01-05');
INSERT INTO student1 VALUES (6, 'Arjun', DATE '2026-01-06');
INSERT INTO student1 VALUES (7, 'Priya', DATE '2026-01-07');
INSERT INTO student1 VALUES (8, 'Kiran', DATE '2026-01-08');
INSERT INTO student1 VALUES (9, 'Meena', DATE '2026-01-09');
INSERT INTO student1 VALUES (10, 'Rahul', DATE '2026-01-10');
INSERT INTO student1 VALUES (11, 'Anil', DATE '2026-01-11');
INSERT INTO student1 VALUES (12, 'Divya', DATE '2026-01-12');
INSERT INTO student1 VALUES (13, 'Vijay', DATE '2026-01-13');
INSERT INTO student1 VALUES (14, 'Pooja', DATE '2026-01-14');
INSERT INTO student1 VALUES (15, 'Suresh', DATE '2026-01-15');
INSERT INTO student1 VALUES (16, 'Lakshmi', DATE '2026-01-16');
INSERT INTO student1 VALUES (17, 'Manoj', DATE '2026-01-17');
INSERT INTO student1 VALUES (18, 'Sneha', DATE '2026-01-18');
INSERT INTO student1 VALUES (19, 'Ramesh', DATE '2026-01-19');
INSERT INTO student1 VALUES (20, 'Keerthi', DATE '2026-01-20');
   
-- 2. write a query to display students information who joined from last 30 days
SELECT *
FROM student1
WHERE MONTHS_BETWEEN(sysdate,joindate) <= 1;

-- 3. create a student table with the following columns 
-- 	slno, name, mm , pm, cm
CREATE TABLE student (
    slno NUMBER,
    name VARCHAR2(30),
    mm NUMBER,
    pm NUMBER,
    cm NUMBER
); 
	
-- 4. insert the records in student table only into the following columns 
-- 	slno, name, mm,pm,cm 
INSERT INTO student (slno, name, mm, pm, cm)
VALUES (1, 'Amit', 80, 70, 60);

INSERT INTO student (slno, name, mm, pm, cm)
VALUES (2, 'Ravi', 50, 55, 45);	
-- 5. write a query to display student information along with tm, avgmarks,and result 
--    of the student like Pass / Failed, 
--    if pass then distinction / First class / Second Class / third class 
SELECT slno, name, mm, pm,cm,
    (mm + pm + cm) AS total_marks,
    ROUND((mm + pm + cm)/3, 2) AS avg_marks,
    (CASE WHEN (mm < 40 OR pm < 40 OR cm < 40) THEN 'Fail'
        WHEN (mm + pm + cm)/3 >= 75 THEN 'Distinction'
        WHEN (mm + pm + cm)/3 >= 60 THEN 'First Class'
        WHEN (mm + pm + cm)/3 >= 50 THEN 'Second Class'
        WHEN (mm + pm + cm)/3 >= 40 THEN 'Third Class'
        ELSE 'Fail'
    END ) result
FROM student;