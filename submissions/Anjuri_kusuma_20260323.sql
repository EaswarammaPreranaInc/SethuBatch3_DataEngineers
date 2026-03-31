use employee_db; 
#1. Write a query to display the employees information who has more than 30 years of exp.
select * from employees where(sysdate-hiredate)/365>30;

#2. Write a query to divide the below string as first name, middle name, last name.
	#Raja Ram Mohan
   SELECT 
  SUBSTRING_INDEX(name, ' ', 1) AS FIRST_NAME,

  SUBSTRING_INDEX(SUBSTRING_INDEX(name, ' ', 2), ' ', -1) AS MIDDLE_NAME,

  SUBSTRING_INDEX(name, ' ', -1) AS LAST_NAME

FROM (SELECT 'Raja Ram Mohan' AS name) AS t;

#3. Write a query to display the employees information with their salary with the below format.
#	ex: Salary is 5000 then output would be XXX5000
	#	Salary is 800 then output would be XXXX800
    SELECT ENAME,
       LPAD(SAL, 7, 'X') AS SALARY
FROM EMP;

#4. Write a query to display the output as below 
#	like employee name is working as job 
	#Ex: 
	#KING is working as President
	#BLAKE is working as CLERK 
    SELECT emp_name || ' is working as ' || JOB AS DETAILS
FROM employees;