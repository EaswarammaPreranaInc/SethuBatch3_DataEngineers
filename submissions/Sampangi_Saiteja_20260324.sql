
#24.3.26
# ============================================================
# 1. Create STUDENT table and insert ~20 records with different joining dates
# ============================================================

CREATE TABLE student (
    slno INT,
    name VARCHAR(50),
    joining_date DATE
);

# Insert records (example dates from Jan 1 to current range)

INSERT INTO student VALUES (1, 'A', DATE '2026-01-01');
INSERT INTO student VALUES (2, 'B', DATE '2026-01-05');
INSERT INTO student VALUES (3, 'C', DATE '2026-01-10');
INSERT INTO student VALUES (4, 'D', DATE '2026-01-15');
INSERT INTO student VALUES (5, 'E', DATE '2026-01-20');
INSERT INTO student VALUES (6, 'F', DATE '2026-01-25');
INSERT INTO student VALUES (7, 'G', DATE '2026-02-01');
INSERT INTO student VALUES (8, 'H', DATE '2026-02-05');
INSERT INTO student VALUES (9, 'I', DATE '2026-02-10');
INSERT INTO student VALUES (10, 'J', DATE '2026-02-15');
INSERT INTO student VALUES (11, 'K', DATE '2026-02-20');
INSERT INTO student VALUES (12, 'L', DATE '2026-02-25');
INSERT INTO student VALUES (13, 'M', DATE '2026-03-01');
INSERT INTO student VALUES (14, 'N', DATE '2026-03-05');
INSERT INTO student VALUES (15, 'O', DATE '2026-03-10');
INSERT INTO student VALUES (16, 'P', DATE '2026-03-15');
INSERT INTO student VALUES (17, 'Q', DATE '2026-03-18');
INSERT INTO student VALUES (18, 'R', DATE '2026-03-20');
INSERT INTO student VALUES (19, 'S', DATE '2026-03-25');
INSERT INTO student VALUES (20, 'T', DATE '2026-03-30');


# ============================================================
# 2. Display students who joined in last 30 days
# ============================================================

SELECT *
FROM student
WHERE joining_date >= SYSDATE - 30;


# ============================================================
# 3. Create student table with marks columns
# ============================================================

CREATE TABLE student_marks (
    slno INT,
    name VARCHAR(50),
    mm INT,   # Maths marks
    pm INT,   # Physics marks
    cm INT    # Chemistry marks
);


# ============================================================
# 4. Insert records into specific columns
# ============================================================

INSERT INTO student_marks (slno, name, mm, pm, cm) VALUES (1, 'RAJ', 80, 70, 60);
INSERT INTO student_marks (slno, name, mm, pm, cm) VALUES (2, 'RAM', 90, 85, 88);
INSERT INTO student_marks (slno, name, mm, pm, cm) VALUES (3, 'RAKI', 50, 45, 40);
INSERT INTO student_marks (slno, name, mm, pm, cm) VALUES (4, 'ABC', 35, 30, 25);
INSERT INTO student_marks (slno, name, mm, pm, cm) VALUES (5, 'XYZ', 70, 75, 80);


# ============================================================
# 5. Display student info with TM, AVG, RESULT & CLASS
# ============================================================

SELECT 
    slno,
    name,
    mm,
    pm,
    cm,

    # Total Marks
    (mm + pm + cm) AS total_marks,

    # Average Marks
    (mm + pm + cm)/3 AS avg_marks,

    # Result (Pass/Fail)
    CASE 
        WHEN mm < 35 OR pm < 35 OR cm < 35 THEN 'FAIL'
        ELSE 'PASS'
    END AS result,

    # Classification
    CASE 
        WHEN mm < 35 OR pm < 35 OR cm < 35 THEN 'FAIL'
        WHEN (mm + pm + cm)/3 >= 75 THEN 'DISTINCTION'
        WHEN (mm + pm + cm)/3 >= 60 THEN 'FIRST CLASS'
        WHEN (mm + pm + cm)/3 >= 50 THEN 'SECOND CLASS'
        ELSE 'THIRD CLASS'
    END AS class

FROM student_marks;

# ============================================================