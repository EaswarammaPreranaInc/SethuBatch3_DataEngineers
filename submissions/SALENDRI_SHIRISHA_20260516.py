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
			self.empno = int(input('Enter Employee Number : ')) 
      self.ename = input('Enter Employee Name : ')
      self.sal = int(input('Enter Employee Salary : ')) #How  to  read  empno , ename , sal  into  the  object	
	def  disp(self):
			print(F'Employee Number : {self.empno}') 
      #How  to  print  empno , ename , sal  of  the  object  in  same  line	
# End  of  the  class
def  create(f):
	How  to  read  each  object  from  keyboard  and  write  to  the  file  until  user   input  is  'N'  (or)  'n'
def  display(f):
	How  to  print  each  object  of  the  file  in  user  understandable  form
def  num_records(f):
	How  to  return  number  of   objects  in  the  file
def  disp_ith_record(f , i):  
	How  to  print  ith  object  of  the   file
def  append(f , e):
    How  to  append  a  new  object  to  the  file
# End  of  the  function
How  to  open  the  file  in  r+  mode  if  it  is  existing  and  w+  mode  if  it  is  not  existing
while True:
	menu()
	ch = int(input('Enter choice: '))
	match  ch:
		case  1:
			How  to  print  the  file
		case  2:
			i = int(input('Enter  record  number : '))
			How  to  print  ith object  of  the  file
		case  3:
			print('Number  of  records : ' ,  ???)
		case  4:
			How  to  append  an  object  to   the  file
		case  5:
			How  to  stop  execution


# Write  a  program  to  create  a  zip  file
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


# Write  a  program  to  determine  length  of  linked  list
class  sll(linked_list):  
	def  length(a):
			How  to  count  each  node  of  linked  list  and  return  number  of  nodes
# End  of  the  class
How  to  create  a  linked  list
print('Number  of  nodes : ' ,  ???)


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


'''
Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  the  node   where  'x'  is  found

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
'''
class  singly_linked_list(linked_list):  
	def  search(a , x):
			Return  that  node  where  'x'  is  found  and  None  otherwise			
# End  of  the  class
How  to  create  a  linked  list 
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	How  to  search  for  'x'  in  the  linked  list
	if  ???:
		print(F'{???}  is  not  found')
	else:
		print(F'Found  at  that  node  whose  address  :  {???)}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')


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
		if  'i'  is   an  invalid  node  number:
				print(F'Node  {i}  does  not  exist')
		elif  insertion  at  the  begining  of  linked  list:
				How  to  create  a  new  node  with  value  'x'
				How  to  insert  a  node  at  the   begining   of  linked  list				
		else:  
				How  to  create  a  new  node  with  value  'x'		
				How  to  insert  the  node  after  ith  node  of  LL		
# End  of  the  class
How  to  create  a  linked  list 
while  True:
	i = int(input("Enter  value  of  'i' :  (0 - At  the  begin) "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	How  to  insert  'x'  after  ith  node
	How  to  print  linked  list
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break


    
