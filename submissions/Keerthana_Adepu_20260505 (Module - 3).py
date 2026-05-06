# Save  in  any  file  of  cwd
from p1 import mod1 # How  to  import  mod1  of  package  p1  with  from  statement
print(mod1 . x) # How  to  print  object  'x'  of   mod1  in  package  p1
mod1 . f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1 . c1()
a . m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print(p1 . mod1 . x)  # error , because p1 is not imported 
print()
print()
from p1 . p2 import mod2 # How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2 . x) # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2 . f1() # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a = mod2 . c1()
a . m1() # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
print(p1 . p2 . mod2 . x)  # error , p1 and p2 are not imported 
from  p1  import   p2 . mod2  
from  p2  import  mod2



# Save  in  any  file  of  cwd
from p1 . mod1 import * # How  to  import  members  of  mod1  in   package  p1
print(x) # How  to  print  object  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a . m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1 . p2 . mod2 import * # How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x) # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a = c1()
a . m1() # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
from  p1  import  mod1 . * # error , '.' cannot be used in import clause of from statement
