# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))		    # 5
print(sys . getrefcount(c1()))		# 1
print(sys . getrefcount(352))		# 3
print(sys . getrefcount([10 , 20 , 15 , 18]))	# 1
print(sys . getrefcount(10.8))		# 3
print(sys . getrefcount({10 , 20 , 15 , 18}))	# 1
print(sys . getrefcount('Hyd'))		# 3
print(sys . getrefcount({10 : 20 , 30 : 40}))	# 1
print(sys . getrefcount((10 , 20 , 30 , 40)))	# 3

#====================================================================================================

# Find  outputs  (Home  work)
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()
print(t . __init__())
print(sys . getrefcount(t))
print(t . __del__())
print(sys . getrefcount(t))
print('Bye')

# Constructor : address of self
# Constructor : address of self
# None
# 2
# Destructor : address of self
# 25
# 2
# Bye
# 2
# Destructor : address of self

#====================================================================================================

# Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
# End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()
	print(a)
	print('Function  end')
	return   a
print('Program  Begin')
b = f1()
print(b)
print('Program  End')


# Program  Begin
# Function  Begin
# Object  is    created
# class and address of an object
# Function  end
# class and address of an object
# Program  End
# Object  is  lost

#====================================================================================================

#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
# End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
        return   a
print('Program  Begin')
f1()
print('Program  End')

# Program  Begin
# Function  begin
# Object  is    created
# Function  end
# Object  is  lost
# Program  End

#====================================================================================================

#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
# End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
print('Program  Begin')
b = f1()
print(b)
print('Program  End')


# Program  Begin
# Function  begin
# Object  is    created
# Function  end
# Object  is  lost
# None
# Program  End

#====================================================================================================

# Most  tricky  program  (Can  not  do  figure)
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()
print('program end')


# Program  begin
# c2  class  object  is  created
# c1  class  object  is  created
# End  of  c1  class constructor
# End  of  c2  class constructor
# program end
# c2  class  object  is  lost       (first in first out)
# c1  class  object  is  lost       (last in last out)

#====================================================================================================

'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

1) First  rational  number  --->  2 / 3
   Second  rational  number ---> 5 / 9
   What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
   What  is  the  difference  ?  --->  2 / 3 - 5 / 9 = (18 - 15) / 27 =  3 / 27 = 1 / 9
   What  is  the  product  ?  ---> 2 / 3 * 5 / 9 = 10 / 27 =  10 / 27
   What  is   the  division  ?  ---> 2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 = 18 / 15 = 6 / 5

2) First  rational  number  --->  2 / 3
   Second  rational  number ---> 0 / 9
   What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  difference  ?  --->  2 / 3 - 0 / 9 = (18 - 0) / 27 = 18 / 27 = 2 / 3
   What  is  the  product  ?  ---> 2 / 3 * 0 / 9 =  0 / 27 = 0 / 27  (simplification  is  not  required  becoz  numerator  is  0)
    What  is   the  division  ?  ---> 2 / 3 /  0 / 9 =  2 / 3 * 0 / 9  --->  Division  is  not  possible  becoz  b . nr  is  0

3) Modify  the  following  program  with  operator  overloding  methods

