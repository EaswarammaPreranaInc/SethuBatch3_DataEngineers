1. Write a query to display department details which  contains employees.
select  * from dept where  (select deptid from emp group by empid having dept_count>1) =deptid);

2. Write a query to display employees information whose sal is greater than or equal to sum of sal of each department.
select * from emp e where sal >= (select sum(sal)  from emp x where e.deptid=x.deptid);

3. write a query to display the department information which contains more than 3 employees.
select  * from dept where  (select deptid from emp group by empid having dept_count>3) =deptid);

4. write a query to display the max sal who is working as clerks in 20 department.
select max(sal) from emp where dept=20 and job= 'CLERK'

5. create a table emp_dtls with the below columns and insert multiple records for each country code.
	EMPNO,ENAME,JOB,COUNTRY_CODE
	
	101 , RAJ, IT     US
	102, RAM,  MED    US 
	103, RAKI  MECH   AUS
	104, ABC,  MECH   IND
	105, XYZ , IT     IND 
    
    create table emp_dtls(EMPNO integer primary key ,ENAME varchar(30) ,JOB varchar(30),COUNTRY_CODE varchar(5));
	insert into emp_dtls values(101 , 'RAJ', 'IT', 'US'),
	(102, 'RAM',  'MED',  'US' ),
	(103, 'RAKI' ,'MECH' ,'AUS'),
	(104, 'ABC',  'MECH' ,'IND'),
	(105, 'XYZ' , 'IT' ,  'IND' )
    
6. create a table country_details with the below columns 

	COUNTRY_CODE	COUNTRY_NAME	CODE
	US 				United States	01
	AUS 			Australia       61
	MAL             MALAYSIA        65 
	create table country_details(COUNTRY_CODE varchar(5),COUNTRY_NAME varchar(20),CODE integer);
    insert into country_details values ('US', 'United States',	01),
	('AUS', 'Australia',   61),
	('MAL', 'MALAYSIA',65)
    
7. Write a query to display employees information who are working as IT in INDIA and MECH from AUS. 
 select * from emp_dtls where (JOB= 'IT' and COUNTRY_CODE='IND') or (JOB='MECH' and COUNTRY_CODE='AUS');
 
8. the current existing query as below, in that add a new column to display country name 

	existing QUery:
	
	SELECT *,COUNTRY_NAME from emp_dtls;
	
	