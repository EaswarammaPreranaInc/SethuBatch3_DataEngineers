# mod1 . py
'''
print('Hyd') #Hyd
print('Sec') #Sec
print('Cyb') #Cyb
x = 25
def  f1():
	print('Function')
class   c1:
	def   m1(self):
			print('Method')'''


'''
1) What  are  the  members  of  mod1 ?  --->  Object  'x' ,  function  f1()  and  class  c1

2) py  mod1.py
    What  are  the  outputs ?  --->  Hyd  <next line>  Sec  <next  line>  Cyb  <next  line>

3) Why  are  function  f1()  and  method  m1()  not  executed ?  --->  Since  they  are  not  called
'''

'''
#  How  to  reuse  mod1  ?  (Home  work)
print('Hello')
import mod1 #How  to  import  mod1
print(mod1.x)#(How  to  print   variable  'x'   of  mod1)
mod1.f1()#How  to  call  function  f1()  of  mod1
obj = mod1.c1()
obj.m1()#How  to  call  method  m1()  of  class  c1  in  mod1
print('Bye')
import  mod4
print(x)
f1()'''

'''
#  Find  outputs  (Home  work)
import mod1
import runpy
print('Before')
#How  to  run  mod1
print(mod1 . x)
mod1 . f1()
a = mod1 . c1()
print('After')
run_module('mod1') #correct order is runpy.run_module('mod1')
runpy . run_module(mod1) # mod1 should be in str'''


'''
# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import *  #How  to  import  all  the  members  of  cal  module
print(x)#(How  to  print  variable  'x'  of  cal   module)
print(y)#(How  to  print  variable  'y'  of  cal   module)
print(cal . x) #Error due to cal is not imported.
print(add(10,7)#(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(sub(10,7))#(How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(mul(10,7))#(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10,7))#(How  to  call  div()  function  of  cal  module  with  10  and  7)
print(cal . add(x , y)) #Error becoz cal ins not imported
obj=c1()
obj.m1()#How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1() #Error cal is not imported. It works when we import cal directly.'''



# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
'''
print('Begin')
from cal import x , add, mul, c1#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(x) #How  to  print  variable  'x'  of  cal   module)
print(y)
print(cal . x) #Error due to cal is not imported directly.
print(add(10,7))#How  to  call  add()  function  of  cal  module  with  10  and  7)
print(sub(10 , 7)) # It raises error it is not imported.
print(mul(10,7))#(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10 , 7)) # Error not imported
d=c1()
d.m1()How  to  call  m1()  method  of  class  c1  in  cal  module'''


'''
# Module  alias
print('Begin')
from cal as c #How  to  import  cal  module  with   another  name  using  import  statement
print(c.x)#How  to  print  variable  'x'  of  cal   module)
print(c.y)#How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7))#How  to  call  add()  function  of  cal  module  with  10  and  7)
print(c.sub(10,7))#How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(c.mul(10,7))#How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(c.div(10,7))#How  to  call  div()  function  of  cal  module  with  10  and  7)
obj=c()
obj.m1()How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x)# Error
from  math  as   m  import  * #Imports all the elements in it.

output:
Begin
10
7
17
3
70
1.4285714285714286
Method m1 from class c1 '''



# Member  alias
"""
from cal as c import x as a, add as ad, mul as ml, cl as c#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(a)#How  to  print  variable  'x'  of  cal   module)
print(x)#Error module is not directly imported.
print(ad(10,7))#How  to  call  add()  function  of  cal  module  with  10  and  7)
print(ml(10,7))#How  to  call  mul()  function  of  cal  module  with  10  and  7)
o = c()
0.m1()#How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7))#Error
b = c1() #Error"""
'''
output:
10
17
70
Method m1 from class c1'''


'''
# cal . py
x = 100
y = 200
def  add(a , b):
	return  a + b
def	 sub(a , b):
	return  a - b
def	 mul(a , b):
	return  a * b
def	 div(a , b):
	return  a / b
class   c1:
	def  m1(self):
		print('m1  method')'''