4) Leave  get() ,  test() , __str__()  and  simplify()  methods  unchanged
'''
import  math
class  rat:
	def  get(self):  #  Do  not  modify  the  method
		self . nr = int(input('Enter  numerator : '))
		self . dr = int(input('Enter  denominator : '))
		self . test()
	def  test(self): #  Do  not  modify  the  method
		while  self . dr == 0:
			self . dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
	def    __str__(self):  #  Do  not  modify  the  method
		return  F'{self . nr} / {self . dr}'
	def  add(self, a , b):  #  Modify  the  method
		self . nr = a . nr * b . dr + a . dr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	def  sub(self, a , b):   #  Modify  the  method
		self . nr = a . nr * b . dr - a . dr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	def  mul(self ,  a , b):   #  Modify  the  method
		self . nr = a . nr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	def  div(self, a , b):   #  Modify  the  method
		self . nr = a . nr * b . dr
		self . dr = a . dr * b . nr
		self . simplify()
	def   simplify(self):   #  Do  not  modify  the  method
		if self . nr != 0:
			g = math . gcd(self . nr, self . dr)
			self . nr = self . nr // g
			self . dr = self . dr // g
# End  of  the  class
#  Modify  the  following  statements
a = rat()
b = rat()
c = rat()
d = rat()
e = rat()
f = rat()
a . get()
b . get()
c . add(a , b)
d . sub(a , b)
e .  mul(a , b)
print('Sum :  ' , c)
print('Difference :  ' , d)
print('Product :  ' ,  e)
if b . nr != 0:
	f . div(a , b)
	print('Division  : ' , f)
else:
	print('Division is not permitted.')

#====================================================================================================

# Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')

# Destructor
# Hello

#====================================================================================================

# Is  10 + 20  a  recursion ?
class   c1:
	def  __add__(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)

# 30
# None

#====================================================================================================

# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)

# recursion error becoz cannot call class inside method. it call the method multiple times leads to recursion error.

#====================================================================================================

# Find  outputs
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __gt__(m , n):		
		print('__gt__ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)
b = c1(20)
print(a > b)
print(a < b)


'''
Object  'a'   --->  10  20

Object  'b'   --->  20  10
'''

# __gt__ method  :  10 20
# None
# __gt__ method  :  20 10
# None

#====================================================================================================

# Find  outputs  (Home work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ge__(m , n):
		print('__ge__ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b)
print(a <= b)  #  b >= a


'''
Object  'a'   --->  10  20

Object  'b'   --->  20  10
'''

# __ge__ method : 10 20
# False
# __ge__ method : 20 10
# True

#====================================================================================================

# Find  outputs (Home  work)
class   c1:
	def   __init__(self , y):
			self . x = y
	def    __eq__(m , n):
			print('__eq__ method  : ' , m . x , n . x)
			return  m . x == n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a == b)
print(a != b)  # not (a == b)

# __eq__ method  : 10 20 
# False
# __eq__ method  : 10 20
# True

#====================================================================================================

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
			self . x = y
	def    __eq__(m , n):
			print('__eq__ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)
print(a != b)
print(a . x !=  b . x)

# __eq__ method  : 25 25
# None
# __eq__ method  : 25 25
# True
# False

#====================================================================================================

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('__ne__ method :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(25)
b = c1(25)
print(a != b)
print(a == b)
print(a  is  b)


# __ne__ method : 25 25
# False
# False
# False

#====================================================================================================

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('__ne__ method  :  ' , m . x , n . x)
		return  m . x != n . x
# End  of  the  class
a = c1(10)
b = a
print(a != b)
print(a == b)

# __ne__ method  :  10 10
# False
# True

#====================================================================================================

#  Is  10 > 20  a  recursion ?
class  c1:
	def   __gt__(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b)

# recursion error

#====================================================================================================

# Find  outputs  (Home  work)
class  c1:
	def __init__(self , y):
		self . x = y
	def  __gt__(p , q):
		print('c1  class  __gt__  method : ' , p . x , q . x)
class  c2:
	def __init__(self , y):
		self . x = y
	def __gt__(p , q):
		print('c2  class  __gt__  method : ' , p . x , q . x)
# End  of  the  class
a = c1(10)
b = c1(20)
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b

# c1  class  __gt__  method : 10 20 
# c1  class  __gt__  method : 20 10
# c2  class  __gt__  method : 30 10
# c2  class  __gt__  method : 20 40 

#====================================================================================================

# Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  __init__(self):
		self . empno = 25
		self . hr = 250
	def __mul__(x , y):
		print('__mul__  method  of  class   c1')
		# return  hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('__mul__  method  of  class   c2')
		# return  number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1()
b = c2()
print(a * b)
print(b * a)

# __mul__  method  of  class   c1
# None
# __mul__  method  of  class   c2
# None

#====================================================================================================

# Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '__add__ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)
print('a + 7 : ' , a + 7)
# print(7 + a)
print('7 + 8 : ' , 7 + 8)
m = c2()
n = c2()
# print(m + n)
print('a + m : ' , a + m)
# print(m + a)

# a + b :  __add__ method  of  class   c1
# a + 7 :  __add__ method  of  class   c1
# 7 + 8 :  15
# a + m :  __add__ method  of  class   c1