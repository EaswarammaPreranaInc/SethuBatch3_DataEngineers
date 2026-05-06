'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
import mysql.connector

# connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Teji@1836",
    database="emp"
)
cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM employee")
total_rows = cur.fetchone()[0]
n = int(input("Enter number of records to fetch: "))
if n > total_rows:
    print("Invalid input! You requested more records than available.")
    print(f"Total records available: {total_rows}")
else:
    cur.execute("SELECT * FROM emp")
    rows = cur.fetchmany(n)
    print(f"\nFirst {n} records:")
    for row in rows:
        print(row)
cur.close()
con.close()
--------------------------------------------------------------------------------------------------------
# Write  a  program  to  insert  multiple  rows  into  emp  table
import mysql.connector

# connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Teji@1836",
    database="emp"
)
cur = con.cursor()
data = [
    (101, 'A', 5000),
    (102, 'B', 6000),
    (103, 'C', 7000),
    (104, 'D', 8000)
]
query = "INSERT INTO employee (emp_id, name, salary) VALUES (%s, %s, %s)"
cur.executemany(query, data)
con.commit()
print("Records inserted successfully!")
cur.close()
con.close()