#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) # 35.8
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32)) # 32
import  builtins
print(builtins . abs(-25)) # 25


#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) # 5.9
print(max(25 , 10.8)) # 25
import  builtins
print(builtins . max(10 , 20 , 30)) # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5


# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) # 0.01
print(pow(4 , pow(3 , 2))) #262144
import  builtins
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) # -0.125


# Find  outputs
How  to  import   kw  list # import kw module or import keyword module
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....] # import keyword
How  to  print  number  of  keywords  i.e.  35 # import keyword
How  to  print  type  of kwlist  i.e.  <class 'list'> # import keyword
print(keyword . kwlist) # [and , or , not , is , in , None , True , False , ....]


#  Find  outputs  (Home  work)
How  to  import   keyword  module # import keyword
How  to  print  kwlist # import keyword
How  to  print  number  of  keywords # import keyword
How  to  print  type  of kwlist # import keyword
print(kwlist) # Error


# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) # 4 + 2j
print(type(x)) # <class 'complex'>
print(x) # 4 + 2j


#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd
hyd = 'Sec'
print(eval('hyd')) # sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) # 25
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # 10.8


#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # print(eval(Hyd))----> print (Hyd)---> Error

#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # Empty
print(eval('')) # Error
print(eval('  " "   ')) # True
print(eval(' ')) # Error


# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) # 12
print(type(x)) # <class 'int'>
print(x) # 12


# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # Bhanu
print(len(a)) # 5
print(a) # Bhanu
b = eval(input('Enter   any  string  : ')) # Bhanu
print(len(b)) # 5
print(b) # Bhanu