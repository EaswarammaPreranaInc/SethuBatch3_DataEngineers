#  Write   a  program   to  perform  following  operations  on  employee  file  i.e.  binary  file

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
        self.empno=int(input('Enter employee number : '))
        self.ename=input('Enter employee name : ')
        self.sal=float(input('Enter salary : '))
    def disp(self):
        print(self.empno,'\t',self.ename,'\t',self.sal)
def create(f):
    while True:
        e=emp()
        e.get()
        pickle.dump(e,f)
        ch=input('Would you like to enter another record (y/n) ? : ')
        if ch.lower()=='n':
            break
def display(f):
    f.seek(0)
    try:
        while True:
            e=pickle.load(f)
            e.disp()
    except EOFError:
        pass
def num_records(f):
    f.seek(0)
    c=0
    try:
        while True:
            pickle.load(f)
            c+=1
    except EOFError:
        pass
    return c
def disp_ith_record(f,i):
    f.seek(0)
    c=1
    try:
        while True:
            e=pickle.load(f)
            if c==i:
                e.disp()
                return
            c+=1
    except EOFError:
        print('Invalid record number')
def append(f,e):
    f.seek(0,2)
    pickle.dump(e,f)
    print('Object is appended to the file')

fname=input('Enter file name : ')
if isfile(fname):
    f=open(fname,'rb+')
else:
    f=open(fname,'wb+')
    create(f)
    
while True:
    menu()
    ch=int(input('Enter choice: '))
    match ch:
        case 1:
            display(f)
        case 2:
            i=int(input('Enter record number : '))
            disp_ith_record(f,i)
        case 3:
            print('Number of records : ',num_records(f))
        case 4:
            e=emp()
            e.get()
            append(f,e)
        case 5:
            f.close()
            break


# Write  a  program  to  create  a  zip  file
from zipfile import ZipFile
from os.path import isfile
zfname=input('Enter zip file name : ')
zf=ZipFile(zfname,'w')
n=int(input('How many files ? : '))
for i in range(n):
    while True:
        fname=input('Enter file name : ')
        if isfile(fname):
            zf.write(fname)
            break
        else:
            print('Invalid file name and reenter : ',end='')
zf.close()
print(f'zip file is created with {n} files')

#Write  a  program  to  print  each  file  of  zipfile
from zipfile import ZipFile
import os
def disp(f):
    print('Filename :',f)
    fp=open(f,'r')
    data=fp.read()
    print(data)
    fp.close()
    if f.endswith('.py'):
        print('Execution results\n')
        os.system(f'py {f}')
def display(z):
    for f in z.namelist():
        z.extract(f)
        disp(f)
try:
    filename=input('Enter zip file name : ')
    z=ZipFile(filename,'r')
    display(z)
    z.close()
except FileNotFoundError:
    print(f'{filename} file does not exist')


# Write  a  program  to  determine  length  of  linked  list
from prog2 import linked_list
class sll(linked_list):
    def length(a):
        c=0
        p=a.first
        while p!=None:
            c+=1
            p=p.link
        return c
a=sll()
a.create()
print('Number of nodes : ',a.length())

#Write  a  progam  to  determine  data  of  ith  node
class linkedlist(sll):
    def find(a,i):
        if i<=0:
            return None
        p=a.first
        c=1
        while p!=None:
            if c==i:
                return p.data
            c+=1
            p=p.link
        return None
a=linkedlist()
a.create()

while True:
    i=int(input("Enter value of 'i': "))
    x=a.find(i)
    if x==None:
        print(f'Node {i} does not exist')
    else:
        print(f'Data of node {i} is : {x}')
    ch=input('Do you wish to continue (y / n): ')
    if ch=='N'or ch=='n':
        break
print('Good Bye')


'''Write  a  method  to  search  for  a  value  in  the  linked  list.
1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node
2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  the  node   where  'x'  is  found
3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop'''

from prog2 import linked_list
class singly_linked_list(linked_list):
    def search(a,x):
        p=a.first
        while p!=None:
            if p.data==x:
                return p
            p=p.link
        return None
a=singly_linked_list()
a.create()

while True:
    x=eval(input("Enter value to be searched : "))
    p=a.search(x)
    if p==None:
        print(f'{x} is not found')
    else:
        print(f'Found at that node whose address : {id(p)}')
    ch=input('Do you wish to continue (y / n) : ')
    if ch=='N'or ch=='n':
        break
print('Good Bye')

'''Write  a  method  to  insert  a  node  in  the  linked  list
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
															a . first  reference  remains  unchanged  when  node  is   inserted  anywhere  else'''   
from linked_list import linked_list,node
from length import sll
class linkedlist(sll):
    def insert(a,i,x):
        if i<0 or i>a.length():
            print(f'Node {i} does not exist')
        elif i==0:
            new=node(x)
            new.link=a.first
            a.first=new
        else:
            p=a.first
            c=1
            while c<i:
                p=p.link
                c+=1
            new=node(x)
            new.link=p.link
            p.link=new
a=linkedlist()
a.create()

while True:
    i=int(input("Enter value of 'i' : (0 - At the begin) "))
    x=eval(input('Enter value to be inserted : '))
    a.insert(i,x)
    a.disp()
    ch=input('Would you like to insert another node (Y or N) ? : ')
    if ch=='n'or ch=='N':
        break