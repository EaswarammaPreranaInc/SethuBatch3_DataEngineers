'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
'''
import mysql.connector as mc
con = mc.connect(host='localhost',user='root',password='Dhanya@120805',database='emp')
cur = con.cursor()
c = con.cursor()
c.execute('select * from emp')
l = c.fetchall()
n = int(input("How many rows ? :  "))
try:
    if n<=0 or n>len(l):
        print('Invalid input')
    else:
        try:
            cur.execute('select * from emp')
            list = cur.fetchmany(n)
            for x in cur.description:
                print(f'{x[0]:^10}',end='\t')
            print()
            for row in list:
                for val in row:
                    print(f'{val:^10}',end='\t')
                print()
            print('Number of tuples fetched :  ',cur.rowcount)
            cur.close() 
            con.close()
        except mc.errors.InternalError:
            print('Cursor can not be closed')
except mc.errors.InterfaceError:
    print('Please connect to the database')
except mc.errors.ProgrammingError:
    print('The database or user or password is incorrect')
'''



'''
# Write  a  program  to  insert  multiple  rows  into  emp  table
'''

'''
import mysql.connector as mc
con = mc.connect(host='localhost',user='root',password='Dhanya@120805',database='emp')
cur = con.cursor()
n = int(input("How many rows would you like to insert ?  :  "))
try:
    list = []
    for i in range(n):
        print('Employee : ',i+1)
        emp_no = int(input('Enter employee number : '))
        emp_name = input('Enter employee name :  ')
        emp_sal = int(input('Enter salary : '))
        temp = (emp_no,emp_name,emp_sal)
        list.append(temp)
    cur.executemany('insert into emp values (%s,%s,%s)',list)
    print(f'{cur.rowcount} rows are inserted')
    cur.close() 
    con.close()
except mc.errors.IntegrityError as msg:
    print('Duplicate emp no  : ',msg)
except mc.errors.InterfaceError:
    print('Please connect to the database')
except mc.errors.ProgrammingError:
    print('The database or user or password is incorrect')
'''