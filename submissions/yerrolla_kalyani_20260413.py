# Find  outputs
import   sys
class   c1:
        pass

# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))#5
print(sys . getrefcount(c1()))#1
print(sys . getrefcount(352))#unpredictable as 352 is immutable obj and reusable object
print(sys . getrefcount([10 , 20 , 15 , 18]))#1
print(sys . getrefcount(10.8))#unpredictable as 10.8 is immutable obj and reusable object
print(sys . getrefcount({10 , 20 , 15 , 18}))#1
print(sys . getrefcount('Hyd'))#unprdictable 
print(sys . getrefcount({10 : 20 , 30 : 40}))#1
print(sys . getrefcount((10 , 20 , 30 , 40)))#unpredictable 

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
print(t . __init__())#Constructor  :  ' , id(self)<nxt> None
print(sys . getrefcount(t))#2
print(t . __del__())#Destructor  :  ' , id(self)<nxt>25
print(sys . getrefcount(t))#2
print('Bye')#Bye<nxt>Destructor  :  ' , id(self)#


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
	print(a)#__str__() of obj class which returns type and address of the object 
	print('Function  end')
	return   a
print('Program  Begin')#Program  Begin
b = f1()#Function  Begin<nxt>Object  is    created<nxt> type and address of onject a <nxt>Function  end           f1() return a which is reference b is pointing a where a is pointing to c1() i.e.b=a 
print(b)#type and address of the object b  ,i.e. <__main__.c1 object  at address >
print('Program  End')#Program  End  <nxt>  Object  is  lost  



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
print('Program  Begin')#Program  Begin
f1()#Function  begin<nxt>Object  is    created<nxt>Function  end <nxt> Object  is  lost
print('Program  End')#Program  End




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
		#Object  is  lost as end of the class 
print('Program  Begin')#Program  Begin
b = f1()#Function  begin<nx>Object  is    created<nxt>Function  end <nxt>Object  is  lost  (b=None)
print(b)#None
print('Program  End')#Program  End


# Most  tricky  program  (Can  not  do  figure)
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k):#a,x
		print('c1  class  object  is  created')
		self . b = k#a.b=x a.b=x
		print('End  of  c1  class constructor')
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created')
		self . a = c1(self)#x.a=c1(x),a.a=c1(a)
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')#Program  begin
x = c2()#c2  class  object  is  created<nxt>c1  class  object  is  created<nxt>End  of  c1  class constructor <nxt> End  of  c2  class constructor
print('program end')#program end<nxt>c1 class  object  is  lost<nxt>c2  class  object  is  lost


# Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self#b=a 
a = c1()
del  a#Destructor<nxt>
print('Hello')#Hello  <nxt> when prog want ot terminate 

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
	def    __str__(self):  #  Do  not  modify  the  method
		return  F'{self . nr} / {self . dr}'
	def  __add__(self,value):  #  Modify  the  method
		r=rat()
		r . nr = self. nr * value . dr +self . dr * value . nr
		r  . dr = self. dr * value . dr
		r . simplify()
		return r 
	def  __sub__(self,value):   #  Modify  the  method
		r=rat()
        r . nr = self . nr * value . dr - self . dr * value . nr
		r . dr = self . dr * value . dr
		r. simplify()
	    return r 
	def  __mul__(self ,value):   #  Modify  the  method
		r=rat()
        r . nr = a . self * b . nr
		r . dr = a . dr * b . dr
		r . simplify()
	    return r 
	def  __truediv__(self, value):   #  Modify  the  method
		if value.nr==0:
			r=rat()
		r . nr = a . nr * b . dr
		r . dr = a . dr * b . nr
		r . simplify()
		return r
	def   simplify(self):   #  Do  not  modify  the  method
		if self . nr != 0:
			g = math . gcd(self . nr, self . dr)
			self . nr = self . nr // g
			self . dr = self . dr // g
# End  of  the  class
#  Modify  the  following  statements
a = rat()
b = rat()
a.get()
b.get()

print('Sum :  ' ,a+b )
print('Difference :  ' , a-b)
print('Product :  ' ,  a*b)
if a/b:
	
	print('Division  : ' a/b )
