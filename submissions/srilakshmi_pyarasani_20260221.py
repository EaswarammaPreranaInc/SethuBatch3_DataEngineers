1) abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))#35.8
print(abs(-27))#27
print(abs(29.5))#29.5
print(abs(32))#32
import  builtins
print(builtins . abs(-25))#25

2) max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))#20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))#5.9
print(max(25 , 10.8))#25
import  builtins
print(builtins . max(10 , 20 , 30))#30
print(builtins . min(10 , 20 , 15 , 5 , 12))#5

3) # pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))#0.01
print(pow(4 , pow(3 , 2)))#262144
import  builtins
print(builtins . pow(2 , 3))#8
print(builtins . pow(-2 , -3))#-0.125

4) outputs
How  to  import   kw  list #import keyword
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
How  to  print  number  of  keywords  i.e.  35 #print(32(keyword.kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'>#print(type(keyword.kwlist))
print(keyword . kwlist)#[and , or , not , is , in , None , True]

5) outputs  
How  to  import   keyword  module#import keyword
How  to  print  kwlist #print(keyword.kwlist))
How  to  print  number  of  keywords #print("Number of keywords:",len(keyword.kwlist))
How  to  print  type  of kwlist #print(type(keywords.kwlist))
print(kwlist)

6) How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))#3+6j
print(type(x))#<class 'complex'>
print(x)#3+6j

7)  Tricky  program Outputs
print(eval("    'hyd'   "))#hyd
hyd = 'Sec'
print(eval('hyd'))#Sec
sec = '25'
print(eval('sec'))#25
print(eval(sec))#Error because it is not permitted
cyb = 10.8
print(eval('cyb'))#10.8
print(eval(cyb))#Error because it is not permitted

8)  Most  tricky  program outputs  
print(eval('print("Hyd")'))#Hyd
                            None

9) outputs  
print(bool('False'))#True
print(eval('False'))#False
print(bool(''))#False
print(eval('  ""  '))#Empty
print(eval(''))#error because it is not permitted
print(eval('  " "   '))#empty
print(eval(' '))#error because it is not valid

10) What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))#16
print(type(x))#<class 'int'>
print(x)#16

11) What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')#Hello
print(len(a))#5
print(a)#Hello
b = eval(input('Enter   any  string  : '))#bye
print(len(b))#error because it is not valid
print(b)#error because it is not valid