[9:09 pm, 23/02/2026] Mani: #  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) #Output: Error
print(abs(-27)) #Output: 27
print(abs(29.5)) #Output: 29.5
print(abs(32)) #Output: 32
import  builtins
print(builtins . abs(-25)) #Output:25
#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))#Output:20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) #Output:5.9
print(max(25 , 10.8)) #Output:
import  builtins
print(builtins . max(10 , 20 , 30)) #Output:30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #Output:5
# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) #Output:0.01
print(pow(4 , pow(3 , 2))) #Output:262144
import  builtins
print(builtins . pow(2 , 3)) #Output:8
print(builtins . pow(-2 , -3)) #Output:-0.125
# Find  outputs
How  to  import   kw  list
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
How  to  print  number  of  keywords  i.e.  35
How  to  print  type  of kwlist  i.e.  <class 'list'>
from keyword import kwlist
 print(kwlist)
 print(len(keyword.kwlist))
 print(type(kwlist))

#  Find  outputs  (Home  work)
How  to  import   keyword  module
How  to  print  kwlist
How  to  print  number  of  keywords
How  to  print  type  of kwlist
#import keyword
 print(keyword.kwlist)
 print(keyword . kwlist)
 print(len(keyword.kwlist))
 print(kwlist)
# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) #3+4j
print(type(x)) #Output:<class 'complex'>
print(x) #Output:(3+4j)
#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) #Output:'hyd'
hyd = 'Sec'
print(eval('hyd')) #Output:'Sec'
sec = '25'
print(eval('sec')) #Output: '25'
print(eval(sec)) #Output:'25'
cyb = 10.8
print(eval('cyb')) #Output:10.8
print(eval(cyb)) #Output:Error
#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) #Output:'None'
#  Find  outputs  (Home  work)
print(bool('False')) #Output:True
print(eval('False')) #Output:False
print(bool('')) #Output:False
print(eval('  ""  ')) #Output:""
print(eval('')) #Output:Error
print(eval('  " "   ')) #Output:""
print(eval(' ')) #Output:Error
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))#'hyd'
print(type(x)) #Output:<class 'str'>
print(x) #Output:'hyd'
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')#'cyb'
print(len(a)) #Output:3
print(a) #Output:'cyb'
b = eval(input('Enter   any  string  : ')) #Rama Rao
print(len(b)) #Output:8
print(b) #Output:'Rama Rao
