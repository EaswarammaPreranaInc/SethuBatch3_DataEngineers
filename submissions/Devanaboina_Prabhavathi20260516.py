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
			self.empno=int(input("Enter empno : ")) 
			self.ename=input("Enter ename : ")
			self.sal=float(input("Enter salary : "))#How  to  read  empno , ename , sal  into  the  object	
	def  disp(self):
			print(self.empno,self.ename,self.sal)#How  to  print  empno , ename , sal  of  the  object  in  same  line	
# End  of  the  class
def  create(f):
	while True:
		e=emp()
		e.get()
		pickle.dump(e,f)
		ch=input("Would you like to continue : ")
		if ch in 'Nn':
			break#How  to  read  each  object  from  keyboard  and  write  to  the  file  until  user   input  is  'N'  (or)  'n'
def  display(f):
	f.seek(0)
	try:
		while True:
			e=pickle.load(f)
			e.disp()
	except EOFError:
		pass #How  to  print  each  object  of  the  file  in  user  understandable  form
def  num_records(f):
	c=0
	try:
		while True:
			pickle.load(f)
			c+=1
	except EOFError:
		pass
	return c #How  to  return  number  of   objects  in  the  file
def  disp_ith_record(f , i): 
	f.seek(0) 
	c=0
	try:
		while True:
			e=pickle.load(f)
			c+=1
			if c==i:
				print("Record found")
				e.disp()
				break
			print("not found")
	except EOFError:
		pass
		
				 #How  to  print  ith  object  of  the   file
def  append(f , e):
	f.seek(0,2)
	pickle.dump(e,f)#How  to  append  a  new  object  to  the  file
# End  of  the  function
filename=input("Enter file name : ")
if isfile(filename):
	f=open(filename,'r+b') #
else:
	f=open(filename,'w+b') #How  to  open  the  file  in  r+  mode  if  it  is  existing  and  w+  mode  if  it  is  not  existing
while True:
	menu()
	ch = int(input('Enter choice: '))
	match  ch:
		case  1:
			display(f) #How  to  print  the  file
		case  2:
			i = int(input('Enter  record  number : '))
			disp_ith_record(f,i) #How  to  print  ith object  of  the  file
		case  3:
			print('Number  of  records : ' ,  num_records(f))
		case  4:
			e=emp()
			e.get()
			append(e,f) #How  to  append  an  object  to   the  file
		case  5:
			exit() #How  to  stop  execution


# Write  a  program  to  create  a  zip  file
from  zipfile  import  ZipFile
filename=input("Enter file name : ")#How  to  read  zip   filename
z=ZipFile(filename,'w')
#How  to  open  zip  file
n = int(input('How  many  files ?  : '))
for  i  in   range(n):
	file=input("Enter file name : ")
	#How  to  read  each   filename
	z.write(file) #How  to  write  each  file  to  zip  file
z.close() #How  to  close  zip  file
print(F'zip  file  is  created  with  {n}  files')


from os import *
def  disp(f):	
		fp=open(f,'r')
		print(fp.read())
		fp.close()
		if f.endswith('.py'):
			system(f'python {f}') #How  to  print  content  of  the  file  and  also  execute  the  file  if  it  is  .py  file
def  display(z):
		list=z.namelist()
		for f in list:
			difp(f)
			#How  to  call  disp()  function  to  print  each  file  of  zip  file
# End  of  the  function
try:
	filename=input("Enter fiename : ") #How  to  read  filename
	z=ZipFile() #How  to  open  zip  file
	display(z) #How  to  print  display()  to  print  zip  file
	z.close() #How  to  close  the  file
except  FileNotFoundError:
	print(F'{filename}  file  does  not  exist')
	

# Write  a  program  to  determine  length  of  linked  list
from LinkedList_file import *
class  sll(linked_list):  
	def  length(a):
			c=0
			p=a.first
			while p!=None:
				p=p.link
				c+=1
			return c #How  to  count  each  node  of  linked  list  and  return  number  of  nodes
# End  of  the  class
s=sll()
s.create() #How  to  create  a  linked  list
print('Number  of  nodes : ' ,  s.length())


'''
Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  ---> Returns  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Returns  None
'''
class  linkedlist(sll): 
	def  find(a , i):
			while p!=None:
				p=p.link
				c+=1
				if i==c:
					return  p.data
			return None #data  of  ith  node  if  ith  node  exists  and  None  otherwise				
# End  of  the  class
a=linkedlist()
try:
	while True:
		d=input("Enter data values : ")
		a.append(d)
except EOFError:
	pass
c=0#How  to  create  a  linked  list  
p=a.first
while  True:
	i = int(input("Enter  value  of  'i':  "))
	#How  to  obtain  data  of  ith  node
	if  a.find(i)==None:
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {i}  is  :  {a.find(i)}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')

class  singly_linked_list(linked_list):  
	def  search(a , x):
		while p!=None:
			p=p.link
			if p.data==x:
				return p
		return None
#Return  that  node  where  'x'  is  found  and  None  otherwise			
# End  of  the  class
a=singly_linked_list() #How  to  create  a  linked  list 
try:
	while True:
		d=input("Enter data values : ")
		a.append(d)
except EOFError:
	pass
c=0#How  to  create  a  linked  list  
p=a.first
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	s=a.search(x) #How  to  search  for  'x'  in  the  linked  list
	if  s==None:
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  that  node  whose  address  :  {s}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')
