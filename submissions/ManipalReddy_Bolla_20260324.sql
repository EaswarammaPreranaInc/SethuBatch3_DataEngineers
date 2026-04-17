 -- 1. Create student table and insert 20 records with joining dates from Jan 1st to today
--Create student table
CREATE TABLE student_new (
    slno INT PRIMARY KEY,
    name VARCHAR(100),
    joining_date DATE
);
--Insert 20 records with 2026 dates
INSERT INTO student_new (slno, name, joining_date) VALUES
(1, 'Aarav Reddy', '2026-01-02'),
(2, 'Ishani Sharma', '2026-01-08'),
(3, 'Vihaan Gupta', '2026-01-15'),
(4, 'Myra Kapoor', '2026-01-22'),
(5, 'Sai Teja', '2026-01-29'),
(6, 'Ananya Verma', '2026-02-03'),
(7, 'Karthik Rao', '2026-02-10'),
(8, 'Diya Menon', '2026-02-14'),
(9, 'Rohan Malhotra', '2026-02-20'),
(10, 'Sana Khan', '2026-02-25'),
(11, 'Pranav Joshi', '2026-03-01'),
(12, 'Kavya Nair', '2026-03-04'),
(13, 'Manish Yadav', '2026-03-08'),
(14, 'Ritika Singh', '2026-03-12'),
(15, 'Arjun Deshmukh', '2026-03-15'),
(16, 'Zoya Ahmed', '2026-03-18'),
(17, 'Abhinav Patil', '2026-03-22'),
(18, 'Tanvi Bhatia', '2026-03-25'),
(19, 'Siddharth Jain', '2026-03-28'),
(20, 'Meera Iyer', '2026-03-30');

-- 2. Query to display students who joined in last 30 days
SELECT * FROM student_new 
WHERE joining_date >= DATEADD(DAY, -30, CAST(GETDATE() AS DATE));

-- 3 & 4. Create and insert into student table
-- Create table for marks
CREATE TABLE student_marks (
    slno INT PRIMARY KEY,
    name VARCHAR(100),
    mm INT, -- Maths Marks
    pm INT, -- Physics Marks
    cm INT  -- Chemistry Marks
);
-- Insert new records
INSERT INTO student_marks (slno, name, mm, pm, cm) VALUES
(1, 'Abhishek Murthy', 45, 52, 48),
(2, 'Priyanka Das', 88, 91, 85),
(3, 'Rahul Saxena', 35, 40, 38),
(4, 'Sushmita Sen', 72, 65, 68),
(5, 'Vikram Rathore', 55, 58, 60);

-- 5. Query to display student info with total marks, average marks, and result/class
SELECT 
    slno, 
    name, 
    mm, 
    pm, 
    cm,
    (mm + pm + cm) AS tm,
    ROUND((mm + pm + cm) / 3.0, 2) AS avgmarks,
    CASE 
        WHEN (mm + pm + cm) / 3.0 >= 40 THEN 
            CASE 
                WHEN (mm + pm + cm) / 3.0 >= 75 THEN 'Pass - Distinction'
                WHEN (mm + pm + cm) / 3.0 >= 60 THEN 'Pass - First Class'
                WHEN (mm + pm + cm) / 3.0 >= 50 THEN 'Pass - Second Class'
                ELSE 'Pass - Third Class'
            END
        ELSE 'Failed'
    END AS result
FROM student_marks;