1) Write   a  program   to  perform  following  operations  on  employee  file  i.e.  binary  file
from os.path import isfile
import pickle
def menu():
    print('1. Print binary file')
    print('2. Print ith record of the file')
    print('3. Number of records in the file')
    print('4. Append new record to the file')
    print('5. Exit')
class emp:
    def get(self):
        self.empno = int(input('Enter employee number : '))
        self.ename = input('Enter employee name : ')
        self.sal = float(input('Enter salary : '))
    def disp(self):
        print(self.empno, '\t', self.ename, '\t', self.sal)
# End of the class
def create(f):
    while True:
        e = emp()
        e.get()
        pickle.dump(e, f)
        ch = input('Would you like to enter another record (y/n) ?: ')
        if ch == 'n' or ch == 'N':
            break
def display(f):
    f.seek(0)
    try:
        while True:
            e = pickle.load(f)
            e.disp()
    except EOFError:
        pass
def num_records(f):
    f.seek(0)
    count = 0
    try:
        while True:
            pickle.load(f)
            count += 1
    except EOFError:
        pass
    return count
def disp_ith_record(f, i):
    f.seek(0)
    count = 1
    try:
        while True:
            e = pickle.load(f)
            if count == i:
                e.disp()
                return
            count += 1
        print('Invalid record number')
    except EOFError:
        print('Invalid record number')
def append(f, e):
    f.seek(0, 2)
    pickle.dump(e, f)
# End of the functions
fname = 'emp.dat'
if isfile(fname):
    f = open(fname, 'r+b')
else:
    f = open(fname, 'w+b')
    create(f)
while True:
    menu()
    ch = int(input('Enter choice: '))
    match ch:
        case 1:
            display(f)
        case 2:
            i = int(input('Enter record number : '))
            disp_ith_record(f, i)
        case 3:
            print('Number of records : ', num_records(f))
        case 4:
            e = emp()
            e.get()
            append(f, e)
            print('Object is appended to the file')
        case 5:
            print('Program terminated')
            break
        case _:
            print('Invalid choice')
f.close()


2) Write  a  program  to  create  a  zip  file
from zipfile import ZipFile
from os.path import isfile
zfname = input('Enter zip file name : ')
zf = ZipFile(zfname, 'w')
n = int(input('How many files ? : '))
for i in range(n):
    while True:
        fname = input('Enter file name : ')
        if isfile(fname):
           
            zf.write(fname)
            break
        else:
            print('Invalid file name and reenter : ', end='')

zf.close()
print(f'zip file is created with {n} files')



3) Write  a  program  to  print  each  file  of  zipfile

Let  zip  file  contain  1.py , 2.txt , 3.py , 4.txt , 5.py

1) Print  each  file  name  and   file  contents

2) Also  execute  the  file  if  it  is  a  py  file

