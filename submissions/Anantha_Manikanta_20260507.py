# 1) Write a program to determine total and average of student and gross pay and net pay of teacher
from abc import *
class person(ABC):
	def get(self):
		self.no = int(input('Enter number : '))
		self.name = input('Enter name : ')
		self.age = int(input('Enter age : '))
		self.gender = input('Enter gender : ')
	def disp(self):
		print(self.no, self.name, self.age, self.gender, sep='\t')
	@abstractmethod
	def compute(self):
		pass
class student(person):
	def get(self):
		super().get()
		self.marks = []
		for i in range(3):
			self.marks.append(int(input(f'Enter mark {i+1} : ')))
	def compute(self):
		self.total = sum(self.marks)
		self.avg = self.total / 3
	def disp(self):
		super().disp()
		print(self.total, self.avg, sep='\t')
class teacher(person):
	def get(self):
		super().get()
		self.subject = input('Enter subject : ')
		self.salary = float(input('Enter salary : '))
		self.city = input('Enter city : ')
	def compute(self):
		da = 0.50 * self.salary
		hra = 0.20 * self.salary
		cca = 1000 if self.city == 'Hyd' else 800
		self.grosspay = self.salary + da + hra + cca
		pf = min(0.08 * self.grosspay, 400)
		tax = 0.10 * self.grosspay if self.grosspay < 10000 else 0.15 * self.grosspay
		self.netpay = self.grosspay - pf - tax
	def disp(self):
		super().disp()
		print(self.subject, self.salary, self.grosspay, self.netpay, sep='\t')
def menu():
	print('1. Teacher')
	print('2. Student')
	print('3. Exit')
a = []
while True:
	menu()
	ch = eval(input('Enter choice : '))
	if ch == 1:
		obj = teacher()
		a.append(obj)
	elif ch == 2:
		obj = student()
		a.append(obj)
	else:
		break
	obj.get()
	obj.compute()
print('Teachers')
for x in a:
	if isinstance(x, teacher):
		x.disp()
print('Students')
for x in a:
	if isinstance(x, student):
		x.disp()
print('Good  Bye')

# 2) Write a progran to add num class objects and join str class objects
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
		self.x = int(input('Enter number : '))
	def add(self , m , n):
		self.x = m.x + n.x
	def display(self):
		print('Sum of the numbers : ' , self.x)
class string(datatype):
	def get(self):
		self.x = input('Enter string : ')
	def add(self , m , n):
		self.x = m.x + n.x
	def display(self):
		print('Join of the two strings : ' , self.x)
def menu():
	print('1. Add numbers')
	print('2. Join Strings')
	print('3. Exit')
while True:
	menu()
	ch = eval(input('Enter choice : '))
	if ch == 1:
		a = [number(), number(), number()]
	elif ch == 2:
		a = [string(), string(), string()]
	else:
		break
	a[0].get()
	a[1].get()
	a[2].add(a[0], a[1])
	a[2].display()
print('Good  Bye')