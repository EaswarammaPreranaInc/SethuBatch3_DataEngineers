# 1)Write a program to perform operations on employee binary file

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
def create(f):
    while True:
        e = emp()
        e.get()
        pickle.dump(e, f)
        option = input('Would you like to enter another record (y/n) ? : ')
        if option == 'n' or option == 'N':
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
    except EOFError:
        print('Invalid record number')
def append(f, e):
    f.seek(0, 2)
    pickle.dump(e, f)
    print('Object is appended to the file')
if isfile('emp.dat'):
    f = open('emp.dat', 'rb+')
else:
    f = open('emp.dat', 'wb+')
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
            print('Number of records :', num_records(f))
        case 4:
            e = emp()
            e.get()
            append(f, e)
        case 5:
            break
f.close()

'''
2) Write  a  program  to  create  a  zip  file
from  zipfile  import  ZipFile
How  to  read  zip   filename
How  to  open  zip  file
n = int(input('How  many  files ?  : ')
for  i  in   range(n):
	How  to  read  each   filename
	How  to  write  each  file  to  zip  file
How  to  close  zip  file
print(F'zip  file  is  created  with  {n}  files')
'''
from zipfile import ZipFile
from os.path import isfile
zipname = input('Enter zip file name : ')
zf = ZipFile(zipname, 'w')
n = int(input('How many files ? : '))
for i in range(n):
    while True:
        fname = input('Enter file name : ')
        if isfile(fname):
            zf.write(fname)
            break
        else:
            print('Invalid file name and reenter :', end=' ')
zf.close()
print(f'zip file is created with {n} files')

'''
3) Write  a  program  to  print  each  file  of  zipfile

Let  zip  file  contain  1.py , 2.txt , 3.py , 4.txt , 5.py

1) Print  each  file  name  and   file  contents

2) Also  execute  the  file  if  it  is  a  py  file

3) How  to  execute  python  file  from  python  program ?  --->  os . system('py   filename.py')
def  disp(f):	
		How  to  print  content  of  the  file  and  also  execute  the  file  if  it  is  .py  file
def  display(z):
		How  to  call  disp()  function  to  print  each  file  of  zip  file
# End  of  the  function
try :
	How  to  read  filename
	How  to  open  zip  file
	How  to  print  display()  to  print  zip  file
	How  to  close  the  file
except  FileNotFoundError:
	print(F'{filename}  file  does  not  exist')
'''

from zipfile import ZipFile
import os
def disp(f):
    print('Filename :', f.filename)
    data = f.read().decode()
    print(data)
    if f.filename.endswith('.py'):
        temp = open(f.filename, 'w')
        temp.write(data)
        temp.close()
        print('Execution results')
        os.system(f'py {f.filename}')
def display(z):
    for f in z.infolist():
        disp(f)
try:
    filename = input('Enter zip file name : ')
    z = ZipFile(filename, 'r')
    display(z)
    z.close()
except FileNotFoundError:
    print(f'{filename} file does not exist')

'''
4) # Write  a  program  to  determine  length  of  linked  list
class  sll(linked_list):  
	def  length(a):
			How  to  count  each  node  of  linked  list  and  return  number  of  nodes
# End  of  the  class
How  to  create  a  linked  list
print('Number  of  nodes : ' ,  ???)
'''

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    def append(self, data):
        n = node(data)
        if self.head == None:
            self.head = n
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = n
class sll(linked_list):
    def length(a):
        count = 0
        temp = a.head
        while temp != None:
            count += 1
            temp = temp.next
        return count
l = sll()
print('Enter values terminated by ctrl+z')
try:
    while True:
        x = input()
        l.append(eval(x))
except EOFError:
    pass
print('Number of nodes :', l.length())

