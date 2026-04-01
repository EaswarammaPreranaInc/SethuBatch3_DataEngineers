1. create a view based on multiple tables.
   #CREATE VIEW view_name AS
   SELECT t1.column1, t2.column2
   FROM table1 t1
   JOIN table2 t2
   ON t1.common_column = t2.common_column;

---

2. what are pseudo columns which are using for sequences.
   #Pseudo columns used with sequences are:

* sequence_name.NEXTVAL → gives next value in sequence
* sequence_name.CURRVAL → gives current value of sequence

Example:
#SELECT seq1.NEXTVAL FROM dual;

---

3. can we create a view without table.
   #NO, we cannot create a view without a base table
   (A view must be based on at least one table or another view)

---

4. I have created a table T1 and inserted 10 records and based on T1 I have created View v1
   after that I have deleted 2 records from T1, now when we query from V1 how many records fetched.
   #SELECT * FROM v1;

Answer: 8 records
(View always shows current data from base table)

---

5. how to increase the maxvalue of the sequence.
   #ALTER SEQUENCE sequence_name
   MAXVALUE new_value;

---

6. how to remove the views
   #DROP VIEW view_name;
