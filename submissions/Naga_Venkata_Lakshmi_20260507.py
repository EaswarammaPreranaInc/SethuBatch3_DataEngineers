#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.number=int(input('Enter number : '))
		self.name=input('Enter name :')
		self.age=int(input('Enter age : '))
		self.gender=input('Enter gender : ')
	def   disp(self):
		print(self.number,self.name,self.age,self.gender,sep='\t',end='\t')
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		super().get()
		self.li=[0,0,0]
		for i in range(3):
			self.li[i]=float(input(f'Enter marks for subject {i+1} :'))
	def  compute(self):
		self.sum=sum(self.li)
		self.avg=self.sum/3
	def  disp(self):
		super().disp()
		print(self.sum,self.avg,sep='\t')
class  teacher(person):
	def   get(self):
		super().get()
		self.subject=input('Enter subject: ')
		self.salary=float(input('Enter salary: '))
		self.city=input('Enter city: ')
	def   compute(self):
		da = self.salary*0.5
		hra = self.salary*0.2
		cca = 1000  if  self.city=='Hyd'  else 800 
		self.gross=self.salary + da + hra + cca
		pf = self.gross*0.08 if self.gross*0.08 < 400 else 400		
		tax = self.gross*0.1 if  self.gross < 10000  else self.gross*0.15
		self.net=self.gross - pf - tax
	def   disp(self):
		super().disp()
		print(self.subject , self.salary , self.gross , self.net,sep='\t')
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
			o=teacher()
			a.append(o)
	elif  ch == 2:
			o=student()
			a.append(o)
	else:
			break
	o.get()
	o.compute()#How  to  store   results  in  object
# End  of  the  loop
print('Teachers')
for i in a:
	if hasattr(i,'salary'):
		i.disp()
print()
print('Students')
for i in a:
	if hasattr(i,'li'):
		i.disp()
print()
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
			self.x=int(input('enter number : '))#How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.res=m+n
	def  display(self):
			print('Sum  of  the  numbers  :  ' , self.res)
class   string(datatype):
	def  get(self):
		self.x=input('enter String: ')
	def  add(self , m , n):
		self.res=m+n
	def  display(self):
			print('Join  of  the  two  strings :  ' , self.res)
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
while  True:
	menu()
	ch =  eval(input('Enter choice : '))
	li=[]
	if   ch == 1:
		for i in range(3):
			o=number()
			li.append(o)
	elif  ch  == 2:
		for i in range(3):
			o=string()
			li.append(o)
	else:
		break
	li[0].get()
	li[1].get()
	li[2].add(li[0].x,li[1].x)
	li[2].display()
# End  of  while  loop
print('Good  Bye')