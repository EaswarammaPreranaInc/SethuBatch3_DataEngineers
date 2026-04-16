-- 1. Print Odd Numbers from 1 to N (All Loops)
DECLARE
    n NUMBER := 10;
    i NUMBER;
BEGIN
    -- Using FOR Loop
    FOR j IN 1..n LOOP
        IF MOD(j, 2) != 0 THEN
            DBMS_OUTPUT.PUT_LINE(j);
        END IF;
    END LOOP;

    -- Using WHILE Loop
    i := 1;
    WHILE i <= n LOOP
        DBMS_OUTPUT.PUT_LINE(i);
        i := i + 2;
    END LOOP;

    -- Using Basic LOOP
    i := 1;
    LOOP
        EXIT WHEN i > n;
        DBMS_OUTPUT.PUT_LINE(i);
        i := i + 2;
    END LOOP;
END;
/

-- 2. Check if a Given Number is a Palindrome
DECLARE
    num NUMBER := 12321;
    temp_num NUMBER;
    reversed_num NUMBER := 0;
    remainder NUMBER;
BEGIN
    temp_num := num;
    
    WHILE temp_num > 0 LOOP
        remainder := MOD(temp_num, 10);
        reversed_num := (reversed_num * 10) + remainder;
        temp_num := TRUNC(temp_num / 10);
    END LOOP;

    IF num = reversed_num THEN
        DBMS_OUTPUT.PUT_LINE(num || ' is a Palindrome.');
    ELSE
        DBMS_OUTPUT.PUT_LINE(num || ' is NOT a Palindrome.');
    END IF;
END;
/

-- 3. Print Prime Numbers from 1 to N
DECLARE
    n NUMBER := 20;
    is_prime BOOLEAN;
BEGIN
    FOR i IN 2..n LOOP
        is_prime := TRUE;
        FOR j IN 2..TRUNC(i/2) LOOP
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

-- 4. Fibonacci Series (All Loops)
DECLARE
    n NUMBER := 8;
    a NUMBER;
    b NUMBER;
    c NUMBER;
    counter NUMBER;
BEGIN
    -- Using FOR Loop
    a := 0; b := 1;
    DBMS_OUTPUT.PUT_LINE(a);
    DBMS_OUTPUT.PUT_LINE(b);
    FOR i IN 3..n LOOP
        c := a + b;
        DBMS_OUTPUT.PUT_LINE(c);
        a := b;
        b := c;
    END LOOP;

    -- Using WHILE Loop
    a := 0; b := 1; counter := 3;
    DBMS_OUTPUT.PUT_LINE(a);
    DBMS_OUTPUT.PUT_LINE(b);
    WHILE counter <= n LOOP
        c := a + b;
        DBMS_OUTPUT.PUT_LINE(c);
        a := b;
        b := c;
        counter := counter + 1;
    END LOOP;

    -- Using Basic LOOP
    a := 0; b := 1; counter := 3;
    DBMS_OUTPUT.PUT_LINE(a);
    DBMS_OUTPUT.PUT_LINE(b);
    LOOP
        EXIT WHEN counter > n;
        c := a + b;
        DBMS_OUTPUT.PUT_LINE(c);
        a := b;
        b := c;
        counter := counter + 1;
    END LOOP;
END;
/