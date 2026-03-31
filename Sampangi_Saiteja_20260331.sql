1. create a view based on multiple tables.
CREATE VIEW view_name AS
SELECT t1.column1, t2.column2
FROM table1 t1
JOIN table2 t2
ON t1.common_column = t2.common_column;

2. what are pseudo columns which are using for sequences.

SELECT seq_name.NEXTVAL FROM dual;
SELECT seq_name.CURRVAL FROM dual;

3. can we create a view without table.

CREATE VIEW v1 AS
SELECT 1 AS num FROM dual;

4. I have created a table T1 and inserted 10 records and based on T1 I have created View v1
   after that I have deleted 2 records from T1, now when we query from V1 how many records fetched.
5. how to increase the maxvalue of the sequence.

ALTER SEQUENCE seq_name MAXVALUE 1000;

6. how to remove the views
DROP VIEW view_name;