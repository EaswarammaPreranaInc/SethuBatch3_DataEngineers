--1. Write a query to display the employees information who has more than 30 years of exp.
--select * from emp where extract(year from hiredate) <= (select extract(year from sysdate)-30);
                   --or
--select * from emp where months_between(hiredate,sysdate)/12 >30;

select substr('Raja Ram Mohan',instr('Raja Ram Mohan',' ',1,1)+1,instr('Raja Ram Mohan',' ',1,2)-) from dual;

--2. Write a query to divide the below string as first name, middle name, last name.
--Raja Ram Mohan
select length(substr('Raja Ram Mohan',1,instr('Raja Ram Mohan',' ',1,1)-1))as firstname,
length(substr('Raja Ram Mohan',instr('Raja Ram Mohan',' ',1,1)+1,instr('Raja Ran Mohan',' ',1,2)-instr('Raja Ram Mohan',' ',1,1)-1))as middlename,
length(substr('Raja Ram Mohan',instr('Raja Ram Mohan',' ',1,2)+1)) as lastname from dual;
	
/*3. Write a query to display the employees information with their salary with the below format.

	ex: Salary is 5000 then output would be XXX5000
		Salary is 800 then output would be XXXX800*/
select lpad(500,7,'X') from dual;
		
/*4. Write a query to display the output as below 

	like employee name is working as job 
	Ex: 
	KING is working as President
	BLAKE is working as CLERK */
    
select e.ename || ' is working as ' || e.job from emp e; 