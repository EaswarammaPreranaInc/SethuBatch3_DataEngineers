#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
# End  of  the  class
x = parent()
x . m1()#Overridden  Method
x = child()
x . m1()#Overriding  Method


# Find  outputs  (Home  work)
class  parent:
	def  marriage(self):
		print('Arranged Marriage')
	def  property(self):
		print('One  Crore')
	def  study(self):
		print('Studies only' , end = '\t')
class  child(parent):
	def  marriage(self):
		print('Love Marriage')
	def  study(self):
		super() . study()
		print(' + Entertainment')
# End  of  the  class
c = child()
c . marriage()
c . property()
c . study()


# Find  outputs   (Home  work)
class   parent:
	def  m1(self):
		print('m1  method  of  parent  class')
	def  m2(self):
		print('m2  method  of  parent class')
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
	def  m3(self):
		print('m3  method  of  child  class')
# End  of  the  class
x = parent()
x . m1()#m1  method  of  parent  class
x . m2()#m2  method  of  parent class
#x . m3()#error  
x = child()
x . m1()#m1 method of child class 
x . m2()#m2 method of parent class
x . m3()#m3 method of child class


# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End  of  the  class
c = child()
print(c . add(10 , 20 , 30))#60 
#print(c . add(10 , 20))#error
print(super(child , c) . add(40,50))#90


# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		print('parent  method')
		return  x + y
class  child(parent):
	def   add(self , x , y , z = 3):
		print('child  method')
		return  x + y + z
# End  of  the  class
c = child()
print(c . add(10 , 20 , 30))#child method <nextline> 60
print(c . add(10 , 20))#child method <nextline> 33


#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)#child method ---> x : 10 <tab> y : 20
c . m1(30 , 40)#child method ---> x : 30 <tab> y : 40


# Find  outputs (Home  work)
from  abc  import  ABC , abstractmethod
class  c1(ABC):
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(slef):
		print('c1  class  constructor')
class  c2(ABC):
	def  m1(self):
		pass
	def  __init__(slef):
		print('c2  class  constructor')
class  c3:
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(slef):
		print('c3  class  constructor')
class  c4(c1):
	def  m1(self):
		pass
	def  __init__(slef):
		print('c4  class  constructor')
class  c5(c1):
	def  __init__(slef):
		print('c1  class  constructor')
# End  of  the  class
c1()#  
c2()#c2 class constructor 
c3()#c3 class constructor 
c4()#c4 class constructor
c5()#c1 class constructor




# Find  outputs (Home  work)
from   abc    import    *
class   parent(ABC):
	@abstractmethod
	def  m1(self):
		pass
	@abstractmethod
	def  m2(self):
		pass
	@abstractmethod
	def  m3(self):
		pass
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
class  gc(child):
	def  m2(self):
		print('m2  method  of    gc  class')
class  ggc(gc):
	def  m3(self):
		print('m3  method  of  ggc  class')
# End  of  the  class
a = ggc()
a . m3()#m3 method of ggc class
a . m2()#m2 method of gc class
a . m1()#m1 mthod of child class
parent()#error
child()#error  
gc()#error 


# Save  in  any  file  of  cwd
from p1 import mod1#How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x)#How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1()#How  to  call  function  f1()  of   mod1  in  package  p1
ob=mod1.c1#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
ob.m1()
print(p1 . mod1 . x)  
print()
print()
from p1.p2 import mod2#How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x)#How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1()#How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
ob=mod2.c1()#How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
ob.m1()
print(p1 . p2 . mod2 . x)  
from  p1  import   p2 . mod2  
from  p2  import  mod2


# Save  in  any  file  of  cwd
from p1.mod1 import * #How  to  import  members  of  mod1  in   package  p1
print(x)#How  to  print  object  'x'  of   mod1  in  package  p1
f1()#How  to  call  function  f1()  of   mod1  in  package  p1
ob=c1()#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
ob.m1()
print()
print()
from p1.p2.mod2 import *#How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x)#How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1()#How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
ob=c1()How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
ob.m1()
from  p1  import  mod1 . *