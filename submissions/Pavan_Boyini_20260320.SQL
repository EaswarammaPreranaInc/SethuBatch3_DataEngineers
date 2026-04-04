-- Create the Database
CREATE DATABASE CompanyDB;

-- Use the database (Specific to MySQL/SQL Server)
-- USE CompanyDB; 

-- Creating the EMP table with common columns
CREATE TABLE EMP (
    EMPNO NUMBER PRIMARY KEY,
    ENAME VARCHAR2(50),
    JOB VARCHAR2(50),
    MGR NUMBER,
    HIREDATE DATE,
    SAL NUMBER,
    COMM NUMBER,
    DEPTNO NUMBER
);

-- Creating a DEPT table for reference
CREATE TABLE DEPT (
    DEPTNO NUMBER PRIMARY KEY,
    DNAME VARCHAR2(50),
    LOC VARCHAR2(50)
);

-- 1. Remove column from an existing table.
ALTER TABLE EMP DROP COLUMN MGR;

-- 2. Write a query to display the deptno which does not contains the employees.
-- This selects departments from the DEPT table that have no matching records in EMP.
SELECT DEPTNO 
FROM DEPT 
WHERE DEPTNO NOT IN (SELECT DISTINCT DEPTNO FROM EMP WHERE DEPTNO IS NOT NULL);

-- 3. Write a query to display the given employee details irrespective of case sensitive.
-- Using UPPER ensures that 'scott', 'SCOTT', or 'Scott' all match correctly.
SELECT * FROM EMP 
WHERE UPPER(ENAME) = UPPER('scott');

-- 4. Write a query to display employees information who are all working as MANAGER in department 20.
SELECT * FROM EMP 
WHERE JOB = 'MANAGER' 
AND DEPTNO = 20;

-- 5. Modify the employee names from lower case to upper case from the emp table.
UPDATE EMP 
SET ENAME = UPPER(ENAME);

-- 6. Delete the employees whose name starts with J.
-- The '%' is a wildcard representing any characters following 'J'.
DELETE FROM EMP 
WHERE ENAME LIKE 'J%';