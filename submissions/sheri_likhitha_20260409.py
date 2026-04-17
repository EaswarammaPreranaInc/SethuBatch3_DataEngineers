#  How  to  reuse  mod1  ?  (Home  work)
print('Hello')
import mod1	#How  to  import  mod1
print(mod1.x)		#How  to  print   variable  'x'   of  mod1
mod1.f1()			#How  to  call  function  f1()  of  mod1
obj=mod1.c1()			#How  to  call  method  m1()  of  class  c1  in  mod1
obj.m1()
print('Bye')
import  mod4
print(x)
f1()





#  Find  outputs  (Home  work)
print('Before')
import mod1	#How  to  run  mod1
print(mod1 . x)
mod1 . f1()
a = mod1 . c1()
print('After')
import runpy
runpy . run_module('mod1')





# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import*     #How  to  import  all  the  members  of  cal  module
print(x)		     #How  to  print  variable  'x'  of  cal   module
print(y)		#How  to  print  variable  'y'  of  cal   module)
print(cal . x)
print(add(10,7)		#How  to  call  add()  function  of  cal  module  with  10  and  7)
print(sub(10,7)		#How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(mul(10,7)		#How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10,7)		#How  to  call  div()  function  of  cal  module  with  10  and  7)
print(cal . add(x , y))
b=c1()		#How  to  call  m1()  method  of  class  c1  in  cal  module
b . m1()





# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from cal import x,add,mul,c1		#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x)				#How  to  print  variable  'x'  of  cal   module
print(y)
print(cal . x)
print(add(10,7)				#How  to  call  add()  function  of  cal  module  with  10  and  7)
print(sub(10 , 7))
print(mul(10,7)				#How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10 , 7))
b=c1()					#How  to  call  m1()  method  of  class  c1  in  cal  module
b.m1()






# Module  alias
print('Begin')
import cal as c				#How  to  import  cal  module  with   another  name  using  import  statement
print(c.x)					#How  to  print  variable  'x'  of  cal   module
print(c.y)				#How  to  print  variable  'y'  of  cal   module
print(c.add(10,7))			#How  to  call  add()  function  of  cal  module  with  10  and  7
print(c.sub(10,7))			#How  to  call  sub()  function  of  cal  module  with  10  and  7
print(c.mul(10,7))			#How  to  call  mul()  function  of  cal  module  with  10  and  7
print(c.div(10,7))			#How  to  call  div()  function  of  cal  module  with  10  and  7
b=c.c1()				#How  to  call  m1()  method  of  c1  class  in  cal  module
b.m1()
print(cal . x)
from  math  as   m  import  *






# Member  alias
from cal import x as a,add as ad,mul as ml, c1 as myclass					#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(a)						#How  to  print  variable  'x'  of  cal   module)

print(ad(10,7))					#How  to  call  add()  function  of  cal  module  with  10  and  7)
print(ml(10,7))					#How  to  call  mul()  function  of  cal  module  with  10  and  7)
b=myclass()					#How  to  call  m1()  method  of  class  c1  in  cal  module
b=m1()





# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)	#30
disp()		#disp function of same module
a = c1()
a . m1()	#m1 method of class c1 in same module






# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)	#30
disp()		#disp function of same module
a = c1()
a . m1()	#m1 method of class c1 in same module






# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1,mod2     #How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)		#How  to  print  variable  'x'  of  mod1
mod1.disp()		#How  to  call  disp()  function  of  mod1
b=mod1.c1()			#How  to  call  method  m1()  of  class   c1  in  mod1
b.m1()
print()
print(mod2.x)		#How  to  print  variable  'x'  of  mod2
mod2.disp()		#How  to  call  disp()  function  of  mod2
a=mod2.c1()			#How  to  call  method  m1()  of  class   c1  in  mod2
a.m1()
print()
print(x)		#How  to  print  variable  'x'  of  current  module)
disp()			#How  to  call  disp()  function  of current  module
c=c1()			#How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()





# How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import *		#How  to  import  members  of  mod1
from mod2 import*               #How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(mod1.x)			#How  to  print  variable  'x'  of  mod1)
mod1.disp()			#How  to  call  disp()  function  of  mod1
a=mod1.cl()				#How  to  call  method  m1()  of  class   c1  in  mod1
a.m1()
print()
print()
print(mod2.x)			#How  to  print  variable  'x'  of  mod2)
mod2.disp()				#How  to  call  disp()  function  of  mod2
b=mod2.c1()				#How  to  call  method  m1()  of  class   c1  in  mod2
b.m1()
print()
print()
print(x)			#How  to  print  variable  'x'  of  current  module)
disp()				#How  to  call  disp()  function  of current  module
c=c1()				#How  to  call  method  m1()  of  class   c1  in  current  module
c.m1()





# mod1.py  (Home  work)
# How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
if __name__=='__main___':
    print('One')
    print('Two')
    print('Three')
    print('Four')
    print('Five')
    print('Six')
    print('Seven')
    print('Eight')
    print('Nine')




# Find  outputs (Home  work)
print('Begining  of  mod2')	#Begining of mod2
import   mod1
print('End  of  mod2')		#End of mod2





#  Find  outputs
import  cal
print(cal . x)	#100
print(cal . y)	#200
print(cal . add(10 , 7))	#17
print(cal . sub(10 , 7))	#3
print(cal . mul(10 , 7))	#70
print(cal . div(10 , 7))	#1.4
a = cal . c1()			#creating the c1 class method
a . m1()			#m1 method




#  Find  outputs
from  cal  import   y , sub , mul
print(x)	#error
print(y)	#200
print(add(10 , 7))	#error add is not imported
print(sub(10 , 7))	#3
print(mul(10 , 7))	#70
print(div(10 , 7))	#error div is not importedd
a = c1()		#error c1 is not deffined




# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()
b = Rat(9)
c = Rat(5,  8)
d = Rat(dr1 = 9)
e = Rat(dr1 = 3 , nr1 = 2)
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)
print('a  :  ' , a)	#22/7
print('b  :  ' , b)	#9/7
print('c  :  ' , c)	#5/8
print('d  :  ' , d)	#22/9
print('e  :  ' , e)	#2/3
print('f  :  ' , f)	#11/15
c . __init__()
print('c  :  ' , c)	#22/7
a . __init__(3.8  , 4.6)
print('a  :  ' , a)	#3.8/4.6
g = Rat(nr1 = 9 , 5)	#error positional argument after keyword agrument
h = Rat(nr = 9 , dr = 5) #error name error for parameter






# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . __dict__)	#{'dd':15,'mm':8,'yy':1947}
print('b  :  ' , b . __dict__)	#{'dd':26,'mm':1,'yy':1950}
print('c  :  ' , c . __dict__)	#{'dd':19,'mm':7,'yy':1985}
d = Date()	#error arguments missiing
e = Date(dd = 30 , mm = 4 , yy = 2022)	#error positional argument after keyword argument
f = Date(dd1 = 26 , mm1 = 8 , 2023)	#error



# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')
		return  25
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
a = c1()	#error
b = c2()	#c2 class constructor
print(b)	#___main___.c2 at address of the object
print(b . __init__())	#c2 class constructor <next> None
c = c3()		#c3 class constructor
print(c . __init__())	#c3 class constructor  <next> None








# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()	#constructor 2
# End  of  class
a = c1()	#constructor   1





#  Difference  between  init()    and  __init__()   methods (Home  work)
class c1:
    def  __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1()	#constructor
print(a . __dict__)	#{'x':10,'y':20}
b = c2()
print(b . __dict__)	#{}
b . init()		#Method
print(b . __dict__)	#{'x':30,'y':40}




# Find  outputs (Home  work)
class   c1:
        def   __init__(self):
                self . a = 10
        def   m1(self):
                self . b = 20
#End  of  class  c1
class   c2:
        def  m3(self):
                x . e = 50
# End  of  class  c2
def   f1():
        x . c = 30
#  End  of  function  f1
x = c1()
print(x . __dict__)	#{'a':10}
x . m1()
print(x . __dict__)	#{'a':10,'b':20}
f1()
print(x . __dict__)	#{'a':10,'b':20,'c':30}
x . d = 40
print(x . __dict__)	#{'a':10,'b':20,'c':30,'d':40}
y = c2()
y . m3()
print(x . __dict__)	#{'a':10,'b':20,'c':30,'d':40,'e':50}
z = c1()
print(z . __dict__)	#{'a':10}




# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__)	#{'x':10,'y':20,'z':30}
print(b . __dict__)	#{'x':10,'y':20,'z':30}
del  a . x
del  b . y
print(a . __dict__)	#{'y':20,'z':30}
print(b . __dict__)	#{'x':10,'z':30}
print(a . x)		#error
print(b . y)		#error





#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()	#3rd constructor






#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)		#Two argument constructor : 10,20
b = c1(30)		#error type error
c = c1()		#error type error







#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)		#Two  argument  constructor : 10,20
b = c1(30)		#Two  argument  constructor : 30,200
c = c1()		#Two  argument  constructor : 100,200





# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')	#class is executed
# End  of  the  class
a = f1()
print(a)	#constructor





# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()	#fuunction
print(a)	#None





# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()	#error
b = c1(25)	#function:25
print(b)	#error




#  Save  the  program  in  prog9a.py  file
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')






#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1()	#c1 class of prog9b





#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()	#c1 class of prog9a




#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import c1 as c1_a				#How  to  import  class  c1  from  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
obj_local = c1()   			#How  to  create  c1  class  object  of  current  module
obj_prog9a = c1_a() 			#How  to  create  c1  class  object  of  prog9a





'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
import prog9a			#How  to  import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
obj_local=c1()				#How  to  create  c1  class  object  of  current  module
obj_prog9a=prog9a.c1()			#How  to  create  c1  class  object  of  prog9a