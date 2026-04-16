 # Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))#5
print(sys . getrefcount(c1())) #2
print(sys . getrefcount(352)) #2
print(sys . getrefcount([10 , 20 , 15 , 18])) #2
print(sys . getrefcount(10.8)) #2
print(sys . getrefcount({10 , 20 , 15 , 18})) #2
print(sys . getrefcount('Hyd')) #2
print(sys . getrefcount({10 : 20 , 30 : 40})) #2
print(sys . getrefcount((10 , 20 , 30 , 40))) #2
------------------------------------------------------------------------
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
t = Test()                             #Constructor : 1000
print(t . _init_())                    #None
print(sys . getrefcount(t))            #2       
print(t . _del_())                     #Destructor : 1000
print(sys . getrefcount(t))            #25
print('Bye')                           #2    #Bye     #Destructor : 1000
--------------------------------------------------------------------------
 # Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')          #Prodram Begin
	def  _del_(self):                               #Function Begin
		print('Object  is  lost')               #Object is created
# End  of  the  class                                   #<__main__.c1object add>
def    f1():                                            #Function end
	print('Function  Begin')                        #b points a
	a  =  c1()                                      #<__main__.c1object add>
	print(a)                                        #Program end
	print('Function  end')                          #Object is lost
	return   a
print('Program  Begin')
b = f1()
print(b)
print('Program  End')
-------------------------------------------------------------------------
 #  Tricky  program
# Find  outputs (Home  work)                         #Program Begin
class  c1:                                           #Function Begin
	def  _init_(self):                           #Object is Created
		print('Object  is    created')       #Function end
	def  _del_(self):                            #
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
--------------------------------------------------------------------------
 #  Tricky  program
# Find  outputs (Home  work)                     #Program Begin
class  c1:                                       #Function Begin
	def  _init_(self):                       #Object is created
		print('Object  is    created')   #Function end
	def  _del_(self):                        #Object is lost
		print('Object  is  lost')        #None
# End  of  the  class                            #Program end
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
print('Program  Begin')
b = f1()
print(b)
print('Program  End')
------------------------------------------------------------------------------
# Most  tricky  program  (Can  not  do  figure)
# Circular  reference (Home  work)                          #Program begin           
class   c1:                                                 #c2  class  object  is  created
	def   _init_(self , k):                             #c1  class  object  is  created
		print('c1  class  object  is  created')     #End of c1 class constructor
		self . b = k                                #End of c2 class constructor
		print('End  of  c1  class constructor')     #
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
#obj x--->a=c1(self)
#obj a--->b=k

------------------------------------------------------------------------------
 # Lucky  object
# Find  outputs (Home  work)                #Destructor
class   c1:                                 #b=a so ref is there cannot be removed
	def  _del_(self):                   #Hello
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')
---------------------------------------------------
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
	def    _str_(self):  #  Do  not  modify  the  method
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
c = rat()  #remove
d = rat()  #remove
e = rat()  #remove
f = rat()  #remove
a . get()
b . get()
c . add(a , b)  #c=a+b
d . sub(a , b)  #d=a-b
e .  mul(a , b) #e=a*b
print('Sum :  ' , c)
print('Difference :  ' , d)
print('Product :  ' ,  e)
if b . nr != 0:
	f . div(a , b)
	print('Division  : ' , f)
else:
	print('Division is not permitted.')
---------------------------------------------------------------------------
 # Is  10 + 20  a  recursion ?
class   c1:
	def  _add_(a , b):
			print(10 + 20)   #30
a = c1()                                 #None
b = c1()                                 #not recursion
print(a + b)
----------------------------------------------------------------------------
 # Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  _add_(a , b):         #yes x+y is recursion
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)
----------------------------------------------------------------------------
 # Find  outputs
class   c1:                                                 #__gt__ method : 10,20 #None
	def   _init_(self , y):                             #__ggt__method : 20,10 #None
		self . x = y
	def    _gt_(m , n):
		print('_gt_ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)
b = c1(20)
print(a > b)
print(a < b)


'''
Object  'a'   --->  x=10

Object  'b'   --->  x=20
'''
---------------------------------------------------------------------------
# Find  outputs  (Home work)
class   c1:
	def   _init_(self , y):                   #__ge__method : 10,20           
		self . x = y                      #False
	def    _ge_(m , n):                       #__ge__method : 20,10   #True
		print('_ge_ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b)
print(a <= b)  #  b >= a


'''
Object  'a'   --->  x=10

Object  'b'   --->  x=20
'''
----------------------------------------------------------------------------
 # Find  outputs (Home  work)
class   c1:                                        #__eq__method : 10,20
	def   _init_(self , y):                    #False
			self . x = y               #__eq__method : 10,20
	def    _eq_(m , n):                        #True
			print('_eq_ method  : ' , m . x , n . x)
			return  m . x == n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a == b)
print(a != b)  # not (a == b)
---------------------------------------------------------------------------
 # Find  outputs  (Home  work)
class   c1:                                  #__eq__method : 25,25
	def   _init_(self , y):             #None
			self . x = y        #__eq__method : 25,25
	def    _eq_(m , n):                 #False
			print('_eq_ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)
print(a != b)
print(a . x !=  b . x)
---------------------------------------------------------------------------
 # Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ne_(m , n):
		print('_ne_ method :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(25)
b = c1(25)
print(a != b) #__ne__method : 25,25   #False
print(a == b) #__ne__method : 25,25   #True
print(a  is  b)  #False
-------------------------------------------------------------------------
 # Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ne_(m , n):
		print('_ne_ method  :  ' , m . x , n . x)
		return  m . x != n . x
# End  of  the  class
a = c1(10)   
b = a
print(a != b)  #__ne__method : 10,10  #False
print(a == b)  #__ne__method :10,10   #True
-----------------------------------------------------------------------
 #  Is  10 > 20  a  recursion ?      #
class  c1:
	def   _gt_(a , b):
		print(10 > 20)  #False
		print(a > b)     #False  yes recursion
a = c1()
b = c1()
print(a > b)
---------------------------------------------------------------------
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
a = c1(10)
b = c1(20)
a > b   #c1 class __gt__method : 10,20  
a < b   #c1 class __gt__method :20,10   
m = c2(30)
n = c2(40)
a < m  #c2 class __gt__method : 30,10 
n < b  #c2 class __gt__method : 20,40 
-----------------------------------------------------------------------
 # Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  _init_(self):
		self . empno = 25
		self . hr = 250
	def _mul_(x , y):
		print('_mul_  method  of  class   c1')
		return  hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
class c2:
	def _init_(self):
		self . empno = 25
		self . noh = 8
	def _mul_(x , y):
		print('_mul_  method  of  class   c2')
		return  number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1()
b = c2()
print(a * b)  #__mul__method of class c1   #2000
print(b * a)  #__mul__method of class c2  #200
-----------------------------------------------------------------------
 # Find  outputs  (Home  work)
class c1:
	def _add_(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)
print('a + 7 : ' , a + 7)
print(7 + a)
print('7 + 8 : ' , 7 + 8)
m = c2()
n = c2()
print(m + n)
print('a + m : ' , a + m)
print(m + a)
------------------------------------------------------------------------
 # Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     _init_(self , y):
		self . x = y
	def _add_(p , q):
		return  sum  of  numbers  (or)  join  of  strings
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b)  #30
print('Join : ' , m + n)#1020


'''
Object  a  --->x=10

Object  b  --->x=20

Object  m  --->x='10'

Object  n  --->x='20'