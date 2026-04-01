-- 1. Create a view based on multiple tables
CREATE OR REPLACE VIEW EMP_DEPT_VIEW AS
SELECT e.EMPNO, e.ENAME, e.JOB, d.DNAME, d.LOC
FROM EMP e
JOIN DEPT d ON e.DEPTNO = d.DEPTNO;

-- Example of using sequence pseudo-columns
-- To get the next number:
SELECT my_sequence.NEXTVAL FROM DUAL;

-- To see the current number:
SELECT my_sequence.CURRVAL FROM DUAL;

-- 3. Create a view without a physical user table (using DUAL)
CREATE VIEW DUMMY_VIEW AS 
SELECT 'Hello World' AS MESSAGE, 2026 AS CURRENT_YEAR FROM DUAL;

/*4. Record count in View after deletion
Scenario: Table T1 has 10 records. View V1 is created from T1. 2 records are deleted from T1.

Answer: When you query V1, 8 records will be fetched.*/

-- 5. How to increase the maxvalue of the sequence
ALTER SEQUENCE my_sequence_name 
MAXVALUE 999999;

-- 6. How to remove the views
DROP VIEW EMP_DEPT_VIEW;