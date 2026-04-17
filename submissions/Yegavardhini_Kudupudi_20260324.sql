1. create a student table and insert the records from 1st Jan to till data as 
   a joining date.( around 20 records with different dates).
Ans:
create table student (slno number primary key,name varchar2(30),joining_date date);
insert into student values(1,'Vardhini','2026-03-01'),
		(2,'Satya','2026-03-24'),
		(3,'Sai'.'2026-01-01'),
		(4,'Ram','2026-02-28'),
		(5,'Venkat','2026-01-29'),
		(6,'Yoga','2026-01-03'),
		(7,'Bhagya','2026-03-01'),
		(8,'Sri','2026-02-25'),
		(9,'devi','2026-01-25'),
		(10,'Neha','2026-02-18'),
		(11,'Pinky','2026-02-20'),
		(12,'Varshini','2026-02-17')
		(13,'Sita','2026-02-15'),
		(14,'Lakshman','2026-03-20'),
		(15,'Raghu','2026-01-13'),
		(16,'Shayam','2026-01-15'),
		(17,'Rayan','2026-02-05'),
		(18,'Janaki','2026-03-16'),
		(19,'Ganesh','2026-02-06'),
		(20,'Hema','2026-01-04');
   
2. write a query to display students information who joined from last 30 days
Ans:
select * from student
where months_betwee(sysdate,joindate)<=1;

3. create a student table with the following columns 
	slno, name, mm , pm, cm 
Ans:
create table stdnt(slno number,
	          name varchar2(30),
	          mm number,
	          pm number,
	          cm number);	

4. insert the records in student table only into the following columns 
	slno, name, mm,pm,cm 
Ans:
insert into stdnt values(1,'Ram',70,60,40);
	
5. write a query to display student information along with tm, avgmarks,and result 
   of the student like Pass / Failed, 
   if pass then distinction / First class / Second Class / third class 
Ans:
select slno,name,mm,pm,cm,(mm+pm+cm) as total_marks,
round((mm+pm+cm)/3,2) as avg_marks,
where (mm+pm+cm)/3>=75 then 'distnction'
when (mm+pm+cm)/3>=60 then 'first class'
when (mm+pm+cm)/3>=50 then 'second class'
when (mm+pm+cm)/3>=40 then 'third class'
when (mm+pm+cm)/3<40 then 'fail'
result  from stdnt;