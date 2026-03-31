3.3.26
# 1. Write a query to display department details which contains employees.

SELECT d.*
FROM dept d
WHERE d.deptno IN (
    SELECT DISTINCT deptno FROM emp
);

# ------------------------------------------------------------

# 2. Write a query to display employees information whose sal 
# is greater than or equal to sum of sal of each department.

SELECT *
FROM emp e
WHERE e.sal >= ALL (
    SELECT SUM(sal)
    FROM emp
    GROUP BY deptno
);

# ------------------------------------------------------------

# 3. write a query to display the department information 
# which contains more than 3 employees.

SELECT d.*
FROM dept d
WHERE d.deptno IN (
    SELECT deptno
    FROM emp
    GROUP BY deptno
    HAVING COUNT(*) > 3
);

# ------------------------------------------------------------

# 4. write a query to display the max sal who is working 
# as clerks in 20 department.

SELECT MAX(sal) AS max_salary
FROM emp
WHERE job = 'CLERK'
AND deptno = 20;

# ------------------------------------------------------------

# 5. create a table emp_dtls with the below columns and insert data

CREATE TABLE emp_dtls (
    empno INT,
    ename VARCHAR(50),
    job VARCHAR(50),
    country_code VARCHAR(10)
);

INSERT INTO emp_dtls VALUES
(101, 'RAJ',  'IT',   'US'),
(102, 'RAM',  'MED',  'US'),
(103, 'RAKI', 'MECH', 'AUS'),
(104, 'ABC',  'MECH', 'IND'),
(105, 'XYZ',  'IT',   'IND');

# ------------------------------------------------------------

# 6. create a table country_details

CREATE TABLE country_details (
    country_code VARCHAR(10),
    country_name VARCHAR(50),
    code INT
);

INSERT INTO country_details VALUES
('US',  'United States', 01),
('AUS', 'Australia',     61),
('MAL', 'Malaysia',      65);

# ------------------------------------------------------------

# 7. Write a query to display employees information who are 
# working as IT in INDIA and MECH from AUS.

SELECT *
FROM emp_dtls
WHERE (job = 'IT' AND country_code = 'IND')
   OR (job = 'MECH' AND country_code = 'AUS');

# ------------------------------------------------------------

# 8. Add a new column to display country name in existing query

SELECT e.*, c.country_name
FROM emp_dtls e
LEFT JOIN country_details c
ON e.country_code = c.country_code;

# ------------------------------------------------------------





# ============================================================
#9. OUTER JOIN (Left Outer Join using Oracle (+))

SELECT d.deptno, dname, loc, ename
FROM dept d, emp e
WHERE d.deptno = e.deptno(+);


# ============================================================
# 10. Create table using another table (Full backup)


CREATE TABLE emp_bkp AS
SELECT * FROM emp;


# ============================================================
# 11. Update NULL values


UPDATE emp
SET comm = 100
WHERE comm IS NULL;


# ============================================================
# 12. Create table with selected columns


CREATE TABLE emp_bkp2 AS
SELECT empno, ename, job FROM emp;

SELECT * FROM emp_bkp2;


# ============================================================
# 13. Create table structure only (No data)


CREATE TABLE emp_bkp3 AS
SELECT * FROM emp WHERE 1 = 2;


# ============================================================
# 14. Insert data into empty table
INSERT INTO emp_bkp3
SELECT * FROM emp;


# ============================================================
# 15. Insert specific columns into another table


INSERT INTO emp_bkp2
SELECT empno, ename, job FROM emp;

# ============================================================