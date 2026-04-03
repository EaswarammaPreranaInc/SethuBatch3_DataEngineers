views:

normal views:  it can be create on single table,
		also called as virtual table created based on the output of a select statement
				-----------
		normal views can be allowed to modify i.e dml operations can be used.
		views doesn't get stored in database.x
		all views are stored in the table called user_views.




select * from emp
create view emp_v as selelct empno,ename ,job from emp;


create or replace view emp_v as select empno,ename,job from emp
where job='clerk';

view doesn't get stored in database


complex views:
view with multiple tables and conditions.
doesn't allow dml operation in view
used in longer queries with many conditions

forced view:
it doesnot depend on any table
creating without any table.
if view created with warning it is called forced view


select * from emp_v;

insert into emp_v values(121,'XYZ','CLERK')
 
materialized views:


















 