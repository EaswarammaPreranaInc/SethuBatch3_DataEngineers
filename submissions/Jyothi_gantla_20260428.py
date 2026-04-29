import mysql.connector
try:
    con = mysql.connector.connect(database = "emp" ,host ="localhost",password= "abc@1234",user = "root")
    cur = con.cursor()
    cur.execute("select * from emp")
    print(cur.rowcount)
    for x in cur:
        print(x)
    cur.close()
    con.close()
except:
    print("Enter proper database")




con = mysql.connector.connect(database = "employee" ,host ="localhost",password= "abc@1234",user = "root")
cur = con.cursor()
cur.execute("""select * from employees_demo""")
def new_func(cur):
    print(f"{'empno':5}\t{'ename':10}\t{'sal':10}")
    while tpl := cur.fetchone():
        print(f"{tpl[0]} \t {tpl[1]:10} \t {tpl[3]:5}")
new_func(cur)



con = mysql.connector.connect(database = "employee" ,host ="localhost",password= "abc@1234",user = "root")
cur = con.cursor()
cond= input("Enter:")
cur.execute(f"select * from employees_demo where {cond}")
def new_func(cur):
    print(f"{'empno':<10}\t{'ename':<10}\t{'sal':<10}")
    c=0
    while tpl := cur.fetchone():
        print(f"{tpl[0]:<10} \t {tpl[1]:<10} \t {tpl[3]:<10}")
        c +=1
    if c > 0:
        print("Number of tuples:",c)
    else:
        c = -1
        print("Number of tuples:",c)
new_func(cur)


con = mysql.connector.connect(database = "employee" ,host ="localhost",password= "abc@1234",user = "root")
cur = con.cursor()
table=input("Enter:")
cond= input("Enter:")
cur.execute(f"select * from {table} where {cond}")
c = 0
print(f"{'empno':10}\t{'ename':10}\t{'sal':10}")
while True:
    try :
        tpl = next(cur)
        print(f"{tpl[0]:<10} \t {tpl[1]:10} \t {tpl[3]:10}")
        c +=1
    except:
        break
if c > 0:
        print("Number of tuples:",c)
else:
        c = -1
        print("Number of tuples:",c)



con = mysql.connector.connect(database = "employee" ,host ="localhost",password= "abc@1234",user = "root")
cur = con.cursor()
cur.execute("select * from employees_demo")
list = cur.fetchall()
print(f"{'empno':5}\t{'ename':10}\t{'sal':10}")
for tpl in list:
    print(f"{tpl[0]} \t {tpl[1]:10} \t {tpl[3]:5}")




con = mysql.connector.connect(database = "employee" ,host ="localhost",password= "abc@1234",user = "root")
cur = con.cursor()
cond= input("Enter column name:")
order=  input("Enter order: ")
cur.execute(f"select * from employees_demo order by {cond} {order} ")
def new_func(cur):
    print(f"{'empno':<10}\t{'ename':<10}\t{'sal':<10}")
    c=0
    while tpl := cur.fetchone():
        print(f"{tpl[0]:<10} \t {tpl[1]:<10} \t {tpl[3]:<10}")
        c +=1
    if c > 0:
        print("Number of tuples:",c)
    else:
        c = -1
        print("Number of tuples:",c)
new_func(cur)
