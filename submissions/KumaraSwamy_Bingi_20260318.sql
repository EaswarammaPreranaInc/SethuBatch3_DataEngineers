-- 1. Remove column from an existing table.
ALTER TABLE table_name
DROP COLUMN column_name;

-- 2.write a query to display the deptno which does not contains the employees.
SELECT deptno
FROM dept
WHERE deptno NOT IN (SELECT deptno FROM emp);

-- 3. write a query to display the given employee details irrespective of case sensitive.
	
-- ( I may give the value either in upper case or lower case but record should fetch the query)
SELECT * FROM emp
WHERE UPPER(emp_name) = UPPER('value');

-- 4. Write a query to display employees information who are all working as MANAGER in department 20
SELECT * FROM emp
WHERE job = 'MANAGER'
AND deptno = 20;

-- 5. Modify the employee names from lower case to upper case from the emp table.
UPDATE emp
SET emp_name = UPPER(emp_name);

-- 6. delete the employees whose name starts with J.
DELETE FROM emp
WHERE emp_name LIKE 'J%';
 