PL SQL ASSIGNMENT (15/04/2026)

#DECLARE
    num1 NUMBER := &ENTER_FIRST_NUMBER;
    num2 NUMBER := &ENTER_SECOND_NUMBER;
    op   CHAR(1) := &'ENTER OPERATOR';
    result NUMBER;
BEGIN
    IF op = '+' THEN
        result := num1 + num2;
        DBMS_OUTPUT.PUT_LINE('Addition = ' || result);

    ELSIF op = '-' THEN
        result := num1 - num2;
        DBMS_OUTPUT.PUT_LINE('Subtraction = ' || result);

    ELSIF op = '*' THEN
        result := num1 * num2;
        DBMS_OUTPUT.PUT_LINE('Multiplication = ' || result);

    ELSIF op = '/' THEN
        IF num2 != 0 THEN
            result := num1 / num2;
            DBMS_OUTPUT.PUT_LINE('Division = ' || result);
        ELSE
            DBMS_OUTPUT.PUT_LINE('Error: Division by zero');
        END IF;

    ELSE
        DBMS_OUTPUT.PUT_LINE('Invalid Operator');
    END IF;
END;


#DECLARE

	LV_JOB = VARHCAR2(20) := &ENTER_JOB_NAME;

BEGIN
 	IF LV_JOB = 'CLERK' THEN
		UPDATE EMP
		SET SAL = SAL (SAL * 10/100)
		WHERE JOB = LV_JOB;

	ELSIF LV_JOB = 'MANAGER' THEN
		UPDATE EMP
		SET SAL = SAL (SAL * 5/100)
		WHERE JOB = LV_JOB;

	ELSIF LV_JOB = 'SALESMAN' THEN
		UPDATE EMP
		SET SAL = SAL (SAL * 8/100)
		WHERE JOB = LV_JOB;

	ELSE 
		UPDATE EMP
		SET SAL = SAL (SAL * 1/100)
		WHERE JOB = LV_JOB;

END IF;

	DBMS_OUTPUT.PUT_LINE('SALARY UPDATED:' || LV_JOB);

END;















