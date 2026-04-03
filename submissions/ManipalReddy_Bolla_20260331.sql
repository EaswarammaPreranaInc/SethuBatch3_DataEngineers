--1. create a view based on multiple tables.
CREATE OR REPLACE VIEW employee_dept_v AS
SELECT e.employee_id, e.first_name, e.last_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;


--2. what are pseudo columns which are using for sequences.
-- To get the next value
SELECT my_sequence.NEXTVAL FROM dual;


-- To check the current value
SELECT my_sequence.CURRVAL FROM dual;


--Can we create a view without a table
CREATE FORCE VIEW future_view AS 
SELECT * FROM non_existent_table;


--How to increase the MAXVALUE of a sequence?
ALTER SEQUENCE my_sequence_name 
MAXVALUE 10000;


--How to remove the views?
DROP VIEW employee_dept_v;