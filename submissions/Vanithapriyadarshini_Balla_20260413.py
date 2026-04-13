# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))#1
print(sys . getrefcount(c1()))#3
print(sys . getrefcount(352))#1
print(sys . getrefcount([10 , 20 , 15 , 18]))#3
print(sys . getrefcount(10.8))#1
print(sys . getrefcount({10 , 20 , 15 , 18}))#1
print(sys . getrefcount('Hyd'))#3
print(sys . getrefcount({10 : 20 , 30 : 40}))#1
print(sys . getrefcount((10 , 20 , 30 , 40)))#2

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
t = Test()#Constructor  :  address of t 
print(t . __init__())#Constructor  : address of t    None
print(sys . getrefcount(t))#2
print(t . __del__())#Destructor  :  add of t     25
print(sys . getrefcount(t))# 2
print('Bye')#Bye    #Destructor  :  add of t 

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
print('Program  Begin')#Program  Begin
b = f1()# func begin   obj is created  atype and address   func end
print(b)# atype and address
print('Program  End')# program 
#end  destructor: addr of b

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
print('Program  Begin')# Program  Begin
f1()# Func begin   obj is created     func end     
print('Program  End')# prog end   obj lost

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
print('Program  Begin')# prog begin
b = f1()# func begin     obj is created    func end  
print(b)# None
print('Program  End')# prog end       destructor: obj lost

# Most  tricky  program  (Can  not  do  figure)
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class 
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')# prog begin
x = c2()# c2 class obj is created , c1  class  object  is  created, End  of  c1  class constructor, End  of  c2  class constructor
print('program end')#prog end

## c2 class obj is lost , c1 class obj is lost

# Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()# obj created
del  a# Destructor
print('Hello')#Hello

#Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects


# Is  10 + 20  a  recursion ?
class   c1:
	def  _add_(a , b):
			print(10 + 20)
a = c1()# obj created
b = c1()# one more obj is created
print(a + b)# error

# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  _add_(a , b):
		x = c1()# obj
		y = c1()# obj
		print(x + y)
a = c1()#obj is created
b = c1()#one more obj is created
print(a + b)

# Find  outputs
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __gt__(m , n):
		print('_gt_ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)# x=10, 
b = c1(20)# x=20,    _ gt_ method: 10 20
print(a > b)
print(a < b)


# Find  outputs  (Home work)
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ge_(m , n):
		print('_ge_ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)#x=10
b = c1(20)# x=20    10 20   20 10    true
print(a >= b)
print(a <= b)  #  b >= a

# Find  outputs (Home  work)
class   c1:
	def   _init_(self , y):
			self . x = y
	def    _eq_(m , n):
			print('_eq_ method  : ' , m . x , n . x)
			return  m . x == n . x
# End  of  the  class
a = c1(10)#x=10  _eq_method: 10 20 
b = c1(20)# x=20       
print(a == b)
print(a != b)  # not (a == b)

# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
			self . x = y
	def    _eq_(m , n):
			print('_eq_ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)#x=25  _eq_method : 25 
b = c1(25)#x=25  _eq_method : 25
print(a == b) #True
print(a != b)
print(a . x !=  b . x)


# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ne_(m , n):
		print('_ne_ method :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(25)# _ne_method : 25 
b = c1(25)# _ne_method : 25
print(a != b)#ture
print(a == b)# False
print(a  is  b)

# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):
		self . x = y
	def    _ne_(m , n):
		print('_ne_ method  :  ' , m . x , n . x)
		return  m . x != n . x
# End  of  the  class
a = c1(10)# x=10
b = a# x=10
print(a != b)# false
print(a == b)#True


#  Is  10 > 20  a  recursion ?
class  c1:
	def   _gt_(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()#Error
print(a > b)


# Find  outputs  (Home  work)
class  c1:
	def __init__(self , y):
		self . x = y
	def  __gt__(p , q):
		print('c1  class  _gt_  method : ' , p . x , q . x)
class  c2:
	def __init__(self , y):
		self . x = y
	def __gt__(p , q):
		print('c2  class  _gt_  method : ' , p . x , q . x)
# End  of  the  class
a = c1(10)#c1  class  _gt_  method :  10 20
b = c1(20)#c1  class  _gt_  method :  20 10
a > b
a < b
m = c2(30)#c2  class  _gt_  method :  30 10
n = c2(40)#c1  class  _gt_  method :  20 40
a < m
n < b\

# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     _init_(self , y):
		self . x = y
	def _add_(p , q):
		return  p+Q
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b)
print('Join : ' , m + n)