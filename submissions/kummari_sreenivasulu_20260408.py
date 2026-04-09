# (Home  work)
# Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
# i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

# Hint:  Use  setattr()  and  getattr()  functions

class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
# How  to  convert  dictionary  to  object  'e'  with  for  loop
# How  to  print  object  'e'  with  for  loop

# output : 

class Emp:
    pass
# End of the class

# Given dictionary
data = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}

# Create object
e = Emp()

# Convert dictionary to object using for loop
for key, value in data.items():
    setattr(e, key, value)

# Print object values using for loop
for key in data.keys():
    print(key, "=", getattr(e, key))


#-----------------------------------------------------------------------

# 2 . #  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . _dict_)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break

# output : 
'''
{'x': 10, 'y': 20}
10
10
20
Invalid variable name : z
'''

#-------------------------------------------------------------------------

# 3 . # Find  outputs  (Home  work)
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


# output : 
'''
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''

#---------------------------------------------------------------------

# 4 . #  Find  outputs  (Home  work)
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


# Object  'a'  --->


# output : 
'''
True
False
True
False
True
False
False
'''
# -------------------------------------------------------------------------

# 5 . #  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a))


# output : 
'''
[... all built-in methods ..., 'm1']

[... all built-in methods ..., 'dr', 'm1', 'nr']
'''

# ----------------------------------------------------------------------

# 6 . '''
# Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

# 1) 1st  rational  number  --->  2 / 3
#     2nd  rational  number  --->   5 / 9
#     What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
#     What  is  the  difference  ?  --->  2 / 3 - 5 / 9 =  (18 - 15) / 27 = 3 / 27 = 1 / 9
#     What  is  the  product  ?  --->  2 / 3 * 5 / 9 =  10 / 27 = 10 / 27
#     What  is   the  division  ?  --->  2 / 3 /  5 / 9 = 2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division

# 2) 1st  rational  number  --->  2 / 3
#     2nd  rational  number  --->   0 / 9
#     What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 =  2 / 3
#     What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 =  (18 - 0) / 27 =  18 / 27 =  2 / 3
#     What  is  the  product  ?  --->  2 / 3 * 0 / 9 =  0 / 27  =  0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
#     What  is   the  division  ?  --->  2 / 3 /  0 / 9 =  2 / 3 * 9 / 0 =  18 / 0  ---> Division  is  not   permitted

# 3) When  is  simplification  needed ?  --->  When  numerator  is  non-zero
'''
import  math
class  Rat:
	def  get(self):
		How  to  read  numerator  
		How  to  read  denominator 
		How  to  call  test()  method
	def  test(self):
		Ask  user  to  reenter  denom  when  denom  is  zero
	def    __str__(self):
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


# output : 

import math

class Rat:
    
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        self.test()

    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero. Re-enter:")
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
        
        # simplify only if numerator is not zero
        if self.num != 0:
            self.simplify()

    def div(self, a, b):
        if b.num == 0:
            return False
        self.num = a.num * b.den
        self.den = a.den * b.num
        self.simplify()
        return True

    def simplify(self):
        if self.num != 0:
            g = math.gcd(self.num, self.den)
            self.num //= g
            self.den //= g


# ---------------- MAIN PROGRAM ----------------

# Create objects
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

# Read inputs
print("Enter 1st rational number:")
a.get()

print("Enter 2nd rational number:")
b.get()

# Perform operations
c.add(a, b)
d.sub(a, b)
e.mul(a, b)
result = f.div(a, b)

# Print results
print("\nObject a --->", a)
print("Object b --->", b)
print("Object c (Sum) --->", c)
print("Object d (Difference) --->", d)
print("Object e (Product) --->", e)

if result:
    print("Object f (Division) --->", f)
else:
    print("Division is not permitted")


# ------------------------------------------------------------

# 7 . Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  prog9a  import  student
How  to  read  number  of  students  into   variable  'n'
How  to  store  'n'  student  class  objects   in  list  'a'
How  to   read  each  student  data  into   the  object  held  by  the  list
How  to   store  results  in   each  object  held  by  the  list
How  to   print  each  object  held  by  the  list


# output : 


from prog9a import student

# Read number of students
n = int(input("Enter number of students: "))

# Create empty list
a = []

# Create 'n' student objects and store in list
for i in range(n):
    s = student()     
    a.append(s)    

# Read data into each object
for i in range(n):
    print(f"\nEnter details of student {i+1}:")
    a[i].get()        

# Store results (like total, avg, grade etc.)
for i in range(n):
    a[i].compute()    

# Print all student objects
print("\nStudent Details:")
for i in range(n):
    print(a[i])        


#--------------------------------------------------------------------------

# 8 . # What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . _dict_)
s . get()
print(s . _dict_)
s . compute()
print(s . _dict_)

# output : 
{}

# --------------------------------------------------------------

# 9 .Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
How  to  create  triangle  object
How  to  call  get()  method  in  another  way
How  to  call  test()  method  in  another  way
print('Area : ',  How  to  call  area()  method  in  another  way)
print('Perimeter: ',  How  to  call  peri()  method  in  another  way)

# output : 

from prog5a import triangle

# Create object
t = triangle()

triangle.get(t)
triangle.test(t)

print("Area :", triangle.area(t))
print("Perimeter :", triangle.peri(t))