#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) # 35.8
print(abs(-27))   # 27
print(abs(29.5))  # 29.5
print(abs(32))    # 32
import  builtins
print(builtins . abs(-25)) # 25

# max()  and  min()   functions  demo  program

from  builtins  import   max , min
print(max(10.8 , 20.6)) # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) # 5.9
print(max(25 , 10.8)) # 25
import  builtins
print(builtins . max(10 , 20 , 30))  # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5

#pow()  function  demo  program

from  builtins  import  pow
print(pow(10 , -2)) # 0.001
print(pow(4 , pow(3 , 2))) # 3 ^ 2 = 9 , 4 ^ 9 = 262144
import  builtins
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) # -0.125

# Find  outputs
How  to  import   kw  list #  Using kwlist from keyword module

#How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....] 
import keyword 
print(keyword.kwlist)

#How  to  print  number  of  keywords  i.e.  35 
import keyword
print(len(keyword.kwlist))

#How  to  print  type  of kwlist  i.e.  <class 'list'>
import keyword
print(type(keyword.kwlist))

print(keyword . kwlist) # prints the list of Python keywords

#  Find  outputs  (Home  work)
How  to  import   keyword  module # Using import keyword

#How  to  print  kwlist
import keyword
print(keyword.kwlist)

#How  to  print  number  of  keywords
import keyword
print(len(keyword.kwlist))

#How  to  print  type  of kwlist
print(kwlist)

# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))  # converts string into complex number 2+3j
print(type(x)) # <class 'complex'>
print(x) # (2+3j)




#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))     # eval() removes extra spaces and evaluates the string --> hyd

hyd = 'Sec'
print(eval('hyd'))  # Sec

sec = '25'
print(eval('sec')) # '25'
print(eval(sec)) # int 25

cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # Error argument should be string


#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # Hyd

#  Find  outputs  (Home  work)
print(bool('False')) #  Non-empty string -> True
print(eval('False')) #  False
print(bool(''))      #  Empty string -> False
print(eval('  ""  ')) # empty string -> ''
print(eval(''))     # Error
print(eval('  " "   '))  # Error
print(eval(' '))  # Error

# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x))  # <class 'str'>
print(x) # Value of x

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # input() always returns a string -> input() is best
print(len(a)) # len of input a
print(a)   # string entered by the user

b = eval(input('Enter   any  string  : ')) # must enter string inside quotes
print(len(b)) # len of input b
print(b) # string entered by the user

