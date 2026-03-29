-- 1. Department details which contain employees
SELECT * FROM DEPT d
WHERE EXISTS (SELECT 1 FROM EMP e WHERE e.DEPTNO = d.DEPTNO);

-- 2. Employees whose salary is greater than or equal to the total salary of ANY department
SELECT * FROM EMP 
WHERE SAL >= ANY (SELECT SUM(SAL) FROM EMP GROUP BY DEPTNO);

-- 3. Department information containing more than 3 employees
SELECT DEPTNO, COUNT(*) 
FROM EMP 
GROUP BY DEPTNO 
HAVING COUNT(*) > 3;

-- 4. Max salary for CLERKS in department 20
SELECT MAX(SAL) AS MAX_CLERK_SAL
FROM EMP 
WHERE JOB = 'CLERK' AND DEPTNO = 20;

-- 5. Create and Insert: emp_dtls
CREATE TABLE emp_dtls (
    EMPNO NUMBER(3),
    ENAME VARCHAR2(20),
    JOB VARCHAR2(20),
    COUNTRY_CODE VARCHAR2(5)
);

INSERT ALL 
    INTO emp_dtls VALUES (101, 'RAJ', 'IT', 'US')
    INTO emp_dtls VALUES (102, 'RAM', 'MED', 'US')
    INTO emp_dtls VALUES (103, 'RAKI', 'MECH', 'AUS')
    INTO emp_dtls VALUES (104, 'ABC', 'MECH', 'IND')
    INTO emp_dtls VALUES (105, 'XYZ', 'IT', 'IND')
SELECT * FROM dual;

-- 6. Create and Insert: country_details
CREATE TABLE country_details (
    COUNTRY_CODE VARCHAR2(5),
    COUNTRY_NAME VARCHAR2(20),
    CODE VARCHAR2(5)
);

INSERT ALL 
    INTO country_details VALUES ('US', 'United States', '01')
    INTO country_details VALUES ('AUS', 'Australia', '61')
    INTO country_details VALUES ('MAL', 'MALAYSIA', '65')
    INTO country_details VALUES ('IND', 'INDIA', '91')
SELECT * FROM dual;

-- 7. IT in INDIA and MECH from AUS
SELECT e.* FROM emp_dtls e
JOIN country_details c ON e.COUNTRY_CODE = c.COUNTRY_CODE
WHERE (e.JOB = 'IT' AND c.COUNTRY_NAME = 'INDIA')
   OR (e.JOB = 'MECH' AND c.COUNTRY_NAME = 'Australia');

-- 8. Existing query modified to display country name
SELECT e.*, c.COUNTRY_NAME 
FROM emp_dtls e
LEFT JOIN country_details c ON e.COUNTRY_CODE = c.COUNTRY_CODE;
	
	