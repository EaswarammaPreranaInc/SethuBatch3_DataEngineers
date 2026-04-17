class Triangle:
    def get(self):
        self.a = float(input('Enter 1st side: '))
        self.b = float(input('Enter 2nd side: '))
        self.c = float(input('Enter 3rd side: '))
    def test(self):
        if self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b:
            pass
        else:
            print('Invalid triangle')
            exit()
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    def peri(self):
        return self.a + self.b + self.c
t = Triangle()  # object creation
Triangle.get(t)  # calling get() method using classname.method(object)
Triangle.test(t)  # calling test() method using classname.method(object)
print('Area : ', Triangle.area(t))  # calling area() method using classname.method(object)
print('Perimeter: ', Triangle.peri(t))  # calling peri() method using classname.method(object)

from Ajay_Sougani_20260407 import  Student
a = Student()
b = Student()
c = Student()
n = int(input('Enter number of students : '))
students = []
for i in range(n):
    student = Student()
    students.append(student)
print(students) # list of objects
for student in students:
    student.get()
    student.compute()
    student.disp()

#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) # True
print(hasattr(a , 'dr')) # FAlse
print(hasattr(a , 'm1')) # True
print(hasattr(a , 'm2')) # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False

#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) # ['m1']
print() # Blank  line
print()
print(dir(a)) # ['dr', 'm1', 'nr']

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
		x . talk() # 'Meow Meow Meow ....' \n 'Bhow Bhow Bhow ....' \n 'Mehar  Mehar  Mehar  ....'
	else:
		x . bark()



#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__) # {'x': 10, 'y': 20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname)) # 10  in 1st iteration , 20 in 2nd iteration and error in 3rd iteration
	except:
		print(F'Invalid  variable   name   :  {varname}') # Invalid variable name : z
		break

class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
# How  to  convert  dictionary  to  object  'e'  with  for  loop
e = Emp()
for x,y in dict.items():
        setattr(e, x, y) 
# How  to  print  object  'e'  with  for  loop
for x in dict.keys():
        print(getattr(e, x))    

import math

class Rat:

    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        self.test()

    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero.")
            self.den = int(input("Enter denominator: "))

    def __str__(self):
        return f"{self.num} / {self.den}"

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
            raise ValueError("Division by zero")
        self.num = a.num * b.den
        self.den = a.den * b.num
        self.simplify()

    def simplify(self):
        if self.num == 0:
            self.den = 1
            return
        gcd = math.gcd(abs(self.num), abs(self.den))
        self.num //= gcd
        self.den //= gcd

# End of the class
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

a.get()
b.get()

c.add(a, b)
d.sub(a, b)
e.mul(a, b)

try:
    f.div(a, b)
    print(f)
except ValueError:
    print('Division is not permitted')

print(f"Object 'a' ---> {a}")
print(f"Object 'b' ---> {b}")
print(f"Object 'c' ---> {c}")
print(f"Object 'd' ---> {d}")
print(f"Object 'e' ---> {e}")
print(f"Object 'f' ---> {f}")