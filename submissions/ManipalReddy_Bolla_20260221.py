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
print(builtins . min(10 , 20 , 15 , 5 , 12))#5

# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))#0.01
print(pow(4 , pow(3 , 2)))#262144
import  builtins
print(builtins . pow(2 , 3))#8
print(builtins . pow(-2 , -3))#-0.125

# Find  outputs
How  to  import   kw  list #import keyword
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]#print(keyword.kwlist)
How  to  print  number  of  keywords  i.e.  35 #print(len(keyword.kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'> #print(type(keyword.kwlist))
print(keyword . kwlist)#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#  Find  outputs  (Home  work)
How  to  import   keyword  module#import keyword
How  to  print  kwlist#print(keyword.kwlist)
How  to  print  number  of  keywords#print(len(keyword.kwlist))
How  to  print  type  of kwlist#print(type(keyword.kwlist))
print(kwlist)#error

# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))#4+4j
print(type(x))#class 'complex'
print(x)#4+4j

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))#'hyd'
hyd = 'Sec'
print(eval('hyd'))#Sec
sec = '25'
print(eval('sec'))#'25'
print(eval(sec))#25
cyb = 10.8
print(eval('cyb'))#10.8
print(eval(cyb))#error

#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))#Hyd <next line> None

#  Find  outputs  (Home  work)
print(bool('False'))#True
print(eval('False'))#False
print(bool(''))#False
print(eval('  ""  '))#''
print(eval(''))#error
print(eval('  " "   '))#' '
print(eval(' '))#error

# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))#4
print(type(x))#class 'int'
print(x)#4

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')#Python
print(len(a))#6
print(a)#Python
b = eval(input('Enter   any  string  : '))#'Python'
print(len(b))#6
print(b)#Python
