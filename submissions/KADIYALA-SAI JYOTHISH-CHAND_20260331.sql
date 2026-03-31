-- 1
SELECT d.*
FROM dept d
WHERE EXISTS (
    SELECT 1
    FROM emp e
    WHERE e.deptno = d.deptno
);

-- 2
SELECT *
FROM emp
WHERE sal >= ALL (
    SELECT SUM(sal)
    FROM emp
    GROUP BY deptno
);

-- 3
SELECT d.*
FROM dept d
JOIN emp e ON d.deptno = e.deptno
GROUP BY d.deptno, d.dname, d.loc
HAVING COUNT(e.empno) > 3;

-- 4
SELECT MAX(sal)
FROM emp
WHERE job = 'CLERK'
  AND deptno = 20;

-- 5
CREATE TABLE emp_dtls (
    empno INT,
    ename VARCHAR(50),
    job VARCHAR(50),
    country_code VARCHAR(10)
);

INSERT INTO emp_dtls VALUES (101,'RAJ','IT','US');
INSERT INTO emp_dtls VALUES (102,'RAM','MED','US');
INSERT INTO emp_dtls VALUES (103,'RAKI','MECH','AUS');
INSERT INTO emp_dtls VALUES (104,'ABC','MECH','IND');
INSERT INTO emp_dtls VALUES (105,'XYZ','IT','IND');

-- 6
CREATE TABLE country_details (
    country_code VARCHAR(10),
    country_name VARCHAR(50),
    code INT
);

INSERT INTO country_details VALUES ('US','United States',01);
INSERT INTO country_details VALUES ('AUS','Australia',61);
INSERT INTO country_details VALUES ('MAL','Malaysia',65);

-- 7
SELECT e.*
FROM emp_dtls e
JOIN country_details c ON e.country_code = c.country_code
WHERE (e.job = 'IT' AND c.country_name = 'INDIA')
   OR (e.job = 'MECH' AND c.country_name = 'Australia');

-- 8
SELECT e.*, c.country_name
FROM emp_dtls e
LEFT JOIN country_details c
ON e.country_code = c.country_code;