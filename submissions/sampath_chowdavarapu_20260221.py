#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) # 35.8
print(abs(-27))  # 27
print(abs(29.5)) # 29.5
print(abs(32)) # 32
import  builtins
print(builtins . abs(-25)) # 25


#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))  # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  # 5.9
print(max(25 , 10.8))  # 25
import  builtins
print(builtins . max(10 , 20 , 30))  # 30
print(builtins . min(10 , 20 , 15 , 5 , 12))  # 5


# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))  # 0.01
print(pow(4 , pow(3 , 2)))  # pow(4,9) --->262144
import  builtins
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3))  # -0.125


# How  to  import   kw  list   # import keyword
# How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]  # import keyword
print(keyword.kwlist)
# How  to  print  number  of  keywords  i.e.  35   c))
# How  to  print  type  of kwlist  i.e.  <class 'list'>   # print(type(keyword.kwlist))
print(keyword . kwlist)  #  [and , or , is , in , None , True , False , yield , return , try , except , for , while , if , else , elif , as , break , continue , class , def , del , from ,global , import , not]


# How  to  import   keyword  module # import keyword
# How  to  print  kwlist   #  import keyword
print(keyword.kwlist)

# How  to  print  number  of  keywords   #  print(len(keyword.kwlist))
# How  to  print  type  of kwlist    #  print(type(keyword.kwlist))
print(kwlist)  # error 


x = complex(input('Enter  complex  number  :  '))  #  ex: 2+1j
print(type(x))  # <class 'complex'> 
print(x)  # 2+1j


# Find  outputs  (Home  work)
print(eval("    'hyd'   "))  # hyd
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec))  # 25
cyb = 10.8
print(eval('cyb'))  # 10.8
print(eval(cyb))   # error


#  Find  output  (Home  work)
print(eval('print("Hyd")'))   #  Hyd
   

print(bool('False'))  # True
print(eval('False'))  # False
print(bool(''))       # False
print(eval('  ""  '))  # empty string
print(eval(''))       # ''
print(eval('  " "   '))  # empty string
print(eval(' '))   # error


x = eval(input('Enter  any  input  :  '))  # 9
print(type(x))   # <class 'int'>
print(x)   # 9


# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')   # abc
print(len(a))  # 3
print(a)  # abc
b = eval(input('Enter   any  string  : '))  # "xyz"
print(len(b))  # 3 
print(b)  # xyz