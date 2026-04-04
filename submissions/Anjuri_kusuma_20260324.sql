#1. create a student table and insert the records from 1st Jan to till data as 
 #  a joining date.( around 20 records with different dates).
 CREATE TABLE STUDENT1 (
    slno int PRIMARY KEY,
    name VARCHAR(30),
    JOIN_DATE DATE
);
INSERT INTO STUDENT1 VALUES (1, 'RAJA', CURDATE()-5);
INSERT INTO STUDENT1 VALUES (2, 'RAM', CURDATE()-interval 10 day);
INSERT INTO STUDENT1 VALUES (3, 'MOHAN', CURDATE()-interval 15 day);
INSERT INTO STUDENT1 VALUES (4, 'KIRAN', CURDATE()-interval 20 day);
INSERT INTO STUDENT1 VALUES (5, 'ARUN', CURDATE()-interval 25 day);
INSERT INTO STUDENT1 VALUES (6, 'VARUN', CURDATE()-interval 30 day);
INSERT INTO STUDENT1 VALUES (7, 'AJAY', CURDATE()-interval 35 day);
INSERT INTO STUDENT1 VALUES (8, 'VIJAY', CURDATE()-interval 40 day);
INSERT INTO STUDENT1 VALUES (9, 'SUNIL', CURDATE()-interval 45 day);
INSERT INTO STUDENT1 VALUES (10, 'ANIL', CURDATE()-interval 50 day);
INSERT INTO STUDENT1 VALUES (11, 'RAVI', CURDATE()-interval 3 day);
INSERT INTO STUDENT1 VALUES (12, 'KUMAR', CURDATE()-interval 7 day);
INSERT INTO STUDENT1 VALUES (13, 'SURESH', CURDATE()-interval 12 day);
INSERT INTO STUDENT1 VALUES (14, 'MAHESH', CURDATE()-interval 18 day);
INSERT INTO STUDENT1 VALUES (15, 'GANESH', CURDATE()-interval 22 day);
INSERT INTO STUDENT1 VALUES (16, 'LOKESH', CURDATE()-interval 28 day);
INSERT INTO STUDENT1 VALUES (17, 'NAVEEN', CURDATE()-interval 32 day);
INSERT INTO STUDENT1 VALUES (18, 'PRAVEEN', CURDATE()-interval 38 day);
INSERT INTO STUDENT1 VALUES (19, 'DINESH', CURDATE()-interval 42 day);
INSERT INTO STUDENT1 VALUES (20, 'RAMESH', CURDATE()-interval 48 day);

#3. create a student table with the following columns 
#	slno, name, mm , pm, cm 
CREATE TABLE STUDENT2 (
    slno int PRIMARY KEY,
    NAME VARCHAR(30),
    MM int,
    PM int,
    CM int
);


#4. insert the records in student table only into the following columns 
#	slno, name, mm,pm,cm 
INSERT INTO STUDENT2 (SLNO, NAME, MM, PM, CM)
VALUES (1, 'RAJA', 80, 75, 70);
INSERT INTO STUDENT2 (SLNO, NAME, MM, PM, CM)
VALUES (2, 'RAM', 60, 65, 55);
INSERT INTO STUDENT2 (SLNO, NAME, MM, PM, CM)
VALUES (3, 'MOHAN', 40, 35, 45);
INSERT INTO STUDENT2 (SLNO, NAME, MM, PM, CM)
VALUES (4, 'KIRAN', 90, 92, 88);
INSERT INTO STUDENT2 (SLNO, NAME, MM, PM, CM)
VALUES (5, 'ARUN', 30, 25, 20);


#5. write a query to display student information along with tm, avgmarks,and result 
  # of the student like Pass / Failed, 
   #if pass then distinction / First class / Second Class / third class 
   SELECT 
SLNO,
NAME,
MM,
PM,
CM,
(MM + PM + CM) AS TM,
ROUND((MM + PM + CM)/3, 2) AS AVG,
CASE 
    WHEN MM < 35 OR PM < 35 OR CM < 35 THEN 'FAILED'
    WHEN (MM + PM + CM)/3 >= 75 THEN 'DISTINCTION'
    WHEN (MM + PM + CM)/3 >= 60 THEN 'FIRST CLASS'
    WHEN (MM + PM + CM)/3 >= 50 THEN 'SECOND CLASS'
    ELSE 'THIRD CLASS'
END AS RESULT
FROM STUDENT2;


