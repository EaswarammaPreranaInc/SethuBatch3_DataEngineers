# #  Write   a  program   to  perform  following  operations  on  employee  file  i.e.  binary  file
# # Write a program to perform operations on employee binary file

# from os.path import isfile
# import pickle
# def menu():
#     print("1. Print binary file")
#     print("2. Print ith record of the file")
#     print("3. Number of records in the file")
#     print("4. Append new record to the file")
#     print("5. Exit")
# class emp:
#     def get(self):
#         self.empno = int(input("Enter Employee Number : "))
#         self.ename = input("Enter Employee Name : ")
#         self.sal = float(input("Enter Salary : "))
#     def disp(self):
#         print(self.empno, self.ename, self.sal)
# # End of class
# def create(f):
#     while True:
#         e = emp()
#         e.get()

#         pickle.dump(e, f)

#         ch = input("Do you want to add another record (Y/N) : ")

#         if ch == 'N' or ch == 'n':
#             break
# def display(f):
#     f.seek(0)
#     try:
#         while True:
#             e = pickle.load(f)
#             e.disp()
#     except EOFError:
#         pass
# def num_records(f):
#     f.seek(0)
#     count = 0
#     try:
#         while True:
#             pickle.load(f)
#             count += 1
#     except EOFError:
#         pass
#     return count
# def disp_ith_record(f, i):
#     f.seek(0)
#     count = 1
#     try:
#         while True:
#             e = pickle.load(f)
#             if count == i:
#                 print("Record Found:")
#                 e.disp()
#                 return
#             count += 1
#     except EOFError:
#         print("Record does not exist")
# def append(f, e):
#     f.seek(0, 2)
#     pickle.dump(e, f)
# fname = "emp.dat"
# if isfile(fname):
#     f = open(fname, "r+b")
# else:
#     f = open(fname, "w+b")
#     create(f)
# while True:
#     menu()
#     ch = int(input("Enter choice : "))
#     match ch:
#         case 1:
#             print("\nEmployee Records")
#             display(f)
#         case 2:
#             i = int(input("Enter record number : "))
#             disp_ith_record(f, i)
#         case 3:
#             print("Number of records :", num_records(f))
#         case 4:
#             e = emp()
#             e.get()
#             append(f, e)
#         case 5:
#             print("Program terminated")
#             break
#         case _:
#             print("Invalid Choice")
# f.close()

''' Write  a  program  to  create  a  zip  file'''
# from  zipfile  import  ZipFile
# zipname = input("Enter zip filename : ")
# zf = ZipFile(zipname, 'w')
# n = int(input('How  many  files ?  : '))
# for  i  in   range(n):
# 	fname = input("Enter filename : ")
# 	zf.write(fname)
# zf.close()
# print(F'zip  file  is  created  with  {n}  files')

'''
Write  a  program  to  print  each  file  of  zipfile
Let  zip  file  contain  1.py , 2.txt , 3.py , 4.txt , 5.py
1) Print  each  file  name  and   file  contents
2) Also  execute  the  file  if  it  is  a  py  file
3) How  to  execute  python  file  from  python  program ?  --->  os . system('py   filename.py')
'''
'''
Write a program to print each file of zipfile

1) Print each file name and file contents

2) Also execute the file if it is a .py file

3) Execute python file using:
   os.system('py filename.py')
'''

# from zipfile import ZipFile
# import os
# def disp(f):
#     print("\nFile Name :", f.filename)
#     print("File Contents :")
#     data = f.read().decode()
#     print(data)
#     if f.filename.endswith('.py'):
#         temp = open(f.filename, 'w')
#         temp.write(data)
#         temp.close()
#         print("Executing Python File...\n")
#         os.system(f'py {f.filename}')
# def display(z):
#     for fname in z.namelist():
#         f = z.open(fname)
#         disp(f)
#         f.close()
# try:
#     filename = input("Enter zip filename : ")
#     z = ZipFile(filename, 'r')
#     display(z)
#     z.close()
# except FileNotFoundError:
#     print(f'{filename} file does not exist')

''' Write  a  program  to  determine  length  of  linked  list'''

class  sll(linked_list):  
	def  length(a):
			ctr = 0
			p = a . first
			while p:
				ctr += 1
				p = p . link
			return ctr
# End  of  the  class
l = sll()
l . create()  
print('Number  of  nodes : ' , length(l))

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
				new = node(x) 
				new . link = a . first
				a . first = new 			
		else:  
				new = node (x) # H	
				p = a . first
				for x in range(i):
					p = p . link
				new . link = p . link
				p . link = new 
# End  of  the  class
l = linkedlist() 
l . create() 
while  True:
	i = int(input("Enter  value  of  'i' :  (0 - At  the  begin) "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	l . insert(l , x , i) 
	l . disp() 
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break
		


