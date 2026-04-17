#1. Write a query to display department details which  contains employees.
SELECT *
FROM DEPT
WHERE DEPTNO IN (SELECT DISTINCT DEPTNO FROM EMP);

#2. Write a query to display employees information whose sal is greater than or equal to sum of sal of each department.
SELECT *
FROM employees,dept
WHERE salary >= ALL (
    SELECT SUM(salary)
    FROM employees
    GROUP BY deptno
);

#3. write a query to display the department information which contains more than 3 employees.
SELECT deptno
FROM dept
GROUP BY deptno
HAVING COUNT(*) > 3;

#4. write a query to display the max sal who is working as clerks in 20 department.
SELECT MAX(salary)
FROM employees,dept
WHERE JOB = 'CLERK'
AND deptno = 20;

#5. create a table emp_dtls with the below columns and insert multiple records for each country code.
	#EMPNO,ENAME,JOB,COUNTRY_CODE
	#101 , RAJ, IT     US
	#102, RAM,  MED    US 
	#103, RAKI  MECH   AUS
	#104, ABC,  MECH   IND
	#105, XYZ , IT     IND 
    CREATE TABLE employee_details (
    empno int,
    ename VARCHAR(20),
    JOB VARCHAR(20),
    COUNTRY_CODE VARCHAR(10)
);
INSERT INTO employee_details VALUES (101, 'RAJ', 'IT', 'US');
INSERT INTO employee_details VALUES (102, 'RAM', 'MED', 'US');
INSERT INTO employee_details VALUES (103, 'RAKI', 'MECH', 'AUS');
INSERT INTO employee_details VALUES (104, 'ABC', 'MECH', 'IND');
INSERT INTO employee_details VALUES (105, 'XYZ', 'IT', 'IND');

#6. create a table country_details with the below columns 
	#COUNTRY_CODE	COUNTRY_NAME	CODE
	#US 				United States	01
	#AUS 			Australia       61
	#MAL             MALAYSIA        65 
   CREATE TABLE country_details (
    country_code VARCHAR(10),
    country_name VARCHAR(30),
    CODE int
);
INSERT INTO country_details VALUES ('US', 'United States', 01);
INSERT INTO country_details VALUES ('AUS', 'Australia', 61);
INSERT INTO country_details VALUES ('MAL', 'Malaysia', 65);

#7. Write a query to display employees information who are working as IT in INDIA and MECH from AUS. 
SELECT *
FROM employee_details
WHERE (JOB = 'IT' AND country_code = 'IND')
   OR (JOB = 'MECH' AND country_code = 'AUS');
   
#8. the current existing query as below, in that add a new column to display country name 
	#existing QUery:
	SELECT * from emp_dtls;   