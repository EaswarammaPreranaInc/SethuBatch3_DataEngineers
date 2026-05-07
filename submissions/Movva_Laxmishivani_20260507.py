'''
#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		How  to   read  number
		How  to   read  name
		How  to   read   age
		How  to   read   gender
	def   disp(self):
		How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                statements
class  student(person):
	def  get(self):
		How  to  read   number , name , age , gender
		How  to  read  marks  of  3  subjects  into  a  list
	def  compute(self):
		How  to  calculate  total  marks
		How  to  calculate  average  marks
	def  disp(self):
		How  to  print  number , name , age , gender
		How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		How  to  read  number , name , age  and  gender
		How  to  read   subject
		How  to  read   salary
		How  to  read   city
	def   compute(self):
		da = 50%  of  salary
		hra = 20%  of  salary
		cca = 1000  if  city  is  'Hyd'  and  800  otherwise
		How  to  calculate  grosspay  i.e. salary + da + hra + cca
		pf =  8%  of  grosspay  but  a  max  of  400 		
		tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		How  to  calculate  netpay  i.e. grosspay - pf - tax
	def   disp(self):
		How  to  print  number , name , age , gender
		How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
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
			How  to  append  teacher  object  to  list  'a'
	elif  ch == 2:
			How  to  append  student  object  to  list  'a'
	else:
			How  to  move  out  of  loop
	How  to  read  inputs  into  object
	How  to  store   results  in  object
# End  of  the  loop
print('Teachers')
How  to  print  all  teacher  objects
print('Students')
How  to  print  all  teacher  objects
print('Good  Bye')
'''
Sample output:
1. Teacher
2. Student
3. Exit
Enter choice : 2
Enter number : 111
Enter name : AAA
Enter age : 21
Enter gender : m
Enter marks for subject 1 : 52
Enter marks for subject 2 : 48
Enter marks for subject 3 : 55

1. Teacher
2. Student
3. Exit
Enter choice : 1
Enter number : 222
Enter name : BBB
Enter age : 35
Enter gender : f
Enter subject : Python
Enter city : Hyd
Enter salary : 10000

1. Teacher
2. Student
3. Exit
Enter choice : 2
Enter number : 333
Enter name : CCC
Enter age : 25
Enter gender : f
Enter marks for subject 1 : 100
Enter marks for subject 2 : 100
Enter marks for subject 3 : 0

1. Teacher
2. Student
3. Exit
Enter choice : 1
Enter number : 444
Enter name : DDD
Enter age : 45
Enter gender : m
Enter subject : Java
Enter city : 20000
Enter salary : 20000

1. Teacher
2. Student
3. Exit
Enter choice : 3


Teachers
222    BBB    35    f    Python    10000.0    18000.0    15400.0
444    DDD    45    m    Java      20000.0    34800.0    29680.0

Students
111    AAA    21    m    155    51.666666666666664
333    CCC    25    f    200    66.66666666666667

Good Bye
from abc import *
class person(ABC):
    def get(self):
        self.no = int(input('Enter number : '))
        self.name = input('Enter name : ')
        self.age = int(input('Enter age : '))
        self.gender = input('Enter gender : ')
    def disp(self):
        print(self.no, self.name, self.age, self.gender, end='\t')
    @abstractmethod
    def compute(self):
        pass

class student(person):
    def get(self):
        super().get()
        self.marks = []
        for i in range(3):
            x = int(input(f'Enter marks for subject {i+1} : '))
            self.marks.append(x)
    def compute(self):
        self.total = sum(self.marks)
        self.avg = self.total / 3
    def disp(self):
        super().disp()
        print(self.total, self.avg)


class teacher(person):
    def get(self):
        super().get()
        self.subject = input('Enter subject : ')
        self.city = input('Enter city : ')
        self.salary = float(input('Enter salary : '))
    def compute(self):
        da = 0.5 * self.salary
        hra = 0.2 * self.salary
        if self.city == 'Hyd':
            cca = 1000
        else:
            cca = 800
        self.grosspay = self.salary + da + hra + cca
        pf = 0.08 * self.grosspay
        if pf > 400:
            pf = 400
        if self.grosspay < 10000:
            tax = 0.10 * self.grosspay
        else:
            tax = 0.15 * self.grosspay
        self.netpay = self.grosspay - pf - tax
    def disp(self):
        super().disp()
        print(self.subject, self.salary,self.grosspay, self.netpay)

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
print('Good Bye')

'''
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
			How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum  of  the  numbers  :  ' , How  to  print  sum  result)
class   string(datatype):
	def  get(self):
			How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' , How  to  print  the   join  result
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
while  True:
	menu()
	ch =  eval(input('Enter choice : '))  
	if   ch == 1:
		How  to  create  list  of  3  number  class  objects
	elif  ch  == 2:
		How  to  create  list  of  3  string  class  objects
	else:
		How  to  get  out   of  the  loop
	How  to  read  input  into  first  object
	How  to  read  input  into  2nd  object
	How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
	How  to  print  3rd  object
# End  of  while  loop
print('Good  Bye')
'''
Sample output:
1. Add numbers
2. Join Strings
3. Exit

Enter choice : 2
Enter a string: 10
Enter a string: 20
Join : 1020

1. Add numbers
2. Join Strings
3. Exit

Enter choice : 1
Enter a number: 10
Enter a number: 20
Sum : 30

1. Add numbers
2. Join Strings
3. Exit

Enter choice : 2
Enter a string: Hyder
Enter a string: abad
Join : Hyderabad

1. Add numbers
2. Join Strings
3. Exit

Enter choice : 3

Good Bye
----------------------------------------------------------------------------------------
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
        self.x = int(input('Enter a number: '))
    def add(self, m, n):
        self.x = m.x + n.x
    def display(self):
        print('Sum : ', self.x)


class string(datatype):
    def get(self):
        self.x = input('Enter a string: ')
    def add(self, m, n):
        self.x = m.x + n.x
    def display(self):
        print('Join : ', self.x)


def menu():
    print('1. Add  numbers')
    print('2. Join  Strings')
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
print('Good Bye')