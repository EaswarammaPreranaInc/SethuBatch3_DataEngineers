#1
'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
import mysql . connector as msc

try:
    con = msc . connect(host = 'localhost' , database = 'PDBC' , user = 'root' , password = '')

    cur = con . cursor()

    cur . execute('SELECT COUNT(*) FROM employees')
    total = cur . fetchone()[0]

    n = int(input('How many rows to be fetched?: '))

    if n <= 0:
        print(f'Invalid Input, {n} rows cannot be fetched')
        exit()

    if n > total:
        print('Invalid Input, the table has fewer rows than given input')
        exit()

    cur . execute('SELECT * FROM employees')
    rows = cur . fetchmany(n)

    for x in cur . description:
        print(f'{x[0]:^10}', end='\t')
    print()

    for row in rows:
        for col in row:
            print(f'{str(col):^10}', end='\t')
        print()

    print('\nNumber of tuples fetched:', len(rows))

    cur . close()
    con . close()
except msc . errors . ProgrammingError:
    print('Invalid Database / User / Password / Table')
except msc . errors . InternalError:
    print('Cursor cannot be closed')



# Write  a  program  to  insert  multiple  rows  into  emp  table
import mysql . connector as msc

try:
    con = msc . connect(host = 'localhost' , database = 'PDBC' , user = 'root' , password = '')

    cur = con.cursor()

    n = int(input('How many rows would you like to insert?'))

    l = []

    for i in range(n):
        print(f'Student {i + 1}')
        v = int(input('Enter Student ID:'))
        w = input('Enter Student Name:')
        x = input('Enter Major:')
        y = float(input('Enter CPGA (out of 5):'))
        z = int(input('Enter Enrollment Year:'))

        a = (v , w , x , y , z)

        l . append (a)

    cur . executemany('insert into students values (%s , %s , %s , %s , %s)', l)
    con . commit()

    print(f'{cur . rowcount} row(s) inserted')

    cur . close()
    con . close()

except msc . errors . IntegrityError:
    print('Duplicate Student ID cannot be inserted')
except msc . errors . ProgrammingError:
    print('Invalid Database / User / Password / Table')    


#1
import pandas as pd 
from sqlalchemy import create_engine
from sqlalchemy . engine import URL

connection_url = URL.create(
    drivername = "mysql+pymysql",
    username = "root",
    password = "",
    host = "localhost",
    database = "PDBC"
    )
engine = create_engine(connection_url)
df = pd . read_sql("select  *  from   employees", engine)
for x in df . columns:
    print(x , end = '\t')
print()	
for x in df . itertuples(index = False):
    print(x[0] , x[1] , x[2] , sep = '\t')
