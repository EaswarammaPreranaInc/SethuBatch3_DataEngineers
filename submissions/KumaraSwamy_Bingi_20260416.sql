-- 1. ODD NUMBERS FROM 1 TO N
DECLARE
    n NUMBER := 20;
    i NUMBER := 1;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Odd Numbers from 1 to ' || n || ':');
    WHILE i <= n LOOP
        IF MOD(i, 2) != 0 THEN
            DBMS_OUTPUT.PUT_LINE(i);
        END IF;
        i := i + 1;
    END LOOP;
END;
/


-- 2. PALINDROME CHECK
DECLARE
    num NUMBER := 121;
    temp NUMBER;
    rev NUMBER := 0;
    remainder NUMBER;
BEGIN
    temp := num;
    WHILE temp > 0 LOOP
        remainder := MOD(temp, 10);
        rev := (rev * 10) + remainder;
        temp := TRUNC(temp / 10);
    END LOOP;
    IF rev = num THEN
        DBMS_OUTPUT.PUT_LINE(num || ' is a Palindrome');
    ELSE
        DBMS_OUTPUT.PUT_LINE(num || ' is not a Palindrome');
    END IF;
END;
/


-- 3. PRIME NUMBERS FROM 1 TO N
DECLARE
    n NUMBER := 50;
    i NUMBER;
    j NUMBER;
    is_prime BOOLEAN;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Prime Numbers from 1 to ' || n || ':');
    FOR i IN 2..n LOOP
        is_prime := TRUE;
        FOR j IN 2..TRUNC(SQRT(i)) LOOP
            IF MOD(i, j) = 0 THEN
                is_prime := FALSE;
                EXIT;
            END IF;
        END LOOP;
        IF is_prime THEN
            DBMS_OUTPUT.PUT_LINE(i);
        END IF;
    END LOOP;
END;
/


-- 4. FIBONACCI SERIES USING WHILE LOOP
DECLARE
    n NUMBER := 10;
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
    i NUMBER := 1;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Fibonacci Series using WHILE Loop:');
    DBMS_OUTPUT.PUT_LINE(a);
    DBMS_OUTPUT.PUT_LINE(b);
    WHILE i <= n - 2 LOOP
        c := a + b;
        DBMS_OUTPUT.PUT_LINE(c);
        a := b;
        b := c;
        i := i + 1;
    END LOOP;
END;
/


-- 4. FIBONACCI SERIES USING FOR LOOP
DECLARE
    n NUMBER := 10;
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Fibonacci Series using FOR Loop:');
    DBMS_OUTPUT.PUT_LINE(a);
    DBMS_OUTPUT.PUT_LINE(b);
    FOR i IN 1..n - 2 LOOP
        c := a + b;
        DBMS_OUTPUT.PUT_LINE(c);
        a := b;
        b := c;
    END LOOP;
END;
/


-- 4. FIBONACCI SERIES USING LOOP...EXIT WHEN
DECLARE
    n NUMBER := 10;
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
    i NUMBER := 1;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Fibonacci Series using LOOP...EXIT WHEN:');
    DBMS_OUTPUT.PUT_LINE(a);
    DBMS_OUTPUT.PUT_LINE(b);
    LOOP
        EXIT WHEN i > n - 2;
        c := a + b;
        DBMS_OUTPUT.PUT_LINE(c);
        a := b;
        b := c;
        i := i + 1;
    END LOOP;
END;
/
