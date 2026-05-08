
#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.a = int(input('Enter number: '))#How  to   read  number
		self.b = input('Enter name:')#How  to   read  name
		self.c = int(input('Enter age:'))#How  to   read   age
		self.d = input('Enter gender: ')#How  to   read   gender
	def   disp(self):
		print(f'{self.a} \t {self.b} \t {self.c} \t {self.d} \t',end= ' ')#How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                statements
class  student(person):
	def  get(self):
		super().get()#How  to  read   number , name , age , gender
		self.marks = []
		for i in range(3):
			m = int(input(f'Enter marks for subject {i+1} : '))
			self.marks.append(m)#How  to  read  marks  of  3  subjects  into  a  list
	def  compute(self):
		self.total = sum(self.marks)#How  to  calculate  total  marks
		self.avg = self.total / len(self.marks)#How  to  calculate  average  marks
	def  disp(self):
		super().disp()#How  to  print  number , name , age , gender
		print(f'{self.total} \t {self.avg}')#How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super().get()#How  to  read  number , name , age  and  gender
		self.sub = input('Enter subject:')#How  to  read   subject
		self.sal = float(input('Enter salary:'))#How  to  read   salary
		self.city = input('Enter city:')#How  to  read   city
	def   compute(self):
		da = self.sal * 0.05 #50%  of  salary
		hra = self.sal * 0.02 #20%  of  salary
		if self.city == 'Hyd':
			cca = 1000
		else:
			cca = 800 #cca = 1000  if  city  is  'Hyd'  and  800  otherwise
		self.gpay = self.sal + da + hra + cca#How  to  calculate  grosspay  i.e. salary + da + hra + cca
		pf = self.gpay * 0.08
		if pf > 400:
			pf = 400 #pf =  8%  of  grosspay  but  a  max  of  400 		
		if self.gpay < 10000:
			tax = self.gpay * 0.10
		else:
			tax = self.gpay * 0.15 #tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		self.npay = self.gpay - pf - tax #How  to  calculate  netpay  i.e. grosspay - pf - tax
	def   disp(self):
		super().disp()#How  to  print  number , name , age , gender
		print(f'{self.sub} \t {self.sal} \t {self.gpay} \t {self.npay}')#How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
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
			t = teacher()
			a.append(t)#How  to  append  teacher  object  to  list  'a'
			t.get()
			t.compute()
	elif  ch == 2:
			s=student()
			a.append(s)#How  to  append  student  object  to  list  'a'
			s.get()
			s.compute()
	else:
			break#How  to  move  out  of  loop
	#a.get()#How  to  read  inputs  into  object
	#a.compute()#How  to  store   results  in  object
# End  of  the  loop
print('Teachers')
t.disp()#How  to  print  all  teacher  objects
print('Students')
s.disp()#How  to  print  all  teacher  objects
print('Good  Bye')



#  Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
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
			self.x = int(input('Enter number:')) #How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x = m.x + n.x #How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum:',self.x) # How  to  print  sum  result)
class   string(datatype):
	def  get(self):
			self.x = input('Enter string:') # How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x = m.x + n.x # How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join:',self.x) # How  to  print  the   join  result
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
while  True:
	menu()
	ch =  eval(input('Enter choice : '))  
	if   ch == 1:
		a= [number(),number(),number()]#How  to  create  list  of  3  number  class  objects
	elif  ch  == 2:
		a = [string(),string(),string()] # How  to  create  list  of  3  string  class  objects
	else:
		break # How  to  get  out   of  the  loop
	a[0].get() # How  to  read  input  into  first  object
	a[1].get() #How  to  read  input  into  2nd  object
	a[2].add(a[0],a[1]) # How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
	a[2].display() # How  to  print  3rd  object
# End  of  while  loop
print('Good  Bye')
