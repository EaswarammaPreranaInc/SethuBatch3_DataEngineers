1. Remove column from an existing table.

ALTER TABLE employees
DROP COLUMN age;


2. write a query to display the deptno which does not contains the employees.

SELECT d.deptno
FROM dept d
WHERE NOT EXISTS (
    SELECT 1
    FROM emp e
    WHERE e.deptno = d.deptno
);


3. write a query to display the given employee details irrespective of case sensitive.

SELECT *
FROM emp
WHERE LOWER(ename) = LOWER('john');


SELECT *
FROM emp
WHERE UPPER(ename) = UPPER('John');  -- You can give 'John', 'JOHN', 'john', etc.


4. Write a query to display employees information who are all working as MANAGER in department 20

SELECT *
FROM emp
WHERE UPPER(job) = 'MANAGER'  -- Case-insensitive check
  AND deptno = 20;


5. Modify the employee names from lower case to upper case from the emp table.

UPDATE emp
SET ename = UPPER(ename);


6. delete the employees whose name starts with J.

DELETE FROM emp
WHERE UPPER(ename) LIKE 'J%';














