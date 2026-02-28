#  abs()  function  demo  program
from  builtins  import  abs #optional
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
import  builtins #bmandatory
print(builtins . max(10 , 20 , 30)) # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5

# pow()  function  demo  program
from  builtins  import  pow #optional
print(pow(10 , -2)) # 0.01
print(pow(4 , pow(3 , 2))) # 262144
import  builtins # mandatory
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) # -0.125

# Find  outputs
from keyword import kwlist #  to  import   kw  list
print(kwlist) #  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
print(len(kwlist)) #  to  print  number  of  keywords  i.e.  35
print(type(kwlist)) #  to  print  type  of kwlist  i.e.  <class 'list'>
#print(keyword . kwlist) # error bcz we didn't imported keyword module 

#  Find  outputs  (Home  work)
import keyword # to  import   keyword  module
print(keyword.kwlist) # to  print  kwlist
print(len(keyword.kwlist)) # to  print  number  of  keywords
print(type(keyword.kwlist)  # to  print  type  of kwlist
#print(kwlist) error kwlist not imported

# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) # 3+4j
print(type(x)) # <class complex>
print(x) # 3+4j

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # 'hyd'
hyd = 'Sec'
print(eval('hyd')) # 'Sec'
sec = '25'
print(eval('sec')) # '25'
print(eval(sec)) # 25 converts string object to respective object
cyb = 10.8
print(eval('cyb')) # 10.8
#print(eval(cyb)) # Error bcz argument has to be in string

#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # Hyd 
                            # None

#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # Empty string
#print(eval('')) # Error
print(eval('  " "   ')) # space
#print(eval(' ')) # Error

# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) # 2
print(type(x)) # <class 'int'>
print(x) # 2

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # hyd
print(len(a)) # 3
print(a) # hyd
b = eval(input('Enter   any  string  : ')) # this isn't better way,# "sec"
print(len(b)) # 3
print(b) # sec