3) How  to  execute  python  file  from  python  program ?  --->  os . system('py   filename.py')
'''
from zipfile import ZipFile
import os
def disp(f):
    print('File name : ', f)
    file = z.open(f)
    data = file.read().decode()
    print(data)
    file.close()
    if f.endswith('.py'):
        os.system('py ' + f)
def display(z):
    for f in z.namelist():
        disp(f)

try:
    filename = input('Enter zip file name : '
    z = ZipFile(filename, 'r')
    display(z)
    z.close()
except FileNotFoundError:
    print(f'{filename} file does not exist')


4) Write  a  program  to  determine  length  of  linked  list
class node:
    def __init__(self, data):
        self.data = data
        self.link = None
class linked_list:
    def __init__(self):
        self.first = None
    def create(self):
        n = int(input('How many nodes ? : '))
        for i in range(n):
            x = eval(input('Enter value : '))
            new = node(x)
            if self.first is None:
                self.first = new
            else:
                temp = self.first
                while temp.link is not None:
                    temp = temp.link
                temp.link = new
class sll(linked_list):
    def length(a):
        temp = a.first
        count = 0
        while temp is not None:
            count += 1
            temp = temp.link
        return count
a = sll()
a.create()
print('Number of nodes : ', a.length())


5) Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  ---> Returns  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Returns  None
class node:
    def __init__(self, data):
        self.data = data
        self.link = None
class sll:
    def __init__(self):
        self.first = None
    def create(self):
        n = int(input('How many nodes ? : '))
        for i in range(n):
            x = eval(input('Enter value : '))
            new = node(x)
            if self.first is None:
                self.first = new
            else:
                temp = self.first
                while temp.link is not None:
                    temp = temp.link
                temp.link = new
class linkedlist(sll):
    def find(a, i):
        temp = a.first
        count = 1
        while temp is not None:
            if count == i:
                return temp.data
            count += 1
            temp = temp.link
        return None
a = linkedlist()
a.create()
while True:
    i = int(input("Enter value of 'i': "))
    x = a.find(i)
    if x is None:
        print(f'Node {i} does not exist')
    else:
        print(f'Data of node {i} is : {x}')
    ch = input('Do you wish to continue (y / n) : ')
    if ch == 'N' or ch == 'n':
        break
print('Good Bye')




6) Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  the  node   where  'x'  is  found

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
class node:
    def __init__(self, data):
        self.data = data
        self.link = None
class linked_list:
    def __init__(self):
        self.first = None
    def create(self):
        n = int(input('How many nodes ? : '))
        for i in range(n):
            x = eval(input('Enter value : '))
            new = node(x)
            if self.first is None:
                self.first = new
            else:
                temp = self.first
                while temp.link is not None:
                    temp = temp.link
                temp.link = new
class singly_linked_list(linked_list):
    def search(a, x):
        temp = a.first
        while temp is not None:
            if temp.data == x:
                return temp
            temp = temp.link
        return None
a = singly_linked_list()
a.create()
while True:
    x = eval(input("Enter value to be searched : "))
    p = a.search(x)
    if p is None:
        print(f'{x} is not found')
    else:
        print(f'Found at that node whose address : {p}')
    ch = input('Do you wish to continue (y / n) : ')
    if ch == 'N' or ch == 'n':
        break
print('Good Bye')


7) Write  a  method  to  insert  a  node  in  the  linked  list
1) How  many  links  have  to  be  modified  for  insertion ?  --->  Two  links

2) How  to  insert  a  node  at  the  begining  of  linked list ?  --->  Modify  new  node  link  to  1st  node and modify  reference  a . first  to  new  node

3) How  to  insert  a  node  at  the  end  of  linked list ?  --->  Modify  new  node  link  to  None and modify  last  node  link  to  new  node

4) How  to  insert  a  node  after  ith  node ?  --->  Modify  new  node  link  to  (i + 1)th  node  and modify  ith  node  link   to  new  node

5) In  which  order  can  links  be  modified ?  --->  Modify  new  node  link  first  and  then  existing  node  link

6) Is  logic  same  for  middle  insertion  and  insertion  at  the  end  ? --->  Yes

7) What  is  the  difference  between  insertion  at  the  begining  and  insertion  anywhere  else ?  ---> a . first  is  modified  when  node  is   inserted  at  the  begining  and a . first  reference  remains  unchanged  when  node  is   inserted  anywhere  else
#class node:
    def __init__(self, data):
        self.data = data
        self.link = None
class linked_list:
    def __init__(self):
        self.first = None
    def create(self):
        n = int(input('How many nodes ? : '))
        for i in range(n):class node:
    def __init__(self, data):
        self.data = data
        self.link = None
class sll:
    def __init__(self):
        self.first = None
    def create(self):
        n = int(input('How many nodes ? : '))
        for i in range(n):
            x = eval(input('Enter value : '))
            new = node(x)
            if self.first is None:
                self.first = new
            else:
                temp = self.first
                while temp.link is not None:
                    temp = temp.link
                temp.link = new
    def display(self):
        temp = self.first
        while temp is not None:
            print(temp.data, end=' -> ')
            temp = temp.link
        print('None')
class linkedlist(sll):
    def insert(a, i, x):
        if i < 0 or i > a.length():
            print(f'Node {i} does not exist')
        elif i == 0:
            # Create new node
            new = node(x)
            # Insert at beginning
            new.link = a.first
            a.first = new
        else:
            temp = a.first
            count = 1
            while count < i:
                temp = temp.link
                count += 1
            # Create new node
            new = node(x)
            # Insert after ith node
            new.link = temp.link
            temp.link = new
    def length(a):
        temp = a.first
        count = 0
        while temp is not None:
            count += 1
            temp = temp.link
        return count
# End of the class
a = linkedlist()
a.create()
while True:
    i = int(input("Enter value of 'i' : (0 - At the begin) "))
    x = eval(input('Enter value to be inserted : '))
    a.insert(i, x)
    a.display()
    ch = input('Would you like to insert another node (Y or N) ? : ')
    if ch == 'n' or ch == 'N':
        break
            x = eval(input('Enter value : '))
            new = node(x)
            if self.first is None:
                self.first = new
            else:
                temp = self.first
                while temp.link is not None:
                    temp = temp.link
                temp.link = new
class singly_linked_list(linked_list):
    def search(a, x):
        temp = a.first
        while temp is not None:
            if temp.data == x:
                return temp
            temp = temp.link
        return None
a = singly_linked_list()
a.create()
while True:
    x = eval(input("Enter value to be searched : "))
    p = a.search(x)
    if p is None:
        print(f'{x} is not found')
    else:
        print(f'Found at that node whose address : {p}')
    ch = input('Do you wish to continue (y / n) : ')
    if ch == 'N' or ch == 'n':
        break
print('Good Bye')