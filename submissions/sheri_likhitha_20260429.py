import mysql.connector

# connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cur = conn.cursor()

# execute query
cur.execute("SELECT * FROM emp")

# input number of rows
n = int(input("Enter number of rows: "))

# fetch first n rows (list)
rows = cur.fetchmany(n)

# convert list to tuple (optional)
tpl = tuple(rows)

# display rows
for row in tpl:
    print(row)

# close connection
cur.close()
conn.close()




import mysql.connector

# connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cur = conn.cursor()

while True:
    try:
        # read inputs (pre-requisite)
        empno = int(input("Enter empno: "))
        ename = input("Enter ename: ")
        sal = float(input("Enter salary: "))

        # execute insert query
        cur.execute(
            "INSERT INTO emp (empno, ename, sal) VALUES (%s, %s, %s)",
            (empno, ename, sal)   # tuple is passed here
        )

        # commit changes
        conn.commit()

        print("Row inserted successfully")
        print("Rows affected:", cur.rowcount)

    except mysql.connector.IntegrityError as e:
        print("Error:", e)

    ch = input("Do you want to insert another row? (y/n): ")
    if ch.lower() != 'y':
        break

# close connection
cur.close()
conn.close()




import mysql.connector

# connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cur = conn.cursor()

try:
    # read condition input (example: empno)
    empno = int(input("Enter empno to delete: "))

    # execute delete query safely
    cur.execute("DELETE FROM emp WHERE empno = %s", (empno,))

    # commit changes
    conn.commit()

    print("Rows deleted:", cur.rowcount)

except Exception as e:
    print("Error:", e)

# close connection
cur.close()
conn.close()




import mysql.connector

# connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cur = conn.cursor()

try:
    # read inputs (pre-requisite)
    empno = int(input("Enter empno to update: "))
    new_sal = float(input("Enter new salary: "))

    # execute update query safely
    cur.execute(
        "UPDATE emp SET sal = %s WHERE empno = %s",
        (new_sal, empno)
    )

    # commit changes
    conn.commit()

    print("Rows updated:", cur.rowcount)

except Exception as e:
    print("Error:", e)

# close connection
cur.close()
conn.close()



import mysql.connector

# connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cur = conn.cursor()

# read table name (pre-requisite)
tablename = input("Enter table name: ")

try:
    # create table safely
    query = f"""
    CREATE TABLE IF NOT EXISTS {tablename} (
        rollno INT PRIMARY KEY,
        sname VARCHAR(20),
        marks FLOAT
    )
    """
    
    cur.execute(query)
    print("Table created successfully (or already exists).")

except Exception as e:
    print("Error:", e)

# close connection
cur.close()
conn.close()




class parent:
    @classmethod
    def m1(cls):
        print("parent method")

class child(parent):
    @classmethod
    def m2(cls):
        # 1) using class name
        parent.m1()

        # 2) using cls (recommended inside classmethod)
        cls.m1()

        # 3) using super()
        super().m1()

        # 4) another indirect way (via child class itself)
        child.m1()

        print("child method")




class parent:
    @classmethod
    def m1(cls):
        print("parent method")

class child(parent):
    @classmethod
    def m1(cls):
        # 1) Call parent class method (without object)
        parent.m1()

        # 2) Another way using super()
        super().m1()

        print("child method")



class parent:
    @staticmethod
    def m1():
        print("parent method")

class child(parent):
    @staticmethod
    def m2():
        # 1) correct way
        parent.m1()

        # 2) another correct way
        child.m1()

        print("child method")




class parent:
    @staticmethod
    def m1():
        print("parent method")

class child(parent):
    @staticmethod
    def m1():
        # 1) call parent class method (direct way)
        parent.m1()

        # 2) another valid way
        child.m1.__func__(child)  # rarely used, not recommended

        print("child method")





class parent:
    x = 10

    def m1(self):
        # 1) correct way (inside method)
        print(self.x)

        # 2) another way
        print(parent.x)

class child(parent):
    y = 20

    def m2(self):
        # -------- accessing parent variable x --------

        # 1) using self (inheritance)
        print(self.x)

        # 2) using parent class name
        print(parent.x)

        # 3) using class name of child (inherits x)
        print(child.x)

        # 4) using super()
        print(super().x)

        # -------- accessing child variable y --------

        # correct way
        print(self.y)

        # another way
        print(child.y)




class parent:
    def get(self):
        self.a = int(input())
        self.b = int(input())

    def disp(self):
        print(self.a, self.b, sep="\t")


class child(parent):
    def get(self):
        self.a = int(input())
        self.b = int(input())
        self.c = int(input())
        self.d = int(input())

    def disp(self):
        print(self.a, self.b, sep="\t")
        print(self.c, self.d, sep="\t")

    def total(self):
        return self.a + self.b + self.c + self.d


# ---------------- Execution ----------------

print("parent object")
p = parent()
p.get()

print("child object")
c = child()
c.get()

print("parent object : ", end="\t")
p.disp()
print()

print("child object : ", end="\t")
c.disp()

print("Sum of the values in child object : ", c.total())





