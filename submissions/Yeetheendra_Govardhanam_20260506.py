'''
1) # Save in any file of cwd
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
# How to print object 'x' of _init_ module in package p1
print(p1._init_.x)
# How to call function f1() of _init_ module in package p1
p1._init_.f1()
# How to call method m1() of class c1 in init module of package p1
a = p1._init_.c1()
print(p1 . _init_ . x)
p1 . _init_ . f1()
a = p1 . _init_ . c1()
# Because this works only if p1/_init_.py exists as a real module; otherwise it is an import/access error.
'''
'''
2) # Save in any file of cwd
from  p1   import  mod1
# How to print object 'x' of mod1 in package p1
print(mod1.x)
# How to call function f1() of mod1 in package p1
mod1.f1()
# How to call method m1() of class c1 in mod1 of package p1
a = mod1.c1()
a.m1()
# print(p1 . x) # Error as name 'p1' is not defined
# print(p1 . _init_ . x) # Error as name 'p1' is not defined
# print(_init_ . x) # Error as name '_init_' is not defined
'''
'''
3) # Save in any file of cwd
from  p1 . mod1   import  *
# How to print object 'x' of mod1 in package p1
print(x)
# How to call function f1() of mod1 in package p1
f1()
# How to call method m1() of class c1 in mod1 of package p1
a = c1()
a.m1()
# print(p1 . x) # Error as name 'p1' is not defined
# print(p1 . _init_ . x) # Error as name 'p1' is not defined
# print(_init_ . x) # Error as name '_init_' is not defined
from  p1  import  mod1 . * # SyntaxError
'''
'''
4) # Save in any file of cwd
# How to import _init_ module of package p1 with import statement
import p1._init_
# How to print object 'x' of _init_ module in package p1
print(p1._init_.x)
# How to call function f1() of _init_ module in package p1
p1._init_.f1()
# How to call method m1() of class c1 in _init_ module of package p1
a = p1._init_.c1()
# How to print object 'x' of _init_ module in package p1 in another way
from p1 import _init_
print(_init_.x)
# How to call function f1() of _init_ module in package p1 in another way
_init_.f1()
# How to call method m1() of class c1 in _init_ module of package p1 in another way
a = _init_.c1()
# print(p1 . mod1 . x) # Error or NameError as depending on whether mod1 was imported
'''
'''
5) # Save in any file of cwd
import   p1
import  p1 . mod1
from   p1   import  mod1
from   p1 . mod1  import   *
import  p1 . _init_
# Because imports are redundant and may overwrite earlier names; the last import* affects local names.
'''