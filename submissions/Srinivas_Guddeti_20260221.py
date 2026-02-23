#----- abs() Function Demo Program -----

from builtins import abs
print(abs(-35.8)) # 35.8
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32)) # 32
import builtins
print(builtins . abs(-25)) # 25


#----- max() and min() Functions Demo Program -----

from builtins import max , min
print(max(10.8 , 20.6)) # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) # 5.9
print(max(25 , 10.8)) # 25
import builtins
print(builtins . max(10 , 20 , 30)) # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5


#----- pow() Function Demo Program -----

from builtins import pow
print(pow(10 , -2)) # 0.01
print(pow(4 , pow(3 , 2))) # 262144
import builtins
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) # -0.125


#----- Find Outputs -----

import keyword
print(keyword . kwlist) # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(len(keyword . kwlist)) # 35
print(type(keyword . kwlist)) # <class 'list'>


#----- Find Outputs -----

import keyword
from keyword import kwlist
print(kwlist) # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(len(kwlist)) # 35
print(type(kwlist)) # <class 'list'>


#----- How to read complex input? -----

x = complex('5+6j')
print(type(x)) # <class 'complex'>
print(x) # (5+6j)


#----- Tricky Program -----

print(eval(" 'hyd' ")) # hyd
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) # 25
cyb = 10.8
print(eval('cyb')) # 10.8
#print(eval(cyb)) # Error because eval expects string argument


#----- Most Tricky Program -----

print(eval('print("Hyd")')) # Hyd None


#----- Find Outputs -----

print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval(' "" ')) #
#print(eval('')) # Error because empty string is invalid syntax
print(eval(' " " ')) #
#print(eval(' ')) # Error because blank string is invalid syntax


#----- What is the advantage of eval(input())? -----

x = eval('30+40')
print(type(x)) # <class 'int'>
print(x) # 70


#----- What is a better approach to read string input? -----

a = ('Sec')
print(len(a)) # 3
print(a) # Sec
b = eval('"Sec"')
print(len(b)) # 3
print(b) # Sec