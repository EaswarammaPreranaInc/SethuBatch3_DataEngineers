1. create a student table and insert the records from 1st Jan to till data as 
a joining date.( around 20 records with different dates).
CREATE TABLE student1 (
    slno NUMBER,
    name VARCHAR2(30),
    join_date DATE
);
INSERT INTO student1 VALUES (1, 'Pooja', DATE '2026-05-01'),
(2, 'Subbu', DATE '2026-05-02'), (3, 'Deepak', DATE '2026-02-03'),
(4, 'Dinesh', DATE '2026-02-04'),(5, 'Shiva', DATE '2026-08-10'),
(6, 'Suma', DATE '2026-01-06'),(7, 'Gangadri', DATE '2026-01-07'),
(8, 'Anil', DATE '2026-01-08'),(9, 'Akhil', DATE '2026-01-09'),
(10, 'Nikhil', DATE '2026-01-10'),(11, 'Praneel', DATE '2026-01-11'),
(12, 'Harini', DATE '2026-01-12'),(13, 'Vijay', DATE '2026-01-13'),
(14, 'Kalyan', DATE '2026-01-14'),(15, 'Vinay', DATE '2026-01-15'),
(16, 'Killer', DATE '2026-01-16'),(17, 'Latha', DATE '2026-01-17'),
(18, 'Lakshmi', DATE '2026-01-18'),(19, 'Narayana', DATE '2026-01-19'),
(20, 'Jyothi', DATE '2026-01-20');



   
2. write a query to display students information who joined from last 30 days
SELECT *
FROM student1
WHERE MONTHS_BETWEEN(sysdate,joindate) <= 1;



3. create a student table with the following columns slno, name, mm , pm, cm
CREATE TABLE student (
    slno NUMBER,
    name VARCHAR2(30),
    mm NUMBER,
    pm NUMBER,
    cm NUMBER
); 



	
 4. insert the records in student table only into the following columns slno, name, mm,pm,cm 
INSERT INTO student (slno, name, mm, pm, cm)
VALUES (1, 'Pooja', 80, 70, 60);

INSERT INTO student (slno, name, mm, pm, cm)
VALUES (2, 'Subbu', 50, 55, 45);	



 5. write a query to display student information along with tm, avgmarks,and result of the student like Pass / Failed, 
   if pass then distinction / First class / Second Class / third class 
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