#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) # 35.8 Here abs converts any value into positive value.
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32)) # 32
import  builtins
print(builtins . abs(-25)) # 25

#  max()  and  min()   functions  demo  program
from  builtins  import   max , min  # min & max prints max & min objects in a data. 
print(max(10.8 , 20.6)) #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) #5.9
print(max(25 , 10.8)) #25
import  builtins
print(builtins . max(10 , 20 , 30)) # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #5

# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) #0.01
print(pow(4 , pow(3 , 2))) # pow(4,9) = 262144
import  builtins
print(builtins . pow(2 , 3)) # 2^3 = 8
print(builtins . pow(-2 , -3)) # -0.125

# Find  outputs
How  to  import   kw  list # import keyword
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....] #print(keyword.kwlist)
How  to  print  number  of  keywords  i.e.  35 #print(len(keyword.kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'> # print(type(keyword.kwlist))
print(keyword . kwlist) #It prints all the 35 elements in the list.

#  Find  outputs  (Home  work)
How  to  import   keyword  module #import keyword
How  to  print  kwlist # print(keyword.kwlist)
How  to  print  number  of  keywords #print(len(keyword.kwlist))
How  to  print  type  of kwlist #print(type(keyword.kwlist)) o/p: <class 'list'>
print(kwlist) # Error due to keyword is not defined before kwlist. It should be print(keyword.kwlist)

# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) #3+4j
print(type(x)) #<class 'complex'>
print(x) #3+4j

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd # It removes all the extra spaces and prints string
hyd = 'Sec'
print(eval('hyd')) # sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) # 25
cyb = 10.8
print(eval('cyb')) #10.8
print(eval(cyb)) #Error due to the cyb ref is pointing to the object int not str.

#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # Hyd # It is the o/p of print()
                            # None #It is the o/p of eval () here print() becomes None internally.


#  Find  outputs  (Home  work)
print(bool('False')) # True # Due to string is not empty.
print(eval('False')) #False
print(bool('')) # False due to the string is empty.
print(eval('  ""  ')) # Empty due to no value is present.
print(eval('')) # Error due to no string / value is present.
print(eval('  " "   ')) #<space>
print(eval(' ')) # Error

# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) #25 eval("25")
print(type(x)) #<class 'int'>
print(x) #25

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # Hello
print(len(a)) #5
print(a) # Hello
b = eval(input('Enter   any  string  : ')) #'Hyd' # If we removes '' it gives error it thinks as a reference name.
print(len(b)) # 3
print(b) # Hyd