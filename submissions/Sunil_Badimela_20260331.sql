1. create a view based on multiple tables. 
 create view emp_dept_v as 
 select e.emp_id, e.emp_name, d.dept_name 
 from emp e 
 join dept d 
 on e.dept_id = d.dept_id; 
  
 2. what are pseudo columns which are using for sequences. 
 nextval -- gets next value of the sequence 
 currval -- gets current highest value of the sequence 
  
 3. can we create a view without table. 
 -- no, views cannot be created without a table or psuedo table 
  
 4. I have created a table T1 and inserted 10 records and based on T1 I have created View v1 
    after that I have deleted 2 records from T1, now when we query from V1 how many records fetched. 
 -- 8 records 
  
 5. how to increase the maxvalue of the sequence. 
 alter sequence sequence_name 
 maxvalue 100; 
  
 6. how to remove the views 
 drop view view_name;