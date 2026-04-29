'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
import mysql.connector
try:
    con = mysql.connector.connect(database = "emp" ,host ="localhost",password= "Shilpa@2345",user = "root")
    cur = con.cursor()
    cur.execute("select * from emp")
    print(cur.rowcount)
    for x in cur:
        print(x)
    cur.close()
    con.close()
except:
    print("Enter proper database")

'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''
con = mysql.connector.connect(database = "employee" ,host ="localhost",password= "Shilpa@2345",user = "root")
cur = con.cursor()
cur.execute("""select * from employees_demo""")
def new_func(cur):
    print(f"{'empno':5}\t{'ename':10}\t{'sal':10}")
    while tpl := cur.fetchone():
        print(f"{tpl[0]} \t {tpl[1]:10} \t {tpl[3]:5}")
new_func(cur)

'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
con = mysql.connector.connect(database = "employee" ,host ="localhost",password= "Shilpa@2345",user = "root")
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

'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Raises StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''
con = mysql.connector.connect(database = "employee" ,host ="localhost",password= "Shilpa@2345",user = "root")
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


'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
con = mysql.connector.connect(database = "employee" ,host ="localhost",password= "Shilpa@2345",user = "root")
cur = con.cursor()
cur.execute("select * from employees_demo")
list = cur.fetchall()
print(f"{'empno':5}\t{'ename':10}\t{'sal':10}")
for tpl in list:
    print(f"{tpl[0]} \t {tpl[1]:10} \t {tpl[3]:5}")


con = mysql.connector.connect(database = "employee" ,host ="localhost",password= "Shilpa@2345",user = "root")
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