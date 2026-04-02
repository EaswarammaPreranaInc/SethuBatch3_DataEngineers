1. Remove column from an existing table.

ALTER table table_name
DROP column column_name;

2. write a query to display the deptno which does not contains the employees.


SELECT deptno
from dept
WHERE deptno not in(
select deptno
from emp
);


3. write a query to display the given employee details irrespective of case sensitive.	

SELECT * 
FROM emp 
WHERE UPPER(ename) = UPPER('king');


4. Write a query to display employees information who are all working as MANAGER in department 20


SELECT deptno,ename
FROM emp 
WHERE job = 'MANAGER' and deptno = 20;


5. Modify the employee names from lower case to upper case from the emp table.

update table_name
column_name = upper(column_name);


6. delete the employees whose name starts with J.

DELETE FROM emp
WHERE ename like 'J%'