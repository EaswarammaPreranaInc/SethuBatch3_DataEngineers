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
import  math
class  Rat:
	def  get(self):
		How  to  read  numerator  
		How  to  read  denominator 
		How  to  call  test()  method
	def  test(self):
		Ask  user  to  reenter  denom  when  denom  is  zero
	def    _str_(self):
			 return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		How  to  add  objects  'a'  and  'b' and  store  results  in  object  
		How  to  simplify  object  
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		How  to  subtract  objects  'a'  and  'b' and  store  results  in  object 
		How  to  simplify  object  
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  
		How  to  simplify  object 
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		How  to  divide  objects  'a'  and  'b' and  store  results  in  object  
		How  to  simplify  object 
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
			How  to  find  gcd  of  numerator  and   denominator
			How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
How  to  create  6  objects  a , b , c , d , e , f
How  to  read  rational  number  into  object  'a'
How to  read  rational  number  into  object  'b'
How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
How  to  print  object   'c'
How  to  print  object   'd'
How  to  print  object   'e'
if  ???
	How  to  print  object  'f
else:
	print('Division  is  not  permitted')


'''
Object  'a'  --->  

Object  'b'  --->  

Object  'c'  --->  

Object  'd'  --->  

Object  'e'  --->  

Object  'f'  --->  
'''

import math

class Rat:
    
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        self.test()   # validate denominator
    
    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero. Re-enter:")
            self.den = int(input("Enter denominator: "))
    
    def __str__(self):
        return f"{self.num} / {self.den}"
    
    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        if self.num != 0:
            self.simplify()
    
    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        if self.num != 0:
            self.simplify()
    
    def mul(self, a, b):
        self.num = a.num * b.num
        self.den = a.den * b.den
        if self.num != 0:
            self.simplify()
    
    def div(self, a, b):
        if b.num == 0:
            self.den = 0   # mark invalid division
            return
        self.num = a.num * b.den
        self.den = a.den * b.num
        if self.num != 0:
            self.simplify()
    
    def simplify(self):
        gcd = math.gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd


# -------- Main Program --------

# create objects
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

# input
print("Enter first rational number:")
a.get()

print("Enter second rational number:")
b.get()

# operations
c.add(a, b)
d.sub(a, b)
e.mul(a, b)
f.div(a, b)

#----------------------------------------------------------------------------------
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  prog9a  import  student
How  to  read  number  of  students  into   variable  'n'
How  to  store  'n'  student  class  objects   in  list  'a'
How  to   read  each  student  data  into   the  object  held  by  the  list
How  to   store  results  in   each  object  held  by  the  list
How  to   print  each  object  held  by  the  list

# import student class from prog9a
from prog9a import student

# read number of students
n = int(input("Enter number of students: "))

# create empty list
a = []

# create 'n' objects and store in list
for i in range(n):
    s = student()   # create object
    a.append(s)     # store in list

# read data into each object
for i in range(n):
    print(f"\nEnter details of student {i+1}:")
    a[i].get()      # read input
    a[i].compute()  # calculate total, average, grade (assuming method name)

# print all student details
print("\n----- Student Details -----")
for i in range(n):
    print(a[i])     # calls __str__ method

#FIND OUT PUT
class Rat:
    def m1():
        pass

a = Rat()
a.nr = 22
print(hasattr(a , 'nr'))   # True
print(hasattr(a , 'dr'))   # False
print(hasattr(a , 'm1'))   # True
print(hasattr(a , 'm2'))   # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False


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

OUTPUT
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
  
FIND OUTPUT
class Emp:
    pass
# End of the class

# given dictionary
d = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}

# create object
e = Emp()

# convert dictionary → object
for key, value in d.items():
    setattr(e, key, value)

# print object using getattr()
for key in d.keys():
    print(key, "=", getattr(e, key))