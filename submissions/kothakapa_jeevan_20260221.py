#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) ---> 35.8
print(abs(-27)) ---> 27
print(abs(29.5)) ---> 29.5
print(abs(32)) ---> 32
import  builtins
print(builtins . abs(-25)) -->

#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))  ---> 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) ---> 5.9
print(max(25 , 10.8))  ---> 25
import  builtins
print(builtins . max(10 , 20 , 30)) ----> 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) --> 5

# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) ---> 0.01
print(pow(4 , pow(3 , 2))) --->
import  builtins
print(builtins . pow(2 , 3)) ---> 8
print(builtins . pow(-2 , -3)) --> -0.125


# Find  outputs
How  to  import   kw list 
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
How  to  print  number  of  keywords  i.e.  35
How  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword.kwlist)

#  Find  outputs  (Home  work)
How  to  import   keyword  module ---> import keyword 
How  to  print  kwlist	---> print(keyword.kwlist)
How  to  print  number  of  keywords ----> print(len(keyword.kwlist))
How  to  print  type  of kwlist ---> print(type(keyword))
print(kwlist) ---> print(keyword.kwlist)


# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x)) --> str type
print(x) ---> Enter  complex  number  :  6
#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) --> hyd
hyd = 'Sec'
print(eval('hyd')) ---> sec
sec = '25'
print(eval('sec')) ---> sec
print(eval(sec)) ---> error
cyb = 10.8
print(eval('cyb')) ---> cyb
print(eval(cyb)) ---> error


#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) ---> first it prints Hyd and in return it gives None
#  Find  outputs  (Home  work)
print(bool('False')) ---> True
print(eval('False')) ---> False
print(bool('')) ---> False
print(eval('  ""  ')) ---> error 
print(eval(''))   ---> error
print(eval('  " "   ')) --> empty str ( here space is occupied)
print(eval(' ')) ---> error


# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x)) ---> type depends on the what user gives
print(x) ---> type depends on the what user gives
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a)) ---> len depends on the what user gives
print(a) ---> prints what user gives
b = eval(input('Enter   any  string  : '))
print(len(b)) ---> len (b) depends on user and we have eval function here it will gives appropriate type
print(b) ---> prints what user gives