1) Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.no = int(input("Enter any number:")) #How  to   read  number
		self.name = input("Enter any name:") #How  to   read  name
		self.age = int(input("Enter age:")) #How  to   read   age
		self.gender = input('Enter gender : ') #How  to   read   gender
	def   disp(self):
		print(self.no, '\t', self.name, '\t', self.age, '\t', self.gender, end='\t') #How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
               pass  #statements
class  student(person):
	def  get(self):
		super().get() #How  to  read   number , name , age , gender
		self.marks = []
		for i in range(3):
		    x = int(input(f'Enter marks of subject {i+1}:'))
		    self.marks.append(x) #How  to  read  marks  of  3  subjects  into  a  list
	def  compute(self):
		self.total = sum(self.marks) #How  to  calculate  total  marks
		self.avg = self.total / 3 #How  to  calculate  average  marks
	def  disp(self):
		super().disp() #How  to  print  number , name , age , gender
		print(self.total, '\t', self.avg) #How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super().get() #How  to  read  number , name , age  and  gender
		self.subject = input('Enter subject : ')#How  to  read   subject
		self.city = input('Enter city : ') #How  to  read   salary
		self.salary = float(input('Enter salary : ')) #How  to  read   city
	def   compute(self):
		da = 0.5 * self.salary #50%  of  salary
		hra = 0.2 * self.salary #20%  of  salary
		
		if self.city == 'Hyd':
   			cca = 1000
		else:
   			cca = 800    
		self.grosspay = self.salary + da + hra + cca #How  to  calculate  grosspay  i.e. salary + da + hra + cca
		pf = 0.08 * self.grosspay #8%  of  grosspay  but  a  max  of  400 		
		if pf > 400:
			pf = 400

		if self.grosspay < 10000:
			tax = 0.10 * self.grosspay
		else:
			tax = 0.15 * self.grosspay

		self.netpay = self.grosspay - pf - tax
	def   disp(self):
		super().disp() #How  to  print  number , name , age , gender
		print(self.subject, '\t', self.salary, '\t', self.grosspay, '\t', self.netpay) #How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
def  menu():
	print('1. Teacher')
	print('2. Student')
	print('3. Exit')
# End  of  the  function
a = []
while  True: 
	menu()
	ch = eval(input('Enter choice : '))  
	if   ch == 1:
		obj = teacher()
		a.append(obj) #How  to  append  teacher  object  to  list  'a'
	elif  ch == 2:
		obj = student()
		a.append(obj) #How  to  append  student  object  to  list  'a'
	else:
		break #How  to  move  out  of  loop
	obj.get() #How  to  read  inputs  into  object
	obj.compute() #How  to  store   results  in  object
# End  of  the  loop
print('Teachers')
for x in a:
	if isinstance(x, teacher):
		x.disp() #How  to  print  all  teacher  objects
print('Students')
for x in a:
	if isinstance(x, student):
		x.disp() #How  to  print  all  teacher  objects
print('Good  Bye')


2) Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
from  abc  import  abstractmethod , ABC
class   datatype(ABC):
	@abstractmethod
	def  get(self):
		 pass
	@abstractmethod
	def  add(self , m ,  n):
		pass
	@abstractmethod
	def  display(self):
		pass
class   number(datatype):
	def  get(self):
		self.x = int(input('Enter a number: ')) #How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
		self.x = m.x + n.x #How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum  of  the  numbers  :  ' , self.x) #How  to  print  sum  result)
class   string(datatype):
	def  get(self):
		self.x = input('Enter a string: ') #How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
		self.x = m.x + n.x #How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' , self.x)
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
while  True:
	menu()
	ch =  eval(input('Enter choice : '))  
	if   ch == 1:
		a = [number(), number(), number()] #How  to  create  list  of  3  number  class  objects
	elif  ch  == 2:
		a = [string(), string(), string()] #How  to  create  list  of  3  string  class  objects
	else:
		break #How  to  get  out   of  the  loop
	a[0].get() #How  to  read  input  into  first  object
	a[1].get() #How  to  read  input  into  2nd  object
	a[2].add(a[0], a[1]) #How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
	a[2].display() #How  to  print  3rd  object
# End  of  while  loop
print('Good  Bye')