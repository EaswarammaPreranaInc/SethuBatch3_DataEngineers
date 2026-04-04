1. Write a query to display the employees information who has more than 30 years of exp.

select * from emp where to_char(sysdate() - hire_date,'YYYY') > 30

2. Write a query to divide the below string as first name, middle name, last name.
	Raja Ram Mohan
    
    select  substr('Raja Ram Mohan',1,instr('Raja Ram Mohan',' ',1,1)-1) firstname,
    substr('Raja Ram Mohan',instr('Raja Ram Mohan',' ',1,1)+1,instr('Raja Ram Mohan',' ',1,2)-instr('Raja Ram Mohan',' ',1,1)-1) middle_name,
    substr('Raja Ram Mohan',instr('Raja Ram Mohan',' ',1,2)+1) lastname from dual
	
3. Write a query to display the employees information with their salary with the below format.

	ex: Salary is 5000 then output would be XXX5000
    select lpad(salary,7,'X') from dual
		Salary is 800 then output would be XXXX800
		
4. Write a query to display the output as below 

	like employee name is working as job 
	Ex: 
	KING is working as President
	BLAKE is working as CLERK 
    
    select name, job from emp