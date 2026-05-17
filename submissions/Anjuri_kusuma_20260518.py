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
		self.empno = int(input('Enter employee number : '))
        self.ename = input('Enter employee name : ')
        self.sal = float(input('Enter salary : '))		
	def  disp(self):
		print(self.empno, self.ename, self.sal)
			
# End  of  the  class
def  create(f):
	 while True:
        e = emp()
        e.get()
        pickle.dump(e, f)
        ch = input('Do you wish to add another record (Y/N) ? : ')
        if ch == 'n' or ch == 'N':
            break	
def  display(f):
	f.seek(0)
    try:
        while True:
            e = pickle.load(f)
            e.disp()
    except EOFError:
        pass
def  num_records(f):
	f.seek(0)
    count = 0
    try:
        while True:
            e = pickle.load(f)
            count += 1
    except EOFError:
        return count
def  disp_ith_record(f , i):  
	f.seek(0)
    count = 0
    try:
        while True:
            e = pickle.load(f)
            count += 1
            if count == i:
                e.disp()
                return
    except EOFError:
        print('Record does not exist')
def  append(f , e):
    f.seek(0, 2)
    pickle.dump(e, f)
# End  of  the  function
filename = 'emp.dat'
if isfile(filename):
    f = open(filename, 'rb+')
else:
    f = open(filename, 'wb+')
    create(f)
while True:
	menu()
	ch = int(input('Enter choice: '))
	match  ch:
		case  1:
			display(f)
		case  2:
			i = int(input('Enter  record  number : '))
			disp_ith_record(f, i)
		case  3:
			print('Number  of  records : ' ,num_records(f) )
		case  4:
			e = emp()
            e.get()
            append(f, e)
		case  5:
			f.close()
            break
-------------------------------------------------------------------------------------------------------------
#Write  a  program  to  create  a  zip  file
from  zipfile  import  ZipFile
zipfilename = input('Enter zip file name : ')
zf = ZipFile(zipfilename, 'w')
n = int(input('How  many  files ?  : ')
for  i  in   range(n):
	fname = input('Enter file name : ')
	zf.write(fname)
zf.close()
print(F'zip  file  is  created  with  {n}  files')

-------------------------------------------------------------------------------------------------------------
Write  a  program  to  print  each  file  of  zipfile

Let  zip  file  contain  1.py , 2.txt , 3.py , 4.txt , 5.py

1) Print  each  file  name  and   file  contents

2) Also  execute  the  file  if  it  is  a  py  file

3) How  to  execute  python  file  from  python  program ?  --->  os . system('py   filename.py')
'''
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
------------------------------------------------------------------------------------------------------------------
# Write  a  program  to  determine  length  of  linked  list
class  sll(linked_list):  
	def  length(a):
			How  to  count  each  node  of  linked  list  and  return  number  of  nodes
# End  of  the  class
How  to  create  a  linked  list
print('Number  of  nodes : ' ,  ???)
-------------------------------------------------------------------------------------------------------------------
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
--------------------------------------------------------------------------------------------------------------------
'''
Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  the  node   where  'x'  is  found

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
'''
class  singly_linked_list(linked_list):  
	def  search(a , x):
		n=self.head  
		while n!=None:  
			if n.data==x:
				return n
			n=n.ref	
		return None		
# End  of  the  class
How  to  create  a  linked  list 
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	How  to  search  for  'x'  in  the  linked  list
	if  result==None:
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  that  node  whose  address  :  {result}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')
--------------------------------------------------------------------------------------------------------------------------
'''
Write  a  method  to  insert  a  node  in  the  linked  list
1) How  many  links  have  to  be  modified  for  insertion ?  --->  Two  links

2) How  to  insert  a  node  at  the  begining  of  linked list ?  --->  Modify  new  node  link  to  1st  node
and modify  reference  a . first  to  new  node

3) How  to  insert  a  node  at  the  end  of  linked list ?  --->  Modify  new  node  link  to  None and
modify  last  node  link  to  new  node

4) How  to  insert  a  node  after  ith  node ?  --->  Modify  new  node  link  to  (i + 1)th  node  and
modify  ith  node  link   to  new  node

5) In  which  order  can  links  be  modified ?  --->  Modify  new  node  link  first  and  then  existing  node  link

6) Is  logic  same  for  middle  insertion  and  insertion  at  the  end  ? --->  Yes

7) What  is  the  difference  between  insertion  at  the  begining  and  insertion  anywhere  else ?  --->															
a . first  is  modified  when  node  is   inserted  at  the  begining  and
a . first  reference  remains  unchanged  when  node  is   inserted  anywhere  else
'''
class  linkedlist(sll): 
	def  insert(a , i , x):
		if i<0:
			print(F'Node  {i}  does  not  exist')
		elif  i==0:
			new_node=Node(x)
			new_node.ref=self.head
			self.head=new_node		
		else:
        	n=self.head
        	count=1
            while n!=None and count<i:
                n=n.ref
                count=count+1
            if n==None:
                print(f'Node {i} does not exist')
            else:
                new_node=Node(x)
                new_node.ref=n.ref
                n.ref=new_node		
# End  of  the  class
How  to  create  a  linked  list 
while  True:
	i = int(input("Enter  value  of  'i' :  (0 - At  the  begin) "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	ll.insert(i,x)
	ll.display()
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break