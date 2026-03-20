1. Remove column from an existing table.

Alter table table_name
drop column column_name;

2. write a query to display the deptno which does not contains the employees.

SELECT D.DEPTNO
FROM DEPT D
LEFT JOIN EMP E
ON D.DEPTNO = E.DEPTNO
WHERE E.DEPTNO IS NULL;


3. write a query to display the given employee details irrespective of case sensitive.

SELECT *
FROM EMP
WHERE UPPER(ENAME) = UPPER('Raj');


4. Write a query to display employees information who are all working as MANAGER in department 20

select * from emp 
where job='MANAGER' and deptno=20;

5. Modify the employee names from lower case to upper case from the emp table.

update emp
set ename=upper(ename);


6. delete the employees whose name starts with J.

DELETE FROM EMP
WHERE ENAME LIKE 'J%';

