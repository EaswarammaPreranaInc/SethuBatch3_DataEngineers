'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
# import mysql.connector
# try:
#     con = mysql.connector.connect(host="localhost", database="studentdb", user = 'root' , password = 'keerthi123')
#     cur = con.cursor()
#     cur.execute("select * from company_employees")
#     while  tpl  := cur . fetchone():
#         print(f"{tpl[0]:<5} {tpl[2]:<10} {tpl[6]:<10}")
#     print(f"Number of tuples : {cur.rowcount}")
# except:
#     print("eRROR")

'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''

# import mysql.connector
# try:
#     con = mysql.connector.connect(host="localhost", database="studentdb", user = 'root' , password = 'keerthi123')
#     cur = con.cursor()
#     cond = input("Enter condition :")
#     cur.execute(f"select * from company_employees where {cond}")
#     while  tpl  := cur . fetchone():
#         print(f"{tpl[0]:<5} {tpl[2]:<10} {tpl[6]:<10}")
#     print(f"Number of tuples : {cur.rowcount}")
# except:
#     print("eRROR")


'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
# import mysql.connector
# try:
#     con = mysql.connector.connect(host="localhost", database="studentdb", user = 'root' , password = 'keerthi123')
#     cur = con.cursor()
#     columnname = input("Enter column name :")
#     cur.execute(f"select * from company_employees order by {columnname}")
#     while  tpl  := cur . fetchone():
#         print(f"{tpl[0]:<5} {tpl[2]:<10} {tpl[6]:<10}")
#     print(f"Number of tuples : {cur.rowcount}")
# except:
#     print("eRROR")

'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Raises StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''

#import mysql.connector
# try:
#     con = mysql.connector.connect(host="localhost", database="studentdb", user = 'root' , password = 'keerthi123')
#     cur = con.cursor()
#     tablename = input("Enter table name :")
#     cur.execute(f"select * from {tablename}")
#     c =0
#     while  True:
#         try:
#             tpl = next(cur)
#             print(f"{tpl[0]:<5} {tpl[2]:<10} {tpl[6]:<10}")
#             c +=1
#         except StopIteration:
#             break;
#     print(f"Number of tuples : {c}")
# except:
#     print("eRROR")


'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
import mysql.connector
try:
    con = mysql.connector.connect(host="localhost", database="studentdb", user = 'root' , password = 'keerthi123')
    cur = con.cursor()
    columnname = input("Enter column name :")
    cur.execute(f"select * from company_employees order by {columnname}")
    list_tup = cur . fetchall()
    for tpl in list_tup:
        print(f"{tpl[0]:<5} {tpl[2]:<10} {tpl[6]:<10}")
    print(f"Number of tuples : {cur.rowcount}")
except:
    print("eRROR")

# for  i  in   range(4):  #  i = 0
# 	for   i   in  range(2): #  i = 1
# 			pass
# 	print(i)
#op 
# 1
# 1
# 1
# 1

#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)

import  random
for  x  in  range(10):
    sr = ""
    for i in range(6): 
	    sr += str(random.randint(0 , 9)) 
    print(eval(sr))