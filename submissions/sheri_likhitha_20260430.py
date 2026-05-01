import sqlite3

# connect to database
con = sqlite3.connect("mydb.db")
cur = con.cursor()

# execute query
cur.execute("SELECT * FROM emp")

# get total number of rows
rows = cur.fetchall()
total = len(rows)

# ask user input
n = int(input("Enter number of rows to fetch: "))

# validate input
if n > total:
    print("Requested rows exceed available tuples.")
else:
    # re-execute query because fetchall() exhausted cursor
    cur.execute("SELECT * FROM emp")
    result = cur.fetchmany(n)
    
    for row in result:
        print(row)

# close connection
con.close()





import sqlite3

# connect to database
con = sqlite3.connect("mydb.db")
cur = con.cursor()

# create table (if not exists)
cur.execute("""
CREATE TABLE IF NOT EXISTS emp(
    empno INTEGER,
    ename TEXT,
    sal REAL
)
""")

# multiple rows data
employees = [
    (101, "Alice", 50000),
    (102, "Bob", 60000),
    (103, "Charlie", 55000),
    (104, "David", 65000)
]

# insert multiple rows
cur.executemany("INSERT INTO emp VALUES (?, ?, ?)", employees)

# commit changes
con.commit()

print("Multiple rows inserted successfully.")

# close connection
con.close()



