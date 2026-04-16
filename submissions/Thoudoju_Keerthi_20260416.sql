-- 1 to n using for loop

declare
    lv_no NUMBER := &EnterAnyNumber;
begin
    for i in 1 .. lv_no
    LOOP
        dbms_output.put_line(i);
    END LOOP;
end;

-- prime number (range)
declare 
    lv_no1 NUMBER := &EnterfirstNumber;
    lv_no2 NUMBER := &EnterSecondNumber;
    lv_temp NUMBER;
begin 
    for i in lv_no1 .. lv_no2
    LOOP
         lv_temp := 0;
        for j in 2 .. i-1
        LOOP 
            if mod(i,j) = 0 then 
               lv_temp := lv_temp +1; 
            END if;
        END LOOP;
        if lv_temp = 0 then 
            dbms_output.put_line(i);
        END if;
        
    END LOOP;
end;


declare 
    lv_no number := &EnterAnyNumber;
    lv_rev number := 0;
    lv_temp number := lv_no;
begin
    while lv_no > 0
    LOOP
        lv_rev := lv_rev * 10 + mod(lv_no, 10);
        lv_no := floor(lv_no / 10);
    END LOOP;
    if lv_rev= lv_temp then
        dbms_output.put_line(lv_rev ||' is Palindrome ');
    else
        dbms_output.put_line(lv_rev ||' is not Palindrome ');
    END if;
end;



declare
    lv_n number := &EnterNumber;
    lv_f number := 0;
    lv_s number := 1;
    lv_temp number;
begin
    while lv_n > 0
    LOOP
        dbms_output.put_line(lv_f);
        lv_temp := lv_f + lv_s;
        lv_f := lv_s;
        lv_s := lv_temp;
        lv_n := lv_n -1;
    END LOOP;
end;
   