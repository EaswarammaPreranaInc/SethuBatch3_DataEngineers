1. Write a query to display department details which  contains employees.
	select * from dept d where exists (select * from employess e where e.deptid = d.deptid)

2. Write a query to display employees information whose sal is greater than or equal to sum of sal of each department.

select * from employees e where sal >=ALL( select sum(salary) from dept group by dept_id )

3. write a query to display the department information which contains more than 3 employees.

select d.* from dept d inner join employees e using(deptid)  gruop by deptnme, d.did having count(*) >3

4. write a query to display the max sal who is working as clerks in 20 department.
select max(sal) from emp e where job ='clerk' and e.did= 20

5. create a table emp_dtls with the below columns and insert multiple records for each country code.
	
	EMPNO,ENAME,JOB,COUNTRY_CODE
	
	101 , RAJ, IT     US
	102, RAM,  MED    US 
	103, RAKI  MECH   AUS
	104, ABC,  MECH   IND
	105, XYZ , IT     IND 
	
6. create a table country_details with the below columns 

	COUNTRY_CODE	COUNTRY_NAME	CODE
	US 				United States	01
	AUS 			Australia       61
	MAL             MALAYSIA        65 
	

7. Write a query to display employees information who are working as IT in INDIA and MECH from AUS. 

select e.* from emp_dtls e inner join country_details c using (COUNTRY_CODE) where (JOB = 'IT' and COUNTRY_NAME = 'INDIA') or (JOB = 'MECH' and COUNTRY_CODE = 'AUS)'

8. the current existing query as below, in that add a new column to display country name 

	existing QUery:
	
	SELECT * , (select c.COUNTRY_NAME from country_details where c.COUNTRY_CODE = e.COUNTRY_CODE) COUNTRY_NAME as  from emp_dtls e;
	
	