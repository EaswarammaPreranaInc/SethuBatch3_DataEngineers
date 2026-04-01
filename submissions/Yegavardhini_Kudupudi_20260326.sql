1. Write a query to display department details which  contains employees.

select *  from dept d
where exists ( select 1 
               from emp e
               where e.depno=d.deptno);

2. Write a query to display employees information whose sal is greater than or equal to sum of sal of each department.

select * from emp e
where e.sal >= ALL(select sum(sal) 
              from emp 
              group by dept_id);

3. write a query to display the department information which contains more than 3 employees.

select * from dept d
where dept_id in ( select dept_id
                   from emp
                   group by dept_id
                   having count(*) >=3);

4. write a query to display the max sal who is working as clerks in 20 department.

select max(sal)
from emp
where job = 'CLERK' and dept_id = 20;

5. create a table emp_dtls with the below columns and insert multiple records for each country code.
 	
 	EMPNO,ENAME,JOB,COUNTRY_CODE
 	
 	101 , RAJ, IT     US
 	102, RAM,  MED    US 
 	103, RAKI  MECH   AUS
 	104, ABC,  MECH   IND
	105, XYZ , IT     IND 


create table emp_dtls(
       empno number constraint emp_pk primary key,
       ename varchar2,
       job varchar2,
       country_code varchar2,
       foriegn key country_code reference country_dtls(country_code));

insert into emp_dtls values(101 , 'RAJ', 'IT','US'),
                           (102, 'RAM','MED','US'),
                           (103,'RAKI','MECH','AUS'),
                           (104, 'ABC','MECH','IND'),
                           (105,'XYZ' , 'IT','IND');

6. create a table country_details with the below columns 

 	COUNTRY_CODE	COUNTRY_NAME	CODE
 	US 				United States	01
 	AUS 			Australia       61
 	MAL             MALAYSIA        65 

create table emp_dtls(
       country_code varchar2 constraint cc_pk primary key,
       country_name varchar2,
       code varchar2 );

insert into emp_dtls values('US','United States','01'),
                           ('AUS','Australia','61'),
	         ('MAL','MALAYSIA','65');

7. Write a query to display employees information who are working as IT in INDIA and MECH from AUS. 

select * from emp_dtls 
where (job = 'IT' and country_code = 'IND') 
or 
(job = 'MECH' and country_code='AUS');

8.the current existing query as below, in that add a new column to display country name 
existing QUery:

select * ,c.country_name from emp_dtls,country_details c
where emp_dtls.country_code = c.country_code;