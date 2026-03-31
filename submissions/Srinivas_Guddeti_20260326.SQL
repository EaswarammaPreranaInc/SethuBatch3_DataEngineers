
1. Write a query to display department details which  contains employees.
SELECT *
FROM dept d
WHERE d.deptno IN (
    SELECT deptno FROM emp
);

2. Write a query to display employees information whose sal is greater than or equal to sum of sal of each department.
SELECT *
FROM emp e
WHERE sal >= ALL (
    SELECT SUM(sal)
    FROM emp
    GROUP BY deptno
);

3. write a query to display the department information which contains more than 3 employees.
SELECT d.*
FROM dept d
JOIN emp e ON d.deptno = e.deptno
GROUP BY d.deptno, d.dname, d.loc
HAVING COUNT(e.empno) > 3;

4. write a query to display the max sal who is working as clerks in 20 department.
SELECT MAX(sal)
FROM emp
WHERE job = 'CLERK'
AND deptno = 20;

5. create a table emp_dtls with the below columns and insert multiple records for each country code.
	
	EMPNO,ENAME,JOB,COUNTRY_CODE
	
	101 , RAJ, IT     US
	102, RAM,  MED    US 
	103, RAKI  MECH   AUS
	104, ABC,  MECH   IND
	105, XYZ , IT     IND 
CREATE TABLE emp_dtls (
    empno INT,
    ename VARCHAR(20),
    job VARCHAR(20),
    country_code VARCHAR(5)
);

INSERT INTO emp_dtls VALUES
(101, 'RAJ', 'IT', 'US'),
(102, 'RAM', 'MED', 'US'),
(103, 'RAKI', 'MECH', 'AUS'),
(104, 'ABC', 'MECH', 'IND'),
(105, 'XYZ', 'IT', 'IND');

6. create a table country_details with the below columns 

	COUNTRY_CODE	COUNTRY_NAME	CODE
	US 				United States	01
	AUS 			Australia       61
	MAL             MALAYSIA        65 
CREATE TABLE country_details (
    country_code VARCHAR(5),
    country_name VARCHAR(30),
    code INT
);

INSERT INTO country_details VALUES
('US', 'United States', 01),
('AUS', 'Australia', 61),
('MAL', 'Malaysia', 65);	

7. Write a query to display employees information who are working as IT in INDIA and MECH from AUS. 
SELECT *
FROM emp_dtls
WHERE (job = 'IT' AND country_code = 'IND')
   OR (job = 'MECH' AND country_code = 'AUS');

8. the current existing query as below, in that add a new column to display country name 

	existing QUery:
SELECT * from emp_dtls;

SELECT e.*, c.country_name
FROM emp_dtls e
LEFT JOIN country_details c
ON e.country_code = c.country_code;
	
	
