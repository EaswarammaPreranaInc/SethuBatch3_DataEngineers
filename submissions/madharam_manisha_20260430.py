'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="your_database"
    )

    cur = con.cursor()

    # Get total rows
    cur.execute("SELECT * FROM emp")
    all_rows = cur.fetchall()
    total_rows = len(all_rows)

    n = int(input("How many rows ?: "))

    # Validation
    if n <= 0:
        print("Invalid input")

    elif n > total_rows:
        print("Input exceeds number of rows")
        print("Total rows available:", total_rows)

    else:
        # Re-execute query (important!)
        cur.execute("SELECT * FROM emp")

        rows = cur.fetchmany(n)

        print("empno    ename    sal")
        for row in rows:
            print(row[0], "   ", row[1], "   ", row[2])

        print("Number of rows:", len(rows))

except Exception as e:
    print("Error:", e)

finally:
    if cur:
        cur.close()
    if con:
        con.close()
#=======================================================================================================
# Write  a  program  to  insert  multiple  rows  into  emp  table
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="your_database"
    )

    cur = con.cursor()

    n = int(input("How many rows would you like to insert ?: "))

    if n <= 0:
        print("Invalid input")

    else:
        for i in range(1, n + 1):
            print("Employee :", i)

            empno = int(input("Enter employee number : "))
            ename = input("Enter employee name : ")
            sal = float(input("Enter salary : "))

            try:
                cur.execute(
                    "INSERT INTO emp (empno, ename, sal) VALUES (%s, %s, %s)",
                    (empno, ename, sal)
                )
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    print("Duplicate emp no:", empno)
                else:
                    print("Error:", err)

        con.commit()
        print(n, "rows are inserted")

except Exception as e:
    print("Error:", e)

finally:
    if cur:
        cur.close()
    if con:
        con.close()        