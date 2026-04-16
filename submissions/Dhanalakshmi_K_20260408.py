'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
from triangles import triangle
t = triangle()
triangle.get(t)
triangle.test(t)#How  to  call  test()  method  in  another  way
print('Area : ',  triangle.area(t))#How  to  call  area()  method  in  another  way)
print('Perimeter: ',  triangle.peri(t))#How  to  call  peri()  method  in  another  way)


# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  students  import  student
s = student()
print(s . __dict__) 
s . get()
print(s . __dict__)  
s . compute()
print(s . __dict__) 
'''
Roll Number : 25
Student Name : Rama Rao
Gender : m
Total Marks : 155.0
Average : 51.67
Grade : Second class
25, Rama Rao, m, 155.0, 51.67, Second class
'''


'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  students  import  student
n = int(input("Enter number of students: "))
a = [student() for _ in range(n)] 
for i in range(n):
    a[i].get()
    a[i].compute()
for obj in a:
    print(obj.__dict__)




'''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
    What  is  the  difference  ?  --->  2 / 3 - 5 / 9 =  (18 - 15) / 27 = 3 / 27 = 1 / 9
    What  is  the  product  ?  --->  2 / 3 * 5 / 9 =  10 / 27 = 10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 = 2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 =  (18 - 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  product  ?  --->  2 / 3 * 0 / 9 =  0 / 27  =  0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  --->  2 / 3 /  0 / 9 =  2 / 3 * 9 / 0 =  18 / 0  ---> Division  is  not   permitted

3) When  is  simplification  needed ?  --->  When  numerator  is  non-zero
'''
import math

class Rat:
    def __init__(self):
        self.num = 0
        self.den = 1

    def get(self):
        self.num = int(input("Enter the numerator: "))
        self.den = int(input("Enter the denominator: "))
        self.test()

    def test(self):
        # Ask user to re-enter denom when denom is zero
        while self.den == 0:
            print("Denominator cannot be zero.")
            self.den = int(input("Please re-enter a non-zero denominator: "))

    def __str__(self):
        # Return values of object in the form of '2 / 3'
        return f"{self.num} / {self.den}"

    def add(self, a, b):
        # Formula: (n1*d2 + n2*d1) / (d1*d2)
        self.num = (a.num * b.den) + (b.num * a.den)
        self.den = a.den * b.den
        self.simplify()

    def sub(self, a, b):
        # Formula: (n1*d2 - n2*d1) / (d1*d2)
        self.num = (a.num * b.den) - (b.num * a.den)
        self.den = a.den * b.den
        self.simplify()

    def mul(self, a, b):
        # Formula: (n1*n2) / (d1*d2)
        self.num = a.num * b.num
        self.den = a.den * b.den
        self.simplify()

    def div(self, a, b):
        # Formula: (n1/d1) / (n2/d2) = (n1*d2) / (d1*n2)
        if b.num != 0:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()
            return True
        else:
            return False

    def simplify(self):
        # Only simplify if numerator is non-zero
        if self.num != 0:
            common = math.gcd(self.num, self.den)
            self.num //= common
            self.den //= common

# --- Main Execution ---

# Create 6 objects
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

# Read rational numbers
print("Rational Number 1:")
a.get()
print("\nRational Number 2:")
b.get()

# Perform Operations
c.add(a, b)
d.sub(a, b)
e.mul(a, b)

# Display Results
print("\n--- Results ---")
print(f"Sum: {c}")
print(f"Difference: {d}")
print(f"Product: {e}")

# Division Check
if f.div(a, b):
    print(f"Division: {f}")
else:
    print("Division: Not permitted (divisor numerator is zero)")


'''
Object  'a'  --->  

Object  'b'  --->  

Object  'c'  --->  

Object  'd'  --->  

Object  'e'  --->  

Object  'f'  --->  
'''



#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a))
'''
# ['_init_', 'reduce', etc.]
# ['dr', 'nr', '_init_', etc.]
'''


#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))
print(hasattr(a , 'dr'))
print(hasattr(a , 'm1'))
print(hasattr(a , 'm2'))
print(hasattr(Rat , 'm1'))
print(hasattr(Rat , 'm2'))
print(hasattr(Rat , 'nr'))
'''
True
False
True
False
True
False
False'''



# Object  'a'  --->


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
'''
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''



#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
'''
{'x':10,'y':20}
10
infinite loop
'''


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
e=Emp()
for key ,value in dict.items():
        setattr(e,key.lower(),value)
        #How  to  convert  dictionary  to  object  'e'  with  for  loop
for x in dict:
        print(f"{x}: {getattr(e, x.lower())}")#How  to  print  object  'e'  with  for  loop