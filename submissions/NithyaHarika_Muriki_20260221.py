#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))#OUTPUT:35.8
print(abs(-27))#OUTPUT:27
print(abs(29.5))#OUTPUT:29.5
print(abs(32))#OUTPUT:32
import  builtins
print(builtins . abs(-25))#OUTPUT:25


#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))#OUTPUT:20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))#OUTPUT:5.9
print(max(25 , 10.8))#OUTPUT:25
import  builtins
print(builtins . max(10 , 20 , 30))#OUTPUT:30
print(builtins . min(10 , 20 , 15 , 5 , 12))#OUTPUT:5



# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))#OUTPUT:0.01
print(pow(4 , pow(3 , 2)))#OUTPUT:4^9
import  builtins
print(builtins . pow(2 , 3))#OUTPUT:8
print(builtins . pow(-2 , -3))#OUTPUT:-1/8

# Find  outputs
How  to  import   kw  list
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
How  to  print  number  of  keywords  i.e.  35
How  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword . kwlist)


#  Find  outputs  (Home  work)
How  to  import   keyword  module
How  to  print  kwlist
How  to  print  number  of  keywords
How  to  print  type  of kwlist
print(kwlist)


# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x))#OUTPUT:<class 'complex'>
print(x)#OUTPUT:object of x

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))#OUTPUT:hyd
hyd = 'Sec'
print(eval('hyd'))#OUTPUT:Sec
sec = '25'
print(eval('sec'))#OUTPUT:25
print(eval(sec))#OUTPUT:25
cyb = 10.8
print(eval('cyb'))#OUTPUT:10.8
print(eval(cyb))#OUTPUT:error


#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))#OUTPUT:Hyd

#  Find  outputs  (Home  work)
print(bool('False'))#OUTPUT:True
print(eval('False'))#OUTPUT:True
print(bool(''))#OUTPUT:False
print(eval('  ""  '))#OUTPUT:empty string
print(eval(''))#OUTPUT:error
print(eval('  " "   '))#OUTPUT:<spacebar>
print(eval(' '))#OUTPUT:error


# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))#2
print(type(x))#OUTPUT:<class 'int'>
print(x)#OUTPUT:2


# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')#hello
print(len(a))#OUTPUT:5
print(a)#OUTPUT:hello
b = eval(input('Enter   any  string  : '))#good
print(len(b))#OUTPUT:4
print(b)#OUTPUT:good