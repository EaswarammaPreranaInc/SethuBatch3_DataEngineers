1. create a view based on multiple tables.

CREATE VIEW emp_dept_view AS
SELECT e.emp_id, e.emp_name, d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id;



2. what are pseudo columns which are using for sequences.

SELECT seq_emp.NEXTVAL FROM dual;
SELECT seq_emp.CURRVAL FROM dual;




3. can we create a view without table.

Yes, as Forced view doesnot depend on any table, as they are created with warning.



4. I have created a table T1 and inserted 10 records and based on T1 I have created View v1
   after that I have deleted 2 records from T1, now when we query from V1 how many records fetched.

T1 has 10 records
Deleted 2 records from T1
Remaining 8 records 
So, view V1 shows 8 records



5. how to increase the maxvalue of the sequence.

alter sequence seq_emp
maxvalue x;



6. how to remove the views

drop view view_name;