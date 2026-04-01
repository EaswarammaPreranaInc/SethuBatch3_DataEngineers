1. create a view based on multiple tables.
CREATE VIEW emp_dept_view AS
SELECT e.emp_id, e.emp_name, d.dept_name
FROM emp e
JOIN dept d
ON e.dept_id = d.dept_id;

2. what are pseudo columns which are using for sequences.
NEXTVAL → gives next value
CURRVAL → gives current value
example:
SELECT my_seq.NEXTVAL FROM dual;
SELECT my_seq.CURRVAL FROM dual;

3. can we create a view without table.
No,normally a view must have a table.
CREATE VIEW test_view AS
SELECT 1 AS num FROM dual;

4. I have created a table T1 and inserted 10 records and based on T1 I have created View v1
   after that I have deleted 2 records from T1, now when we query from V1 how many records fetched.
We created T1 with 10 records
Created view V1
Deleted 2 records from T1
Now when you query V1:
It shows 8 records
(Views do NOT store data, they always fetch latest data from base table.)

5. how to increase the maxvalue of the sequence.
ALTER SEQUENCE my_seq
MAXVALUE 10000;

6. how to remove the views
DROP VIEW <view_name>;
