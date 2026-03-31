CREATE TABLE emp (
    empno NUMBER PRIMARY KEY,
    ename VARCHAR2(50),
    job   VARCHAR2(30),
    sal   NUMBER,
    deptno NUMBER
);

INSERT INTO emp VALUES (7839, 'KING', 'MANAGER', 5000, 10);
INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 2450, 10);
INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 1300, 10);
INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 800, 20);
INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 1600, 30);

INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 1250, 30);
INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 2975, 20);
INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 1250, 30);
INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 2850, 30);
INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 3000, 20);
INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 1500, 30);
INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 1100, 20);
INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 950, 30);
INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 3000, 20);


CREATE TABLE dept (
    deptno NUMBER PRIMARY KEY,
    dname  VARCHAR2(50),
    loc    VARCHAR2(50)
);

INSERT INTO dept VALUES (10, 'ACCOUNTING', 'NEW YORK');
INSERT INTO dept VALUES (20, 'RESEARCH', 'DALLAS');
INSERT INTO dept VALUES (30, 'SALES', 'CHICAGO');
INSERT INTO dept VALUES (40, 'OPERATIONS', 'BOSTON');
select * from emp;

--normal view
create view emp_v as 
Select  empno,ename 
from emp
where deptno=10;


select * from  emp_v;

insert into emp_v values(9001,'raju');

Select  empno,ename 
from emp
where empno=9001;

--complex view
create view emp_dept_v as 
select e.empno, e.ename, e.deptno, d.dname
from emp e,dept d
where e.deptno=d.deptno;


select * from emp_dept_v;


--sequence 
CREATE TABLE student (
    sid   NUMBER PRIMARY KEY,
    sname VARCHAR2(50)
)
--creating sequence 
create sequence st_seq
MINVALUE 1
INCREMENT by 1
START WITH 1
maxvalue 50
NOCYCLE;


insert into student values(st_seq.nextval,'shankar');

select * from student;