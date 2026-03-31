# ============================================================
# 1. Display employees whose name contains exactly 5 characters
# ============================================================

SELECT *
FROM emp
WHERE LENGTH(ename) = 5;


# ============================================================
# 2. Display employees whose names do NOT contain 'A'
# ============================================================

SELECT *
FROM emp
WHERE UPPER(ename) NOT LIKE '%A%';


# ============================================================
# 3. Employees working as CLERK with salary between 1000–2000
# ============================================================

SELECT *
FROM emp
WHERE job = 'CLERK'
AND sal BETWEEN 1000 AND 2000;


# ============================================================
# 4. Employees who are NOT getting commission
# ============================================================

SELECT *
FROM emp
WHERE comm IS NULL;


# ============================================================
# 5. Employees whose annual salary > 30000
# ============================================================

SELECT *
FROM emp
WHERE sal * 12 > 30000;


# ============================================================
# 6. Create COLLEGE table (Parent Table)
# ============================================================

CREATE TABLE college_details (
    college_code VARCHAR2(30) PRIMARY KEY,
    college_name VARCHAR2(100),
    principal_name VARCHAR2(100),
    college_address VARCHAR2(200)
);


# ============================================================
# 7. Create STUDENT table (Child Table with constraints)
# ============================================================

CREATE TABLE student_details (
    slno NUMBER PRIMARY KEY,
    sname VARCHAR2(30),
    dob DATE NOT NULL,
    fname VARCHAR2(30),
    college_code VARCHAR2(30),
    fees NUMBER CHECK (fees > 0),

    CONSTRAINT fk_college
    FOREIGN KEY (college_code)
    REFERENCES college_details(college_code)
);


# ============================================================
# 8. Get constraint details of STUDENT table
# ============================================================

SELECT constraint_name, constraint_type, table_name
FROM user_constraints
WHERE table_name = 'STUDENT_DETAILS';


# ============================================================
# 9. Modify NULL values to 100 in SLNO column
# ============================================================

# NOTE: SLNO is PRIMARY KEY → cannot be NULL normally

UPDATE student_details
SET slno = 100
WHERE slno IS NULL;


# ============================================================
# 10. Difference between TRUNCATE, DELETE, DROP
# ============================================================

# DELETE:
# - Removes selected rows (WHERE allowed)
# - Can rollback
# - Slower

# TRUNCATE:
# - Removes all rows (no WHERE)
# - Cannot rollback
# - Faster

# DROP:
# - Deletes entire table (structure + data)
# - Cannot rollback
# - Table removed permanently

# ============================================================