
# Save  in  any  file  of  cwd
import  p1 . mod1
print(mod1.x)   #How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1()   #How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1() 
a.m1()  #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1.x)    #How  to  print  object  'x'  of  _init_  module  in  package  p1
p1.f1()    #How  to  call  function  f1()  of  _init_  module  in  package  p1
a=p1.c1 #
a.m1() #How  to  call  method  m1()  of  class  c1  in   init  module  of  package  p1
print(p1 . _init_ . x) # Error, bcz __init__ is not imported
p1 . _init_ . f1()  #Error pakage p1 is not imported
a = p1 . _init_ . c1() ##Error  pakage p1 is not imported



# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)   #How  to  print  object  'x'  of  mod1  in  package  p1
mod1.f1()   #How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1() #
a.m1()  #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)  #  error pakage p1 is not imported 
print(p1 . _init_ . x)  #error pakage p1 is not imported
print(_init_ . x) #pakage p1 is not imported

 # Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)    #How  to  print  object  'x'  of  mod1  in  package  p1
f1() #How  to  call  function  f1()  of  mod1  in  package  p1
a=c1() #
a.m1()  #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)  #  Error
print(p1 . _init_ . x)  #error  
print(_init_ . x)  #error there is no __init__ in cwd
from  p1  import  mod1 . *#error '.' is not permetted in import clause 

# Save  in  any  file  of  cwd
import p1.__init__.py #How  to  import  _init_  module  of  package  p1  with  import  statement
print(x) #How  to  print  object  'x'  of   _init_  module   in   package  p1
f1() #How  to  call  function  f1()  of   _init_  module  in  package  p1
a=c1() #
a.m1() #How  to  call method  m1()  of  class  c1  in   _init_  module  of  package  p1
print(__init__.x)   #How  to  print  object  'x'  of   _init_  module   in   package  p1  in  another  way
__init__.f1()   #How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a=__init__.c1() #
a.m1()  #How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
print(p1 . mod1 . x)#error becoz the p1 i s not imported


# Save  in  any  file  of  cwd
import   p1
import  p1 . mod1
from   p1   import  mod1
from   p1 . mod1  import   *
import  p1 . _init_