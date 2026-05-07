# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1 . mod1 . x) # How  to  print  object  'x'  of  mod1  in  package  p1
p1 . mod1 . f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = p1 . mod1 . c1()
a . m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print()
print()
print(p1 . x) # How  to  print  object  'x'  of  __init__  module  in  package  p1
p1 . f1() # How  to  call  function  f1()  of  __init__  module  in  package  p1
a = p1 . c1()
a . m1() # How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1
print(p1 . __init__ . x)  # error , __init__ is not imported
p1 . __init__ . f1()  # error , __init__ is not imported
a = p1 . __init__ . c1() # error , __init__ is not imported


# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1 . x) # How  to  print  object  'x'  of  mod1  in  package  p1
mod1 . f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = mod1 . c1()
a . m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)  # error , p1 is not important 
print(p1 . __init__ . x)  # error , p1 and __init__ are not imported
print(__init__ . x) # error , __init__ is not imported



# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x) # How  to  print  object  'x'  of  mod1  in  package  p1
f1() # How  to  call  function  f1()  of  mod1  in  package  p1
a = c1()
a . m1() # How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
print(p1 . x)  #  Error
print(p1 . __init__ . x) # error , p1 and __init__ are not imported
print(__init__ . x)  # error , __init__ is not imported
from  p1  import  mod1 . * # error , '.' cannot be used in the import clause of from statement 



# Save  in  any  file  of  cwd
import p1 . __init__ # How  to  import  __init__  module  of  package  p1  with  import  statement
print(p1 . __init__ . x) # How  to  print  object  'x'  of   __init__  module   in   package  p1
p1 . __init__ . f1() # How  to  call  function  f1()  of   __init__  module  in  package  p1
a = p1 . __init__ . c1()
a . m1() # How  to  call method  m1()  of  class  c1  in   __init__  module  of  package  p1
print(p1 . x) # How  to  print  object  'x'  of   __init__  module   in   package  p1  in  another  way
p1 . f1() # How  to  call  function  f1()  of   __init__  module  in  package  p1  in  another  way
a = p1 . c1() 
a . m1() # How  to  call  method  m1()  of  class  c1  in   __init__  module  of  package  p1  in  another  way
print(p1 . mod1 . x) # error , mod1 is not imported 



# Save  in  any  file  of  cwd
import   p1
import  p1 . mod1
from   p1   import  mod1
from   p1 . mod1  import   *
import  p1 . __init__
'''
__init__ is excecuted
__name__ : p1
__init__ is excecuted
__name__ : p1 . __init__
'''
