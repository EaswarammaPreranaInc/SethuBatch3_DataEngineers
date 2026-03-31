

1. Create a view based on multiple tables

CREATE VIEW v_emp_dept AS
SELECT e.emp_id, e.emp_name, d.dept_name
FROM emp e
JOIN dept d ON e.dept_id = d.dept_id;

2. what are pseudo columns which are using for sequences.


NEXTVAL → gives next value

CURRVAL → gives current value

SELECT seq_name.NEXTVAL FROM dual;
SELECT seq_name.CURRVAL FROM dual;


3. Can we create a view without table?

CREATE VIEW v_dummy AS
SELECT 1 AS num FROM dual;

4. I have created a table T1 and inserted 10 records and based on T1 I have created View v1
   after that I have deleted 2 records from T1, now when we query from V1 how many records fetched.


CREATE TABLE T1 (
    id NUMBER,
    name VARCHAR2(50)
);

INSERT INTO T1 VALUES (1, 'A');
INSERT INTO T1 VALUES (2, 'B');
INSERT INTO T1 VALUES (3, 'C');
INSERT INTO T1 VALUES (4, 'D');
INSERT INTO T1 VALUES (5, 'E');
INSERT INTO T1 VALUES (6, 'F');
INSERT INTO T1 VALUES (7, 'G');
INSERT INTO T1 VALUES (8, 'H');
INSERT INTO T1 VALUES (9, 'I');
INSERT INTO T1 VALUES (10, 'J');
CREATE VIEW V1 AS
SELECT * FROM T1;
DELETE FROM T1 WHERE id IN (1, 2);
SELECT * FROM V1;
SELECT COUNT(*) FROM V1;



5. how to increase the maxvalue of the sequence.

ALTER SEQUENCE seq_name
MAXVALUE 10000;

6. how to remove the views


DROP VIEW view_name;