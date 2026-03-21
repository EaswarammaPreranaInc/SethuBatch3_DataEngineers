select * from emp where ename like _____;

select * from emp where ename not like %A%;

select * from emp where (dept=clerk and sal in (1000,2000));

select * from emp where cmm is null;

select * from emp where sal>30000;

create table college_details
(
c_code varchar2(20),
c_name varchar2(20),
P_name varchar2(20),
c_address varchar2(20)
);

create table student_details
(
sl_no number,
sname varchar2(20),
dob date,
Fname varchar2(20),
c_code varchar2(20),
fee number check(fee>5000)
)
primary key(sl_no),
foreign key(c_code) reference college_details(c_code);

select constraints from student_details;

update student_details modify sl_no=100;

delete: delete command is used to delete the specified column or row or table.
truncate: truncate command is used to deletes only data but not table structure.
drop: drop command is used to delete entire data along with table structure.