'''
1) What  is  the  module  name ?  --->  cal

2) What  are  the  members  of  cal  module ?  --->  Two  objects  x  and  y ,
																			      Four  functions  add() , sub() , mul()  and  div()  and
																				  class  c1

3) Is  m1()  a  member  of  cal  module ?  --->  No  becoz  it  is  a  method  of  class

4) How  many  statements  are  in  cal  module ?  --->  Two
																				     i.e.  x =  100   and  y = 200

5) py  cal . py
    What  are  the  outputs ?  --->  Nothing  becoz  there  are  no  print  statements  in  cal  module
'''
'''
# mod1.py
x = 10
def  disp():
	print('disp  function  of  mod1')
class   c1:
	def   m1(self):
		print('m1  method  of  class  c1  in  mod1')



#What  are  the  members  of  mod1 ?   ---> Object  'x' , function  disp()  and  class  c1

# mod2.py
x = 20
def   disp():
	print('disp  function  of  mod2')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  mod2')



#What  are  the  members  of  mod2 ? --->  Object  'x' ,  function  disp()  and  class  c1




# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x) #10
disp() #disp  function  of  mod1 <nextline> m1  method  of  class  c1  in  mod1
a = c1()
a . m1()
'''
'''
# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) 
disp() 
a = c1()
a . m1()

output:
30
disp  function  of  same  module
m1  method of  class  c1  in  same  module'''



'''
# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1
import mod2#How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x)#How  to  print  variable  'x'  of  mod1
mod1.disp()#How  to  call  disp()  function  of  mod1
a1 = mod1.c1()
a1.m1()#How  to  call  method  m1()  of  class   c1  in  mod1
print() #next line
print(mod2.x)#How  to  print  variable  'x'  of  mod2
mod2.disp()#How  to  call  disp()  function  of  mod2
a2 = mod2.c1()
a2.m1()#How  to  call  method  m1()  of  class   c1  in  mod2
print() #Next line
print(x)#How  to  print  variable  'x'  of  current  module)
disp()#How  to  call  disp()  function  of current  module
a3 = c1()
a3.m1()#How  to  call  method  m1()  of  class   c1  in  current  module'''


'''
output:
10
disp from mod1
m1 from mod1

20
disp from mod2
m1 from mod2

30
disp function of same module
m1 method of class c1 in same module'''


'''
# How  to  use  members  of  all  the  three  modules  with  from  statement ?

from mod1 import x as x1, disp as d1, c1 as C1 #How  to  import  members  of  mod1
from mod2 import x as x2, disp as d2, c1 as C2 #How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(x1)#How  to  print  variable  'x'  of  mod1)
d1()#How  to  call  disp()  function  of  mod1
d = c1()
d.m1()#How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()

print(x2)#How  to  print  variable  'x'  of  mod2)
d2()#How  to  call  disp()  function  of  mod2
s = c1()
s.m1()#How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(x)#How  to  print  variable  'x'  of  current  module)
disp()#How  to  call  disp()  function  of current  module
w = c1()
w.m1()#How  to  call  method  m1()  of  class   c1  in  current  module
'''
'''
output:
10
disp from mod1
m1 from mod1


20
disp from mod2
m1 from mod2


30
disp function of same module
m1 method of class c1 in same module'''




# mod1.py  (Home  work)
# How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
'''
print('One')
if __name__ == "__main__":
    print('Two')
    print('Three')
    print('Four')
print('Five')
print('Six')
print('Seven')
print('Eight')
print('Nine')'''

'''
# Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod1
print('End  of  mod2')

output:
Begining of mod2
One
Five
Six
Seven
Eight
Nine
End of mod2'''

'''
#  Find  outputs
import  cal
print(cal . x) # 10
print(cal . y) # 7
print(cal . add(10 , 7)) # 17
print(cal . sub(10 , 7)) #3
print(cal . mul(10 , 7)) # 70
print(cal . div(10 , 7)) # 1.428
a = cal . c1()
a . m1() #method m1 from class c1'''


'''
#  Find  outputs
from  cal  import   y , sub , mul
print(x) #error x is not imported
print(y) #7
print(add(10 , 7)) 
print(sub(10 , 7))
print(mul(10 , 7))
print(div(10 , 7))
a = c1() 

output:
#Error due to x is not imported.'''






