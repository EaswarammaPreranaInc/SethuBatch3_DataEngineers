
'''
Write a program to print first 'n' rows of emp table

 emp table --------------->  cur object --------------->   list ------------->   tpl ------------>   monitor
                       execute()                          fetchmany(n)              for loop               print()
'''
import mysql.connector as mc
con = mc.connect(host='localhost', user='root', password='root', database='mydb')
cur = con.cursor()
n = int(input('Enter n: '))
cur.execute('select * from emp')
rows = cur.fetchmany(n)
for tpl in rows:
    print(tpl)

con.close()



'''
Write a program to insert rows into emp table, one at a time

1) How to call execute() method ? --->
                                    cur.execute(F"insert into emp values ({empno}, '{ename}', {sal})")

2) Are quotes mandatory for ename ? --->  Yes becoz it is a string

3) What is the pre-requisite to call execute() method ? ---> Read inputs empno, ename and sal

4) cur.execute(F'insert into emp values (25, "Rama Rao", 10000.0)')
    What is the result of cur.rowcount ? ---> 1 becoz only one row is inserted into emp table

5) What happens when we try to insert duplicate empno ? --->  Raises mc.errors.IntegrityError

6) Can a tuple be inserted into MySqlCursor object ? --->  No becoz it is immutable
'''
import mysql.connector as mc
con = mc.connect(host='localhost', user='root', password='root', database='mydb')
cur = con.cursor()
empno = int(input('Enter empno: '))
ename = input('Enter ename: ')
sal = float(input('Enter sal: '))
try:
    cur.execute(F"insert into emp values ({empno}, '{ename}', {sal})")

    con.commit()
    print('Row inserted successfully')
except mc.errors.IntegrityError:
    print('Error: Duplicate empno. IntegrityError raised.')
con.close()



'''
Write a program to delete rows of emp table based on user input condition

1) How to call execute() method ? --->  cur.execute(F'delete from emp where {cond}')

2) What is the pre-requisite to call execute() method ? --->  Read the cond
'''
import mysql.connector as mc
con = mc.connect(host='localhost', user='root', password='root', database='mydb')
cur = con.cursor()
cond = input('Enter condition: ')
cur.execute(F'delete from emp where {cond}')

con.commit()
print(cur.rowcount, 'row(s) deleted')
con.close()




'''
Write a program to modify data of emp table

1) How to call execute() method ? --->  cur.execute(F'update emp set {expr} where {cond}')

2) What is the pre-requisite to call execute() method ? --->  Read expr and cond
'''
import mysql.connector as mc
con = mc.connect(host='localhost', user='root', password='root', database='mydb')
cur = con.cursor()
expr = input('Enter set expression: ')
cond = input('Enter condition: ')
cur.execute(F'update emp set {expr} where {cond}')

con.commit()
print(cur.rowcount, 'row(s) updated')
con.close()




'''
Write a program to create student table

1) How to call execute() method ? ---> cur.execute(F'create table {tablename}(rollno int primary key, sname char(20), marks float)')

2) What is the pre-requisite to call execute() method ? ---> Read the table name

3) What action to be made when table already exists ? ---> Delete the existing table and create a new table with same name
'''
import mysql.connector as mc
con = mc.connect(host='localhost', user='root', password='root', database='mydb')
cur = con.cursor()
tablename = input('Enter table name: ')
cur.execute(F'drop table if exists {tablename}')
cur.execute(F'create table {tablename}(rollno int primary key, sname char(20), marks float)')
print(f'Table {tablename} created successfully')
con.close()




# Parent and Child classes have different class methods
class parent:
    @classmethod
    def m1(cls):
        print('parent  Method')
class child(parent):
    @classmethod
    def m2(cls):
        parent.m1()
        super().m1()
        child.m1()
        cls.m1()
        print('child  Method')
parent.m1()
child.m2()
child.m1()




# Parent and Child classes have same class method
class parent:
    @classmethod
    def m1(cls):
        print('parent  Method')
class child(parent):
    @classmethod
    def m1(cls):
        parent.m1()
        super().m1()
        print('child  Method')
parent.m1()
child.m1()



# Parent and Child classes have different static methods
class parent:
    @staticmethod
    def m1():
        print('parent  method')
class child(parent):
    @staticmethod
    def m2():
        parent.m1()
        child.m1()
        print('child  method')
parent.m1()
child.m2()
child.m1()




# Parent and Child classes have same static method
class parent:
    @staticmethod
    def m1():
        print('parent  method')
