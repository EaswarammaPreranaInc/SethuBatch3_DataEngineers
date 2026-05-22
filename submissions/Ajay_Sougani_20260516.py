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
			self . empno = int(input('Enter Employee Number:'))
			self . ename = input('Enter Employee Name:')
			self . sal = float(input('Enter the Salary:'))	
	def  disp(self):
			print(self . empno , self . ename , self . sal , sep = '\t' , end = '\t')	
# End  of  the  class
def  create(f):
	while True:
		x = input('Enter another record [Y/N]:')
		if x . upper() == 'N':
			break
		else:
			a = e . get()
			pickle . dump(a , f)
	
	
    # How  to  read  each  object  from  keyboard  and  write  to  the  file  until  user   input  is  'N'  (or)  'n'
def  display(f):
	a = pickle . load(f)
	print(a)

    # How  to  print  each  object  of  the  file  in  user  understandable  form
def  num_records(f):
	ctr = 0
	while True:
		try:
			x = pickle . load(f)
			ctr += 1
		except EOFError:
			break
	return ctr
def  disp_ith_record(f , i):
	for i in range(i):
		x = pickle . load(f)  
	return x
	# How  to  print  ith  object  of  the   file
def  append(f , e):
    pickle . dump(e , f) # How  to  append  a  new  object  to  the  file
# End  of  the  function
filename = input('Enter the File name:')

if isfile(filename):
	f = open(filename , 'r+')
else:
	e = emp()
	f = open(filename , 'w+')
	
while True:
	menu()
	ch = int(input('Enter choice '))
	match  ch:
		case  1:
			display(f)
			# How  to  print  the  file
		case  2:
			i = int(input('Enter  record  number  '))
			disp_ith_record(f , i) 
			# How  to  print  ith object  of  the  file
		case  3:
			print('Number  of  records  ' ,  num_records(f))
		case  4:
			append(f , e) # How  to  append  an  object  to   the  file
		case  5:
			exit()
			# How  to  stop  execution
	


# Write  a  program  to  create  a  zip  file
from  zipfile  import  ZipFile
filename = input('Enter File Name:') # How  to  read  zip   filename
z = ZipFile(filename , 'w') # How  to  open  zip  file
n = int(input('How  many  files ? : '))
try:
    for i in range(n):
        f = input(f'Enter name of File {i+1}:') # How  to  read  each   filename
        z . write(f) # How  to  write  each  file  to  zip  file
    z . close() # How  to  close  zip  file
except:
    print('Enter valid File Names.')
print(F'zip  file  is  created  with  {n}  files')



#1
'''
Write  a  program  to  print  each  file  of  zipfile

Let  zip  file  contain  1.py , 2.txt , 3.py , 4.txt , 5.py

1) Print  each  file  name  and   file  contents

2) Also  execute  the  file  if  it  is  a  py  file

3) How  to  execute  python  file  from  python  program ?  --->  os . system('py   filename.py')
'''
import re
import os
from zipfile import ZipFile
def  disp(f):
	l = z . namelist()
	for x in l:
		f = open(x , 'r')
		c = f . read()
		print(f'File Name: {x}')
		if re . search('.py$' , x):
			print('Excecution Results:')
			os . system(f'py {x}.py')
			
		os . system('pause')
		os . system('cls')
			
		
# How  to  print  content  of  the  file  and  also  execute  the  file  if  it  is  .py  file
def  display(z):
		disp(z)
# End  of  the  function
try :
	filename = input('Enter the File Name:')
	z = ZipFile(filename , 'r') 
	display(z) # How  to  print  display()  to  print  zip  file
	z . close() # How  to  close  the  file
except  FileNotFoundError:
	print(F'{filename}  file  does  not  exist')
	


# Write  a  program  to  determine  length  of  linked  list
class  sll(linked_list):  
	def  length(a):
			ctr = 0
			p = a . first
			while p:
				ctr += 1
				p = p . link
			return ctr
			# How  to  count  each  node  of  linked  list  and  return  number  of  nodes
# End  of  the  class
l = sll()
l . create()  # How  to  create  a  linked  list
print('Number  of  nodes : ' , length(l))
	  


#2
'''
Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  ---> Returns  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Returns  None
'''
class  linkedlist(sll): 
	def  find(a , i):
			if i > length(a):
				return None
			else:
				p = a . first
				for i in range(i):
					p = p . link
				return p				
# End  of  the  class
l = linkedlist()
l . create() # How  to  create  a  linked  list  
while  True:
	i = int(input("Enter  value  of  'i':  "))
	d = l . find(i) # How  to  obtain  data  of  ith  node
	if d == None:
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {i}  is  :  {d}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')



#3
'''
Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  the  node   where  'x'  is  found

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
'''
class  singly_linked_list(linked_list):  
	def  search(a , x):
			p = a . first
			while True:
				if p . data == x:
					return p
				else:
					p = p . link
			else:
				return None			
# End  of  the  class
l = singly_linked_list()
l . create() # How  to  create  a  linked  list 
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	s = l . search(x) # How  to  search  for  'x'  in  the  linked  list
	if x == None:
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  that  node  whose  address  :  {s}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')



#4
'''
Write  a  method  to  insert  a  node  in  the  linked  list
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
class  linkedlist(sll): 
	def  insert(a , i , x):
		if i > length(a):
				print(F'Node  {i}  does  not  exist')
		elif i == 0:
				new = node(x) # How  to  create  a  new  node  with  value  'x'
				new . link = a . first
				a . first = new # How  to  insert  a  node  at  the   begining   of  linked  list				
		else:  
				new = node (x) # How  to  create  a  new  node  with  value  'x'		
				p = a . first
				for x in range(i):
					p = p . link
				new . link = p . link
				p . link = new # How  to  insert  the  node  after  ith  node  of  LL		
# End  of  the  class
l = linkedlist() 
l . create() # How  to  create  a  linked  list 
while  True:
	i = int(input("Enter  value  of  'i' :  (0 - At  the  begin) "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	l . insert(l , x , i) # How  to  insert  'x'  after  ith  node
	l . disp() # How  to  print  linked  list
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break
