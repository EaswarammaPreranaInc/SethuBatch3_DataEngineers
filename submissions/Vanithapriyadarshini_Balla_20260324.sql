--1. create a student table and insert the records from 1st Jan to till data as 
  -- a joining date.( around 20 records with different dates).
  create table student(
  slno number,
  sname varchar(20),
  mm number,
  pm number,
  cm number);
  
--2. write a query to display students information who joined from last 30 days
select * from emp where hiredate >= sysdate-30; 
--3. create a student table with the following columns slno, name, mm , pm, cm 
create table student(
  slno number,
  sname varchar(20),
  mm number,
  pm number,
  cm number);
  
--4. insert the records in student table only into the following columns slno, name, mm,pm,cm 
insert into student values
(6,'saraswati',88,36,45);

/*5. write a query to display student information along with tm, avgmarks,and result 
   of the student like Pass / Failed, 
   if pass then distinction / First class / Second Class / third class    
*/
select slno,sname,pm,cm,pm,(pm+cm+mm) tm, (pm+cm+mm)/3 avgmarks,
case when (mm>35 and cm>35 and pm>35) then 'pass' 
else 'fail' end result from student; 