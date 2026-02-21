 #  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))  # 35.8
print(abs(-27))  # 27
print(abs(29.5))  # 29.5
print(abs(32))  # 32

import  builtins
print(builtins . abs(-25))
 #  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))  # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  # 5.9
print(max(25 , 10.8))  # 25

import  builtins
print(builtins . max(10 , 20 , 30))  # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5

 # pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))   # 0.01
print(pow(4 , pow(3 , 2)))  # 262144
import  builtins
print(builtins . pow(2 , 3))   # 8
print(builtins . pow(-2 , -3))  # -0.125

# Find  outputs
How  to  import   kw  list  # from keyword import kwlist
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]  # print(kwlist)
How  to  print  number  of  keywords  i.e.  35   # print(len(keyword.kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'>  # print(type(keyword.kwlist))
print(keyword . kwlist)

#  Find  outputs  (Home  work)
How  to  import   keyword  module   # import keyword
How  to  print  kwlist  # print(keyword.kwlist)
How  to  print  number  of  keywords  #print(len(keyword.kwlist))
How  to  print  type  of kwlist  # print(type(keyword.kwlist))
print(keyword.kwlist)

# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))  # taking complex type input from user
print(type(x))  # class 'complex' 
print(x)    # complex number

 #  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))   # string string Hyd
hyd = 'Sec' # assigning hyd to sec
print(eval('hyd'))     # sec
sec = '25'
print(eval('sec'))   # 25 
print(eval(sec))   # 25  here object 25 is because integer is immutable and reusable   ===> sec = 25
cyb = 10.8
print(eval('cyb'))   # 10.8
print(eval(cyb))   # Error  here string float can't convert into into float  ==> cyc = 10.8 

 #  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) #  Hyd
                               None

 #  Find  outputs  (Home  work)
print(bool('False'))   # True
print(eval('False'))   # False
print(bool(''))        # False
print(eval('  ""  '))  # Empty line
print(eval(''))        # Error
print(eval('  " "   '))   # empty line
print(eval(' '))    # Error 

 # What  is  the  advantage  of  eval(input()) ? It automatically converts the entered text into the correct Python datatype.
x = eval(input('Enter  any  input  :  '))   eval function converts the string into the type of input we are giving.
print(type(x))   # type of the object 
print(x)  # print the output which converted using eval function

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')   # Taking input from user
print(len(a))   # length of the string
print(a)   # output
b = eval(input('Enter   any  string  : '))  # eval function converts the string into the type of input we are giving.
print(len(b))   # length of the string
print(b)  # output