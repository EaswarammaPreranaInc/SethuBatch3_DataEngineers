#  abs()  function  demo  program
from  builtins  import  abs # Members of module are imported, but not module
print(abs(-35.8)) # 35.8
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32)) # 32
import  builtins # Module is imported but not members of module imported
print(builtins . abs(-25))  # 25

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
print(pow(4 , pow(3 , 2))) # pow(4, 9) = 4^9
import  builtins
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) # (-2)^(-3)

# Find  outputs
# How  to  import   kw  list # import keyword or from keyword import kwlist
# How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....] 
# import keyword , print(keyword.kwlist)
# How  to  print  number  of  keywords  i.e.  35 # print(len(keyword.kwlist))
# How  to  print  type  of kwlist  i.e.  <class 'list'> # print(type(keyword.kwlist))
# print(keyword . kwlist) # prints list of keywords

#  Find  outputs  (Home  work)
# How  to  import   keyword  module # import keyword
# How  to  print  kwlist # from keyword import kwlist
# How  to  print  number  of  keywords # print(len(keyword.kwlist))
# How  to  print  type  of kwlist # print(type(keyword.kwlist))
print(kwlist) # prints list of keywords

# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) # 3+4j
print(type(x)) # <class 'complex'>
print(x) # 3+4j

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd ( string)
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) # 25 (string)
print(eval(sec)) #  25 (integer)
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # Error

#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # Hyd

#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # Empty string
print(eval('')) # No string is given in input
print(eval('  " "   ')) # String with space
print(eval(' ')) # No string is given in input

# What  is  the  advantage  of  eval(input()) ? # it will do Multiple functions 
x = eval(input('Enter  any  input  :  ')) # 25 takes as string 25
print(type(x)) # <class 'int'>
print(x) # 25  integer

# What  is  a  better  approach  to  read  string  input ? # eval(input("prompt message"))
a = input('Enter  any  string  :  ') # Vani
print(len(a))  # 4
print(a) # Vani
b = eval(input('Enter   any  string  : ')) # Vani
print(len(b)) # Error , bcz input taken as string and the string is converted to obj which is not defined
print(b) # Error