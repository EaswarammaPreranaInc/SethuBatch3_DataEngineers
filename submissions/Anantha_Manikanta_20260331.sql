-- 1. create a view based on multiple tables.
CREATE VIEW emp_dept_view AS
SELECT e.empno, e.ename, d.deptno, d.dname
FROM emp e
JOIN dept d
ON e.deptno = d.deptno;

-- 2. what are pseudo columns which are using for sequences.
SELECT emp_seq.NEXTVAL FROM dual;
SELECT emp_seq.CURRVAL FROM dual;

-- 3. can we create a view without table.
CREATE FORCE VIEW v1 AS
SELECT * FROM t1;

-- 4. I have created a table T1 and inserted 10 records and based on T1 I have created View v1 after that I have deleted 2 records from T1, now when we query from V1 how many records fetched.
-- 8

-- 5. how to increase the maxvalue of the sequence.
ALTER SEQUENCE emp_seq
MAXVALUE 99999;

-- 6. how to remove the views
DROP VIEW view_name;