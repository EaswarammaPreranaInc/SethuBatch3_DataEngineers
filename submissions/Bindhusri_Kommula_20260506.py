# Save  in  any  file  of  cwd
import  p1 . mod1
print(p1.mod1.x)
p1.mod1.f1()
a=p1.mod1.c1()
a.m1()
print()
print()
print(p1.__init__.x)
p1.__init__.f1()
a=p1.__init__.c1()
a.m1()
print(p1 . __init__ . x)  
p1 . __init__ . f1()  
a = p1 . __init__ . c1()



# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)
mod1.f1()
a=mod1.c1()
a.m1()
print(p1 . x)   # error
print(p1 . __init__ . x)  # error 
print(__init__ . x) # error


# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)
f1()
a=c1()
a.m1()
print(p1 . x)  #  Error
print(p1 . __init__ . x)    # error
print(__init__ . x)   # error
from  p1  import  mod1 . * # error



# Save  in  any  file  of  cwd
import p1.__init__ 
print(p1.__init__.x)
p1.__init__.f1()
c=p1.__init__.c1()
c.m1()
print(p1.x)
p1.f1()
c=p1.c1()
c.m1()
print(p1 . mod1 . x) # error



# Save  in  any  file  of  cwd
import   p1
import  p1 . mod1
from   p1   import  mod1
from   p1 . mod1  import   *
import  p1 . __init__