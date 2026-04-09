'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
c=Emp()
for x in dict.items():
        setattr(c,x[0],x[1])
for x in dict.keys():
        print(f'{x}={getattr(c,x)}')
#--------------------------------------------------------------------
'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
import  math
class  triangle:
	def  get(self):
		self.a=int(input("enter side1 of triangle"))
		self.b=int(input("enter side2 of triangle"))
		self.c=int(input("enter side3 of triangle"))
	def  test(self):
		if self.a+self.b>self.c and self.b+self.c>self.a and self.c+self.a>self.b:
			pass
			return True
		else:
			print('Not  a  triangle')
			return False
	def  area(self):
			s=(self.a+self.b+self.c)/2
			return   math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
	def  peri(self):
			return  self.a+self.b+self.c
a=triangle()
triangle.get(a)
if triangle.test(a):
    print('Area : ',triangle.area(a))
    print('Perimeter : ', triangle.peri(a))
#-------------------------------------------------------------
# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s .__dict__) #{}
s . get()
print(s . _dict_)#{Roll  Number':25,'student_name':Rama Rao,'gender':male,'sub1':52,'sub2':48,'sub3':55}
s . compute()
print(s . _dict_)#Roll  Number':25,'student_name':Rama Rao,'gender':male,'sub1':52,'sub2':48,'sub3':55,'grade':third class,'total_marks':155,'average':77.5
#---------------------------------------------------------------------------------------------------------------------------------------
#  Find  outputs  (Home  work)
class   Rat:
	def  m1():
		pass
a = Rat()
a . nr = 22 #nr variable is added to object a
print(hasattr(a , 'nr')) #True
print(hasattr(a , 'dr'))#False
print(hasattr(a , 'm1'))#True
print(hasattr(a , 'm2'))#False
print(hasattr(Rat , 'm1'))#True
print(hasattr(Rat , 'm2'))#False
print(hasattr(Rat , 'nr'))#False
#-----------------------------------------------------
#  dir()  function  demo  program  (Home  work)

a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))#returns all the methos of class in form of list of strings
print()
print()
print(dir(a))#Returns  all  the  instance  variables  of  the  object  and   methods  of  the  class  in  the  form  of  list  of  strings
#---------------------------------------------------------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....')
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....')
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....')
#end of the class
a = [Cat() , Dog() , Goat()]
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()

#Meow Meow Meow ....
#Bhow Bhow Bhow ....'
#Mehar  Mehar  Mehar  ....
#--------------------------------------------------------------------
#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a .__dict__)#{'x':10,'y':20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
#--------------------------------------------------------------------------
import math

class Rat:

    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        self.test()
    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero.enter again:")
            self.den = int(input("Enter denominator: "))
    def __str__(self):
        return f"{self.num} / {self.den}"
    def simplify(self):
        if self.num == 0:
            self.den = 1
            return
        g = math.gcd(self.num, self.den)
        self.num //= g
        self.den //= g
    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        self.simplify()
    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        self.simplify()
    def mul(self, a, b):
        self.num = a.num * b.num
        self.den = a.den * b.den
        self.simplify()
    def div(self, a, b):
        if b.num == 0:
            self.den = 0
            return
        self.num = a.num * b.den
        self.den = a.den * b.num
        self.simplify()
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
print("Enter first rational number:")
a.get()
print("Enter second rational number:")
b.get()
c.add(a, b)
d.sub(a, b)
e.mul(a, b)
f.div(a, b)
print("Addition:", c)
print("Subtraction:", d)
print("Multiplication:", e)
if f.den != 0:
    print("Division:", f)
else:
    print("Division is not permitted")