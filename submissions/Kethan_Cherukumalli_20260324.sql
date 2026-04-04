/*1. create a student table and insert the records from 1st Jan to till data as 
   a joining date.( around 20 records with different dates).
   
2. write a query to display students information who joined from last 30 days

3. create a student table with the following columns 
	slno, name, mm , pm, cm 
	
4. insert the records in student table only into the following columns 
	slno, name, mm,pm,cm 
	
5. write a query to display student information along with tm, avgmarks,and result 
   of the student like Pass / Failed, 
   if pass then distinction / First class / Second Class / third class */

-- Create the Database environment
CREATE DATABASE SchoolDB;

-- 1 & 3. Create a student table with: slno, name, mm (Maths), pm (Physics), cm (Chemistry), and joining_date
CREATE TABLE STUDENT (
    SLNO NUMBER PRIMARY KEY,
    SNAME VARCHAR2(30),
    MM NUMBER,
    PM NUMBER,
    CM NUMBER,
    JOINING_DATE DATE
);

-- 4. Insert 20 records into student table with different joining dates from 1st Jan 2026 to till date
-- Note: 'TO_DATE' is used to ensure the format is handled correctly.
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (1, 'Arjun', 85, 90, 88, TO_DATE('2026-01-05', 'YYYY-MM-DD'));
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (2, 'Sneha', 45, 38, 40, TO_DATE('2026-01-12', 'YYYY-MM-DD'));
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (3, 'Vikram', 72, 65, 70, TO_DATE('2026-01-20', 'YYYY-MM-DD'));
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (4, 'Priya', 92, 95, 98, TO_DATE('2026-02-02', 'YYYY-MM-DD'));
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (5, 'Rohan', 30, 32, 28, TO_DATE('2026-02-10', 'YYYY-MM-DD'));
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (6, 'Anjali', 60, 55, 58, TO_DATE('2026-02-15', 'YYYY-MM-DD'));
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (7, 'Rahul', 88, 82, 85, TO_DATE('2026-02-25', 'YYYY-MM-DD'));
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (8, 'Meera', 52, 48, 50, TO_DATE('2026-03-01', 'YYYY-MM-DD'));
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (9, 'Karan', 78, 75, 77, TO_DATE('2026-03-05', 'YYYY-MM-DD'));
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (10, 'Sonia', 40, 42, 45, TO_DATE('2026-03-10', 'YYYY-MM-DD'));
-- Records joining within the last 30 days (assuming current date is March 24, 2026)
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (11, 'Amit', 95, 96, 94, SYSDATE - 5);
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (12, 'Deepa', 66, 60, 62, SYSDATE - 10);
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (13, 'Vijay', 33, 35, 30, SYSDATE - 15);
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (14, 'Neeta', 81, 79, 83, SYSDATE - 18);
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (15, 'Yash', 44, 46, 48, SYSDATE - 20);
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (16, 'Ishita', 70, 72, 74, SYSDATE - 22);
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (17, 'Abhi', 59, 57, 55, SYSDATE - 25);
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (18, 'Tara', 91, 89, 90, SYSDATE - 27);
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (19, 'Sagar', 38, 40, 42, SYSDATE - 28);
INSERT INTO STUDENT (SLNO, SNAME, MM, PM, CM, JOINING_DATE) VALUES (20, 'Riya', 75, 78, 80, SYSDATE - 29);

-- 2. Write a query to display students information who joined from last 30 days
SELECT * FROM STUDENT 
WHERE JOINING_DATE >= SYSDATE - 30;

-- 5. Write a query to display student information along with tm (Total Marks), avgmarks, and result 
-- (Pass/Failed, and if pass: Distinction/First Class/Second Class/Third Class)
-- We assume 35 is the passing mark for each subject.
SELECT 
    SLNO, 
    SNAME, 
    (MM + PM + CM) AS TM, 
    (MM + PM + CM) / 3 AS AVG_MARKS,
    CASE 
        WHEN MM < 35 OR PM < 35 OR CM < 35 THEN 'FAILED'
        ELSE 'PASS'
    END AS RESULT,
    CASE 
        WHEN MM < 35 OR PM < 35 OR CM < 35 THEN 'N/A'
        WHEN (MM + PM + CM) / 3 >= 75 THEN 'Distinction'
        WHEN (MM + PM + CM) / 3 >= 60 THEN 'First Class'
        WHEN (MM + PM + CM) / 3 >= 50 THEN 'Second Class'
        ELSE 'Third Class'
    END AS CLASS_CATEGORY
FROM STUDENT;