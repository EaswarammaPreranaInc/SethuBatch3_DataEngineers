#1
'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
import mysql . connector

try:
    con = mysql . connector . connect(host = 'localhost' , database = 'empdb' , user = 'root' , password = '')

    cur = con . cursor()
    cur . execute('select * from emp')

    print(cur . rowcount)

    row = cur . fetchone()

    while row:
        print(row[0] , row[1] , row[2] , sep = '\t')
        row = cur . fetchone()

    print('Number of tuples:', cur . rowcount)

    cur.close()
    con.close()

except mysql . connector . errors . ProgrammingError:
    print('Invalid Database / User / Password / Table')
except mysql . connector . errors . DatabaseError:
    print('Start MySQL')


#2
'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->   Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''
import mysql . connector

try:
    con = mysql . connector . connect(host = 'localhost' , database = 'empdb' , user = 'root' , password = '')

    cur = con . cursor()

    cond = input('Enter condition:')

    cur . execute(f'select * from emp where {cond}')

    print(cur . rowcount)

    for row in cur:
        print(row[0] , row[1] , row[2] , sep = '\t')

    print('Number of tuples:', cur . rowcount)

    cur . close()
    con . close()

except mysql . connector . errors . ProgrammingError:
    print('Invalid Database / User / Password / Table')
except mysql . connector . errors . DatabaseError:
    print('Start MySQL')
    


#3
'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
import mysql . connector

try:
    con = mysql . connector . connect(host = 'localhost' , database = 'empdb' , user = 'root' , password = '')

    cur = con . cursor()

    colname = input('Enter column name to sort:')

    cur . execute(f'select * from emp order by {colname}')

    print(cur . rowcount)

    for row in cur:
        print(row[0] , row[1] , row[2] , sep = '\t')

    print('Number of tuples:', cur . rowcount)

    cur . close()
    con . close()

except mysql . connector . errors . ProgrammingError:
    print('Invalid Database / User / Password / Table')
except mysql . connector . errors . DatabaseError:
    print('Start MySQL')



#4
'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Raises StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''
import mysql . connector

try:
    con = mysql . connector . connect(host = 'localhost' , database = 'empdb' , user = 'root' , password = '')

    cur = con . cursor()

    table = input('Enter table name:')

    cur . execute(f'select * from {table}')

    print(cur . rowcount)

    while True:
        try:
            row = next(cur)
            print(row[0] , row[1] , row[2] , sep = '\t')
        except StopIteration:
            break

    print('Number of tuples:', cur . rowcount)

    cur . close()
    con . close()

except mysql . connector . errors . ProgrammingError:
    print('Invalid Database / User / Password / Table')
except mysql . connector . errors . DatabaseError:
    print('Start MySQL')



#5
'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
import mysql . connector

try:
    con = mysql . connector . connect(host = 'localhost' , database = 'empdb' , user = 'root' , password = '')

    cur = con . cursor()

    cur . execute('select * from emp')

    print(cur . rowcount)

    rows = cur . fetchall()

    for row in rows:
        print(row[0] , row[1] , row[2] , sep = '\t')

    print('Number of tuples:', cur . rowcount)

    cur . close()
    con . close()

except mysql . connector . errors . ProgrammingError:
    print('Invalid Database / User / Password / Table')
except mysql . connector . errors . DatabaseError:
    print('Start MySQL')



#6
for  i  in   range(4):  #  i = 0
	for   i   in  range(2): #  i = 1
			pass
	print(i) # 1 , 1 , 1 , 1



#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
from random import randint

for i in range(10):
    otp = ''
    for i in range(6):
        otp += str(randint(0 , 9))
    print(otp)
