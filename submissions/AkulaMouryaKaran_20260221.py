#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))  #35.8
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32))  # 32
import  builtins
print(builtins . abs(-25))  # 25

#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))  #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  # 5.9
print(max(25 , 10.8))  # 25
import  builtins
print(builtins . max(10 , 20 , 30))   # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5

# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))   # 0.01
print(pow(4 , pow(3 , 2)))   # 4 ^ 9
import  builtins
print(builtins . pow(2 , 3))   # 8
print(builtins . pow(-2 , -3))  # -2 ^ -3

# Find  outputs
How  to  import   kw  list

"""
from keyword import kwlist
"""

How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
"""
from keyword import kwlist
print(kwlist)
"""
How  to  print  number  of  keywords  i.e.  35

"""
from keyword import kwlist
print(len(kwlist))

"""

How  to  print  type  of kwlist  i.e.  <class 'list'>

"""
from keyword import kwlist
print(type(kwlist))
"""
print(keyword . kwlist)  ## error because there is no need of keyword. 

#  Find  outputs  (Home  work)
How  to  import   keyword  module
"""
import keyword

"""
How  to  print  kwlist
"""
import keyword
print(keyword.kwlist)
"""
How  to  print  number  of  keywords
"""
import keyword
print(len(keyword.kwlist))
"""
How  to  print  type  of kwlist
"""
import keyword
print(type(keyword.kwlist))
"""
print(kwlist)   # error 

# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x))
print(x)

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))   # hyd
hyd = 'Sec'
print(eval('hyd'))   # Sec
sec = '25'
print(eval('sec'))  # 25 .. string
print(eval(sec))  # error because arg must be str
cyb = 10.8
print(eval('cyb'))   # 10.8
print(eval(cyb))  # error because arg must be str

#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))      # None ... Nonetype

#  Find  outputs  (Home  work)
print(bool('False'))    # True
print(eval('False'))    # False
print(bool(''))          # False
print(eval('  ""  '))     # empty string is printed
print(eval(''))    # error
print(eval('  " "   '))    # space is printed  
print(eval(' '))  # error

# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x))
print(x)
''' eval() converts the object to their respective class objects'''

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a))
print(a)
b = eval(input('Enter   any  string  : '))
print(len(b))
print(b)
''' input() function is best approach to read string input because it converts any user input to string
where as eval() returns the object of the string...that returns error'''