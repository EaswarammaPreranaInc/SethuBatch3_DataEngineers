--PRIME NUMBERS 
declare
     lv_num number := &Enter_number;
     is_prime boolean;
begin
     for i in 2 .. lv_num
     loop
         is_prime := True;
         for j in 2 .. i-1
         loop
           if mod(i,j)=0 then
             is_prime := False;
             exit;
           end if;
           end loop;
           if is_prime then
             dbms_output.put_line(i);
        end if;
    end loop;
end;



--1 TO N NUMBERS

declare
     lv_num number := &Enter_number;
begin
     for i in 1 .. lv_num
     loop
         if mod(i,2)=1 then
             dbms_output.put_line(i);
        end if;
    end loop;
end;


--PALLINDROME

DECLARE
    num NUMBER := &Enter_Number;  -- user input
    original NUMBER;
    reversed NUMBER := 0;
    remainder NUMBER;
BEGIN
    original := num;

    WHILE num > 0 LOOP
        remainder := MOD(num, 10);
        reversed := reversed * 10 + remainder;
        num := FLOOR(num / 10);
    END LOOP;

    IF original = reversed THEN
        DBMS_OUTPUT.PUT_LINE(original || ' is a Palindrome number');
    ELSE
        DBMS_OUTPUT.PUT_LINE(original || ' is NOT a Palindrome number');
    END IF;
END;



-- FIBONACCI SERIRS

DECLARE
    n NUMBER := &Enter_Number;  -- number of terms
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
    i NUMBER := 1;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Fibonacci Series:');

    WHILE i <= n LOOP
        DBMS_OUTPUT.PUT_LINE(a);
        c := a + b;
        a := b;
        b := c;
        i := i + 1;
    END LOOP;
END;
