#1
# Modify following program with 'with' statement
def create(f):
	try:
		print('Type text terminated by ctrl+z')
		while line := input():
			f.write(line + '\n')
	except EOFError:
		print(f'File {f.name} is created')
# End of the function
fname = input('Enter filename : ')
with open(fname, 'w') as f:
	create(f)



#2
'''
Repeat prog5c(File-Create) with writelines() method

Inputs
--------
Rama Rao
9247
+-$
Hyd is green city
ctrl+z

List  --->  ['Rama Rao\n' , '9247\n' , '+-$\n' , 'Hyd is green city\n']

File
-----
Rama Rao
9247
+-$
Hyd is green city
'''
def create(f):
	print('Enter text terminated by ctrl + z')
	lst = []
	try:
		while True:
			line = input()
			lst.append(line + '\n')
	except EOFError:
		pass
	f.writelines(lst)
	print(f'File {f.name} is created')
# End of the function
fname = input('Enter filename : ')
f = open(fname, 'w')
create(f)
f.close()



#3
'''  (Home work)
Write a program to print data of the file

File
-----
Rama Rao
9247
+-$
Hyd is green city

1) Which method is used to read data of the file ?  ---> read()

2) Which function is used to print whole data of the file ?  ---> print()

3) In which mode is file opened ?  ---> read mode
'''
def disp(f):
	data = f.read()
	print(f'Data of the file {f.name}')
	print(data)
# End of the function
fname = input('Enter filename : ')
f = open(fname, 'r')
disp(f)
f.close()



#4
'''  (Home work)
Write a program to print file pagewise and page length = 20 lines
'''
import os
def disp(f):
	count = 0
	while True:
		line = f.readline()
		if line == '':
			break
		print(line, end='')
		count += 1
		if count % 20 == 0:
			os.system('pause')
			os.system('cls')
# End of the function
fname = input('Enter filename : ')
f = open(fname, 'r')
disp(f)
f.close()



#5
'''
Repeat prog9b(File-pagewise) with for loop
'''
import os
def disp(f):
	for i, line in enumerate(f, start=1):
		print(line, end='')
		if i % 20 == 0:
			os.system('pause')
			os.system('cls')
# End of the function
fname = input('Enter filename : ')
f = open(fname, 'r')
disp(f)
f.close()



#6
'''
Repeat prog9b(File-pagewise) with readlines() method
'''
import os
def disp(f):
	lst = f.readlines()
	for i, line in enumerate(lst, start=1):
		print(line, end='')
		if i % 20 == 0:
			os.system('pause')
			os.system('cls')
# End of the function
fname = input('Enter filename : ')
f = open(fname, 'r')
disp(f)
f.close()



#7
'''
Write a program to copy contents of a file to a different file
'''
src = input('Enter source filename : ')
dst = input('Enter destination filename : ')
try:
	f1 = open(src, 'r')
except FileNotFoundError:
	print('Source file not found')
else:
	data = f1.read()
	f1.close()
	f2 = open(dst, 'w')
	f2.write(data)
	f2.close()
	print('File copied successfully')



#8
'''
Write a program to append data of a file to another file
'''
src = input('Enter source filename : ')
dst = input('Enter destination filename : ')
try:
	f1 = open(src, 'r')
except FileNotFoundError:
	print('Source file not found')
else:
	data = f1.read()
	f1.close()
	f2 = open(dst, 'a')
	f2.write(data)
	f2.close()
	print('Data appended successfully')



#9
# Write a program to implement queue using list
class queue:
	def _init_(q):
		q.lst = []
	# q = queue()
	def isempty(q):
		return len(q.lst) == 0
	# q.isempty()
	def enqueue(q , x):
		q.lst.append(x)
	# q.enqueue(25)
	def dequeue(q):
		try:
			return q.lst.pop(0)
		except:
			return None
	# q.dequeue()
	def first(q):
		try:
			return q.lst[0]
		except:
			return None
	# q.first()
	def last(q):
		try:
			return q.lst[-1]
		except:
			return None
	# q.last()
	def disp(q):
		print('Queue : ' , q.lst)
	# q.disp()
	def size(q):
		return len(q.lst)
	# q.size()
# End of the class
def menu():
	print('1. Insertion')
	print('2. Deletion')
	print('3. Print queue')
	print('4. First element of queue')
	print('5. Last element of queue')
	print('6. Number of elements in the queue')
	print('7. Exit')