class child(parent):
    @staticmethod
    def m1():
        parent.m1()
        print('child  method')
parent.m1()
child.m1()




# Parent and child classes have static variables with different names
class parent:
    x = 10
    def m1(self):
        print(self.x)
        print(parent.x)
class child(parent):
    y = 20
    def m2(self):
        print(self.x)
        print(parent.x)
        print(child.x)
        print(super().x)
        print(self.y)
        print(child.y)
parent().m1()
child().m2()




# Parent and Child classes have static variables with same name
class parent:
    x = 10
    def m1(self):
        print(parent.x)
        print(self.x)
class child(parent):
    x = 20
    def m1(self):
        print(parent.x)
        print(super().x)
        print(child.x)
        print(self.x)
parent().m1()
child().m1()



# What are the outputs if inputs are 10, 20, 30, 40, 50, 60
class parent:
    def get(self):
        # How to read inputs into variables a and b of object
        self.a = int(input())   # Reads 10 into self.a
        self.b = int(input())   # Reads 20 into self.b
    def disp(self):
        # How to print variables a and b of object in same line separated by tab
        print(self.a, self.b, sep='\t')   # 10	20
# End of Parent class
class child(parent):
    def get(self):
        # How to read inputs into variables a and b of object
        super().get()           # Calls parent.get(); reads 30 into self.a, 40 into self.b
        # How to read inputs into variables c and d of object
        self.c = int(input())   # Reads 50 into self.c
        self.d = int(input())   # Reads 60 into self.d
    def disp(self):
        # How to print variables a and b of object in same line separated by tab
        super().disp()                    # 30	40
        # How to print variables c and d of object in same line separated by tab
        print(self.c, self.d, sep='\t')   # 50	60
    def total(self):
        return self.a + self.b + self.c + self.d   # Returns 30+40+50+60 = 180
# End of child class
print('parent object')       
# How to read inputs into parent class object 'p'
p = parent()
p.get()                       # Reads 10 into p.a, 20 into p.b (consumes inputs 10, 20)
print('child object')        
# How to read inputs into child class object 'c'
c = child()
c.get()                       # Reads 30 into c.a, 40 into c.b, 50 into c.c, 60 into c.d (consumes inputs 30,40,50,60)
print('parent object : ', end='\t')   # parent object : 	  (no newline, followed by tab)
# How to print object 'p'
p.disp()                      # 10	20
print()                       # (blank line)
print('child object : ', end='\t')    # child object : 	 (no newline, followed by tab)
# How to print object 'c'
c.disp()                      # 30	40
                              # 50	60
print('Sum of the values in child object : ', c.total())   # Sum of the values in child object : 180




'''
Write a program to determine area and circumference of circle.
Also find area and volume of cylinder

1) What is the area of circle ? ---> 3.14159 * r ^ 2
    What is the circumference of circle ? --->  2 * 3.14159 * r

2) What is the area of cylinder ? --->  2 * 3.14159 * r ^ 2 + 2 * 3.14159 * r * h
     What is the volume of cylinder ? ---> 3.14159 * r ^ 2 * h

3) Reuse parent class methods in child class but do not rewrite
'''
import math
class circle:
    def get(self):
        self.r = float(input('Enter radius: '))
    def area(self):
        return math.pi * self.r ** 2
    def cir(self):
        return 2 * math.pi * self.r

class cylinder(circle):
    def get(self):
        super().get()
        self.h = float(input('Enter height: '))
    def area(self):
        return 2 * math.pi * self.r ** 2 + 2 * math.pi * self.r * self.h
    def volume(self):
        return math.pi * self.r ** 2 * self.h

def menu():
    print('1 . Circle')
    print('2 . Cylinder')
    print('3 . Exit')

while True:
    menu()
    ch = eval(input('Enter choice : '))
    match ch:
        case 1:
            c = circle()
            c.get()
            print('Area  :  ', c.area())
            print('Circumference :  ', c.cir())
        case 2:
            cy = cylinder()
            cy.get()
            print('Area : ', cy.area())
            print('Volume :  ', cy.volume())
        case 3:
            break




'''
Write a program to determine area and perimeter of rectangle and square.
Also find surface area and volume of cube

1)  What is the area of square ? --->  a ^ 2
    What is the perimeter of square ? --->  4 * a

2)  What is the area of rectangle ? --->  a * b
    What is the perimeter of rectangle ? ---> 2 * (a + b)

3)  What is the surface area of cube ? --->  6 * a ^ 2
    What is the volume of cube ? --->  a ^ 3

4)  Reuse parent class methods in child classes but do not rewrite
'''
class square:
    def get(self):
        self.a = float(input('Enter side: '))
    def area(self):
        return self.a ** 2
    def peri(self):
        return 4 * self.a
