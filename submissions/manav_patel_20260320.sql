1. Remove column from an existing table.

ALTER TABLE table_name DROP COLUMN column_name;

2. write a query to display the deptno which does not contains the employees.
SELECT d.deptno
FROM dept d
LEFT JOIN emp e
ON d.deptno = e.deptno
WHERE e.deptno IS NULL;

3. write a query to display the given employee details irrespective of case sensitive.
select *  from emp
where upper(emp)=upper('man');
	
( I may give the value either in upper case or lower case but record should fetch the query)

4. Write a query to display employees information who are all working as MANAGER in department 20
SELECT *
FROM emp
WHERE UPPER(job) = 'MANAGER'
AND deptno = 20;

5. Modify the employee names from lower case to upper case from the emp table.
UPDATE emp
SET ename = UPPER(ename);

6. delete the employees whose name starts with J.
DELETE 
From emp
where name like'j%'