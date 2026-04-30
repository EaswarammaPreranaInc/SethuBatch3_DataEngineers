# Write  a  program  to  insert  multiple  rows  into  emp  table


import mysql.connector


try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bindhu@123",    
        database="empdb"
    )

    cur = con.cursor()

    # Multiple rows data
    data = [
        (101, 'Rahul', 50000),
        (102, 'Priya', 60000),
        (103, 'Amit', 55000)
    ]

    # Insert query
    cur.executemany("INSERT INTO emp VALUES (%s, %s, %s)", data)

    con.commit()


except Exception as e:
    print("Error:", e)

finally:
    try:
        cur.close()
        con.close()
    except:
        pass