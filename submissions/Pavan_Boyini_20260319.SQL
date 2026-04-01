
CREATE TABLE EMP (
    EMPNO INT PRIMARY KEY,
    ENAME VARCHAR(50),
    JOB VARCHAR(50),
    SAL NUMBER,
    COMM NUMBER
);

-- 1. Write a Query to display employees information whose name contains only 5 characters
SELECT * FROM EMP 
WHERE ENAME LIKE '_____';

-- 2. Write a query to display employees information whose names does not contains A.
SELECT * FROM EMP 
WHERE ENAME NOT LIKE '%A%';

-- 3. Write a query to display employees information who are all working as CLERK
-- and their salary in range from 1000 to 2000.
SELECT * FROM EMP 
WHERE JOB = 'CLERK' 
AND SAL BETWEEN 1000 AND 2000;

-- 4. Write a query to display employees information who is not getting comm.
SELECT * FROM EMP 
WHERE COMM IS NULL OR COMM = 0;

-- 5. Write a query to display employees information whose annual salary is greater than 30000.
SELECT * FROM EMP 
WHERE (SAL * 12) > 30000;

-- 6. Create College Details as a parent table
CREATE TABLE COLLEGE_DETAILS (
    COLLEGE_CODE VARCHAR2(30) PRIMARY KEY,
    COLLEGE_NAME VARCHAR2(100),
    PRINCIPAL_NAME VARCHAR2(50),
    COLLEGE_ADDRESS VARCHAR2(200)
);

-- 7. Create STUDENT details as a child table and link with Parent table college
CREATE TABLE STUDENT (
    SLNO NUMBER PRIMARY KEY,
    SNAME VARCHAR2(30),
    DOB DATE NOT NULL,
    FNAME VARCHAR2(30),
    COLLEGE_CODE VARCHAR2(30),
    FEES NUMBER CHECK (FEES > 0),
    CONSTRAINT FK_COLLEGE FOREIGN KEY (COLLEGE_CODE) 
        REFERENCES COLLEGE_DETAILS(COLLEGE_CODE)
);

-- 8. Query to get constraint details which are having in the table STUDENT (Oracle specific)
SELECT constraint_name, constraint_type, search_condition
FROM user_constraints
WHERE table_name = 'STUDENT';

-- 9. Modify the data in the student table from NULL values to 100 in the SLNO column.
UPDATE STUDENT 
SET SLNO = 100 
WHERE SLNO IS NULL;

/*
10. Difference between TRUNCATE, DELETE, and DROP:

    DELETE:
    - It is a Data Manipulation Language (DML) command.
    - Used to remove specific rows from a table using a WHERE clause.
    - It is slower than TRUNCATE because it logs each row deletion in the transaction log.
    - You can ROLLBACK the data after a DELETE operation if a COMMIT has not been issued.
    - It does not reset the identity (auto-increment) counter.

    TRUNCATE:
    - It is a Data Definition Language (DDL) command.
    - Used to remove ALL rows from a table at once.
    - It is much faster as it deallocates the data pages rather than logging individual rows.
    - Generally, it cannot be rolled back (though this depends on the specific RDBMS and transaction state).
    - It resets the identity (auto-increment) counter back to its seed value.
    - The table structure remains intact for future use.

    DROP:
    - It is a Data Definition Language (DDL) command.
    - Used to remove the entire table structure, including all data, indexes, triggers, and constraints.
    - This operation cannot be rolled back.
    - Once dropped, the table no longer exists in the database schema.
    - All memory space and definitions associated with the table are released.
*/
