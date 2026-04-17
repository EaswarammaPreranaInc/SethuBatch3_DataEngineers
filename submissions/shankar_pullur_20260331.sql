1. create a view based on multiple tables.
create view emp_dept_v as 
select e.empno, e.ename, e.deptno, d.dname
from emp e,dept d
where e.deptno=d.deptno;


2. what are pseudo columns which are using for sequences.

 1.nextval:give next number sequence 
 2.currval:give current number


3.can we create a view without table.
/*normally, we can't create view without a base table
  but in oracle, we can create view using force witout any base table
*/
--eg:
create force view  v1 as
select  * from hospital;
--where hospital table doesn't exists  even though it creates view
--but when we try view the view raises the error
select * from v1;
-- this query raises error


/* Q4. I have created a table T1 and inserted 10 records and based on T1 I have created View v1
   after that I have deleted 2 records from T1, now when we query from V1 how many records fetched*/

/*
answer : we will get 8 records from view
because view stores only query not physical table

*/

--how to increase the maxvalue of the sequence.
alter sequence sequence_name
maxvalue new_value;

--6. how to remove the views
drop view view_name;