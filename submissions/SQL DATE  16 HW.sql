1. Print 1 to N Odd Numbers

DECLARE
    n NUMBER := 10;
BEGIN
    FOR i IN 1..n LOOP
        IF MOD(i,2) != 0 THEN
            DBMS_OUTPUT.PUT_LINE(i);
        END IF;
    END LOOP;
END;
/

Using WHILE Loop
DECLARE
    i NUMBER := 1;
    n NUMBER := 10;
BEGIN
    WHILE i <= n LOOP
        IF MOD(i,2) != 0 THEN
            DBMS_OUTPUT.PUT_LINE(i);
        END IF;
        i := i + 1;
    END LOOP;
END;
/


2. Check Palindrome Number
DECLARE
    num NUMBER := 121;
    temp NUMBER;
    rev NUMBER := 0;
    rem NUMBER;
BEGIN
    temp := num;

    WHILE temp > 0 LOOP
        rem := MOD(temp,10);
        rev := rev * 10 + rem;
        temp := FLOOR(temp/10);
    END LOOP;

    IF num = rev THEN
        DBMS_OUTPUT.PUT_LINE('Palindrome');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Not Palindrome');
    END IF;
END;
/

3. Print 1 to N Prime Numbers
DECLARE
    n NUMBER := 20;
    i NUMBER;
    j NUMBER;
    flag NUMBER;
BEGIN
    FOR i IN 2..n LOOP
        flag := 0;

        FOR j IN 2..i-1 LOOP
            IF MOD(i,j) = 0 THEN
                flag := 1;
                EXIT;
            END IF;
        END LOOP;

        IF flag = 0 THEN
            DBMS_OUTPUT.PUT_LINE(i);
        END IF;
    END LOOP;
END;
/



4. Fibonacci Series
 Using FOR Loop
DECLARE
    n NUMBER := 10;
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
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


Using WHILE Loop
DECLARE
    n NUMBER := 10;
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
    i NUMBER := 3;
BEGIN
    DBMS_OUTPUT.PUT_LINE(a);
    DBMS_OUTPUT.PUT_LINE(b);

    WHILE i <= n LOOP
        c := a + b;
        DBMS_OUTPUT.PUT_LINE(c);
        a := b;
        b := c;
        i := i + 1;
    END LOOP;
END;
/