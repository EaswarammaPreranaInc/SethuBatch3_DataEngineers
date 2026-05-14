# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x)        #How  to  print  object  'x'  of  mod1  in  package  p1
p1.mod1.f1()            #How  to  call  function  f1()  of  mod1  in  package  p1
a = p1.mod1.c1()
a.m1()                #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
import p1
print(p1.x)         #How  to  print  object  'x'  of  _init_  module  in  package  p1
p1.f1()             #How  to  call  function  f1()  of  _init_  module  in  package  p1
a = p1.c1()
a.m1()              #How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1
print(p1 . _init_ . x)  
p1 . _init_ . f1()  
a = p1 . _init_ . c1()

--------------------------------------------------------------------------------------- 

# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)   #How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1()       #How  to  call  function  f1()  of  mod1  in  package  p1
a = mod1.c1()
a.m1()        #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)  # Error 
print(p1 . _init_ . x)  # Error
print(_init_ . x) # Error

---------------------------------------------------------------------------------------

# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)        #How  to  print  object  'x'  of  mod1  in  package  p1
f1()            #How  to  call  function  f1()  of  mod1  in  package  p1
a = c1()
a.m1()        #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)  #  Error 
print(p1 . _init_ . x)   # Error p1 is not imported
print(_init_ . x)  # Error
from  p1  import  mod1 . * # Error (from p1.mod1 import *)

---------------------------------------------------------------------------------------

# Save  in  any  file  of  cwd
import p1           #How  to  import  _init_  module  of  package  p1  with  import  statement
print(p1.x)         #How  to  print  object  'x'  of   _init_  module   in   package  p1
p1.f1()             #How  to  call  function  f1()  of   _init_  module  in  package  p1
obj = p1.c1()
obj.m1()            #How  to  call method  m1()  of  class  c1  in   _init_  module  of  package  p1
from p1 import x, f1, c1
print(x)            #How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
f1()                #How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a = c1()
a.m1()            #How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1 . mod1 . x) # Error 

---------------------------------------------------------------------------------------

# Save  in  any  file  of  cwd
import   p1     # imports the package p1 and runs __init__.py
import  p1 . mod1 # imports module inside package
from   p1   import  mod1 # imports mod1
from   p1 . mod1  import   *
import  p1 . _init_