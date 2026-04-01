-- 1. create a view based on multiple tables.
CREATE VIEW emp_dept_v As
SELECT e.*,d.dname,d.loc FROM emp e,dept d
WHERE e.deptno=d.deptno;
-- 2. what are pseudo columns which are using for sequences.
The two pseudo columns which are used in sequences are currval and nextval
-- 3. can we create a view without table.
Yes we can create views without tables which are called forced views
CREATE FORCE VIEW view_name AS
SELECT * FROM empdept;
-- 4. I have created a table T1 and inserted 10 records and based on T1 I have created View v1
--    after that I have deleted 2 records from T1, now when we query from V1 how many records fetched.
The view also contains 8 records which are satisfying the condition. View does not store data 
it always shows latest data from table
-- 5. how to increase the maxvalue of the sequence.
ALTER SEQUENCE seq_name MAXVALUE 1000;
-- 6. how to remove the views
DROP VIEW view_name;
