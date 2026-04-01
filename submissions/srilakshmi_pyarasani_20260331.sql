1. create a view based on multiple tables.
#CREATE VIEW emp_view_v as
 select e.emp_id, e.emp_name, d.dept_name from emp e
 Join dept d on e.dept_id = d.dept_id

2. what are pseudo columns which are using for sequences.
# NEXTVAL - select seq.NEXTVAL from dual
  CURRVAL - select seq.CURRVAL from dual

3. can we create a view without table.
# Yes using dual
  CREATE VIEW table_v as
  Select 'View_abc' as viewtable from dual

4. I have created a table T1 and inserted 10 records and based on T1 I have created View v1
   after that I have deleted 2 records from T1, now when we query from V1 how many records fetched.
#8 Records

5. how to increase the maxvalue of the sequence.
# Alter sequence seq
  Maxvalue 1000

6. how to remove the views
#Drop view view_name