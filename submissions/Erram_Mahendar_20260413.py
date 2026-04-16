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
'''
Program  Begin
Function  Begin
Object  is    created
tye and address of obj a
Function  end
Program  End
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
'''
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
'''
Program  Begin
Object  is    created
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
'''
Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end
circular loop
'''
# Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
		print('Destructor')
		global  b # error
		b = self
a = c1()
del  a
print('Hello')
'''
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
	
# Is  10 + 20  a  recursion ? No
class   c1:
	def  _add_(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b) # 30 

# Is  x + y  a  recursion  ?  (Home  work) yes
class   c1:
	def  _add_(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b) 

# Find  outputs
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _gt_(m , n):
		print('_gt_ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)  
b = c1(20)
print(a > b) #_gt_ method  : 10 20
print(a < b) #_gt_ method  : 20 10


'''
Object  'a'   --->   x=10

Object  'b'   ---> x=20
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
print(a >= b) # _ge_ method :  10 20
print(a <= b)  #  b >= a #  _ge_ method :  20 10


'''
Object  'a'   --->  x=10

Object  'b'   --->  x=20
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
print(a == b)  # _eq_ method  :  10 20 False
print(a != b)  # not (a == b)  _eq_ method  :  20 10  True

# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
			self . x = y
	def    _eq_(m , n):
			print('_eq_ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)  # _eq_ method  :  25 25  
print(a != b)  # _eq_ method  :  25 25 
print(a . x !=  b . x) # False

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
print(a != b) #_ne_ method :  25 25 False
print(a == b)  #_ne_ method :  25 25 True
print(a  is  b) #True

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
print(a != b) #  #_ne_ method :  10 10 False
print(a == b)  #_ne_ method :  10 10 True

#  Is  10 > 20  a  recursion ?
class  c1:
	def   _gt_(a , b):
		print(10 > 20)
		print(a > b)
a = c1() 
b = c1()
print(a > b)
'''
False
False...... inififnite'''

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
a > b # c1  class  _gt_  method : 10 20
a < b # c1  class  _gt_  method : 20 10
m = c2(30) 
n = c2(40)
a < m # c2  class  _gt_  method : 30 10
n < b # c1  class  _gt_  method : 20 40

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
		return  x . noh *  y.hr
# End of the class
a = c1()
b = c2()
print(a * b) # 2000
print(b * a) #  200

# Find  outputs  (Home  work)
class c1:
	def _add_(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)  # a + b : _add_ method  of  class   c1
print('a + 7 : ' , a + 7) # a + b : _add_ method  of  class   c1
print(7 + a) # error
print('7 + 8 : ' , 7 + 8) # 7+8 : 13
m = c2()
n = c2()
print(m + n) # error
print('a + m : ' , a + m) # a + b : _add_ method  of  class   c1
print(m + a) # error

# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     _init_(self , y):
		self . x = y
	def _add_(p , q):
		return  p.x + q.x 
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b) # Sum: 30 
print('Join : ' , m + n) # Join: 1020 


'''
Object  a  ---> 10

Object  b  ---> 20
 
Object  m  ---> '10'

Object  n  ---> '20'
'''