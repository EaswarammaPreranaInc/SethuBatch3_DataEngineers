# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1() # Object of class c1() is created
print(sys . getrefcount(b)) # 5
print(sys . getrefcount(c1())) # 1
print(sys . getrefcount(352)) # 3
print(sys . getrefcount([10 , 20 , 15 , 18])) # 1
print(sys . getrefcount(10.8)) # 3
print(sys . getrefcount({10 , 20 , 15 , 18})) # 1
print(sys . getrefcount('Hyd')) # 3
print(sys . getrefcount({10 : 20 , 30 : 40})) # 1
print(sys . getrefcount((10 , 20 , 30 , 40))) # 3

# Find  outputs  (Home  work)
import  sys
class  Test:
	def  _init_(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  _del_(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test() # Object of class Test is created
print(t . _init_()) # Constructor : Address of object t <nextline> None
print(sys . getrefcount(t)) # 2
print(t . _del_()) #  Destructor : Address of object t <nextline> 25
print(sys . getrefcount(t)) # 2
print('Bye') # Bye
# Destructor : Address of object t <nextline> 25

# Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created') 
	def  _del_(self):
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

''' Output:
Program Begin
Function Begin 
Object is created
<class '__main__.c1'> and Address of object a
Function end
<class '__main__.c1'> and Address of object a
Program End
Object  is  lost

'''

#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
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

'''Output:
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
Program  End

'''
#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
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

'''Output:
Program  Begin
Function  begin
Object  is  created
Function  end
Object  is  lost
None
Program  End
'''
# Most  tricky  program  (Can  not  do  figure)
# Circular  reference (Home  work)
class   c1:
	def   _init_(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   _del_(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  _init_(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  _del_(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()
print('program end')

''' Output:
Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end
c2  class  object  is  lost
c1  class  object  is  lost
'''
# Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')

''' Output:
Destructor
Hello

'''
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

4) Leave  get() ,  test() , _str_()  and  simplify()  methods  unchanged
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
	def  __str__(self):  #  Do  not  modify  the  method
		return  F'{self . nr} / {self . dr}'
	def  __add__(a , b):  #  Modify  the  method
		c = rat()
		c.nr = a . nr * b . dr + a . dr * b . nr
		c.dr = a . dr * b . dr
		c.simplify()
		return c
	def  __sub__(a , b):   #  Modify  the  method
		d = rat()
		d. nr = a . nr * b . dr - a . dr * b . nr
		d. dr = a . dr * b . dr
		d. simplify()
		return d
	def  __mul__(a , b):   #  Modify  the  method
		e = rat()
		e. nr = a . nr * b . nr
		e. dr = a . dr * b . dr
		e. simplify()
		return e
	def  __truediv__(a , b):   #  Modify  the  method
		f = rat()
		f. nr = a . nr * b . dr
		f. dr = a . dr * b . nr
		f. simplify()
		return f
	def   simplify(self):   #  Do  not  modify  the  method
		if self . nr != 0:
			g = math . gcd(self . nr, self . dr)
			self . nr = self . nr // g
			self . dr = self . dr // g
# End  of  the  class
a = rat()
b = rat()
a . get()
b . get()
print('Sum :  ' , a+b)
print('Difference :  ' , a-b)
print('Product :  ' ,  a*b)
if b.nr != 0:
	print('Division  : ' , a/b)
else:
	print('Division is not permitted.')

'''Outputs:
Enter  numerator :  2
Enter  denominator : 3
Enter  numerator : 5
Enter  denominator : 9
Sum :   11 / 9
Difference :   1 / 9
Product :   10 / 27
Division  :  6 / 5

Enter  numerator : 2
Enter  denominator : 3
Enter  numerator : 0
Enter  denominator : 9
Sum :   2 / 3
Difference :   2 / 3
Product :   0 / 27
Division is not permitted.
'''

# Is  10 + 20  a  recursion ?
class   c1:
	def  __add__(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b) # 30 <nextline> None

# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b) # Infinite recursion

# Find  outputs
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _gt_(m , n):
		print('_gt_ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)
b = c1(20)
print(a > b) # __gt__ method  :  10 20
print(a < b) # __gt__ method  :  20 10


'''
Object  'a'   --->  x = 10

Object  'b'   --->  x = 20
'''
# Find  outputs  (Home work)
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ge_(m , n):
		print('_ge_ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b) # __ge__ method :  10 20 <nextline> False
print(a <= b)  #  b >= a # __ge__ method : 20 10  <nextline> True


'''
Object  'a'   --->  x = 10

Object  'b'   --->  x = 20
'''
# Find  outputs (Home  work)
class   c1:
	def   _init_(self , y):
			self . x = y
	def    _eq_(m , n):
			print('_eq_ method  : ' , m . x , n . x)
			return  m . x == n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a == b) # __eq__ method  : 10 20 <nextline> False
print(a != b)  # not (a == b) # __eq__ method  : 10 20 <nextline> True

# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
			self . x = y
	def    _eq_(m , n):
			print('_eq_ method  :  ' , m . x , n . x)
#end of the class
a = c1(25) # Object of class c1 is created
b = c1(25) # Object of class c1 is created
print(a == b) # __eq__ method  :  25 25 <nextline> None
print(a != b) # __eq__ method  :  25 25 <nextline> True
print(a . x !=  b . x) # False

# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ne_(m , n):
		print('_ne_ method :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(25) # Object of class c1 is created
b = c1(25) # Object of class c1 is created
print(a != b) # __ne__ method :  25 25 <nextline> False
print(a == b) # __ne__ method :  25 25 <nextline> True
print(a  is  b) # True

# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ne_(m , n):
		print('_ne_ method  :  ' , m . x , n . x)
		return  m . x != n . x
# End  of  the  class
a = c1(10) # Object of class c1 is created
b = a # Reference b points to object a
print(a != b) # __ne__ method  : 10 10 <nextline> False 
print(a == b) # True

#  Is  10 > 20  a  recursion ?
class  c1:
	def   _gt_(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b) # Infinite times False is printed and infinite recursion

# Find  outputs  (Home  work)
class  c1:
	def _init_(self , y):
		self . x = y
	def  _gt_(p , q):
		print('c1  class  _gt_  method : ' , p . x , q . x)
class  c2:
	def _init_(self , y):
		self . x = y
	def _gt_(p , q):
		print('c2  class  _gt_  method : ' , p . x , q . x)
# End  of  the  class
a = c1(10) # Object of class c1 is created
b = c1(20) # Object of class c1 is created
a > b # c1  class  __gt__  method : 10 20
a < b # c1  class  __gt__  method : 20 10
m = c2(30) # Object of class c2 is created
n = c2(40) # Object of class c2 is created
a < m # c2  class  __gt__  method :  30 10
n < b # c1  class  __gt__  method :  20 40 

# Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  _init_(self):
		self . empno = 25
		self . hr = 250
	def _mul_(x , y):
		print('_mul_  method  of  class   c1')
		return  x.hr *  y.noh
class c2:
	def _init_(self):
		self . empno = 25
		self . noh = 8
	def _mul_(x , y):
		print('_mul_  method  of  class   c2')
		return  x.noh *  y.hr
# End of the class
a = c1() # Object of class c1 is created
b = c2() # Object of class c2 is created
print(a * b) # _mul_  method  of  class   c1 <nextline> 2000
print(b * a) # _mul_  method  of  class   c2 <nextline> 2000

# Find  outputs  (Home  work)
class c1:
	def _add_(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1() # Object of class c1 is created
b = c1() # Object of class c1 is created
print('a + b : ' , a + b) # a + b : _add_ method  of  class   c1
print('a + 7 : ' , a + 7) # a + 7 :  _add_ method  of  class   c1
print(7 + a) # Error cannot add a integer and a class object
print('7 + 8 : ' , 7 + 8) # 7 + 8 : 15
m = c2() # Object of class c2 is created
n = c2() # Object of class c2 is created
print(m + n) # Error because addition cannot be possible between two c2 class objects
print('a + m : ' , a + m) # a + m : _add_ method  of  class   c1
print(m + a) # Error because addition is not possible between c2 and c1 class objects

# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     _init_(self , y):
		self . x = y
	def _add_(p , q):
		return  p.x + q.x
#end of the class
a = c1(10) # Object of class c1 is created
b = c1(20) # Object of class c1 is created
m = c1('10') # Object of class c1 is created
n = c1('20') # Object of class c1 is created
print('Sum : ' , a + b) # Sum : 30
print('Join : ' , m + n) # Join : 1020


'''
Object  a  ---> x = 10

Object  b  ---> x = 20

Object  m  ---> x = '10'

Object  n  ---> x = '20'
'''