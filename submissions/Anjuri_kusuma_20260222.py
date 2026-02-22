  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))  #35.8
print(abs(-27))    #27
print(abs(29.5))   #29.5
print(abs(32))     #32
import  builtins
print(builtins . abs(-25))  #25


 #  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))   #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  #5.9
print(max(25 , 10.8))    #25
import  builtins
print(builtins . max(10 , 20 , 30))  #30
print(builtins . min(10 , 20 , 15 , 5 , 12))  #5


 # pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))   #0.01
print(pow(4 , pow(3 , 2)))  #262144
import  builtins
print(builtins . pow(2 , 3))  #8.0
print(builtins . pow(-2 , -3))  #-0.125


# Find  outputs
How  to  import   kw  list  #from keyword import*
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]   #print(kwlist)
How  to  print  number  of  keywords  i.e.  35   #print(len(kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'>  #print(type(kwlist))
print(keyword . kwlist) 


 #  Find  outputs  (Home  work)
How  to  import   keyword  module   #import keyword
How  to  print  kwlist   #print(keyword.kwlist)
How  to  print  number  of  keywords  #print(len(keyword.kwlist))
How  to  print  type  of kwlist    #print(type(keyword.kwlist))
print(kwlist)  


 # How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))  #2+4j
print(type(x))  #class 'complex'
print(x)   #2+4j


 #  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))  #'hyd'
hyd = 'Sec'  #not valid because string is immutable
print(eval('hyd'))  #
sec = '25'  # 25
print(eval('sec'))  #Sec
print(eval(sec))  #Sec
cyb = 10.8
print(eval('cyb'))  #10.8
print(eval(cyb))  #10.8


 #  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))   #Hyd


 #  Find  outputs  (Home  work)
print(bool('False'))  #True
print(eval('False'))  #False
print(bool(''))   #False
print(eval('  ""  '))  #True
print(eval(''))  #False
print(eval('  " "   '))  #True
print(eval(' '))   #True


 # What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))  #75
print(type(x))  #class'int'
print(x)  #75


 # What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')   #kusuma
print(len(a))  #6
print(a)  #kusuma
b = eval(input('Enter   any  string  : '))  #krishna
print(len(b))  #6
print(b)   #krishna