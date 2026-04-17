
 #  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))  # 35.8
print(abs(-27))  # 27
print(abs(29.5))  # 29.5
print(abs(32))  # 32
import  builtins
print(builtins . abs(-25))  # 25
 -----------------------------------:

 #  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))  # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  # 5.9
print(max(25 , 10.8))  # 25
import  builtins
print(builtins . max(10 , 20 , 30))  # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5


-----------------------------------:

 # pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))  #0.01
print(pow(4 , pow(3 , 2))) #4^9
import  builtins
print(builtins . pow(2 , 3))  #8
print(builtins . pow(-2 , -3))  #-2^-3

 -----------------------------------: 

# Find  outputs
How  to  import   kw  list   
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
How  to  print  number  of  keywords  i.e.  35
How  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword . kwlist)

 -----------------------------------:

 #  Find  outputs  (Home  work)
How  to  import   keyword  module   # import keyword
How  to  print  kwlist  # print(keyword.kwlist)
How  to  print  number  of  keywords  # print(len(keyword.kwlist))
How  to  print  type  of kwlist  # print(type(keyword.kwlist))
print(kwlist)  # print(keyword.kwlist)

-----------------------------------:

 # How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))  # 1+2j
print(type(x))  # <class 'str'>
print(x)  # 1+2j

-----------------------------------: 

#  Tricky  program
# Find  outputs  (Home  work) 
print(eval("    'hyd'   "))   # hyd
hyd = 'Sec'
print(eval('hyd'))  # Sec
sec = '25'
print(eval('sec'))  # 25
print(eval(sec))   # error
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb))  # error
-----------------------------------: 

#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))   #Hyd
			       None
-----------------------------------: 

#  Find  outputs  (Home  work)
print(bool('False'))  # True
print(eval('False'))   # false
print(bool(''))  # false
print(eval('  ""  '))  #
print(eval(''))  #
print(eval('  " "   '))  # ' '
print(eval(' '))  # error

-----------------------------------: 

# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))  'Kethan'
print(type(x))   # <class 'str'>
print(x) Kethan

-----------------------------------: 

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')  #'abc'
print(len(a))  # 3
print(a)  # abc
b = eval(input('Enter   any  string  : '))  # 'def'
print(len(b)) #3
print(b) # def