from builtins import abs
print(abs(-35.8))   # 35.8
print(abs(-27))     # 27
print(abs(29.5))    # 29.5
print(abs(32))      # 32

import builtins # imports builtins module
print(builtins.abs(-25))   # 25
from builtins import max, min

print(max(10.8 , 20.6))           # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  # 5.9
print(max(25 , 10.8))             # 25

import builtins
print(builtins.max(10 , 20 , 30))     # 30
print(builtins.min(10 , 20 , 15 , 5 , 12))  # 5
from builtins import max, min

print(max(10.8 , 20.6))           # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  # 5.9
print(max(25 , 10.8))             # 25

import builtins
print(builtins.max(10 , 20 , 30))     # 30
print(builtins.min(10 , 20 , 15 , 5 , 12))  # 5
from builtins import pow

print(pow(10 , -2))        # 0.01
print(pow(4 , pow(3 , 2))) # 262144   (because 3^2=9, 4^9=262144)

import builtins
print(builtins.pow(2 , 3))     # 8
print(builtins.pow(-2 , -3))   # -0.125
import keyword
print(keyword.kwlist)        # prints list of all python keywords
print(len(keyword.kwlist))   # 35  (depends on python version)
print(type(keyword.kwlist))  # <class 'list'>
import keyword
print(keyword.kwlist)        # prints list of all python keywords
print(len(keyword.kwlist))   # 35  (depends on python version)
print(type(keyword.kwlist))  # <class 'list'>
x = complex(input('Enter complex number : '))
print(type(x))   # <class 'complex'>
print(x)         # whatever complex number you entered
x = complex(input('Enter complex number : '))
print(type(x))   # <class 'complex'>
print(x)         # whatever complex number you entered
print(eval("    'hyd'   "))   # hyd

hyd = 'Sec'
print(eval('hyd'))   # Sec

sec = '25'
print(eval('sec'))   # 25  (string '25')
print(eval(sec))     # 25  (integer 25)

cyb = 10.8
print(eval('cyb'))   # 10.8
#4
# print(eval(cyb))     # throws an error (eval needs string)
print(eval('print("Hyd")'))
#Hyd
#None
print(bool('False'))        # True  (non-empty string)
print(eval('False'))        # False

#3
#print(bool(''))             # False
print(eval('  ""  '))       # empty string

#print(eval(''))             # throws an error

print(eval('  " "   '))     #   (one space string)

#print(eval(' '))            # throws an error

x = eval(input('Enter any input : '))
print(type(x))
print(x)
a = input('Enter any string : ')
print(len(a))
print(a) #3
#hyd
b = eval(input('Enter any string : '))
print(len(b))
print(b)