else:
	print('Division is not permitted.')


# Is  10 + 20  a  recursion ?no it prints 20 as the the 1st values is int so int class __add__()method is executed and print 30 and return None to function
class   c1:
	def  __add__(a , b):
			print(10 + 20)#30 
a = c1()
b = c1()
print(a + b)#30 <nxt>None


# Is  x + y  a  recursion  ? yes here x+y is a recurcive call of __add__(a,b) x and y are passed to formal parameters (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)#recursive call to __add__(x,y)
a = c1()
b = c1()
print(a + b)


# Find  outputs
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __gt__(m , n):
		print('__gt__ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)
b = c1(20)
print(a > b)#__gt__ method  :10 20<nxt>None
print(a < b)#__gt__ method  :20 10<nxt>None


'''
Object  'a'   --->  x=10

Object  'b'   --->  x=20
'''

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
print(a >= b)#__ge__ method :10 20# False
print(a <= b)  #  b >= a #__ge__ method :20 10<nxt>  True 


'''
Object  'a'   ---> x=10 

Object  'b'   --->  x=20
'''


#Find  outputs (Home  work)
class   c1:
	def   __init__(self , y):
			self . x = y
	def    __eq__(m , n):
			print('__eq__ method  : ' , m . x , n . x)
			return  m . x == n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a == b)#__eq__ method  :10 20 <nxt >True
print(a != b)  # __eq__ method  : 10  20  <nxt> False


 # Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
			self . x = y 
	def    __eq__(m , n):
			print('__eq__ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)#__eq__ method  :25 25 <nxt>None
print(a != b)#__eq__ method  : 25 25<nxt> None
print(a . x !=  b . x) #False

# obj a---------> x=25
# obj b------------>x=25



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
print(a != b)#__ne__ method :  25 25<nxt> False
print(a == b)#True
print(a  is  b)#True

# obj a--->x=25
# obj b--->x=25


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
print(a != b)#__ne__ method  : 10 10  <nxt> False
print(a == b)#True

# obj  a---->x=10
# obj b-->x=10


# Is  10 > 20  a  recursion ? no it is not a recursive call ,as the a 10 and 20  values they not calling __gt__(a,b)
class  c1:
	def   __gt__(a , b):
		print(10 > 20)#False
		print(a > b)# here it causes the recursive call 
a = c1()
b = c1()
print(a > b)



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
a > b#c1  class  _gt_  method :10 20,nxt> None
a < b#c1  class  _gt_  method : 20 10,nxt> None
m = c2(30)
n = c2(40)
a < m # c2  class  __gt__  method : 30 10 
n < b#c2  class  __gt__  method :   20 40 

# obj a->x=10
# obj b ->x=20
# obj m->x=30
# obj n ->x=40


 # Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  __init__(self):
		self . empno = 25
		self . hr = 250
	def __mul__(x , y):
		print('__mul__  method  of  class   c1')
		return  hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('__mul__  method  of  class   c2')
		return  number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1()
b = c2()
print(a * b)#
print(b * a)#

# obj a ---->empno=25 ,hr =250
# obj a ---->empno=25 ,non =250


 # Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '__add__ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)#a + b : __add__ method  of  class   c1'
print('a + 7 : ' , a + 7)#a + 7 :__add__ method  of  class   c1'
print(7 + a)#error
print('7 + 8 : ' , 7 + 8)#7 + 8 : 15 
m = c2()
n = c2()
print(m + n)#error no __add__ method in c2 class 
print('a + m : ' , a + m)#a + m : __add__ method  of  class   c1'
print(m + a)#error 1st operand is c2 obj where no __add__ method in c2 class




# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     __init__(self , y):
		self . x = y
	def __add__(p , q):
		return  sum  of  numbers  (or)  join  of  strings
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b)#error return  stmt should have quotes "   " in this case they are missing here so error 
print('Join : ' , m + n)#error return  stmt should have quotes "   " in this case they are missing here so error


'''
Object  a  --->x=10

Object  b  --->x=10

Object  m  --->x=10

Object  n  --->x=10
'''

