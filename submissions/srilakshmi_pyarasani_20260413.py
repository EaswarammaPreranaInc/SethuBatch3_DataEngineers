A) outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))#5
print(sys . getrefcount(c1()))#2
print(sys . getrefcount(352))#2
print(sys . getrefcount([10 , 20 , 15 , 18]))#2
print(sys . getrefcount(10.8))#2
print(sys . getrefcount({10 , 20 , 15 , 18}))#2
print(sys . getrefcount('Hyd'))#2
print(sys . getrefcount({10 : 20 , 30 : 40}))#2
print(sys . getrefcount((10 , 20 , 30 , 40)))#2

B) outputs  
import  sys
class  Test:
	def  _init_(self):
		print('Constructor  :  ' , id(self))
		return    None 
	def  _del_(self):
		print('Destructor  :  ' , id(self))
		return  25 
# End  of  the  class
t = Test()
print(t . _init_())#Constructor : Address of object
		    None
print(sys . getrefcount(t))#2
print(t . _del_())#Destructor : Address of object
		   25
print(sys . getrefcount(t))#2
print('Bye')#Bye

C) Tricky  program
 outputs 
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
#Program Begin
Function Begin 
Object is created
<class '__main__.c1'> and Address of object a
Function end
<class '__main__.c1'> and Address of object a
Program End
Object  is  lost

D) Tricky  program
#outputs 
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
#Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
Program  End

E) Tricky  program
# outputs
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
#Program  Begin
Function  begin
Object  is  created
Function  end
Object  is  lost
None
Program  End

F) Most  tricky  program  (Can  not  do  figure)
# Circular  reference 
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
#Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end
c2  class  object  is  lost
c1  class  object  is  lost


G) Lucky  object
#outputs
class   c1:
	def  __del__(self):
		print('Destructor')#Destructor
		global  b
		b = self
a = c1()
del  a
print('Hello')#Hello

'''
H) Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

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
#Enter  numerator :  2
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


I) Is  10 + 20  a  recursion ?
class   c1:
	def  _add_(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)#30
	     None

J) Is  x + y  a  recursion  ?  #Yes
class   c1:
	def  _add_(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)

K) outputs
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _gt_(m , n):
		print('_gt_ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)
b = c1(20)
print(a > b)# __gt__ method  :  10 20
print(a < b)# __gt__ method  :  20 10


'''
Object  'a'   --->  x =10

Object  'b'   --->  x =20
'''
L) outputs  
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ge_(m , n):
		print('_ge_ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b)# __ge__ method :  10 20 <nextline> False
print(a <= b)  # b >= a# __ge__ method :  20 10 <nextline> True


'''
Object  'a'   --->  x = 10

Object  'b'   --->  x = 20
'''
M) outputs 
class   c1:
	def   _init_(self , y):
			self . x = y
	def    _eq_(m , n):
			print('_eq_ method  : ' , m . x , n . x)
			return  m . x == n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a == b)# __eq__ method  : 10 20 <nextline> False
print(a != b)  # not (a == b) # __eq__ method  : 10 20 <nextline> True

N) outputs  
class   c1:
	def   _init_(self , y):
			self . x = y
	def    _eq_(m , n):
			print('_eq_ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b) # __eq__ method  :  25 25 <nextline> None
print(a != b)# __eq__ method  :  25 25 <nextline> True
print(a . x !=  b . x) #False

O) outputs  
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ne_(m , n):
		print('_ne_ method :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(25)
b = c1(25)
print(a != b)#False
print(a == b)#True
print(a  is  b)#True

P) outputs  
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ne_(m , n):
		print('_ne_ method  :  ' , m . x , n . x)
		return  m . x != n . x
# End  of  the  class
a = c1(10)
b = a
print(a != b)#False
print(a == b)#True

Q) Is  10 > 20  a  recursion ?
class  c1:
	def   _gt_(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b)# False False..........

R) outputs  
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
a > b# c1  class  __gt__  method : 10 20
a < b # c1  class  __gt__  method : 20 10
m = c2(30)
n = c2(40)
a < m# c2  class  __gt__  method :  30 10
n < b# c1  class  __gt__  method :  20 40 

S) Overload  *  operator  to  multiply  two  different  class  objects
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
print(a * b) # _mul_  method  of  class   c1 
                2000
print(b * a) # _mul_  method  of  class   c2
                2000


T) outputs 
class c1:
	def _add_(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)# a + b : _add_ method  of  class   c1
print('a + 7 : ' , a + 7)# a + 7 :  _add_ method  of  class   c1
print(7 + a)#Error because it is not permitted
print('7 + 8 : ' , 7 + 8)# 7 + 8 : 15
m = c2()
n = c2()
print(m + n)#Error because it is not permitted
print('a + m : ' , a + m)# a + m : _add_ method  of  class   c1
print(m + a)#Error because it is not permitted

U) Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
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
print('Sum : ' , a + b)#sum : 30 
print('Join : ' , m + n)#Join : 1020


'''
Object  a  ---> x = 10

Object  b  ---> y = 20

Object  m  ---> x = 10(str)

Object  n  ---> y = 20(str)
'''