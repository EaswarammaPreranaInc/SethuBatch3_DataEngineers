1. Remove column from an existing table.
Ans:
alter table table_name
drop column col_name;

2. write a query to display the deptno which does not contains the employees.
Ans:
select *deptno from dept
where deptno not in(select deptno 
		from emp);

3. write a query to display the given employee details irrespective of case sensitive.
	
( I may give the value either in upper case or lower case but record should fetch the query)
Ans:
select * from emp
where upper(ename)=upper('king');

4. Write a query to display employees information who are all working as MANAGER in department 20
Ans:
select * from emp
where job='MANAGER'
and deptno=20;

5. Modify the employee names from lower case to upper case from the emp table.
Ans:
select upper(ename) from emp;

6. delete the employees whose name starts with J.
Ans:
delete * from emp 
where ename like 'J%';
