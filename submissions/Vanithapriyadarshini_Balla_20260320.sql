#1. Remove column from an existing table.

delete ename from emp ; 

#2. write a query to display the deptno which does not contains the employees.

select deptno from dept d left join emp e on d.dept <> e.dept;

#3. write a query to display the given employee details irrespective of case sensitive.
#( I may give the value either in upper case or lower case but record should fetch the query)

select * from emp  where upper(ename)=upper('raj');

#4. Write a query to display employees information who are all working as MANAGER in department 20

select * from emp e where deptname='Manager' and deptno=20;

#5. Modify the employee names from lower case to upper case from the emp table.

update emp modify ename=upper(ename);

#6. delete the employees whose name starts with J.

delete from emp where ename like 'J%';
 