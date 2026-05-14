# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x) # How  to  print  object  'x'  of  mod1  in  package  p1
p1.mod1.f1()  # How  to  call  function  f1()  of  mod1  in  package  p1
c = p1.mod1.c1()  # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
c.m1()
print()
print()
print(p1.x) # How  to  print  object  'x'  of  __init__  module  in  package  p1
p1.f1() # How  to  call  function  f1()  of  __init__  module  in  package  p1
c=p1.c1() # How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1
c.m1()
print(p1 . __init__ . x)   # error
p1 . __init__ . f1()  # error
a = p1 . __init__ . c1()  # error



# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x) # How  to  print  object  'x'  of  mod1  in  package  p1
mod1 .f1() # How  to  call  function  f1()  of  mod1  in  package  p1
c=mod1.c1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
c.m1()
print(p1 . x)  # error only mod1 is imported
print(p1 . __init__ . x)  # error
print(__init__ . x)  # error




# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x) # How  to  print  object  'x'  of  mod1  in  package  p1
f1() # How  to  call  function  f1()  of  mod1  in  package  p1
c=c1()  
c.m1()  # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)  #  Error
print(p1 . __init__ . x)   # error
print(__init__ . x)  # error
from  p1  import  mod1 . *   # error 





# Save  in  any  file  of  cwd
import p1.__init__  # How  to  import  __init__  module  of  package  p1  with  import  statement
print(p1.x)  # How  to  print  object  'x'  of   __init__  module   in   package  p1
p1.f1() # How  to  call  function  f1()  of   __init__  module  in  package  p1
c=p1.c1() 
c.m1()  # How  to  call method  m1()  of  class  c1  in   __init__  module  of  package  p1
from p1 import *  
print(x) # How  to  print  object  'x'  of   __init__  module   in   package  p1  in  another  way
f1()  # How  to  call  function  f1()  of   __init__  module  in  package  p1  in  another  way
c=c1()  
c.m1() # How  to  call  method  m1()  of  class  c1  in   __init__  module  of  package  p1  in  another  way
print(p1 . mod1 . x)  # error




# Save  in  any  file  of  cwd
import   p1
import  p1 . mod1
from   p1   import  mod1
from   p1 . mod1  import   *
import  p1 . __init__