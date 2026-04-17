#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) # 35.8
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32)) # 32
import  builtins
print(builtins . abs(-25)) # 25



#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) # 5.9
print(max(25 , 10.8)) # 25
import  builtins
print(builtins . max(10 , 20 , 30))# 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5



# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) # 0.01
print(pow(4 , pow(3 , 2))) # 262144
import  builtins 
print(builtins . pow(2 , 3))# 8
print(builtins . pow(-2 , -3)) # -0.125



# Find  outputs
How  to  import   kw  list # import keyword
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....] 
How  to  print  number  of  keywords  i.e.  35
How  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword . kwlist)  #[and , or , not , is , in , None , True , False , .....]


#  Find  outputs  (Home  work)
How  to  import   keyword  module # import keyword
How  to  print  kwlist # print(keyword.kwlist)
How  to  print  number  of  keywords #print(len(keyword.kwlist))
How  to  print  type  of kwlist # class int
print(kwlist) # Error


# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) # (3 + 4j)
print(type(x)) # class complex
print(x) # (3+4j)


#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # 'hyd'
hyd = 'Sec'
print(eval('hyd')) # sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) # 25
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # Error because the object not in string form

#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # Hyd next line None


#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # True
print(eval('')) # Empty
print(eval('  " "   ')) # True
print(eval(' ')) # Empty



# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) # 'Hyd'
print(type(x)) # class str
print(x)# Hyd


# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # 'Hyd'
print(len(a)) # 5
print(a) # Hyd
b = eval(input('Enter   any  string  : ')) # 'Hyd'
print(len(b)) # 3
print(b) # Hyd
 Eval is best for me






