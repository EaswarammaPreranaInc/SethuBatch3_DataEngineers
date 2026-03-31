#1. Write a Query to display employees information whose name contains only 5 characters
SElECT * FROM EMP
WHERE ENAME LIKE '_____';

#2. Write a query to display employees information whose names does not contains A.
SELECT * FROM EMP
WHERE ENAME NOT IN '%A';

#3.Write a query to display employees information who are all working as CLERK
-- and their salary in range from 1000 to 2000.
SELECT * FROM EMP
WHERE JOB='CLERK' 
AND WHERE SALARY BETWEEN 1000 AND 2000;

#4. Write a query to display employees information who is not getting comm.
SELECT * FROM EMP
WHERE COMM IS NULL OR COMM=0;

#5.Write a query to display employees information whose annual salary is greater than 30000.
SELECT * FROM EMP
WHERE (SAL*12) > 30000;



