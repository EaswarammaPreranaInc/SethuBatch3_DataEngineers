1. create a student table and insert the records from 1st Jan to till data as 
a joining date.( around 20 records with different dates).
CREATE TABLE student1 (
    slno NUMBER,
    name VARCHAR2(30),
    join_date DATE
);
INSERT INTO student1 VALUES (1, 'Prabha', DATE '2026-05-01');
INSERT INTO student1 VALUES (2, 'Subbu', DATE '2026-05-02');
INSERT INTO student1 VALUES (3, 'Deepak', DATE '2026-02-03');
INSERT INTO student1 VALUES (4, 'Dinesh', DATE '2026-02-04');
INSERT INTO student1 VALUES (5, 'Shiva', DATE '2026-08-10');
INSERT INTO student1 VALUES (6, 'Suma', DATE '2026-01-06');
INSERT INTO student1 VALUES (7, 'Gangadri', DATE '2026-01-07');
INSERT INTO student1 VALUES (8, 'Anil', DATE '2026-01-08');
INSERT INTO student1 VALUES (9, 'Akhil', DATE '2026-01-09');