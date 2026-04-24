1) CREATION OF STUDENT TABLE

#DECLARE
    lv_slno        student.slno%TYPE:= &slno; 
    lv_name        student.sname%TYPE;
    lv_math        student.mathmarks%TYPE;
    lv_phy         student.phymarks%TYPE;
    lv_che         student.chemarks%TYPE;
    lv_total       NUMBER;
    lv_avg         NUMBER;
    lv_result      VARCHAR2(10);
BEGIN
  
    SELECT sname, mathmarks, phymarks, chemarks
    INTO lv_name, lv_math, lv_phy, lv_che
    FROM student
    WHERE slno = lv_slno;

    lv_total := lv_math + lv_phy + lv_che;
    lv_avg := lv_total / 3;

    IF lv_math >= 35 AND lv_phy >= 35 AND lv_che >= 35 THEN
        lv_result := 'PASS';
    ELSE
        lv_result := 'FAIL';
    END IF;

    DBMS_OUTPUT.PUT_LINE('Name: ' || lv_name);
    DBMS_OUTPUT.PUT_LINE('Total Marks: ' || lv_total);
    DBMS_OUTPUT.PUT_LINE('Average Marks: ' || lv_avg);
    DBMS_OUTPUT.PUT_LINE('Result: ' || lv_result);

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Student not found');
END;

2) POWER BILL 

DECLARE
    lv_units NUMBER := &units;  
    lv_bill  NUMBER := 0;
BEGIN
    IF lv_units <= 100 THEN
        lv_bill := lv_units * 1.5;

    ELSIF lv_units <= 200 THEN
        lv_bill := (100 * 1.5) + (lv_units - 100) * 2.5;

    ELSIF lv_units <= 300 THEN
        lv_bill := (100 * 1.5) + (100 * 2.5) + (lv_units - 200) * 4;

    ELSE
        lv_bill := (100 * 1.5) + (100 * 2.5) + (100 * 4) + (lv_units - 300) * 6;
    END IF;

    DBMS_OUTPUT.PUT_LINE('Units Consumed: ' || lv_units);
    DBMS_OUTPUT.PUT_LINE('Total Bill: ₹' || lv_bill);

END;


