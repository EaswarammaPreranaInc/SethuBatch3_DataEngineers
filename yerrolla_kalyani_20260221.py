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
print(pow(4 , pow(3 , 2)))#4^9=262144
import  builtins
print(builtins . pow(2 , 3))#8
print(builtins . pow(-2 , -3))#1/-2^3=1/-8=-0.125

 # Find  outputs
How  to  import   kw  list#import keyword
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]#print(keywords.kwlist)
How  to  print  number  of  keywords  i.e.  35#print(len(keyword.kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'>
print(type(keyword . kwlist))

 #  Find  outputs  (Home  work)
How  to  import   keyword  module #import keyword
How  to  print  kwlist#print(keywords.kwlist)
How  to  print  number  of  keywords#print(len(keyword.kwlist))
How  to  print  type  of kwlist#print(type(keyword.kwlist))
print(kwlist)

# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))#reads input ,and converts it in to the complex eg:3+4j
print(type(x))#<class 'complex'>
print(x)#print input complex number (3+4j)

 #  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))#'hyd'
hyd = 'Sec'
print(eval('hyd'))#Sec
sec = '25'
print(eval('sec'))#25
print(eval(sec))#error 
cyb = 10.8
print(eval('cyb'))#10.8
print(eval(cyb))#error becoz it converts string literal but cyb it is not string

#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))#None

#  Find  outputs  (Home  work)
print(bool('False'))#True
print(eval('False'))#False
print(bool(''))#False
print(eval('  ""  '))#""
print(eval(''))#error
print(eval('  " "   '))#" "
print(eval(' '))#space(nothing is printed)

 # What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))#reads input,converts string object to appropriate class object 
print(type(x))## appropriate class object 
print(x)#object is printed 

 # What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')#reads input 
print(len(a))#length of the string
print(a)#prints a 
b = eval(input('Enter   any  string  : '))#reads input,converts string object to appropriate class object 
print(len(b))#length of the input object
print(b)#print b 