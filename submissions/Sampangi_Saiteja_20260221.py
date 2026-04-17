#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))#35.8
print(abs(-27))#27
print(abs(29.5))#29.5
print(abs(32))#32
import  builtins
print(builtins . abs(-25))#25

#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))#20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))#5.9
print(max(25 , 10.8))#25
import  builtins
print(builtins . max(10 , 20 , 30))#30
print(builtins . min(10 , 20 , 15 , 5 , 12))#

# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))#0.01
print(pow(4 , pow(3 , 2)))#4096
import  builtins
print(builtins . pow(2 , 3))#8
print(builtins . pow(-2 , -3))#-8

# Find  outputs
How  to  import   kw  list # from import km   #import keywords
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]#print(keyword.kwlist)
How  to  print  number  of  keywords  i.e.  35#print(s.keywords)
How  to  print  type  of kwlist  i.e.  <class 'list'> #print(kw type)
print(keyword . kwlist)#key words up to 35

#  Find  outputs  (Home  work)
How  to  import   keyword  module# from builtins import keyword
How  to  print  kwlist#print(kwlist)
How  to  print  number  of  keywords#print(keyword . kwlist)
How  to  print  type  of kwlist#2
print(kwlist)#kwlist


# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))==>complex('3+4j')==>3+4j
print(type(x))#<class 'complex'>
print(x)#3+4j


#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))#'hyd'
hyd = 'Sec'
print(eval('hyd'))#Sec
sec = '25'
print(eval('sec'))#sec
print(eval(sec))#25
cyb = 10.8
print(eval('cyb'))#cyd
print(eval(cyb))#10.8

#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))#print Hyd

#  Find  outputs  (Home  work)
print(bool('False'))#True
print(eval('False'))#False
print(bool(''))#False
print(eval('  ""  '))#""
print(eval(''))#<Empty>
print(eval('  " "   '))#" "
print(eval(' '))#<emty>

# What  is  the  advantage  of  eval(input()) ?# Without using typecasting We can easily convert Anything Sequences and non sequences
x = eval(input('Enter  any  input  :  '))#25
print(type(x))#<class 'int'>
print(x)#25

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')#rama
print(len(a))#4
print(a)#rama
b = eval(input('Enter   any  string  : '))#saiteja
print(len(b))#7
print(b)#saiteja
