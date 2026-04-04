#1. Create a view based on multiple tables:

CREATE VIEW emp_dept_view AS
SELECT e.emp_id, e.emp_name, d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id;


#2. What are pseudo columns used for sequences:

Pseudo columns related to sequences:
- sequence_name.NEXTVAL → gives next value in sequence
- sequence_name.CURRVAL → gives current value of sequence

Example:
SELECT my_seq.NEXTVAL FROM dual;
SELECT my_seq.CURRVAL FROM dual;


#3. Can we create a view without a table:

No, a view must be based on at least one table or another view.
However, you can create a view using DUAL (dummy table):

CREATE VIEW test_view AS
SELECT 'Hello' AS message FROM dual;


#4. Scenario:

Table T1 has 10 records.
View V1 is created based on T1.
After deleting 2 records from T1:

Result:
When querying V1 → 8 records will be fetched.

Reason:
A view always shows current data from the base table.


#5. How to increase the MAXVALUE of a sequence:

ALTER SEQUENCE my_seq
MAXVALUE 10000;


#6. How to remove (drop) views:

DROP VIEW view_name;

Example:
DROP VIEW emp_dept_view;