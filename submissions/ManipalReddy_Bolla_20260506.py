# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x)#How  to  print  object  'x'  of  mod1  in  package  p1
p1.mod1.f1()#How  to  call  function  f1()  of  mod1  in  package  p1
ob=p1.mod1.c1()#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
ob.m1()
print()
print()
print(p1.x)#How  to  print  object  'x'  of  __init__  module  in  package  p1
f1()#How  to  call  function  f1()  of  __init__  module  in  package  p1
#ob=c1()How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1
ob.m1()
print(p1 . __init__ . x)  
p1 . __init__ . f1()  
a = p1 . __init__ . c1()


# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)#How  to  print  object  'x'  of  mod1  in  package  p1
mod11.f1()#How  to  call  function  f1()  of  mod1  in  package  p1
ob=mod1.c1()#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
ob.m1()
print(p1 . x)  
print(p1 . __init__ . x)  
print(__init__ . x)


# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)#How  to  print  object  'x'  of  mod1  in  package  p1
f1()#How  to  call  function  f1()  of  mod1  in  package  p1
ob=c1()#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
ob.m1()
print(p1 . x)  #  Error
print(p1 . __init__ . x)   
print(__init__ . x)  
from  p1  import  mod1 . *


# Save  in  any  file  of  cwd
import p1.__init__#How  to  import  __init__  module  of  package  p1  with  import  statement
print(x)#How  to  print  object  'x'  of   __init__  module   in   package  p1
f1()#How  to  call  function  f1()  of   __init__  module  in  package  p1
#ob=c1()How  to  call method  m1()  of  class  c1  in   __init__  module  of  package  p1
ob.m1()
print(__init__.x)#How  to  print  object  'x'  of   __init__  module   in   package  p1  in  another  way
__init__.f1()#How  to  call  function  f1()  of   __init__  module  in  package  p1  in  another  way
ob=__init__.c1()#How  to  call  method  m1()  of  class  c1  in   __init__  module  of  package  p1  in  another  way
ob.m1()
print(p1 . mod1 . x)


# Save  in  any  file  of  cwd
import   p1
import  p1 . mod1
from   p1   import  mod1
from   p1 . mod1  import   *
import  p1 . __init__