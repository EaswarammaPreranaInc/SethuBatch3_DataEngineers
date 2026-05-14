#  Modify  following  program  with  'with'  statement
def   create(f):
	try:
		print('Type  text  terminated  by  ctrl+z')
		while  line :=  input():
				f . write(line + '\n')
	except  EOFError:
		print(F'File  {f . name}  is  created')
#  End  of  the  function
fname = input('Enter  filename :  ')
with open(fname , 'w') as f:
    create(f)



#1
'''
Repeat  prog5c(File-Create)  with  writelines()  method

Inputs
--------
Rama  Rao
9247
+-$
Hyd is green city
ctrl+z

List  --->  ['Rama  Rao\n' , '9247\n' , '+-$\n' , 'Hyd is green city\n']

File
-----
Rama  Rao
9247
+-$
Hyd is  green city
	
	
'''
def  create(f):
		print('Enter  text  terminated  by  ctrl + z')
		lst = [ ]
		try:
				while  True:
						line = input()
						lst . append(line + '\n')
		except  EOFError:
				f . writelines(lst)
				print('List  --->  ' , lst)
				print(F'File  {f.name}  is  created')
#  End  of  the  function

fname = input('Enter  filename :  ')

with  open(fname , 'w')  as  f:
		create(f)



#2
'''
(Home  work)
Write  a  program  to  print  data  of  the  file

File
-----
Rama  Rao
9247
+-$
Hyd is green city

1) Which  method  is  used  to  read  data  of  the  file  ?  ---> read()

2) Which  function  is  used  to  print  whole  data  of  the  file ?  --->  print()

3) In  which  mode  is  file  opened ?  --->  read  mode
'''
def  disp(f):
		data = f . read()
		print(F'Data  of  the  file  {f . name}')
		print(data)
# End  of  the  function

fname = input('Enter  filename :  ')

with  open(fname , 'r')  as  f:
		disp(f)



#3
'''
(Home  work)
Write  a  program  to  print  file  pagewise  and  page  length = 20   lines

File
-----
Rama  Rao
9247
+-$
Hyd is green city


1) Which  method  is  used  to  read  each  line  of  the  file  ?  --->  readline()

2) Which  function  is  used  to  print  each  line ?  ---> print()

3) How  long  is  the  procedure  repeated ?  --->  Until  end  of  the  file  is  reached

4) In  which  mode  is  file  opened ?  --->  read  mode

5) How  to  pause  execution  for  every  20  lines ?  --->  os . system('pause')  where  pause  is  a  dos  command

6) How  to  clear  the  20  lines   before  printing   next  20  lines ?  ---> os . system('cls')  where  cls  is  a  dos  command
'''
import  os

def  disp(f):
		count = 0

		while  True:
				line = f . readline()

				if  line == '':
						break

				print(line , end = '')

				count += 1

				if  count % 20 == 0:
						os . system('pause')
						os . system('cls')
#  End  of  the  function

fname = input('Enter  filename :  ')

with  open(fname , 'r')  as  f:
		disp(f)



#4
'''
Repeat  prog9b(File-pagewise)  with  for  loop
i.e.  Print  file  pagewise  and  pause  execution  for  every  20  lines

File
-----
Rama  Rao
9247
+-$
Hyd is green city

1) How  to  iterate  thru  the  file ?  --->  With  for  loop

2) Which  function  is  used  to  print  each  line ?  ---> print()

3) How  long  is  the  procedure  repeated ?  ---> Until  end  of  the  file  is  reached

4) In  which  mode  is  file  opened ?  ---> read  mode
'''
import  os

def  disp(f):
		count = 0

		for  line  in  f:
				print(line , end = '')

				count += 1

				if  count % 20 == 0:
						os . system('pause')
						os . system('cls')
# End  of  the  function

fname = input('Enter  filename :  ')

with  open(fname , 'r')  as  f:
		disp(f)



#5
'''
Repeat  prog9b(File-pagewise)  with  readlines()  method
i.e.  Print  file  pagewise  and  pause  execution  for  every  20  lines

File
-----
Rama  Rao
9247
+-$
Hyd is green city

List  --->  ['Rama Rao\n' , '9247\n' , '+-$\n' , 'Hyd is green city']


1) Which  method  is  used  to  read  the  whole  file  ?  ---> readlines()

2) Where  are  all  the  lines  stored ?  ---> List

3) How  to  print  each  line  of  the  list ?  --->  Iterate  thru  the  list  and  print  each  line

4) How  long  is  the  procedure  repeated ?  ---> Until  list  is  fully  iterated

5) In  which  mode  is  file  opened ?  --->  read  mode
'''
import  os

