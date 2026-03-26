-- 1. Write a query to display department details which  contains employees.
SELECT DISTINCT d.*
FROM departments_demo d
JOIN employees_demo e
ON d.dept_id = e.dept_id;
-- 2. Write a query to display employees information whose sal is greater than or equal to sum of sal of each department.
SELECT *
FROM employees_demo e
WHERE salary >= ALL (
    SELECT SUM(salary)
    FROM employees_demo
    GROUP BY dept_id
);
-- 3. write a query to display the department information which contains more than 3 employees.
SELECT dept_id, COUNT(*) AS total_employees
FROM employees_demo
GROUP BY dept_id
HAVING COUNT(*) > 3;
-- 4. write a query to display the max sal who is working as clerks in 20 department.
SELECT MAX(salary) 
FROM employees_demo
WHERE job = 'CLERK' AND dept_id = 20;
-- 5. create a table emp_dtls with the below columns and insert multiple records for each country code.
	
/*	EMPNO,ENAME,JOB,COUNTRY_CODE
	
	101 , RAJ, IT     US
	102, RAM,  MED    US 
	103, RAKI  MECH   AUS
	104, ABC,  MECH   IND
	105, XYZ , IT     IND 
*/	
CREATE TABLE emp_dtls (
EMPNO INT,
ENAME VARCHAR(50),
JOB VARCHAR(50),
COUNTRY_CODE VARCHAR(10)
);
INSERT INTO emp_dtls VALUES
(101,'RAJ','IT','US'),
(102,'RAM','MED','US'),
(103,'RAKI','MECH','AUS'),
(104,'ABC','MECH','IND'),
(105,'XYZ','IT','IND');
-- 6. create a table country_details with the below columns 

/*	COUNTRY_CODE	COUNTRY_NAME	CODE
	US 				United States	01
	AUS 			Australia       61
	MAL             MALAYSIA        65 
*/	
CREATE TABLE country_details (
COUNTRY_CODE VARCHAR(10),
COUNTRY_NAME VARCHAR(50),
CODE INT
);
INSERT INTO country_details VALUES
('US','United States',01),
('AUS','Australia',61),
('MAL','Malaysia',65);
-- 7. Write a query to display employees information who are working as IT in INDIA and MECH from AUS. 
SELECT * 
FROM emp_dtls
WHERE (JOB='IT' AND COUNTRY_CODE='IND')
   OR (JOB='MECH' AND COUNTRY_CODE='AUS');
-- 8. the current existing query as below, in that add a new column to display country name 

/*	existing QUery:
	
	SELECT * from emp_dtls;
   */
   SELECT e.*, c.COUNTRY_NAME
FROM emp_dtls e
LEFT JOIN country_details c
ON e.COUNTRY_CODE = c.COUNTRY_CODE;