import math

class circle:
    def get(self):
        self.r = float(input("Enter radius: "))

    def area(self):
        return math.pi * self.r * self.r

    def cir(self):
        return 2 * math.pi * self.r


class cylinder(circle):
    def get(self):
        self.r = float(input("Enter radius: "))
        self.h = float(input("Enter height: "))

    def area(self):
        # reuse circle area logic + extra formula
        return 2 * super().area() + 2 * math.pi * self.r * self.h

    def volume(self):
        return math.pi * self.r * self.r * self.h


def menu():
    print("1. Circle")
    print("2. Cylinder")
    print("3. Exit")


# objects
c = circle()
cy = cylinder()

while True:
    menu()
    ch = int(input("Enter choice: "))

    match ch:

        case 1:
            c.get()
            print("Area :", c.area())
            print("Circumference :", c.cir())

        case 2:
            cy.get()
            print("Area :", cy.area())
            print("Volume :", cy.volume())

        case 3:
            print("Exiting program...")
            break





class square:
    def get(self):
        self.a = float(input("Enter side of square: "))

    def area(self):
        return self.a * self.a

    def peri(self):
        return 4 * self.a


class rectangle(square):
    def get(self):
        self.a = float(input("Enter length: "))
        self.b = float(input("Enter breadth: "))

    def area(self):
        return self.a * self.b

    def peri(self):
        return 2 * (self.a + self.b)


class cube(square):
    def get(self):
        self.a = float(input("Enter side of cube: "))

    def area(self):
        return 6 * self.a * self.a

    def volume(self):
        return self.a * self.a * self.a


def menu():
    print("1. Square")
    print("2. Rectangle")
    print("3. Cube")
    print("4. Exit")


# objects
s = square()
r = rectangle()
c = cube()

while True:
    menu()
    ch = int(input("Enter choice: "))

    match ch:

        case 1:
            s.get()
            print("Area :", s.area())
            print("Perimeter :", s.peri())

        case 2:
            r.get()
            print("Area :", r.area())
            print("Perimeter :", r.peri())

        case 3:
            c.get()
            print("Area :", c.area())
            print("Volume :", c.volume())

        case 4:
            print("Exiting program...")
            break





class c1:
    def m1(self):
        print("m1 method of class c1")


class c2:
    def m1(self):
        print("m1 method of class c2")


class c3:
    @classmethod
    def m1(cls):
        print("m1 method of class c3")


class c4:
    @staticmethod
    def m1():
        print("m1 method of class c4")


class c5(c1):
    def m1(self):
        print("m1 method of class c5")

    def m2(self):
        # class c3 (classmethod)
        c3.m1()

        # class c4 (staticmethod)
        c4.m1()

        # class c2 (instance method → need object)
        obj2 = c2()
        obj2.m1()

        # class c1 (parent class)
        super().m1()

        # class c5 (current class)
        self.m1()

        # global function
        m1()


def m1():
    print("m1 function")


# calling m2
obj5 = c5()
obj5.m2()
#outputs:
m1 method of class c3
m1 method of class c4
m1 method of class c2
m1 method of class c1
m1 method of class c5
m1 function




import os
import shutil

# take input (directory name or full path)
path = input("Enter directory name or path: ")

try:
    # check if directory exists
    if os.path.isdir(path):

        # delete directory (even if it contains files)
        shutil.rmtree(path)

        print("Directory deleted successfully")

    else:
        print("Directory does not exist")

except Exception as e:
    print("Error:", e)




import os

# input directory path
path = input("Enter directory path: ")

try:
    # get list of items in directory
    items = os.listdir(path)

    for item in items:
        item_path = path + "\\" + item   # simple path join (basic method)

        # check if it is a directory
        if os.path.isdir(item_path):
            os.rmdir(item_path)  # works only if directory is empty

    print("Directories deleted successfully")

except Exception as e:
    print("Error:", e)





import os

# take old file name and new file name
old_name = input("Enter old file name: ")
new_name = input("Enter new file name: ")

try:
    # rename file
    os.rename(old_name, new_name)
    print("File renamed successfully")

except Exception as e:
    print("Error:", e)





import os

# take old and new directory names
old_name = input("Enter old directory name/path: ")
new_name = input("Enter new directory name/path: ")

try:
    # rename directory
    os.rename(old_name, new_name)
    print("Directory renamed successfully")

except Exception as e:
    print("Error:", e)





import os

# input directory path
path = input("Enter directory path: ")

files = []
dirs = []

try:
    # get all items in directory
    items = os.listdir(path)

    for item in items:
        item_path = path + "\\" + item   # basic path joining

        # check if directory or file
        if os.path.isdir(item_path):
            dirs.append(item)
        else:
            files.append(item)

    # output
    print("Files List:", files)
    print("Directories List:", dirs)

except Exception as e:
    print("Error:", e)




import os

# get current working directory
cwd = os.getcwd()

# target directory path
path = cwd + "\\sairam"

try:
    print("Contents of sairam directory:")

    # iterate through directory
    for item in os.listdir(path):
        print(item)

except Exception as e:
    print("Error:", e)




