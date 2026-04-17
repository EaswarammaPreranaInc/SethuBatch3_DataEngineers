# 1 . abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))  # Output : => 35.8
print(abs(-27))  # output : => 27
print(abs(29.5))  # 29.5
print(abs(32))  # => 35
import  builtins
print(builtins . abs(-25)) # => 25


# 2 . max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) # => output : 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) # output : 5.9
print(max(25 , 10.8))  # => Output : 25
import  builtins
print(builtins . max(10 , 20 , 30)) # => Output : 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # output : 5


# 3 .pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) # => Output : 0.01
print(pow(4 , pow(3 , 2)))  # output : 262144
import  builtins
print(builtins . pow(2 , 3)) # => output : 8
print(builtins . pow(-2 , -3)) # => -0.125


# 4 . Find  outputs
How  to  import   kw  list
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
How  to  print  number  of  keywords  i.e.  35
How  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword . kwlist) 


# 5 . Find  outputs  (Home  work)
How  to  import   keyword  module
How  to  print  kwlist # => output : ['False', 'None', 'True', 'and', 'as', ...]
How  to  print  number  of  keywords # => output : 35
How  to  print  type  of kwlist # => output : <class 'list'>
print(kwlist)


#6 . How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x)) # => output : <class 'complex'>
print(x)  # => output : 3+4j


# 7 . Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # => output : hyd
hyd = 'Sec' 
print(eval('hyd'))  => # output : Sec
sec = '25' 
print(eval('sec')) # => output : 25
print(eval(sec))  # => output : 25
cyb = 10.8
print(eval('cyb')) # output : 10.8 
print(eval(cyb))  # => output : Error


# 8 . Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # => output : Hyd


# 9 . Find  outputs  (Home  work)
print(bool('False')) # => output : True
print(eval('False')) # => output : False
print(bool('')) # => output : False
print(eval('  ""  ')) # =>output : ''
print(eval('')) # => output : Error
print(eval('  " "   ')) # => output : ' '
print(eval(' ')) # => output : Error
 

#10 . What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  : 10 '))
print(type(x)) # => <class 'int'>
print(x) 10


#11 . What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # => Always returns string (SAFE)
print(len(a))
print(a)
b = eval(input('Enter   any  string  : ')) # => Converts to Python type (UNSAFE for strings)
print(len(b))
print(b)