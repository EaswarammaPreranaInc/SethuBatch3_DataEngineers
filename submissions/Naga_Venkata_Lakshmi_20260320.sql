ALTER TABLE table_name DROP COLUMN column_name;
SELECT  deptno FROM dept
WHERE deptno NOT IN (SELECT DISTINCT deptno FROM emp);
SELECT * FROM emp 
WHERE UPPER(emp_name) = UPPER('search_value');
SELECT * FROM emp WHERE job = 'MANAGER' AND deptno = 20;
UPDATE employee
SET emp_name = UPPER(emp_name);
DELETE FROM emp 
WHERE emp_name LIKE 'J%';

 