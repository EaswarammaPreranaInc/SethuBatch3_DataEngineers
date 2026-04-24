set SERVEROUTPUT ON;

DECLARE
  n NUMBER:=&number;
  i number:=1;
begin 
 while i<=n LOOP
   if MOD(i,2)!=0 then
      DBMS_OUTPUT.PUT_LINE(i);
    end if;
    i:=i+1;
    end loop;
end;
/
DECLARE
  n NUMBER:=&number;
  i number:=1;
begin 
 while i<=n LOOP
   if MOD(i,2)!=0 then
      DBMS_OUTPUT.PUT_LINE(i);
    end if;
    i:=i+1;
    end loop;
end;
/

DECLARE
  n NUMBER:=&enternumber;
  i number:=n;
  res number:=0;
  rem number;
begin 
 while i>0 LOOP
   rem:=mod(i,10);
   res:=res*10+rem;
   i:=trunc(i/10);
   end loop;
 if n=res then 
    DBMS_OUTPUT.PUT_LINE(n||' is palindrom');
 else 
    DBMS_OUTPUT.PUT_LINE(n||' is not palindrom');
 end if;
end;
/

DECLARE
  n NUMBER:=&number;
  i number:=2;
  c number:=0;
begin 
   for x in i..n LOOP
     for y in i..trunc(x/2) loop
        if mod(x,y)=0 then
         c:=c+1;
        end if;
     end loop;
    if c=0 then
    DBMS_OUTPUT.PUT_LINE(x||' is prime number');
    end if;
    c:=0;
  end loop;   
      
end;
/