def  disp(f):
		lines = f . readlines()

		count = 0

		for  line  in  lines:
				print(line , end = '')

				count += 1

				if  count % 20 == 0:
						os . system('pause')
						os . system('cls')
# End  of  the  function

fname = input('Enter  filename :  ')

with  open(fname , 'r')  as  f:
		disp(f)



#6
'''
Write  a  program  to  copy  contents  of  a  file  to  a  different  file

1st  File
---------
Rama  Rao
9247
+-$
Hyd  is  green  city
Eof 

2nd  file
----------
Rama  Rao
9247
+-$
Hyd  is  green  city



1) In  which  mode  is  1st  file  opened ?  ---> 'r'  mode
    In  which  mode  is  2nd  file  opened ?  ---> 'w'   mode

2) What  action  to  be  made  when  1st  file  does  not  exist ?  --->  Print  a  message

3) What  action  to  be  made  when  2nd  file  does  not  exist ?  --->  Copy  1st  file  to  2nd  file

4) What  action  to  be  made  when  both  the  files  are  existing ? --->																
																	Copy  file  when  user  input  is  yes  and  print  a  message  when  user  input  is  no
'''
import  os

src = input('Enter  source  filename :  ')

dest = input('Enter  destination  filename :  ')

if  not  os . path . exists(src):
		print('Source  file  does  not  exist')

else:
		if  os . path . exists(dest):
				ch = input('Destination  file  already  exists .  Overwrite(yes/no) ?  ')

				if  ch . lower() != 'yes':
						print('Copy  cancelled')
						exit()

		with  open(src , 'r')  as  f1 , open(dest , 'w')  as  f2:
				data = f1 . read()
				f2 . write(data)

		print(F'File  copied  from  {src}  to  {dest}')



#7
'''
Write  a  program  to  append  data  of  a  file  to  another  file
i.e.  Copy  data  of  1st  file  to  the  end  of  2nd  file

1st  file
---------
Rama  Rao
9247
+-$
Hyd  is  green  city

2nd  file
----------
Hyd
Sec
Cyb
Rama  Rao
9247
+-$
Hyd  is  green  city



1) In  which  mode  is  1st  file  opened ?  ---> read  mode
    In  which  mode  is  2nd  file  opened ?  ---> append  mode

2) Where  does  file  handle  points  to  when  file  is  opened  in  append  mode ?  --->  End  of  the  file
    Where  does  file  handle  points  to  when  file  is  opened  in  read  or  write  mode ? --->  Begining  of  the  file
'''

src = input('Enter  source  filename :  ')

dest = input('Enter  destination  filename :  ')

with  open(src , 'r')  as  f1 , open(dest , 'a')  as  f2:
		data = f1 . read()
		f2 . write(data)

print(F'Data  of  {src}  appended  to  {dest}')



#8
'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from prog1b import *

def  icp(operator):
	i = 0

	if operator == '+' or operator == '-':
		i = 1
	elif operator == '*' or operator == '/' or operator == '%':
		i = 2
	elif operator == '^' or operator == '(':
		i = 4

	return i

'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''

def  isp(operator):
	i = 0

	if operator == '+' or operator == '-':
		i = 1
	elif operator == '*' or operator == '/' or operator == '%':
		i = 2
	elif operator == '^':
		i = 3
	elif operator == '(':
		i = 0
	elif operator == '#':
		i = -1

	return i

'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  --->  -1
'''

def  convert(infix):
	s = stack()
	s . push('#')
	postfix = '' 

	for ch in infix:
		if ch . isdigit():
			postfix += ch
		elif ch == ')':
			while not s . peek() == '(':
				postfix += s . pop()

			s . pop()
		else:
			while not icp(ch) > isp(s . peek()):
				postfix += s . pop() 

			s . push(ch)

	#  End  of  for  loop

	while not s . peek() == '#':
		postfix += s . pop()

	return postfix

#  End  of  the  function

x = input('Enter the Infix Expression:')
p = convert(x)
print('Postfix  expression :' , p)

