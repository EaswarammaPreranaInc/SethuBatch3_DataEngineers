-- Create the Database environment
CREATE DATABASE CompanyDB;

-- Create the EMP table with necessary columns for these queries
CREATE TABLE EMP (
    EMPNO NUMBER PRIMARY KEY,
    ENAME VARCHAR2(50),
    JOB VARCHAR2(50),
    HIREDATE DATE,
    SAL NUMBER
);

-- 1. Write a query to display the employees information who has more than 30 years of exp.
-- (MONTHS_BETWEEN finds the total months, dividing by 12 converts it to years)
SELECT * FROM EMP 
WHERE (MONTHS_BETWEEN(SYSDATE, HIREDATE) / 12) > 30;

-- 2. Write a query to divide the below string as first name, middle name, last name: 'Raja Ram Mohan'
-- (REGEXP_SUBSTR searches for a pattern—non-space characters—and picks the 1st, 2nd, and 3rd occurrences)
SELECT 
    REGEXP_SUBSTR('Raja Ram Mohan', '[^ ]+', 1, 1) AS FIRST_NAME,
    REGEXP_SUBSTR('Raja Ram Mohan', '[^ ]+', 1, 2) AS MIDDLE_NAME,
    REGEXP_SUBSTR('Raja Ram Mohan', '[^ ]+', 1, 3) AS LAST_NAME
FROM DUAL;

-- 3. Write a query to display the employees information with their salary with the below format (ex: XXX5000)
-- (LPAD ensures the total length of the string is 7, filling the left side with 'X')
SELECT ENAME, LPAD(SAL, 7, 'X') AS FORMATTED_SALARY 
FROM EMP;

-- 4. Write a query to display the output as below: "KING is working as President"
-- (The || operator joins the strings together into a single sentence)
SELECT ENAME || ' is working as ' || JOB AS EMPLOYEE_STATUS 
FROM EMP;