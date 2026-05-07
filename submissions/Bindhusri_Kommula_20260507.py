#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.number=int(input())
		self.name=input()
		self.age=int(input())
		self.gender=input()
	def   disp(self):
		print(f'{self.number} \t {self.name} \t {self.age} \t {self.gender}')
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		super().get()
                self.marks=[]
		for i in range(3):
			m=int(input())
			self.marks.append(m)
	def  compute(self):
		self.total=sum(self.marks)
		self.avg=sum(self.marks)/3
	def  disp(self):
		super().disp()
		print(f'{self.total}, {self.avg}')
class  teacher(person):
	def   get(self):
		super().get()
		self.subject=input()
		self.salary=float(input())
		self.city=input()
	def   compute(self):
		da = (50/100) *self.salary
		hra = (20/100) *self. salary
		if self.city.lower()=='Hyd':
			cca = 1000
		else:
			cca=800
		self.grosspay=self.salary + da + hra + cca 
		pf = 0.08 * self.grosspay
                if pf > 400:
                	pf = 400
		if  self.grosspay is  < 10000:		
			tax = (10/100)*self.grosspay  
		else:
			tax = (15/100)*self.grosspay 
		self.netpay=self.grosspay - pf - tax
	def   disp(self):
		super().disp()
		print(f'{self.subject} \t , {self.salary} , {self.grosspay} , {self.netpay}')
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
			obj=Teacher()
                        a.append(obj)
	elif  ch == 2:
			obj=Student()
                        a.append(obj)
	else:
			break
	obj.get()
	obj.result()
# End  of  the  loop
print('Teachers')
How  to  print  all  teacher  objects
print('Students')
How  to  print  all  teacher  objects
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
			self.x=int(input())
	def  add(self , m , n):
			self.x=m.x+n.x
	def  display(self):
			print('Sum  of  the  numbers  :  ' , self.x)
class   string(datatype):
	def  get(self):
			self.x=input()
	def  add(self , m , n):
			self.x=m.x+n.x
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
		a = [Number(), Number(), Number()]
	elif  ch  == 2:
		a = [String(), String(), String()]
	else:
		break
	a[0].get()
        a[1].get()
        a[2].add(a[0], a[1])
        a[2].display()
# End  of  while  loop
print('Good  Bye')




