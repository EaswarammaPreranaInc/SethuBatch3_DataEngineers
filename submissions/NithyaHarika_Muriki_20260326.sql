-- Create the EMP_DTLS table
CREATE TABLE EMP_DTLS (
    EMPNO int,
    ENAME VARCHAR(30),
    JOB VARCHAR(20),
    COUNTRY_CODE VARCHAR(5)
);

-- 5. Insert multiple records into EMP_DTLS
INSERT into EMP_DTLS VALUES (101, 'RAJ', 'IT', 'US'),(102, 'RAM', 'MED', 'US'),
     (103, 'RAKI', 'MECH', 'AUS'),
    (104, 'ABC', 'MECH', 'IND'),
    (105, 'XYZ', 'IT', 'IND');
SELECT * FROM DUAL;

-- 6. Create COUNTRY_DETAILS table
CREATE TABLE COUNTRY_DETAILS (
    COUNTRY_CODE VARCHAR(5),
    COUNTRY_NAME VARCHAR(30),
    CODE VARCHAR(5)
);

-- Insert records into COUNTRY_DETAILS
INSERT INTO COUNTRY_DETAILS VALUES ('US', 'United States', '01'),
    ('AUS', 'Australia', '61'),
    ('MAL', 'MALAYSIA', '65'),
   ('IND', 'INDIA', '91');
SELECT * FROM DUAL;

-- 1. Write a query to display department details which contains employees.
-- (Using EXISTS to find departments that have at least one matching entry in EMP)
SELECT * FROM DEPT D
WHERE EXISTS (SELECT 1 FROM EMP E WHERE E.DEPTNO = D.DEPTNO);

-- 2. Write a query to display employees information whose sal is greater than or equal to sum of sal of each department.
-- (This compares individual salary against the total sum of all departments combined)
SELECT * FROM EMP 
WHERE SAL >= (SELECT SUM(SAL) FROM EMP);

-- 3. Write a query to display the department information which contains more than 3 employees.
-- (Grouping by DEPTNO and using HAVING to filter the count)
SELECT * FROM DEPT 
WHERE DEPTNO IN (
    SELECT DEPTNO FROM EMP 
    GROUP BY DEPTNO 
    HAVING COUNT(*) > 3
);

-- 4. Write a query to display the max sal who is working as clerks in 20 department.
SELECT MAX(SAL) AS MAX_CLERK_SAL 
FROM EMP 
WHERE JOB = 'CLERK' AND DEPTNO = 20;

-- 7. Write a query to display employees information who are working as IT in INDIA and MECH from AUS.
-- (Joining the tables and using OR to handle both conditions)
SELECT E.* FROM EMP_DTLS E
JOIN COUNTRY_DETAILS C ON E.COUNTRY_CODE = C.COUNTRY_CODE
WHERE (E.JOB = 'IT' AND C.COUNTRY_NAME = 'INDIA')
   OR (E.JOB = 'MECH' AND C.COUNTRY_NAME = 'Australia');

-- 8. The current existing query as below, in that add a new column to display country name
-- Existing Query: SELECT * from emp_dtls;
-- Modified Query:
SELECT E.*, C.COUNTRY_NAME 
FROM EMP_DTLS E
LEFT JOIN COUNTRY_DETAILS C ON E.COUNTRY_CODE = C.COUNTRY_CODE;