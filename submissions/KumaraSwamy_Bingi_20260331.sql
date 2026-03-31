CREATE VIEW employee_details_v AS
SELECT 
    e.emp_id, 
    e.first_name, 
    d.dept_name, 
    l.city
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
JOIN locations l   ON d.loc_id = l.loc_id;

SELECT my_sequence.NEXTVAL FROM dual;
SELECT my_sequence.CURRVAL FROM dual;

CREATE FORCE VIEW v_pending_table AS 
SELECT * FROM table_not_yet_created;

CREATE VIEW v_status_codes AS 
SELECT 1 AS id, 'Active' AS status FROM dual;

-- Answer to Q4: 8 records will be fetched.

ALTER SEQUENCE my_sequence_name 
MAXVALUE 50000 
NOCYCLE;

DROP VIEW employee_details_v;