# End of the function
q = queue()
q.lst = []
while True:
	menu()
	ch = int(input('Enter choice : '))
	match ch:
		case 1:
			x = eval(input('Enter element to be inserted : '))
			q.enqueue(x)
			q.disp()
		case 2:
			x = q.dequeue()
			if x is None:
				print('Queue is empty , deletion is not permitted')
			else:
				print('Deleted element : ' , x)
			q.disp()
		case 3:
			q.disp()
		case 4:
			x = q.first()
			if x is None:
				print('Queue is empty')
			else:
				print('First element : ' , x)
		case 5:
			x = q.last()
			if x is None:
				print('Queue is empty')
			else:
				print('Last element : ' , x)
		case 6:
			print('Number of elements : ' , q.size())
		case 7:
			break



#10
# Write a program to implement deque using list
class deque:
	def _init_(dq):
		dq.lst = []
	# dq = deque()
	def isempty(dq):
		return len(dq.lst) == 0
	# dq.isempty()
	def ins_rear(dq , x):
		dq.lst.append(x)
	# dq.insrear(x)
	def ins_front(dq , x):
		dq.lst.insert(0, x)
	# dq.insfront(x)
	def del_front(dq):
		try:
			return dq.lst.pop(0)
		except:
			return None
	# dq.delfront()
	def del_rear(dq):
		try:
			return dq.lst.pop()
		except:
			return None
	def disp(dq):
		print('Deque : ' , dq.lst)
	# dq.disp()
	def size(dq):
		return len(dq.lst)
	# dq.size()
	def leftmost(dq):
		try:
			return dq.lst[0]
		except:
			return None
	# dq.leftmost()
	def rightmost(dq):
		try:
			return dq.lst[-1]
		except:
			return None
	# dq.rightmost()
#End of the class
def menu():
	print('1. Insert element at the end of deque')
	print('2. Insert element at the begining of deque')
	print('3. Delete left most element')
	print('4. Delete right most element')
	print('5. Print Deque')
	print('6. Print left most element')
	print('7. Print right most element')
	print('8. Number of elements in deque')
	print('9. Exit')
#end of the function
dq = deque()
dq.lst = []
while True:
	menu()
	ch = int(input('Enter Choice : '))
	match ch:
		case 1:
			x = eval(input('Enter element to be inserted : '))
			dq.ins_rear(x)
			dq.disp()
		case 2:
			x = eval(input('Enter element to be inserted : '))
			dq.ins_front(x)
			dq.disp()
		case 3:
			x = dq.del_front()
			if x is None:
				print('Deque is empty , deletion is not permitted')
			else:
				print('Deleted element : ' , x)
			dq.disp()
		case 4:
			x = dq.del_rear()
			if x is None:
				print('Deque is empty , deletion is not permitted')
			else:
				print('Deleted element : ' , x)
			dq.disp()
		case 5:
			dq.disp()
		case 6:
			x = dq.leftmost()
			if x is None:
				print('Deque is empty')
			else:
				print('Leftmost element : ' , x)
		case 7:
			x = dq.rightmost()
			if x is None:
				print('Deque is empty')
			else:
				print('Rightmost element : ' , x)
		case 8:
			print('Number of elements : ' , dq.size())
		case 9:
			break



#11
'''
Write a program to convert infix to postfix

Reuse stack class defined in prog1b.py file but do not rewrite
'''
from prog1b import stack

def icp(operator):
	if operator == '+':
		return 1
	if operator == '-':
		return 1
	if operator == '*':
		return 2
	if operator == '/':
		return 2
	if operator == '^':
		return 4
	return 0

def isp(operator):
	if operator == '+':
		return 1
	if operator == '-':
		return 1
	if operator == '*':
		return 2
	if operator == '/':
		return 2
	if operator == '^':
		return 3
	if operator == '(':
		return 0
	if operator == '#':
		return -1
	return 0

def convert(infix):
	s = stack()
	s.lst = []
	s.push('#')
	postfix = ''
	for ch in infix:
		if ch.isalnum():
			postfix += ch
		elif ch == ')':
			while s.last() != '(':
				postfix += s.pop()
			s.pop()
		else:
			while icp(ch) <= isp(s.last()):
				postfix += s.pop()
			s.push(ch)
	while s.last() != '#':
		postfix += s.pop()
	s.pop()
	return postfix
# End of the function
infix = input('Enter infix expression : ')
print('Postfix expression : ' , convert(infix))