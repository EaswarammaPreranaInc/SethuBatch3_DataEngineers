# ============================================================
# 1. Display employees who have more than 30 years of experience
# ============================================================

SELECT *
FROM emp
WHERE MONTHS_BETWEEN(SYSDATE, hiredate) / 12 > 30;


# ============================================================
# 2. Split string into First Name, Middle Name, Last Name
# Input: 'Raja Ram Mohan'
# ============================================================

SELECT 
    REGEXP_SUBSTR('Raja Ram Mohan', '[^ ]+', 1, 1) AS first_name,
    REGEXP_SUBSTR('Raja Ram Mohan', '[^ ]+', 1, 2) AS middle_name,
    REGEXP_SUBSTR('Raja Ram Mohan', '[^ ]+', 1, 3) AS last_name
FROM dual;


# ============================================================
# 3. Display salary in format (prefix with X)
# Example:
# 5000 → XXX5000
# 800  → XXXX800
# ============================================================

SELECT ename, sal,
       LPAD(sal, LENGTH(sal) + 3, 'X') AS formatted_salary
FROM emp;


# ============================================================
# 4. Display output as: "ENAME is working as JOB"
# ============================================================

SELECT ename || ' is working as ' || job AS employee_info
FROM emp;

# ============================================================