-- 1. Remove column from an existing table.
drop column column_name;
alter table table_name;
-- 2. write a query to display the deptno which does not contains the employees.
select dept_no from dept where deptno not in ( select dept no from emp)

-- 3. write a query to display the given employee details irrespective of case sensitive.
select * from emp where upper(emp_name)=upper(emp_value)	
( I may give the value either in upper case or lower case but record should fetch the query)

-- 4. Write a query to display employees information who are all working as MANAGER in department 20
select * from emp where job='manager' and dept no=20

-- 5. Modify the employee names from lower case to upper case from the emp table.
update emp where ename =upper(ename)

-- 6. delete the employees whose name starts with J.
delete from emp where emp_name like'%j'
