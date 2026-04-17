from  builtins  import  abs
print(abs(-35.8)) # 35.8
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32)) #32
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
print(pow(4 , pow(3 , 2))) # 42122
import  builtins
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) # 8

# Find  outputs
from builtins import kwlist #  to  import   kw  list
print(kwlist) #  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
print(keyword . kwlist) #  to  print  number  of  keywords  i.e.  35
print(type(keyword)) #  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword . kwlist) # [and , or , not , is , in , None , True , False , .....] 

#  Find  outputs  (Home  work)
from builtins import keyword # to  import   keyword  module
print(kwlist) # to  print  kwlist
#print()  to  print  number  of  keywords
#How  to  print  type  of kwlist
print(kwlist)

# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) # 3+4j
print(type(x)) # <class complex>
print(x) # 3+4j

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) # 25
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # 10.8

#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))

#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # Error
print(bool('')) # False
print(eval('  ""  ')) # empty string
print(eval('')) # Error
print(eval('  " "   ')) # empty string
print(eval(' ')) # empty string

# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) # 2
print(type(x)) # <class 'int'>
print(x) # 2

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # hyd
print(len(a)) # 3
print(a) # hyd
b = eval(input('Enter   any  string  : ')) # this is best way to read string,# sec
print(len(b)) # 3
print(b) # sec