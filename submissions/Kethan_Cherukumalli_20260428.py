#1
'''
Write a program to print emp table of the database with fetchone() method

emp table ----------------> cursor object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''

import sqlite3

con = sqlite3.connect('mydb.db')
cur = con.cursor()

cur.execute('select * from emp')

while True:
	tpl = cur.fetchone()
	if tpl is None:
		break
	print(tpl)

con.close()



#2
'''
Write a program to print emp table based on user condition

1) How to call execute() method ?  --->  cur.execute(f'select * from emp where {cond}')
2) What is the pre-requisite to call execute() method ?  ---> Read the condition from the user

emp table ----------------> cursor object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()             print()
'''

import sqlite3

con = sqlite3.connect('mydb.db')
cur = con.cursor()

cond = input('Enter condition : ')
cur.execute(f'select * from emp where {cond}')

while True:
	tpl = cur.fetchone()
	if tpl is None:
		break
	print(tpl)

con.close()



#3
'''
Write a program to print emp table in sorted order

1) How to call execute() method ?  --->  cur.execute(f'select * from emp order by {colname}')
2) What is the pre-requisite to call execute() method ?  ---> Read the colname

emp table ----------------> cursor object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''

import sqlite3

con = sqlite3.connect('mydb.db')
cur = con.cursor()

colname = input('Enter column name : ')
cur.execute(f'select * from emp order by {colname}')

while True:
	tpl = cur.fetchone()
	if tpl is None:
		break
	print(tpl)

con.close()



#4
'''
Write a program to print user input table with next() function

1) How to call execute() method ?  --->  cur.execute(f'select * from {table}')
2) What is the pre-requisite to call execute() method ?  ---> Read the table name
3) What does next(cur) do ?  ---> Yields the next tuple of cursor object
4) What does next() function do when end of the cursor is reached ?  ---> Raises StopIteration error

emp table ----------------> cursor object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''

import sqlite3

con = sqlite3.connect('mydb.db')
cur = con.cursor()

table = input('Enter table name : ')
cur.execute(f'select * from {table}')

while True:
	try:
		tpl = next(cur)
		print(tpl)
	except StopIteration:
		break

con.close()



#5
'''
Write a program to print cursor with fetchall() method

emp table ---------------> cur object ---------------> list -------------> tpl ------------> monitor
                   execute()                           fetchall()              for loop        print()
'''

import sqlite3

con = sqlite3.connect('mydb.db')
cur = con.cursor()

cur.execute('select * from emp')
lst = cur.fetchall()

for tpl in lst:
	print(tpl)

con.close()



#6
# Repeat previous program such that OTP can be between 000000 and 999999 (may be 000156)
from random import randint

for i in range(10):
	otp = f'{randint(0, 999999):06d}'
	print(otp)