class rectangle(square):
    def get(self):
        self.a = float(input('Enter length: '))
        self.b = float(input('Enter breadth: '))
    def area(self):
        return self.a * self.b
    def peri(self):
        return 2 * (self.a + self.b)
class cube(square):
    def get(self):
        self.a = float(input('Enter side: '))
    def area(self):
        return 6 * self.a ** 2
    def volume(self):
        return self.a ** 3
def menu():
    print('1 . Square')
    print('2 . Rectangle')
    print('3 . Cube')
    print('4 . Exit')

while True:
    menu()
    ch = int(input('Enter choice : '))
    match ch:
        case 1:
            s = square()
            s.get()
            print('Area   :  ', s.area())
            print('Perimeter  :  ', s.peri())
        case 2:
            r = rectangle()
            r.get()
            print('Area  :  ', r.area())
            print('Perimeter  :  ', r.peri())
        case 3:
            c = cube()
            c.get()
            print('Area  :   ', c.area())
            print('Volume  :  ', c.volume())
        case 4:
            break




# Find outputs
class c1:
    def m1(self):
        print('m1  method  of  class  c1')
class c2:
    def m1(self):
        print('m1 method of class c2')
class c3:
    @classmethod
    def m1(cls):
        print('m1 method of  class c3')
class c4:
    @staticmethod
    def m1():
        print('m1 method of  class c4')
class c5(c1):
    def m1(self):
        print('m1 method of class c5')
    def m2(self):
        # How to call m1() method of class c3
        c3.m1()              # m1 method of class c3
        # How to call m1() method of class c4
        c4.m1()              # m1 method of class c4
        # How to call m1() method of class c2
        c2().m1()            # m1 method of class c2 (must create object as c2 is unrelated)
        # How to call m1() method of class c1
        super().m1()         # m1 method of class c1 (super() of c5 is c1)
        # How to call m1() method of class c5
        self.m1()            # m1 method of class c5 (self is a c5 object)
        # How to call m1() function
        m1()                 # m1 function (calls the global function m1)
# End of class c5
def m1():
    print('m1 function')
# End of the function
# How to call m2() method of class c5
c5().m2()   # m1 method of class c3
            # m1 method of class c4
            # m1 method of class c2
            # m1 method of class c1
            # m1 method of class c5
            # m1 function




'''
Write a program to delete a directory.
Input is either directory name (or) path of the directory
'''
import os
import shutil
path = input('Enter directory name or path: ')
try:
    shutil.rmtree(path)
    print(f'Directory "{path}" deleted successfully')
except FileNotFoundError:
    print('Error: Directory not found')
except PermissionError:
    print('Error: Permission denied')




'''
Write a program to delete a group of directories
Input is directory path
'''
import os
import shutil
path = input('Enter directory path: ')
try:
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f'Deleted directory: {item_path}')

    print('All directories deleted successfully')
except FileNotFoundError:
    print('Error: Path not found')




# Write a program to rename a file
import os
old_name = input('Enter current file name (or path): ')
new_name = input('Enter new file name (or path): ')
try:
    os.rename(old_name, new_name)
    print(f'File renamed from "{old_name}" to "{new_name}" successfully')

except FileNotFoundError:
    print('Error: File not found')
except FileExistsError:
    print('Error: A file with the new name already exists')




# Write a program to rename a directory
import os
old_name = input('Enter current directory name (or path): ')
new_name = input('Enter new directory name (or path): ')
try:
    os.rename(old_name, new_name)
    print(f'Directory renamed from "{old_name}" to "{new_name}" successfully')

except FileNotFoundError:
    print('Error: Directory not found')
except FileExistsError:
    print('Error: A directory with the new name already exists')




'''
Write a program to print all the files and sub-directories of input directory
Input : Directory (or) path
Output: Print Two lists where 1st list is all the files and 2nd list is all the directories
'''
import os
path = input('Enter directory name or path: ')
try:
    items = os.listdir(path)
    files = [item for item in items if os.path.isfile(os.path.join(path, item))]
    dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]
    print('Files:', files)
    print('Directories:', dirs)
except FileNotFoundError:
    print('Error: Directory not found')