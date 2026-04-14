'''
=


# Is  10 + 20  a  recursion ?
class   c1:
	def  _add_(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)

#no output:30<next line>none





 # Is  x + y  a  recursion  ?  (Home  work) #yes recursion
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
	def   __init__(self , y):
		self . x = y
	def    __gt__(m , n):
		print('_gt_ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)
b = c1(20)
print(a > b)
print(a < b)

_gt_ method  :   10 20
None
_gt_ method  :   20 10
None




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
print(a >= b)
print(a <= b)  #  b >= a
'''_ge_ method :   10 20
False
_ge_ method :   20 10
True'''




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
print(a == b)
print(a != b)  # not (a == b)

'''_eq_ method  :  10 20
False
_eq_ method  :  10 20
True
'''





# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
			self . x = y
	def    _eq_(m , n):
			print('_eq_ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)
print(a != b)
print(a . x !=  b . x)

'''
_eq_ method  :   25 25
None
_eq_ method  :   25 25
True
False
'''







# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('_ne_ method :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(25)
b = c1(25)
print(a != b)
print(a == b)
print(a  is  b)
'''_ne_ method :   25 25
False
False
False
'''







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
print(a != b)
print(a == b)
'''
_ne_ method  :   10 10
False
True
'''




#  Is  10 > 20  a  recursion ?
class  c1:
	def   _gt_(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b)
#error




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
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b
#error






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
print(a * b)
print(b * a)

#error






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
'''
a + b :  _add_ method  of  class   c1
a + 7 :  _add_ method  of  class   c1
ERROR!
'''








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
print('Sum : ' , a + b)
print('Join : ' , m + n)

#error


