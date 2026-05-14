#1
# Write a program to determine total and average of student and gross pay and net pay of teacher
from abc import *
class person(ABC):
	def get(self):
		# How to read number
		self.no = int(input('Enter number : '))
		# How to read name
		self.name = input('Enter name : ')
		# How to read age
		self.age = int(input('Enter age : '))
		# How to read gender
		self.gender = input('Enter gender : ')
	def disp(self):
		# How to print number , name , age , gender in same line separated by tab
		print(self.no, self.name, self.age, self.gender, sep='\t')
	@abstractmethod
	def compute(self):
		pass
class student(person):
	def get(self):
		# How to read number , name , age , gender
		super().get()
		# How to read marks of 3 subjects into a list
		self.marks = []
		for i in range(3):
			self.marks.append(int(input(f'Enter mark {i+1} : ')))
	def compute(self):
		# How to calculate total marks
		self.total = sum(self.marks)
		# How to calculate average marks
		self.avg = self.total / 3
	def disp(self):
		# How to print number , name , age , gender
		super().disp()
		# How to print total and average in same line separated by tab
		print(self.total, self.avg, sep='\t')
class teacher(person):
	def get(self):
		# How to read number , name , age and gender
		super().get()
		# How to read subject
		self.subject = input('Enter subject : ')
		# How to read salary
		self.salary = float(input('Enter salary : '))
		# How to read city
		self.city = input('Enter city : ')
	def compute(self):
		# da = 50% of salary
		da = 0.50 * self.salary
		# hra = 20% of salary
		hra = 0.20 * self.salary
		# cca = 1000 if city is 'Hyd' and 800 otherwise
		cca = 1000 if self.city == 'Hyd' else 800
		# How to calculate grosspay i.e. salary + da + hra + cca
		self.grosspay = self.salary + da + hra + cca
		# pf = 8% of grosspay but a max of 400
		pf = min(0.08 * self.grosspay, 400)
		# tax = 10% of grosspay if grosspay is < 10000 and 15% otherwise
		tax = 0.10 * self.grosspay if self.grosspay < 10000 else 0.15 * self.grosspay
		# How to calculate netpay i.e. grosspay - pf - tax
		self.netpay = self.grosspay - pf - tax
	def disp(self):
		# How to print number , name , age , gender
		super().disp()
		# How to print subject , salary , grosspay , netpay in same line separated by tab
		print(self.subject, self.salary, self.grosspay, self.netpay, sep='\t')
def menu():
	print('1. Teacher')
	print('2. Student')
	print('3. Exit')
# End of the function
a = []
while True:
	menu()
	ch = eval(input('Enter choice : '))
	if ch == 1:
		# How to append teacher object to list 'a'
		obj = teacher()
		a.append(obj)
	elif ch == 2:
		# How to append student object to list 'a'
		obj = student()
		a.append(obj)
	else:
		# How to move out of loop
		break
	# How to read inputs into object
	obj.get()
	# How to store results in object
	obj.compute()
# End of the loop
print('Teachers')
# How to print all teacher objects
for x in a:
	if isinstance(x, teacher):
		x.disp()
print('Students')
# How to print all teacher objects
for x in a:
	if isinstance(x, student):
		x.disp()
print('Good  Bye')



#2
# Write a progran to add num class objects and join str class objects
from abc import abstractmethod , ABC
class datatype(ABC):
	@abstractmethod
	def get(self):
		pass
	@abstractmethod
	def add(self , m , n):
		pass
	@abstractmethod
	def display(self):
		pass
class number(datatype):
	def get(self):
		# How to read number into variable 'x' of object self
		self.x = int(input('Enter number : '))
	def add(self , m , n):
		# How to add objects m and n and store result in object self
		self.x = m.x + n.x
	def display(self):
		print('Sum of the numbers : ' , self.x)
class string(datatype):
	def get(self):
		# How to read string into variable 'x' of object self
		self.x = input('Enter string : ')
	def add(self , m , n):
		# How to join objects m and n and store result in object self
		self.x = m.x + n.x
	def display(self):
		print('Join of the two strings : ' , self.x)
def menu():
	print('1. Add numbers')
	print('2. Join Strings')
	print('3. Exit')
# End of the function
while True:
	menu()
	ch = eval(input('Enter choice : '))
	if ch == 1:
		# How to create list of 3 number class objects
		a = [number(), number(), number()]
	elif ch == 2:
		# How to create list of 3 string class objects
		a = [string(), string(), string()]
	else:
		# How to get out of the loop
		break
	# How to read input into first object
	a[0].get()
	# How to read input into 2nd object
	a[1].get()
	# How to add (or) join the two objects and store the result in 3rd object
	a[2].add(a[0], a[1])
	# How to print 3rd object
	a[2].display()
# End of while loop
print('Good  Bye')