'''
5) Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  ---> Returns  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Returns  None
class  linkedlist(sll): 
	def  find(a , i):
			return  data  of  ith  node  if  ith  node  exists  and  None  otherwise				
# End  of  the  class
'''
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class sll:
    def __init__(self):
        self.head = None
    def append(self, data):
        n = node(data)
        if self.head == None:
            self.head = n
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = n
class linkedlist(sll):
    def find(a, i):
        temp = a.head
        count = 1
        while temp != None:
            if count == i:
                return temp.data
            temp = temp.next
            count += 1
        return None
l = linkedlist()
print('Enter values terminated by ctrl+z')
try:
    while True:
        x = input()
        l.append(eval(x))
except EOFError:
    pass
while True:
    i = int(input("Enter value of 'i': "))
    data = l.find(i)
    if data == None:
        print(f'Node {i} does not exist')
    else:
        print(f'Data of node {i} is : {data}')
    ch = input('Do you wish to continue (y / n) : ')
    if ch == 'N' or ch == 'n':
        break
print('Good Bye')

'''
6) Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  the  node   where  'x'  is  found

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
'''
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        n = node(data)
        if self.head == None:
            self.head = n
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = n
class singly_linked_list(linked_list):
    def search(a, x):
        temp = a.head
        while temp != None:
            if temp.data == x:
                return temp
            temp = temp.next
        return None
l = singly_linked_list()
print('Enter values terminated by ctrl+z')
try:
    while True:
        x = input()
        l.append(eval(x))
except EOFError:
    pass
while True:
    x = eval(input('Enter value to be searched : '))
    p = l.search(x)
    if p == None:
        print(f'{x} is not found')
    else:
        print(f'Found at that node whose address : {id(p)}')
    ch = input('Do you wish to continue (y / n) : ')
    if ch == 'N' or ch == 'n':
        break
print('Good Bye')

'''
7) Write  a  method  to  insert  a  node  in  the  linked  list
1) How  many  links  have  to  be  modified  for  insertion ?  --->  Two  links

2) How  to  insert  a  node  at  the  begining  of  linked list ?  --->  Modify  new  node  link  to  1st  node
																														and
																									   modify  reference  a . first  to  new  node

3) How  to  insert  a  node  at  the  end  of  linked list ?  --->  Modify  new  node  link  to  None
																												and
																								modify  last  node  link  to  new  node

4) How  to  insert  a  node  after  ith  node ?  --->  Modify  new  node  link  to  (i + 1)th  node  and
																		       modify  ith  node  link   to  new  node

5) In  which  order  can  links  be  modified ?  --->  Modify  new  node  link  first  and  then  existing  node  link

6) Is  logic  same  for  middle  insertion  and  insertion  at  the  end  ? --->  Yes

7) What  is  the  difference  between  insertion  at  the  begining  and  insertion  anywhere  else ?  --->															
															a . first  is  modified  when  node  is   inserted  at  the  begining  and
															a . first  reference  remains  unchanged  when  node  is   inserted  anywhere  else
'''
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class sll:
    def __init__(self):
        self.head = None
    def append(self, data):
        n = node(data)
        if self.head == None:
            self.head = n
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = n
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data, end='    ')
            temp = temp.next
        print()
    def length(self):
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next
        return count
class linkedlist(sll):
    def insert(a, i, x):
        if i < 0 or i > a.length():
            print(f'Node {i} does not exist')
        elif i == 0:
            n = node(x)
            n.next = a.head
            a.head = n
        else:
            temp = a.head
            count = 1
            while count < i:
                temp = temp.next
                count += 1
            n = node(x)
            n.next = temp.next
            temp.next = n
l = linkedlist()
print('Enter values terminated by ctrl+z')
try:
    while True:
        x = input()
        l.append(eval(x))
except EOFError:
    pass
while True:
    i = int(input("Enter value of 'i' : (0 - At the begin) "))
    x = eval(input('Enter value to be inserted : '))
    l.insert(i, x)
    l.display()
    ch = input('Would you like to insert another node (Y or N) ? : ')
    if ch == 'n' or ch == 'N':
        break