1. create a view based on multiple tables.
CREATE  VIEW view_name AS
SELECT Column1 , Column2,
FROM table1
JOIN table2
ON table1.common_column = table2.common_column;

2.what are pseudo columns which are using for sequences.
Pseudo columns in the sequence:
1.NEXTVAL: This pseudo column is used to genereate the value from the given sequence.
2.CURRVAL: This pseudo column is used to display the current sequence value from the given sequence.
select slno_seq.currval from dual;
select slno_seq.nextval from dual;

3.can we create a view without table.
Yes, we can create a view using only expressions or functions without referencing a physical table.
CREATE VIEW dummy_view AS
SELECT 'Hello' AS message;

4.I have created a table T1 and inserted 10 records  and based on T1 I have created view V1 
after that I have deleted 2 records from T1 , now when we query from V1 how many records fetch.
The view will reflect the current state of the underlying table,so querying V1 will fetch 8 records.

5.How to  increase the maxvalue of the sequence.
ALTER SEQUENCE  sequence_name
MAXVALUE new_max_value;

6.How to remove the views.
DROP VIEW view_name;
