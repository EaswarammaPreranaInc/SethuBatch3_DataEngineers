#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))#35.8
print(abs(-27))#27
print(abs(29.5))#29.5
print(abs(32))#32
import  builtins
print(builtins . abs(-25))#25
#============================================================================================================================================================
#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))#20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))#5.9
print(max(25 , 10.8))#25
import  builtins
print(builtins . max(10 , 20 , 30))#30
print(builtins . min(10 , 20 , 15 , 5 , 12))#5
#============================================================================================================================================================
# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))#0.01
print(pow(4 , pow(3 , 2)))#262144
import  builtins
print(builtins . pow(2 , 3))#8
print(builtins . pow(-2 , -3))#-0.125
#===========================================================================================================================================================
# Find  outputs
import keyword #How  to  import   kw  list
print(keyword.kwlist) #How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
print(len(keyword.kwlist)) #How  to  print  number  of  keywords  i.e.  35
print(type(keyword.kwlist))#How  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword.kwlist)
#===========================================================================================================================================================
#  Find  outputs  (Home  work)
from keyword import kwlist #How  to  import   keyword  module
print(kwlist)#How  to  print  kwlist
print(len(kwlist))#How  to  print  number  of  keywords
print(type(kwlist))#How  to  print  type  of kwlist
print(kwlist)
#===========================================================================================================================================================
# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) #3+4j
print(type(x))#<class complex>
print(x)#3+4j
#===========================================================================================================================================================
#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))#hyd
hyd = 'Sec'
print(eval('hyd'))#Sec
sec = '25'
print(eval('sec'))#25
print(eval(sec))#25
cyb = 10.8
print(eval('cyb'))#10.8
#print(eval(cyb))#error-argument should be str i.e '10.8'
#===========================================================================================================================================================
#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))#Hyd
#===========================================================================================================================================================
#  Find  outputs  (Home  work)
print(bool('False'))#True#non empty str
print(eval('False'))#False
print(bool(''))#False -empty str
print(eval('  ""  ')) #empty str ''
#print(eval(''))#error-doesn't eval empty str
print(eval('  " "   '))#empty
#print(eval(' '))#error can't eval
#===========================================================================================================================================================
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))#Manisha
print(type(x))#<class str>
print(x)#Manisha
#===========================================================================================================================================================
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')#Madharam Manisha
print(len(a))#16
print(a)#Madharam Manisha
b = eval(input('Enter   any  string  : '))#'Be kind' this should be str only
print(len(b))#7
print(b)#Be kind
