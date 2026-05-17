#  Write   a  program   to  perform  following  operations  on  employee  file  i.e.  binary  file
from  os . path  import  isfile
import  pickle
def menu():
    print('1. Print  binary  file')
    print('2. Print  ith  record  of  the  file')
    print('3. Number  of  records  in  the  file')
    print('4. Append  new  record  to  the  file')
    print('5. Exit')
class  emp:
	def  get(self):
        #How  to  print  empno , ename , sal  of  the  object  in  same  line	
        self.empno = int(input("Enter employee number: "))
        self.ename = input("Enter employee name: ")
        self.sal = float(input("Enter salary: "))	def  disp(self):
# End  of  the  class
def  create(f):
	#How  to  read  each  object  from  keyboard  and  write  to  the  file  until  user   input  is  'N'  (or)  'n'
    while True:
        e = Emp()
        e.get()
        pickle.dump(e, f)
        ch = input("Do you want to add another record(y/n): ")
        if ch.lower() == 'n':
            break
def  display(f):
	#How  to  print  each  object  of  the  file  in  user  understandable  form
    f.seek(0)
    try:
        while True:
            e = pickle.load(f)
            e.disp()
    except EOFError:
        pass

def  num_records(f):
	#How  to  return  number  of   objects  in  the  file
    f.seek(0)
    count = 0
    try:
        while True:
            pickle.load(f)
            count += 1
    except EOFError:
        return count

def  disp_ith_record(f , i):  
	#How  to  print  ith  object  of  the   file
    f.seek(0)
    count = 1
    try:
        while True:
           e = pickle.load(f)
            if count == i:
                e.disp()
                return
            count += 1
        print("Record not found")
    except EOFError:
        print("Record not found")


def  append(f , e):
    #How  to  append  a  new  object  to  the  file
    f.seek(0, 2)
    pickle.dump(e, f)

# End  of  the  function
#How  to  open  the  file  in  r+  mode  if  it  is  existing  and  w+  mode  if  it  is  not  existing
fname = "emp.dat"
if isfile(fname):
    f = open(fname, "rb+")
else:
    f = open(fname, "wb+")
    create(f)
while True:
    menu()
    ch = int(input("Enter choice: "))
    match ch:
        case 1:
            display(f)
        case 2:
            i = int(input("Enter record number: "))
            disp_ith_record(f, i)
        case 3:
            print("Number of records:", num_records(f))
        case 4:
            e = Emp()
            e.get()
            append(f, e)
        case 5:
            print("Program terminated")
            break
        case _:
            print("Invalid choice")

f.close()





# Write  a  program  to  create  a  zip  file
from  zipfile  import  ZipFile
zipname = input("Enter zip file name: ")
zf = ZipFile(zipname, "w")
n = int(input('How  many  files ?  : ')
for  i  in   range(n):
    fname = input("Enter file name: ")
    zf.write(fname)
zf.close()
print(F'zip  file  is  created  with  {n}  files')




'''
Write  a  program  to  print  each  file  of  zipfile

Let  zip  file  contain  1.py , 2.txt , 3.py , 4.txt , 5.py

1) Print  each  file  name  and   file  contents

2) Also  execute  the  file  if  it  is  a  py  file

3) How  to  execute  python  file  from  python  program ?  --->  os . system('py   filename.py')
'''
from zipfile import ZipFile
import os
def disp(f):
    print("File Name:", f.filename)
    data = f.read().decode()
    print("File Contents:")
    print(data)
    if f.filename.endswith(".py"):
        print("Executing python file...\n")
        temp = open(f.filename, "w")
        temp.write(data)
        temp.close()
        os.system(f'py {f.filename}')
def display(z):
    for name in z.namelist():
        f = z.open(name)
        disp(f)
        f.close()
try:
    filename = input("Enter zip file name: ")
    z = ZipFile(filename, "r")
    display(z)
    z.close()
except FileNotFoundError:
    print(f"{filename} file does not exist")
    
    
    
    
# Write  a  program  to  determine  length  of  linked  list

from prg7b import creation, linked_list
class sll(linked_list):
    def length(a):
        count = 0
        temp = a.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count
l1 = creation()
l = sll()
l.head = l1.head
print("Number of nodes:", l.length())




'''
Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  ---> Returns  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Returns  None
'''
class  linkedlist(sll): 
	def  find(a , i):
			return  data  of  ith  node  if  ith  node  exists  and  None  otherwise				
# End  of  the  class
How  to  create  a  linked  list  
while  True:
	i = int(input("Enter  value  of  'i':  "))
	How  to  obtain  data  of  ith  node
	if  ???:
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {???}  is  :  {???}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')