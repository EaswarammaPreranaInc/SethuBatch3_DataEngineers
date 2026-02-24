import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))

***

import keyword          # To import keyword module

print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', ... ]  (all python keywords list)

print(len(keyword.kwlist))
# Some number (for example 35 – depends on python version)

print(type(keyword.kwlist))
# <class 'list'>

print(keyword.kwlist)
# Again prints list of all keywords


***

x = complex(input('Enter complex number : '))
print(type(x))
print(x)

***

print(type(x))   # <class 'complex'>
print(x)         # (3+4j)

***


print(eval("    'hyd'   "))   
# hyd

***


hyd = 'Sec'
print(eval('hyd'))   
# Sec

***

sec = '25'
print(eval('sec'))   
# 25   (string '25')

print(eval(sec))     
# 25   (converted to int)

***

cyb = 10.8
print(eval('cyb'))   
# 10.8

print(eval(cyb))     
# Error (eval argument must be string)

***

print(eval('print("Hyd")'))

#Hyd
None

***


print(bool('False'))      
# True  (non-empty string)

print(eval('False'))      
# False

print(bool(''))           
# False

print(eval('  ""  '))     
# ''  (empty string)

print(eval(''))           
# Error (invalid syntax)

print(eval('  " "   '))   
# ' '  (one space)

print(eval(' '))          
# Error (invalid syntax)

***

x = eval(input('Enter any input : '))
print(type(x))
print(x)

***

a = input('Enter any string : ')
print(len(a))
print(a)

***


b = eval(input('Enter any string : '))
print(len(b))
print(b)
