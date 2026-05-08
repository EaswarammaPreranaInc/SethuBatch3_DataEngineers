#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.num=int(input("Enter a number:"))#How  to   read  number
		self.name=input("Enter the name:")#How  to   read  name
		self.age=int(input("Enter the age:"))#How  to   read   age
		self.gender=input("Enter the gender:")#How  to   read   gender
	def   disp(self):
		print(self.num,self.name,self.age,self.gender,sep='\t')#How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
            pass
class  student(person):
	def  get(self):
		super().get()#How  to  read   number , name , age , gender
		m1=int(input("enter the marks m1:"))
		m2=int(input("enter the marks m2:"))
		m3=int(input("enter the marks m3:"))
		self.marks=[m1,m2,m3]#How  to  read  marks  of  3  subjects  into  a  list
	def  compute(self):
		self.total_marks=sum(self.marks)#How  to  calculate  total  marks
		self.average_marks=sum(self.marks)/len(self.marks)#How  to  calculate  average  marks
	def  disp(self):
		super().get()#How  to  print  number , name , age , gender
		print(self.total_marks,self.average_marks,sep='\t')#How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super.get()#How  to  read  number , name , age  and  gender
		self.sub=input("Enter the subject:")#How  to  read   subject
		self.salary=int(input("Enter the salary:"))#How  to  read   salary
		self.city=input("Enter the city:")#How  to  read   city
	def   compute(self):
		da = 50%  of  salary
		hra = 20%  of  salary
		cca = 1000  if  city=='Hyd'  else  800 
		self.gross_pay=self.salary+da+hra+cca #How  to  calculate  grosspay  i.e. salary + da + hra + cca
		pf=(8/100) * self.grosspay
		if pf > 400:
			pf=400 #8%  of  grosspay  but  a  max  of  400 		
		if self.grosspay < 10000:
			tax = (10/100)* self.grosspay
		else:
			tax=(15/100)* self.grosspay  #10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		self.net_pay=self.gross_pay-pf-tax#How  to  calculate  netpay  i.e. grosspay - pf - tax
	def   disp(self):
		super().get()#How  to  print  number , name , age , gender
		print(self.sub,self.salary,self.gross_pay,self.net_pay,sep='\t')#How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
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
			t=teacher()
			a.append(t)#How  to  append  teacher  object  to  list  'a'
	elif  ch == 2:
			s=student()
			a.append(s)#How  to  append  student  object  to  list  'a'
	else:
			break#How  to  move  out  of  loop
# End  of  the  loop
print('Teachers')
for x in a:
	if isinstance(x, teacher):
		x.disp()
print('Students')
for x in a:
	if isinstance(x, student):
		x.disp()
print('Good  Bye')







#  Write  a  program  to  add  num  class  objects  and  join  str  class  objects
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
			self.x=int(input("Enter the number:"))#How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x=sum(self.m+self.n)#How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum  of  the  numbers  :  ' , self.x)#How  to  print  sum  result
class   string(datatype):
	def  get(self):
			self.x=input("Enter String:")#How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x=m.x+n.x#How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' , self.x)#How  to  print  the   join  result
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
while  True:
	menu()
	ch =  eval(input('Enter choice : '))  
	if   ch == 1:
		l=[number(),number(),number()] #How  to  create  list  of  3  number  class  objects
	elif  ch  == 2:
		l=[string(),string(),string()] #How  to  create  list  of  3  string  class  objects
	else:
		break #How  to  get  out   of  the  loop
	l[0].get() #How  to  read  input  into  first  object
	l[1].get() #How  to  read  input  into  2nd  object
	l[2].add(l[0],l[1]) #How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
	l[2].display() #How  to  print  3rd  object
# End  of  while  loop
print('Good  Bye')

