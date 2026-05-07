# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x)#How  to  print  object  'x'  of  mod1  in  package  p1
print(p1.mod1.f1())#How  to  call  function  f1()  of  mod1  in  package  p1
a = p1.mod1.c1()
a.m1()#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x)#How  to  print  object  'x'  of  __init__  module  in  package  p1
print(p1.f1())How  to  call  function  f1()  of  __init__  module  in  package  p1
a=p1.c1()
a.m1()How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1
print(p1 . __init__ . x)  
p1 . __init__ . f1()  
a = p1 . __init__ . c1()

# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)#How  to  print  object  'x'  of  mod1  in  package  p1
mo1.f1()#How  to  call  function  f1()  of  mod1  in  package  p1
a = mod1.c1()
a.m1()#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)  
print(p1 . _init_ . x)  
print(_init_ . x)

# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)#How  to  print  object  'x'  of  mod1  in  package  p1
f1()#How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1()#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)  #  Error
print(p1 . __init__ . x) #error,because we are not importing package
print(__init__ . x)  #error,because we are not importing __init__
from  p1  import  mod1 . *#Error



# Save  in  any  file  of  cwd
import p1.__init__#How  to  import  __init__  module  of  package  p1  with  import  statement
print(p1.__init__.x)How  to  print  object  'x'  of   __init__  module   in   package  p1
p1.__init__.f1()#How  to  call  function  f1()  of   __init__  module  in  package  p1
a = p1.__init__.c1()#How  to  call method  m1()  of  class  c1  in   __init__  module  of  package  p1
a.m1()
import p1
print(p1 . x) #How  to  print  object  'x'  of   __init__  module   in   package  p1  in  another  way
p1.f1()#How  to  call  function  f1()  of   __init__  module  in  package  p1  in  another  way
c =c1()
c.m1()# How  to  call  method  m1()  of  class  c1  in   __init__  module  of  package  p1  in  another  way
print(p1 . mod1 . x)#error


# Save  in  any  file  of  cwd
import   p1
import  p1 . mod1
from   p1   import  mod1
from   p1 . mod1  import   *
import  p1 . __init__