-- 1. Remove column from an existing table.
alter table employees
drop column emp_info;

-- 2. write a query to display the deptno which does not contains the employees.
select d.dept_id 
from departemts d
left join
employyes e 
ON e.dept_id = d.dept_id
where e.dept_id is null;

-- 3. write a query to display the given employee details irrespective of case sensitive.
select * from employees where upper(ename) = upper('Keerthi');
	
-- ( I may give the value either in upper case or lower case but record should fetch the query)

-- 4. Write a query to display employees information who are all working as MANAGER in department 20
select * 
from employees e 
inner join employees m
ON e.mgr_id = m.e_id
where e.dept_id = 20;

-- 5. Modify the employee names from lower case to upper case from the emp table.

select upper(ename)  from employees;

update employees
set ename = upper(ename);

-- 6. delete the employees whose name starts with J.

delete from employees where name like 'J%';
 