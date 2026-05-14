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

with  open(fname , 'w')  as  f:
	create(f)



'''
Repeat  prog5c(File-Create)  with  writelines()  method
'''

def  create(f):
	try:
		print('Enter  text  terminated  by  ctrl + z')

		lines = []

		while  True:
			line = input()
			lines . append(line + '\n')

	except  EOFError:

		f . writelines(lines)

		print(F'File  {f.name}  is  created')

#  End  of  the  function

fname = input('Enter  filename : ')

f = open(fname , 'w')

create(f)

f.close()



'''  (Home  work)
Write  a  program  to  print  data  of  the  file
'''

def  disp(f):

	data = f.read()

	print(F'Data  of  the  file  {f . name}')

	print(data)

# End  of  the  function

fname = input('Enter filename : ')

f = open(fname , 'r')

disp(f)

f.close()



'''  (Home  work)
Write  a  program  to  print  file  pagewise  and  page  length = 20   lines
'''

import os

def  disp(f):

	count = 0

	while True:

		line = f.readline()

		if line == '':
			break

		print(line , end = '')

		count += 1

		if count % 20 == 0:
			os.system('pause')
			os.system('cls')

#  End  of  the  function

fname = input('Enter filename : ')

f = open(fname , 'r')

disp(f)

f.close()



'''
Repeat  prog9b(File-pagewise)  with  for  loop
'''

import  os

def  disp(f):

	count = 0

	for  line  in  f:

		print(line , end = '')

		count += 1

		if count % 20 == 0:
			os.system('pause')
			os.system('cls')

# End  of  the  function

fname = input('Enter filename : ')

f = open(fname , 'r')

disp(f)

f.close()



'''
Repeat  prog9b(File-pagewise)  with  readlines()  method
'''

import os

def  disp(f):

	lines = f.readlines()

	count = 0

	for line in lines:

		print(line , end = '')

		count += 1

		if count % 20 == 0:
			os.system('pause')
			os.system('cls')

# End  of  the  function

fname = input('Enter filename : ')

f = open(fname , 'r')

disp(f)

f.close()



'''
Write  a  program  to  copy  contents  of  a  file  to  a  different  file
'''

import os

fname1 = input('Enter  source  filename : ')

fname2 = input('Enter  destination  filename : ')

if  not  os.path.exists(fname1):

	print('Source  file  does  not  exist')

else:

	if  os.path.exists(fname2):

		ch = input('Destination  file  already  exists . Overwrite(yes/no) : ')

		if ch.lower() != 'yes':
			print('Copy  operation  cancelled')
			exit()

	f1 = open(fname1 , 'r')

	f2 = open(fname2 , 'w')

	data = f1.read()

	f2.write(data)

	print('File  copied  successfully')

	f1.close()

	f2.close()



'''
Write  a  program  to  append  data  of  a  file  to  another  file
'''

fname1 = input('Enter  source  filename : ')

fname2 = input('Enter  destination  filename : ')

f1 = open(fname1 , 'r')

f2 = open(fname2 , 'a')

data = f1.read()

f2.write(data)

print('File  appended  successfully')

f1.close()

f2.close()



# Write  a  program  to  implement  queue  using  list

class  queue:

	def  __init__(q):
		q.list = []

	def  isempty(q):
		return q.list == []

	def  enqueue(q , x):
		q.list.append(x)

	def  dequeue(q):
		try:
			return q.list.pop(0)
		except:
			return None

	def  first(q):
		try:
			return q.list[0]
		except:
			return None

	def  last(q):
		try:
			return q.list[-1]
		except:
			return None

	def  disp(q):
		print('Queue  :  ' , q.list)

	def  size(q):
		return len(q.list)

# End  of  the  class

def  menu():

	print('1. Insertion')
	print('2. Deletion')
	print('3. Print  queue')
	print('4. First  element of queue')
	print('5. Last  element of queue')
	print('6. Number  of  elements  in  the  queue')
	print('7. Exit')

# End of  the  function

q = queue()

