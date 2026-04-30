'''prog8b(fetchmany)
Write  a  program  to  print  first  'n'  rows  of  emp  table
 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
How many rows ? : 2
   empno            ename            sal
    111          Rama Rao        10000.0
    222             Sita         20000.0
Number of tuples fetched : 2
Cursor can not be closed
How many rows ? : 5
   empno            ename            sal
    111          Rama Rao        10000.0
    222             Sita         20000.0
    333            Rajesh        15000.0
Number of tuples fetched : 3
How many rows ? : 0
Number of tuples fetched : 0
How many rows ? : -1
Number of tuples fetched : 0

import mysql.connector as mc
try:
    con = mc.connect(database='emp1', user='root')
    cur = con.cursor()
    n = int(input('How many rows ? : '))
    if n <= 0:
        rows = []
    else:
        cur.execute('select * from emp')
        rows = cur.fetchmany(n)
    if len(rows) > 0:
        for x in cur.description:
            print('{:^10}'.format(x[0]), end='\t')
        print()
        for tpl in rows:
            for x in tpl:
                print('{:^10}'.format(str(x)), end='\t')
            print()
    print('Number of tuples fetched :', len(rows))
    try:
        cur.close()
    except:
        print('Cursor can not be closed')
    con.close()
except mc.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) tablename')
except mc.errors.InterfaceError:
    print('Pls start mysql')
'''
'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method

Sample output:
How many rows ? : 5
Invalid input
How many rows ? : 0
Invalid input
How many rows ? : 3
 empno        ename        sal
 111          AAA          10000.0
 222          BBB          20000.0
 333          CCC          15000.0
Number of rows : 3
Cursor can not be closed
'''
import mysql.connector as mc

try:
    con = mc.connect(database='emp1', user='root')
    cur = con.cursor()
    n = int(input('How many rows ? : '))
    if n <= 0:
        print('Invalid input')
    else:
        cur.execute('select count(*) from emp')
        total = cur.fetchone()[0]
        if n > total:
            print('Invalid input')
        else:
            cur.execute('select * from emp')
            rows = cur.fetchmany(n)
            for x in cur.description:
                print('{:^10}'.format(x[0]), end='\t')
            print()
            for tpl in rows:
                for x in tpl:
                    print('{:^10}'.format(str(x)), end='\t')
                print()
            print('Number of rows :', len(rows))
    try:
        cur.close()
    except:
        print('Cursor can not be closed')
    con.close()
except mc.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) tablename')
except mc.errors.InterfaceError:
    print('Pls start mysql')

'''
# Write  a  program  to  insert  multiple  rows  into  emp  table

How many rows would you like to insert ? : 3

Employee : 1
Enter employee number : 777
Enter employee name : PPP
Enter salary : 70000

Employee : 2
Enter employee number : 888
Enter employee name : QQQ
Enter salary : 80000

Employee : 3
Enter employee number : 999
Enter employee name : RRR
Enter salary : 90000

3 rows are inserted
-----------------------------------------------
How many rows would you like to insert ? : 3

Employee : 1
Enter employee number : 100
Enter employee name : A
Enter salary : 10000

Employee : 2
Enter employee number : 100
Enter employee name : B
Enter salary : 20000

Employee : 3
Enter employee number : 200
Enter employee name : C
Enter salary : 30000
Duplicate emp no : 1062 (23000): Duplicate entry '100' for key 'PRIMARY'
'''
import mysql.connector as mc
try:
    con = mc.connect(database='emp1', user='root', password='Umadevi@123')
    cur = con.cursor()
    n = int(input('How many rows would you like to insert ? : '))
    data = []
    for i in range(1, n + 1):
        print('\nEmployee :', i)
        empno = int(input('Enter employee number : '))
        ename = input('Enter employee name : ')
        sal = float(input('Enter salary : '))
        data.append((empno, ename, sal))
    for row in data:
        try:
            cur.execute("insert into emp values (%s,%s,%s)", row)
        except mc.errors.IntegrityError as e:
            print('Duplicate emp no :', e)
            break
    con.commit()
    print(f'{cur.rowcount} rows are inserted')
    cur.close()
    con.close()
except mc.errors.ProgrammingError:
    print('Invalid database (or) user (or) password (or) tablename')
except mc.errors.InterfaceError:
    print('Pls start mysql')