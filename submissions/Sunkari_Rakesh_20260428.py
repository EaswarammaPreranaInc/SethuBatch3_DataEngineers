import oracledb
conn = oracledb.connect(
    user="system",
    password="*****",
    dsn="localhost:1521/ORCL"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM emp2")
print("empno\tename\tsal")
for x in cursor:
    
    print(f'{x[0]}\t{x[1]}\t{x[2]}')
print(f'number pf tuples : {cursor.rowcount}')

cond=input("Enter condition : ")
cursor.execute(f"SELECT * FROM emp2 where {cond}")
print("based on condition ",cond)
print("empno\tename\tsal")
while t:=cursor.fetchone():
    print(f'{t[0]}\t{t[1]}\t{t[2]}')
    

cond2=input("Enter condition2 : ")
cursor.execute(f"SELECT * FROM emp2 order by {cond2}")
print("based on condition ",cond)
print("empno\tename\tsal")
while t:=cursor.fetchone():
    print(f'{t[0]}\t{t[1]}\t{t[2]}')
    

cursor.execute(f"SELECT * FROM emp2")
print("fetching using next() ")
print("empno\tename\tsal")
while True:
    try:
        t=cursor.__next__()
        print(f'{t[0]}\t{t[1]}\t{t[2]}')
    except StopIteration:
        break

    

