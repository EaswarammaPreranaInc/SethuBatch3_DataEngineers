-- PLSQL


--PLSQL Attributes
-- %type - datatype and size
-- %rowtype - all the columns of table - record

--
--declare 
--lv_eno  number := &enterempno;
--lv_name employee.ename%type;
--
--begin
--select ename into
--lv_name from employee
--where lv_eno=empno;
--DBMS_OUTPUT.PUT_LINE('Employee Name: ' || lv_name);
--end;

--
--declare 
--lv_eno  number := &enterempno;
--lv_rec employee%rowtype;
--
--begin
--select * into
--lv_rec from employee
--where lv_eno=empno;
--DBMS_OUTPUT.PUT_LINE('Employee : ' || lv_rec.ename);
--end;


select distinct job from employee;

--declare
--lv_job employee.job%type := '&enterjob';
--begin
--update employee
--set sal = (case  when job = 'CLERK' then  1.1*sal
--                    when job = 'MANAGER' then  1.05*sal 
--                     when job = 'SALESMAN' then 1.08*sal 
--                     else  1.01*sal end)
--                     where job = lv_job;
--DBMS_OUTPUT.PUT_LINE('salary updated: ' );               
--end;


--declare
--
--lv_job employee.job%type := '&enterjob';
--begin
--update employee
--set sal = (case  when job = 'CLERK' then  1.1*sal
--                    when job = 'MANAGER' then  1.05*sal 
--                     when job = 'SALESMAN' then 1.08*sal 
--                     else  1.01*sal end)
--                     where job = lv_job;
--DBMS_OUTPUT.PUT_LINE('salary updated: ' );               
--end;


--declare
--
--lv_job employee.job%type := '&enterjob';
--begin
--update employee
--set sal = (case  when job = 'CLERK' then  1.1*sal
--                    when job = 'MANAGER' then  1.05*sal 
--                     when job = 'SALESMAN' then 1.08*sal 
--                     else  1.01*sal end)
--                     where job = lv_job;
--DBMS_OUTPUT.PUT_LINE('salary updated: ' );               
--end;


declare
    lv_f number := &EnterFirstNo;
    lv_s number := &EnterSecondNo;
    lv_op varchar(1) := '&EnterArithmeticSymbol';
    lv_res number;
begin
    if lv_op = '+' then
        lv_res := lv_f  + lv_s;
    elsif lv_op = '-' then
        lv_res := lv_f - lv_s;
    elsif lv_op = '*' then
        lv_res := lv_f  * lv_s;
    elsif lv_op = '/' then
        lv_res := lv_f   / lv_s;
    else
        DBMS_OUTPUT.PUT_LINE('Enter correct symbol'); 
        return;
    end if;
    DBMS_OUTPUT.PUT_LINE('result :' || lv_res ); 
end;