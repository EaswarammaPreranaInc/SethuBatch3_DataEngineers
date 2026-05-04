#  Save  in  any  file  of  cwd  (Homework)
from p1 import mod1 , mod2 # How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1 . x) # How  to  print  object  'x'  of   mod1  in  package  p1
mod1 . f1() # How  to  call  function  f1()  of   mod1  in  package  p1
# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
obj1 = mod1 . c1()
obj1 . m1()
print()
print()
print(mod2 . x) # How  to  print  object  'x'  of   mod2  in  package  p1
mod2 . f1() # How  to  call  function  f1()  of   mod2  in  package  p1
# How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
obj2 = mod2 . c1()
obj2 . m1() 
print(p1 . mod1 . x) # error , p1 package is not imported
print(x) # error , searches for x in current program



#  Save  in  any  file  of  cwd
from p1 . mod1 import * # How  to  import  members  of  mod1  in  package  p1
print(x) # How  to  print  object  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
obj1 = c1()
obj1 . m1()
print()
print()
from p1 . mod2 import * # How  to  import   members  of  mod2   in  package  p1
print(x) # How  to  print  object  'x'  of   mod2  in  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  package  p1
# How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
obj2 = c1()
obj2 . m1() 
print(p1 . mod1 . x) # error , p1 package and mod1 module are not imported
print(mod1 . x) # error , mod1 module is not imported  
from  p1   import  mod1 . * # error , . cannot be used after import in from statement



#1
'''
(Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    *
from  p1 . mod2    import    *
print(x)  
f1() 
a = c1()
a . m1()
'''
x of mod2
f1() of mod2
m1() of c1 in mod2
'''



#2
'''
(Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod2    import   *
from  p1 . mod1    import   *
print(x)  
f1()
a = c1()
a . m1()
'''
x of mod1
f1() of mod1
m1() of c1 in mod1
'''



#3
'''
(Home work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x) 
f1()
a = c1()
a . m1()
'''
30
Function of same module
Method of class c1 in same module
'''



#4
'''
(Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
from p1 import mod1 , mod2 # How  to  import   members  of  mod1   in  package  p1 .How  to  import   members  of  mod2   in  package  p1  
print(mod1 . x) # How  to  print  object  'x'  of   mod1  in  package  p1
mod1 . f1() # How  to  call  function  f1()  of   mod1  in  package  p1
# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
obj1 = mod1 . c1() 
obj1 . m1() 
print()
print()
print(mod2 . x) # How  to  print  object  'x'  of   mod2  in  package  p1
mod2 . f1() # How  to  call  function  f1()  of   mod2  in  package  p1
# How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
obj2 = mod2 . c1()   
obj2 . m1() 
'''
x of mod1
f1() of mod1
m1() of c1 in mod1

x of mod2
f1() of mod2
m1() of c1 in mod2
'''
