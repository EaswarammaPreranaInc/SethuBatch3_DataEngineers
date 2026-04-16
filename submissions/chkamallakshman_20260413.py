
# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b)) # 4+1 = 5
print(sys . getrefcount(c1())) # 
print(sys . getrefcount(352)) # 1
print(sys . getrefcount([10 , 20 , 15 , 18])) # 1
print(sys . getrefcount(10.8)) # 1
print(sys . getrefcount({10 , 20 , 15 , 18}))
print(sys . getrefcount('Hyd'))
print(sys . getrefcount({10 : 20 , 30 : 40}))  # 1
print(sys . getrefcount((10 , 20 , 30 , 40))) # 1






# Find  outputs  (Home  work)
import  sys
class  Test:
	def  _init_(self):
		print('Constructor  :  ' , id(self)) # Constructor : Address
		return    None
	def  _del_(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()
print(t . _init_())
print(sys . getrefcount(t)) # 2
print(t . _del_())
print(sys . getrefcount(t))
print('Bye')







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











# Is  10 + 20  a  recursion ?
class   c1:
	def  _add_(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)







# Is  x + y  a  recursion  ?  (Home  work)
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
print(a > b)
print(a < b)


'''
Object  'a'   --->  

Object  'b'   --->  
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
print(a >= b)
print(a <= b)  #  b >= a


'''
Object  'a'   --->  

Object  'b'   --->  
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
print(a == b)
print(a != b)  # not (a == b)





# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
			self . x = y
	def    _eq_(m , n):
			print('_eq_ method  :  ' , m . x , n . x) # _eq_ method  :   25 25
#end of the class
a = c1(25)
b = c1(25)
print(a == b) # True
print(a != b) # True 
print(a . x !=  b . x) # FAlse




# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ne_(m , n):
		print('_ne_ method :  ' , m . x , n . x) # _ne_ method :   25 25
		return  m . x != n . x
#end of the class
a = c1(25)
b = c1(25)
print(a != b) # False
print(a == b) # False
print(a  is  b) # False 
 





# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ne_(m , n):
		print('_ne_ method  :  ' , m . x , n . x) # _ne_ method  :   10 10
		return  m . x != n . x
# End  of  the  class
a = c1(10)
b = a
print(a != b) # False
print(a == b) # True





#  Is  10 > 20  a  recursion ?
class  c1:
	def   _gt_(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b) # False






# Find  outputs  (Home  work)
class  c1:
	def _init_(self , y):
		self . x = y
	def  _gt_(p , q):
		print('c1  class  _gt_  method : ' , p . x , q . x) # c1  class  _gt_  method :  10 20
class  c2:
	def _init_(self , y):
		self . x = y
	def _gt_(p , q):
		print('c2  class  _gt_  method : ' , p . x , q . x) # c1  class  _gt_  method :  20 40
# End  of  the  class
a = c1(10)
b = c1(20)
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b






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
print(a * b) # _mul_  method  of  class   c1 200
print(b * a) # _mul_  method  of  class   c2 200








# Find  outputs  (Home  work)
class c1:
	def _add_(x , y):
		return '_add_ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)  # a + b :  _add_ method  of  class   c1
print('a + 7 : ' , a + 7)
print(7 + a) #Error
print('7 + 8 : ' , 7 + 8) # 7 + 8 :  15
m = c2()
n = c2()
print(m + n) 
print('a + m : ' , a + m)
print(m + a)







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


'''
Object  a  --->

Object  b  --->

Object  m  --->

Object  n  --->
'''