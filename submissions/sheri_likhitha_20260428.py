import sqlite3

# connect to database
con = sqlite3.connect("emp.db")

# create cursor
cur = con.cursor()

# execute query
cur.execute("select * from emp")

# fetch and print records one by one
row = cur.fetchone()

while row:
    print(row)
    row = cur.fetchone()

# close connection
con.close()




import sqlite3

# connect to database
con = sqlite3.connect("emp.db")

# create cursor
cur = con.cursor()

# read condition from user
cond = input("Enter condition (e.g. sal > 3000): ")

# execute query with user condition
cur.execute(f"select * from emp where {cond}")

# fetch and print records one by one
row = cur.fetchone()

while row:
    print(row)
    row = cur.fetchone()

# close connection
con.close()




import sqlite3

# connect to database
con = sqlite3.connect("emp.db")

# create cursor
cur = con.cursor()

# read column name from user
colname = input("Enter column name to sort (e.g. sal, ename): ")

# execute query
cur.execute(f"select * from emp order by {colname}")

# fetch and print records one by one
row = cur.fetchone()

while row:
    print(row)
    row = cur.fetchone()

# close connection
con.close()




import sqlite3

# connect to database
con = sqlite3.connect("emp.db")

# create cursor
cur = con.cursor()

# read table name from user
table = input("Enter table name: ")

# execute query
cur.execute(f"select * from {table}")

print("Table Records:\n")

# fetch and print using next()
try:
    while True:
        row = next(cur)   # gets next tuple
        print(row)
except StopIteration:
    pass

# close connection
con.close()




import sqlite3

# connect to database
con = sqlite3.connect("emp.db")

# create cursor
cur = con.cursor()

# execute query
cur.execute("select * from emp")

# fetch all records into a list
rows = cur.fetchall()

# print each tuple using for loop
for row in rows:
    print(row)

# close connection
con.close()