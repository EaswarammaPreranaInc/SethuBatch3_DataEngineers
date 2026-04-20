/*
Sum 1 to N Odd Numbers
This uses a FOR loop to sum odd numbers from 1 to N efficiently.
*/
DECLARE
    n NUMBER;
    sum_odd NUMBER := 0;
BEGIN
    n := &Enter_N;
    FOR i IN 1..n LOOP
        IF MOD(i, 2) = 1 THEN
            sum_odd := sum_odd + i;
        END IF;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Sum of odd numbers from 1 to ' || n || ' is ' || sum_odd);
END;
/

/*
Palindrome Check
This reverses the input number using a WHILE loop and compares it to the original.
*/
DECLARE
    num NUMBER;
    original_num NUMBER;
    reversed_num NUMBER := 0;
    remainder NUMBER;
BEGIN
    num := &Enter_number;
    original_num := num;
    WHILE num > 0 LOOP
        remainder := MOD(num, 10);
        reversed_num := (reversed_num * 10) + remainder;
        num := TRUNC(num / 10);
    END LOOP;
    IF original_num = reversed_num THEN
        DBMS_OUTPUT.PUT_LINE(original_num || ' is a palindrome.');
    ELSE
        DBMS_OUTPUT.PUT_LINE(original_num || ' is not a palindrome.');
    END IF;
END;
/

/*
Prime Numbers 1 to N
This uses nested FOR loops: outer iterates candidates, inner checks divisibility up to sqrt for efficiency.
*/
DECLARE
    n NUMBER;
    i NUMBER;
    j NUMBER;
    is_prime NUMBER;
BEGIN
    n := &Enter_N;
    DBMS_OUTPUT.PUT_LINE('Prime numbers from 1 to ' || n || ':');
    FOR i IN 2..n LOOP
        is_prime := 1;
        FOR j IN 2..SQRT(i) LOOP
            IF MOD(i, j) = 0 THEN
                is_prime := 0;
                EXIT;
            END IF;
        END LOOP;
        IF is_prime = 1 THEN
            DBMS_OUTPUT.PUT_LINE(i);
        END IF;
    END LOOP;
END;
/

/*
Fibonacci Series (All Loop Types)
Four versions demonstrate FOR, WHILE, BASIC LOOP (with EXIT WHEN), and simulates DO-WHILE via REVERSE FOR (prints first then checks).
*/

#FOR Loop Version:

DECLARE
    n NUMBER;
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
BEGIN
    n := &Enter_terms;
    DBMS_OUTPUT.PUT_LINE('Fibonacci (FOR):');
    DBMS_OUTPUT.PUT_LINE(a);
    DBMS_OUTPUT.PUT_LINE(b);
    FOR i IN 2..n LOOP
        c := a + b;
        DBMS_OUTPUT.PUT_LINE(c);
        a := b;
        b := c;
    END LOOP;
END;
/

#WHILE Loop Version:

DECLARE
    n NUMBER;
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
    i NUMBER := 2;
BEGIN
    n := &Enter_terms;
    DBMS_OUTPUT.PUT_LINE('Fibonacci (WHILE):');
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

#BASIC LOOP Version:

DECLARE
    n NUMBER;
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
    i NUMBER := 2;
BEGIN
    n := &Enter_terms;
    DBMS_OUTPUT.PUT_LINE('Fibonacci (BASIC LOOP):');
    DBMS_OUTPUT.PUT_LINE(a);
    DBMS_OUTPUT.PUT_LINE(b);
    LOOP
        c := a + b;
        DBMS_OUTPUT.PUT_LINE(c);
        a := b;
        b := c;
        i := i + 1;
        EXIT WHEN i > n;
    END LOOP;
END;
/

#DO-WHILE Simulation (REVERSE FOR):

DECLARE
    n NUMBER;
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
BEGIN
    n := &Enter_terms;
    DBMS_OUTPUT.PUT_LINE('Fibonacci (DO-WHILE sim):');
    FOR i IN REVERSE 1..n LOOP
        DBMS_OUTPUT.PUT_LINE(a);
        c := a + b;
        a := b;
        b := c;
    END LOOP;
END;
/