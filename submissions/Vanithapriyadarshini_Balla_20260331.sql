--1. create a view based on multiple tables.
create view v1 as select * from xyz;

--2. what are pseudo columns which are using for sequences.
select curr_value() from dual;
select next_value() from dual;

--3. can we create a view without table.
No , we cannot 

--4. I have created a table T1 and inserted 10 records and based on T1 I have created View v1
   --after that I have deleted 2 records from T1, now when we query from V1 how many records fetched.
   10 records
   
--5. how to increase the maxvalue of the sequence.
alter sequence seq_name maxvalue 1000;

--6. how to remove the views
drop view view_name;