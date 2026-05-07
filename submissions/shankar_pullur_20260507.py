#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.number=int(input("enter the number :"))#How  to   read  number
		self.name=input("enter the name :")#How  to   read  name
		self.age=int(input("enter the age :"))#How  to   read   age
		self.gender=input("enter the gender")#How  to   read   gender
	def   disp(self):
		print(self.number,self.name,self.age,self.gender,sep="\t")
	@abstractmethod
	def   compute(self):
		pass
              #   statements
class  student(person):
	def  get(self):
		super().get()
		self.marks=[]#How  to  read  marks  of  3  subjects  into  a  lis
		for i in range(3):
			m=int(input(f"enter marks for subject {i+1} : "))
			self.marks.append(m)
		
	def  compute(self):
		self.sum=sum(self.marks)#How  to  calculate  total  marks
		self.avg=self.sum/3
	def  disp(self):
		super().disp()
		print(f"{self.sum}\t{self.avg}")
		
class  teacher(person):
	def   get(self):
		super().get()
		self.subject=input("enter subject")#How  to  read   subject
		self.salary=float(input("enter the salary"))#How  to  read   salary
		self.city=input("enter the city")#How  to  read   city
	def   compute(self):
		da = 0.5 * self.salary
		hra = 0.2* self.salary
		cca =  1000 if self.city.upper()=="HYDERABAD" else 800# 1000  if  city  is  'Hyd'  and  800  otherwis
		#How  to  calculate  grosspay  i.e. salary + da + hra + cca
		self.grosspay= self.salary + da + hra + cca
		 
		pf =  400 if 0.08*self.grosspay>400 else 0.08*self.grosspay
		tax = 0.1*self.grosspay  if  self.grosspay < 10000  else  0.15*self.grosspay # otherwise
		self.netpay=self.grosspay-pf-tax
	def   disp(self):
		super().disp()
		print(f"{self.salary}\t{self.grosspay}\t{self.netpay}")
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
			a.append(t)
	elif  ch == 2:
			s=student()
			a.append(s)#How  to  append  student  object  to  list  'a'
	else:
			break
	a[-1].get()#How  to  read  inputs  into  object
	a[-1].compute()
# End  of  the  loop
print('Teachers')
for i in a:
	if isinstance(i,teacher):
		i.disp()
print('Students')
for i in a:
	if isinstance(i,student):
		i.disp()
print('Good  Bye')

from abc import ABC, abstractmethod


class datatype(ABC):

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def add(self, m, n):
        pass

    @abstractmethod
    def display(self):
        pass


class number(datatype):

    def get(self):
        # How to read number into variable 'x' of object self
        self.x=eval(input("enter the number : "))

    def add(self, m, n):
        # How to add objects m and n and store result in object self
        self.result=m.x+n.x

    def display(self):
        print('Sum of the numbers : ', self.result)


class string(datatype):

    def get(self):
        # How to read string into variable 'x' of object self
        self.x=input("enter the string : ")

    def add(self, m, n):
        # How to join objects m and n and store result in object self
        self.result=m.x+n.x

    def display(self):
        print('Join of the two strings : ',self.result)


def menu():
    print('1. Add numbers')
    print('2. Join Strings')
    print('3. Exit')


# End of the function

while True:
	menu()
	ch = eval(input('Enter choice : '))
	if ch==1:
		a=[]
		for i in range(3):
			s=number()
			a.append(s)
	elif ch==2:
		a=[]
		for i in range(3):
			s=string()
			a.append(s)
	else:
		break

	a[0].get()
	a[1].get()
	a[2].add(a[0],a[1])
	a[2].display()	



# End of while loop

#print('Good Bye')