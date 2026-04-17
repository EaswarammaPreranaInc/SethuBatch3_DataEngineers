-- 1. Printing 1-n numbers using loops
declare  -- Using normal loop
     ln_no NUMBER :=&Enter_any_number;
     ln_cnt NUMBER :=1;
begin 
     loop
         dbms_output.put_line(ln_cnt);
         if ln_cnt <= ln_no then
              ln_cnt := ln_cnt+1;
         else   
              exit;
         end if;
     end loop;
end;


declare   -- Using while loop
     ln_no NUMBER :=&Enter_any_number;
     ln_cnt NUMBER :=1;
begin
     while ln_cnt <= ln_no 
     loop
          dbms_output.put_line(ln_cnt);
          ln_cnt := ln_cnt+1;
     end loop;
end;

declare  -- Using for loop
      ln_no NUMBER := &Enter_any_number;
begin
      for i in 1..ln_no
      loop
          dbms_output.put_line(i);
      end loop;
end;

-- 2. Printing 1-n odd numbers using loops
declare  -- Using normal loop
     ln_no NUMBER :=&Enter_any_number;
     ln_cnt NUMBER :=1;
begin 
     loop
    
         if ln_cnt <= ln_no then
               if MOD(ln_cnt,2) = 1 then
                 dbms_output.put_line(ln_cnt);
               end if;
               ln_cnt := ln_cnt+1;
         else   
              exit;
         end if;
     end loop;
end;
    
declare   -- Using while loop
     ln_no NUMBER :=&Enter_any_number;
     ln_cnt NUMBER :=1;
begin
     while ln_cnt <= ln_no 
     loop
          if MOD(ln_cnt,2)= 1 then
              dbms_output.put_line(ln_cnt);
          end if;
          ln_cnt := ln_cnt+1;
     end loop;
end;

declare  --Using for loop
     ln_no NUMBER:=&Enter_any_number;
begin
     for i in 1..ln_no
     loop
           if MOD(i,2) = 1 then
               dbms_output.put_line(i);
           end if;
     end loop;
end;

-- 3. Program to print 1 to n prime numbers
declare 
     ln_no NUMBER :=&Enter_any_number;
     lb_flag boolean :=False;
begin
     for i in 2..ln_no
     loop
         for j in 2..i-1
         loop
              if MOD(i,j) = 0 then
                   lb_flag := True;
              end if;
         end loop;
         if lb_flag != True then
              dbms_output.put_line(i);
         end if;
         lb_flag := False;
     end loop;
end;

-- 4.Program to check whether given number is palindrome or not
declare
     ln_no NUMBER :=&Enter_any_number;
     ln_copy NUMBER :=ln_no;
     ln_rev NUMBER :=0;
begin
     while ln_no > 0
     loop
          ln_rev := ln_rev * 10+ MOD(ln_no,10);
          ln_no := TRUNC(ln_no/10);
     end loop;
     if ln_copy = ln_rev then
          dbms_output.put_line(ln_copy || ' is a Palindrome number');
     else
           dbms_output.put_line(ln_copy || ' is not a Palindrome number');
     end if;
end;

-- 5. Program to print fibonacci series upto given number
declare  -- Using for loop
    ln_no NUMBER:=&Enter_any_number;
    ln_fno NUMBER:=0;
    ln_sno NUMBER:=1;
    ln_next NUMBER;
begin
    if ln_no > 1 then
        dbms_output.put_line(ln_fno);
        dbms_output.put_line(ln_sno);
    end if;
    for i in 2..ln_no
    loop
        ln_next := ln_fno+ln_sno;
        if ln_next <= ln_no then
            dbms_output.put_line(ln_next);
            ln_fno := ln_sno;
            ln_sno := ln_next;
        else
            exit;
        end if;
    end loop;
end;

declare --Using while loop
    ln_no NUMBER := &Enter_any_number;
    ln_fno NUMBER :=0;
    ln_sno NUMBER:=1;
    ln_next NUMBER;
begin
    if ln_no > 1 then
        dbms_output.put_line(ln_fno);
        dbms_output.put_line(ln_sno);
    end if;
    ln_next := ln_fno + ln_sno;
    while ln_next <= ln_no
    loop
        dbms_output.put_line(ln_next);
        ln_fno := ln_sno;
        ln_sno := ln_next;
        ln_next := ln_fno + ln_sno;
    end loop;
end;

declare --Using normal loop
    ln_no NUMBER := &Enter_any_number;
    ln_fno NUMBER :=0;
    ln_sno NUMBER:=1;
    ln_next NUMBER;
begin
    if ln_no > 1 then
        dbms_output.put_line(ln_fno);
        dbms_output.put_line(ln_sno);
    end if;
    ln_next := ln_fno + ln_sno;
    loop
        if ln_next <= ln_no then
            dbms_output.put_line(ln_next);
            ln_fno := ln_sno;
            ln_sno := ln_next;
            ln_next := ln_fno + ln_sno;
        else
            exit;
        end if;
    end loop;
end;
    
-- 6.Program to print fibonnaci series upto n numbers
declare  -- Using for loop
    ln_no NUMBER:=&Enter_any_number;
    ln_fno NUMBER:=0;
    ln_sno NUMBER:=1;
    ln_next NUMBER;
begin
    if ln_no >= 1 then
       dbms_output.put_line(ln_fno);
    end if;
    if ln_no >= 2 then
        dbms_output.put_line(ln_sno);
    end if;
    for i in 3..ln_no
    loop
        ln_next := ln_fno+ln_sno;
        dbms_output.put_line(ln_next);
        ln_fno := ln_sno;
        ln_sno := ln_next;
    end loop;
end;

declare --Using while loop
    ln_no NUMBER := &Enter_any_number;
    ln_fno NUMBER :=0;
    ln_sno NUMBER:=1;
    ln_next NUMBER;
begin
    if ln_no >= 1 then
       dbms_output.put_line(ln_fno);
       ln_no :=ln_no-1;
    end if;
    if ln_no >= 2 then
        dbms_output.put_line(ln_sno);
        ln_no :=ln_no-1;
    end if;
    while ln_no > 0
    loop
        ln_next := ln_fno + ln_sno;
        dbms_output.put_line(ln_next);
        ln_fno := ln_sno;
        ln_sno := ln_next;
        ln_no :=ln_no -1;
    end loop;
end;

declare --Using normal loop
    ln_no NUMBER := &Enter_any_number;
    ln_fno NUMBER :=0;
    ln_sno NUMBER:=1;
    ln_next NUMBER;
begin
    if ln_no >= 1 then
       dbms_output.put_line(ln_fno);
       ln_no := ln_no-1;
    end if;
    if ln_no >= 2 then
        dbms_output.put_line(ln_sno);
        ln_no := ln_no-1;
    end if;
    loop
        if ln_no > 0 then
            ln_next := ln_fno + ln_sno;
            dbms_output.put_line(ln_next);
            ln_fno := ln_sno;
            ln_sno := ln_next;
            ln_no := ln_no -1;
        else
            exit;
        end if;
    end loop;
end;