#1 to N odd numbers

DECLARE
   LN_NO NUMBER:=&ENTER_ANY_NUMBER;
   LN_CNT NUMBER:=1;
BEGIN
   LOOP
      LN_CNT:=LN_CNT+1;
      IF LN_CNT<=LN_NO THEN
         DBMS_OUTPUT.PUT_LINE(LN_CNT);
      ELSE
         EXIT;
      END IF;
   END LOOP;



#given number is palindrome or not

DECLARE
   n NUMBER := &num;
   rev NUMBER := 0;
   rem NUMBER;
   temp NUMBER;
BEGIN
   temp := n;
   WHILE temp > 0 LOOP
      rem := MOD(temp,10);        
      rev := rev*10 + rem;        
      temp := TRUNC(temp/10);    
   END LOOP;
   IF n = rev THEN
      DBMS_OUTPUT.PUT_LINE('Palindrome');
   ELSE
      DBMS_OUTPUT.PUT_LINE('Not Palindrome');
   END IF;
END;
/


#1..N prime numbers

DECLARE
   n NUMBER := &num;
   i NUMBER;
   j NUMBER;
   cnt NUMBER;
BEGIN
   FOR i IN 2..n LOOP
      cnt := 0;

      FOR j IN 1..i LOOP
         IF MOD(i,j) = 0 THEN
            cnt := cnt + 1;
         END IF;
      END LOOP;
      IF cnt = 2 THEN
         DBMS_OUTPUT.PUT_LINE(i);
      END IF;
   END LOOP;
END;
/



#FIBONACCI NUMBER
DECLARE
   n NUMBER := &num;
   a NUMBER := 0;
   b NUMBER := 1;
   c NUMBER;
   i NUMBER;
BEGIN
   DBMS_OUTPUT.PUT_LINE(a);
   DBMS_OUTPUT.PUT_LINE(b);

   FOR i IN 3..n LOOP
      c := a + b;
      DBMS_OUTPUT.PUT_LINE(c);
      a := b;
      b := c;
   END LOOP;
END;
/


