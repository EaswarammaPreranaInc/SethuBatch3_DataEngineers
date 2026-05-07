# Save in any file of cwd
import  p1 . mod1
# How to print object 'x' of mod1 in package p1
print(p1.mod1.x)
# How to call function f1() of mod1 in package p1
p1.mod1.f1()
# How to call method m1() of class c1 in mod1 of package p1
a = p1.mod1.c1()
a.m1()
print()
print()
# How to print object 'x' of init module in package p1
print(p1.init.x)
# How to call function f1() of init module in package p1
p1.init.f1()
# How to call method m1() of class c1 in init module of package p1
a = p1.init.c1()
print(p1 . init . x)
p1 . init . f1()
a = p1 . init . c1()
# Because this works only if p1/init.py exists as a real module


# Save in any file of cwd
from  p1   import  mod1
# How to print object 'x' of mod1 in package p1
print(mod1.x)
# How to call function f1() of mod1 in package p1
mod1.f1()
# How to call method m1() of class c1 in mod1 of package p1
a = mod1.c1()
a.m1()
# print(p1 . x) # Error as name 'p1' is not defined
# print(p1 . init . x) # Error as name 'p1' is not defined
# print(init . x) # Error as name 'init' is not defined


# Save in any file of cwd
from  p1 . mod1   import  *
# How to print object 'x' of mod1 in package p1
print(x)
# How to call function f1() of mod1 in package p1
f1()
# How to call method m1() of class c1 in mod1 of package p1
a = c1()
a.m1()
# print(p1 . x) # Error as name 'p1' is not defined
# print(p1 . init . x) # Error as name 'p1' is not defined
# print(init . x) # Error as name 'init' is not defined
from  p1  import  mod1 . * # SyntaxError


# Save in any file of cwd
# How to import init module of package p1 with import statement
import p1.init
# How to print object 'x' of init module in package p1
print(p1.init.x)
# How to call function f1() of init module in package p1
p1.init.f1()
# How to call method m1() of class c1 in init module of package p1
a = p1.init.c1()
# How to print object 'x' of init module in package p1 in another way
from p1 import init
print(init.x)
# How to call function f1() of init module in package p1 in another way
init.f1()
# How to call method m1() of class c1 in init module of package p1 in another way
a = init.c1()
# print(p1 . mod1 . x) # Error or NameError as depending on whether mod1 was imported


# Save in any file of cwd
import   p1
import  p1 . mod1
from   p1   import  mod1
from   p1 . mod1  import   *
import  p1 . init
# Because imports are redundant and may overwrite earlier names; the last import* affects local names