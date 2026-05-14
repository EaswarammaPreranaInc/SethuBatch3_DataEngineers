#1
# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x) # How  to  print  object  'x'  of  mod1  in  package  p1 
p1.mod1.f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = p1.mod1.c1() 
a.m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x) # How  to  print  object  'x'  of  __init__  module  in  package  p1
p1.f1() # How  to  call  function  f1()  of  __init__  module  in  package  p1
b = p1.c1() 
b.m1() # How  to  call  method  m1()  of  class  c1  in   __init__  module  of  package  p1
print(p1 . __init__ . x) # Error , __init__ is not imported 
p1 . __init__ . f1()  # Error , __init__ is not imported 
a = p1 . __init__ . c1() # Error , __init__ is not imported 


#2
# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x) # How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = mod1.c1() 
a.m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x) # Error , p1 is not imported  
print(p1 . __init__ . x)  # Error p1.__init__ not imported 
print(__init__ . x) # Error __init__ not imported


#3
# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)# How  to  print  object  'x'  of  mod1  in  package  p1
f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = c1() 
a.m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)  #  Error
print(p1 . __init__ . x) # Error   
print(__init__ . x)  # Error
from  p1  import  mod1 . * # Error , '.' cannot be used in import clause



#4
# Save  in  any  file  of  cwd
import p1.__init__ # How  to  import  __init__  module  of  package  p1  with  import  statement
print(p1.__init__.x) # How  to  print  object  'x'  of   __init__  module   in   package  p1
p1.__init__.f1() # How  to  call  function  f1()  of   __init__  module  in  package  p1
a = p1.__init__.c1()
a.m1() # How  to  call method  m1()  of  class  c1  in   __init__  module  of  package  p1
import p1
print(p1.x) # How  to  print  object  'x'  of   __init__  module   in   package  p1  in  another  way
p1.f1() # How  to  call  function  f1()  of   __init__  module  in  package  p1  in  another  way
b = p1.c1()
b.m1() # How  to  call  method  m1()  of  class  c1  in   __init__  module  of  package  p1  in  another  way
print(p1 . mod1 . x) # Error , mod1 is not imported





