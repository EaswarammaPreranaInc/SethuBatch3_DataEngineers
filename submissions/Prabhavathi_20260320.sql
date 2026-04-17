1. Remove column from an existing table.

   Alter table table_Name
   drop colume colume_Name;

2. write a query to display the deptno which does not contains the employees.
  
   select * From dept
   where deptno not in(
     select deptno
     from emp
);


3. write a query to display the given employee details irrespective of case sensitive.	

     select * from emp
     where upper(ename) = upper('King');

4. Write a query to display employees information who are all working as MANAGER in department 20

    select * from emp
    where job = 'MANAGER' and dept = 20;

5. Modify the employee names from lower case to upper case from the emp table.

    UPDATE EMP
    UPDATE UPPER(ENAME) = UPPER(ENAME);
    
6. delete the employees whose name starts with J.
    
   DELETE From emp
   WHER EMP ENAME LIKE '%j%';
   
















