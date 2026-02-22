#  abs()  function  demo  program
from  builtins  import  abs # optional
print(abs(-35.8)) # 35.8
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32)) # 32
import  builtins # optional
print(builtins . abs(-25)) # 25



#  max()  and  min()   functions  demo  program
from  builtins  import   max , min # optional
print(max(10.8 , 20.6)) # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) #5.9
print(max(25 , 10.8)) # 25
import  builtins # optional
print(builtins . max(10 , 20 , 30)) # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5



# pow()  function  demo  program
from  builtins  import  pow # optional
print(pow(10 , -2)) # 0.01
print(pow(4 , pow(3 , 2))) # 262144
import  builtins # optional
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) # -0.125




# Find  outputs
'''How  to  import   kw  list # import keyword #From keyword import kwlist
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....] # print (keyword.kwlist) # print (kwlist)
How  to  print  number  of  keywords  i.e.  35 # print (len(keyword.kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'> # print (type ( keyword.kwlist))
'''
import keyword
print(keyword . kwlist) # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await','break', 'class', 'continue', 'def', 'del', 'e 'try', 'while', 'with', 'yield']lif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import','in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass','raise', 'return', 'try', 'while', 'with', 'yield']
 


#  Find  outputs  (Home  work)
'''How  to  import   keyword  module # import keyword 
How  to  print  kwlist  # print (keyword.kwlist)
How  to  print  number  of  keywords # print (len(keyword.kwlist))
How  to  print  type  of kwlist# print (type ( keyword.kwlist))
'''
# print(kwlist) # error 




# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x)) # <class'complex'>
print(x) # x



#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) #str  25
print(eval(sec))# int 25
cyb = 10.8
print(eval('cyb'))# 10.8 
# print(eval(cyb)) # error eval methods accepts only str



#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) #print("Hyd")---> Hyd ---> None


#  Find  outputs  (Home  work)
print(bool('False')) # true
print(eval('False')) # False 
print(bool('')) # False
print(eval('  ""  ')) # ''
# print(eval('')) # error empty str is ivalid for eval
print(eval('  " "   ')) # ' '
# print(eval(' ')) #error white space is invalid expresion



# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x)) # it converts str into current data type
print(x) # current data type



# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a))#  len (string)
print(a) # 'str'
b = eval(input('Enter   any  string  : '))
print(len(b)) # len(str)
print(b) #eval(input())