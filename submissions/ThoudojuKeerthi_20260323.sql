-- 1. Write a query to display the employees information who has more than 30 years of exp.
select * from employees where months_between(sysdate, hire_date)/12 > 30;

-- 2. Write a query to divide the below string as first name, middle name, last name.
-- Raja Ram Mohan
select substr('Raja Ram Mohan', 1, instr('Raja Ram Mohan', ' ', 1)-1) firstName from dual;
select substr('Raja Ram Mohan', instr('Raja Ram Mohan', ' ', 1)+1, (instr('Raja Ram Mohan', ' ', 2)-instr('Raja Ram Mohan', ' ', 1))-1) middleName from dual;
select substr('Raja Ram Mohan', instr('Raja Ram Mohan', ' ', 2)+1, length('Raja Ram Mohan')-instr('Raja Ram Mohan', ' ', 2)-1) lastname from dual;

	
-- 3. Write a query to display the employees information with their salary with the below format.

	ex: Salary is 5000 then output would be XXX5000
		Salary is 800 then output would be XXXX800
		
        select 'Salary is ' || salary || ' then output would be ' || 'XXXX' || salary as output from employees;
-- 4. Write a query to display the output as below 

	like employee name is working as job 
	Ex: 
	KING is working as President
	BLAKE is working as CLERK 
    
    select ename || ' is working as ' || job from employee where ename is not null and job is not null;