#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.no=int(input("enter a number:"))
		self.name=input("enter a name:")
		self.age=int(input("enter age:"))
		self.gender=input("enter gender:")
	def   disp(self):
		print(self.no,/t,self.name,/t,self.age,/t,self.gender/)
	@abstractmethod
	def   compute(self):
                statements
class  student(person):
	def  get(self):
		super().get()
		self.marks=[]
		for i in range(3):
			x=eval(input("enter elements of list:"))
			self.marks.append(x)		
	def  compute(self):
		self.total=sum(self.marks)
		self.avg=self.total/count(self.marks)
	def  disp(self):
		super().disp()
		print(self.total,\t,self.avg)
class  teacher(person):
	def   get(self):
		super().get()
		self.subject=input("enter subject name:")
		self.salary=int(input("enter salary:"))
		self.city=input("enter city:")
	def   compute(self):
		da = 0.5*self.salary
		hra = 0.3*self.salary
		if self.city == 'Hyd':
   			cca = 1000
		else:
   			cca = 800  
	
		self.grosspay=self.salary+da+hra+cca #How  to  calculate  grosspay  i.e. salary + da + hra + cca
		pf = 0.08 * self.grosspay #8%  of  grosspay  but  a  max  of  400 		
		if pf > 400:
			pf = 400
		tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		#self.netpay=self.grosspay-pf-tax
		def   disp(self):
			super().disp()
			print(self.subject, '\t', self.salary, '\t', self.grosspay, '\t', self.netpay)
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
			obj=teacher()
			a.append(obj)
	elif  ch == 2:
			obj=teacher()
			a.append(obj)
	else:
		break()
	obj.get()
		



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