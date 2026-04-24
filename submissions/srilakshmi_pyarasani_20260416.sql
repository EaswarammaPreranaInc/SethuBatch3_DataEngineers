PLSQL 

 Assignments -- 1 to N odd numbers, given number is palindrome or not, 1..N prime numbers, fibonacci series using all types of loops

# 1 TO N ODD NUMBERS

FOR LOOP --

DECLARE
    n NUMBER := 10;
BEGIN
    FOR i IN 1..n LOOP
        IF MOD(i,2) != 0 THEN
            DBMS_OUTPUT.PUT_LINE(i);
        END IF;
    END LOOP;
END;

WHILE LOOP --

DECLARE
    n NUMBER := 10;
    i NUMBER := 1;
BEGIN
    WHILE i <= n LOOP
        IF MOD(i,2) != 0 THEN
            DBMS_OUTPUT.PUT_LINE(i);
        END IF;
        i := i + 1;
    END LOOP;
END;

SIMPLE LOOP --

DECLARE
    n NUMBER := 10;
    i NUMBER := 1;
BEGIN
    LOOP
        EXIT WHEN i > n;
        IF MOD(i,2) != 0 THEN
            DBMS_OUTPUT.PUT_LINE(i);
        END IF;
        i := i + 1;
    END LOOP;
END;


#CHECK PALINDROME

DECLARE
    num NUMBER := 121;
    temp NUMBER;
    rev NUMBER := 0;
    digit NUMBER;
BEGIN
    temp := num;

    WHILE temp > 0 LOOP
        digit := MOD(temp,10);
        rev := rev * 10 + digit;
        temp := TRUNC(temp/10);
    END LOOP;

    IF num = rev THEN
        DBMS_OUTPUT.PUT_LINE('Palindrome');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Not Palindrome');
    END IF;
END;


#PRIME NUMBERS 1 TO N

DECLARE
    n NUMBER := 20;
    i NUMBER;
    j NUMBER;
    flag BOOLEAN;
BEGIN
    FOR i IN 2..n LOOP
        flag := TRUE;

        FOR j IN 2..i-1 LOOP
            IF MOD(i,j) = 0 THEN
                flag := FALSE;
                EXIT;
            END IF;
        END LOOP;

        IF flag = TRUE THEN
            DBMS_OUTPUT.PUT_LINE(i);
        END IF;
    END LOOP;
END;


# FIBONACCI SERIES

FOR LOOP --

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


WHILE LOOP --

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

























