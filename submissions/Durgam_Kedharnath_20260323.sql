1. Write a query to display the employees information who has more than 30 years of exp.
select * 
from emp
where round(MONTHS_BETWEEN(sysdate,hiredate)/12) > 30;


2. Write a query to divide the below string as first name, middle name, last name.
	Raja Ram Mohan

select substr('Raja Ram Mohan',1,instr('Raja Ram Mohan',' ',1,1)-1) first_name,
substr('Raja Ram Mohan',instr('Raja Ram Mohan',' ',1,1)+1, (instr('Raja Ram Mohan',' ',1,2)-instr('Raja Ram Mohan',' ',1,1)-1)) as middle_name,
substr('Raja Ram Mohan',instr('Raja Ram Mohan',' ',1,2)+1) last_name from dual;

	
3. Write a query to display the employees information with their salary with the below format.
ex: Salary is 5000 then output would be XXX5000
Salary is 800 then output would be XXXX800

select empno, ename , job, mgr, hiredate, LPAD(sal,7,'X') as Salary , comm, deptno
from emp;


4. Write a query to display the output as below 

	like employee name is working as job 
	Ex: 
	KING is working as President
	BLAKE is working as CLERK 

select concat(concat(ename,' is working as '),job) 
from emp;