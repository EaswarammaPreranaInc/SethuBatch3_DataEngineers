--1. Write a query to display department details which  contains employees.
select dname from dept d join emp e on d.deptno=e.deptno where e.ename <> null;

--2. Write a query to display employees information whose sal is greater than or equal to sum of sal of each department.
select * from emp e where e.sal>= (select sum(e1.sal) from emp e1 where e1.deptno=e.deptno);

--3. write a query to display the department information which contains more than 3 employees.
select d.* from dept d join emp e on d.deptno=e.deptno group by d.deptno having count(e.ename)>3;

--4. write a query to display the max sal who is working as clerks in 20 department.
select max(sal) from emp where job='clerk' and deptno=20;

/*5. create a table emp_dtls with the below columns and insert multiple records for each country code.
	
	EMPNO,ENAME,JOB,COUNTRY_CODE
	
	101 , RAJ, IT     US
	102, RAM,  MED    US 
	103, RAKI  MECH   AUS
	104, ABC,  MECH   IND
	105, XYZ , IT     IND */

create table emp_dtls(empno number,ename varchar(20),job varchar(20),c_code varchar(20));

insert into emp_dtls values
(105,'XYZ', 'IT','IND');
	
/*6. create a table country_details with the below columns  
	COUNTRY_CODE	COUNTRY_NAME	CODE
	US 				United States	01
	AUS 			Australia       61
	MAL             MALAYSIA        65*/
create table country_dtls(c_code varchar(20),cname varchar(20),code number);
	

--7. Write a query to display employees information who are working as IT in INDIA and MECH from AUS. 
select * from emp_dtls where (job='IT' and c_code='IND') or (job='MECH' and c_code='AUS');

--8. the current existing query as below, in that add a new column to display country name 

	--existing QUery:
	
	SELECT e.*,c.cname from emp_dtls e join country_dtls c on e.c_code = c.c_code;
	