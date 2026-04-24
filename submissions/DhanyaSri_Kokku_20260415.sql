-- Program to take two integers and one operand and perform the operation and return the result
declare
      ln_num1  number := &Enter_first_number;
      ln_num2  number := &Enter_second_number;
      lv_op  varchar(1) := '&Enter_the_operand';
      ln_res number;
begin
      if lv_op = '+' then ln_res := ln_num1+ln_num2;
      elsif lv_op = '-' then ln_res := ln_num1-ln_num2;
      elsif lv_op = '*' then ln_res := ln_num1*ln_num2;
      elsif lv_op = '/' then ln_res := ln_num1/ln_num2;
      end if;
      dbms_output.put_line('Result : '||ln_res);
end;
      
# Program to update the salaries of employees based on their job
begin
      update emp
      set sal = case 
           when job = 'CLERK' then sal + (10/100)*sal
           when job = 'MANAGER' then sal +(8/100)*sal
           when job = 'SALESMAN' then sal + (5/100)*sal
           else sal + (1/100)*sal
      end;  
end;