while  True:

	menu()

	ch = int(input('Enter  choice : '))

	match  ch:

		case  1:

			x = eval(input('Enter  element  to  be  inserted : '))

			q.enqueue(x)

			q.disp()

		case  2:

			x = q.dequeue()

			if x == None:
				print('Queue  is  empty , deletion  is  not  permitted')
			else:
				print('Deleted  element  : ' , x)

			q.disp()

		case  3:

			q.disp()

		case  4:

			x = q.first()

			if x == None:
				print('Queue  is  empty')
			else:
				print('First  element :  ' , x)

		case  5:

			x = q.last()

			if x == None:
				print('Queue  is  empty')
			else:
				print('Last  element :  ' , x)

		case  6:

			print('Number  of  elements  :  ' , q.size())

		case  7:

			exit()



# Write  a  program  to  implement  deque  using  list

class  deque:

	def   __init__(dq):
		dq.list = []

	def  isempty(dq):
		return dq.list == []

	def  ins_rear(dq , x):
		dq.list.append(x)

	def  ins_front(dq , x):
		dq.list.insert(0 , x)

	def  del_front(dq):
		try:
			return dq.list.pop(0)
		except:
			return None

	def  del_rear(dq):
		try:
			return dq.list.pop()
		except:
			return None

	def  disp(dq):
		print('Deque :  ' , dq.list)

	def  size(dq):
		return len(dq.list)

	def  leftmost(dq):
		try:
			return dq.list[0]
		except:
			return None

	def  rightmost(dq):
		try:
			return dq.list[-1]
		except:
			return None

# End of the class

def  menu():

	print('1. Insert  element  at  the  end  of  deque')
	print('2. Insert  element  at  the  begining  of  deque')
	print('3. Delete  left  most  element')
	print('4. Delete  right  most  element')
	print('5. Print  Deque')
	print('6. Print  left  most  element')
	print('7. Print  right  most  element')
	print('8. Number  of  elements  in  deque')
	print('9. Exit')

#end of  the  function

dq = deque()

while  True:

	menu()

	ch = int(input('Enter Choice :   '))

	match  ch:

		case  1:

			x = eval(input('Enter  element  to  be  inserted : '))

			dq.ins_rear(x)

			dq.disp()

		case  2:

			x = eval(input('Enter  element  to  be  inserted : '))

			dq.ins_front(x)

			dq.disp()

		case  3:

			x = dq.del_front()

			if x == None:
				print('Deque  is  empty  ,  deletion  is  not  permitted')
			else:
				print('Deleted  element :  ' , x)

			dq.disp()

		case  4:

			x = dq.del_rear()

			if x == None:
				print('Deque  is  empty  ,  deletion  is  not  permitted')
			else:
				print('Deleted  element :  ' , x)

			dq.disp()

		case  5:

			dq.disp()

		case  6:

			x = dq.leftmost()

			if x == None:
				print('Deque  is  empty')
			else:
				print('Leftmost  element :  ' , x)

		case  7:

			x = dq.rightmost()

			if x == None:
				print('Deque  is  empty')
			else:
				print('Rightmost  element :  ' , x)

		case  8:

			print('Number  of  elements   :  ' , dq.size())

		case  9:

			exit()



'''
Write  a  program  to  convert  infix  to  postfix
'''

from prog1b import stack

def  icp(operator):

	d = {'+':1 , '-':1 , '*':2 , '/':2 , '^':4 , '(':5}

	return d[operator]

def  isp(operator):

	d = {'+':1 , '-':1 , '*':2 , '/':2 , '^':3 , '(':0 , '#':-1}

	return d[operator]

def  convert(infix):

	s = stack()

	s.push('#')

	postfix = ''

	for ch in infix:

		if ch.isalnum():

			postfix += ch

		elif ch == ')':

			while s.peek() != '(':

				postfix += s.pop()

			s.pop()

		else:

			while icp(ch) <= isp(s.peek()):

				postfix += s.pop()

			s.push(ch)

	while s.peek() != '#':

		postfix += s.pop()

	return postfix

# End  of  the  function

infix = input('Enter infix expression : ')

postfix = convert(infix)

print('Postfix  expression :  ' , postfix)