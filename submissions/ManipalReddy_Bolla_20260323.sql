-- 1. Write a query to display the employees information who has more than 30 years of exp.
SELECT * FROM employees WHERE (YEAR(CURDATE()) - YEAR(hire_date)) > 30;
	
-- 2. Write a query to divide the below string as first name, middle name, last name.
-- 	Raja Ram Mohan
SELECT 
		SUBSTRING_INDEX('Raja Ram Mohan', ' ', 1) AS first_name,
		SUBSTRING_INDEX(SUBSTRING_INDEX('Raja Ram Mohan', ' ', 2), ' ', -1) AS middle_name,
		SUBSTRING_INDEX('Raja Ram Mohan', ' ', -1) AS last_name;

	
-- 3. Write a query to display the employees information with their salary with the below format.
-- 	ex: Salary is 5000 then output would be XXX5000
-- 		Salary is 800 then output would be XXXX800
SELECT employee_name, 
		CONCAT(REPEAT('X', 10 - LENGTH(salary)), salary) AS formatted_salary
	FROM employees;
		
-- 4. Write a query to display the output as below 
-- 	like employee name is working as job 
-- 	Ex: 
-- 	KING is working as President
-- 	BLAKE is working as CLERK 
SELECT CONCAT(ename, ' is working as ', job) FROM employees;
