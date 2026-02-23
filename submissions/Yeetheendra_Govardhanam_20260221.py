#Topic-1
#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) # 35.8
print(abs(-27)) #27
print(abs(29.5)) #29.5
print(abs(32)) #32
import  builtins
print(builtins . abs(-25)) #25
 #Topic-2
#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) #5.9
print(max(25 , 10.8)) #25
import  builtins
print(builtins . max(10 , 20 , 30)) #30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5 
#Topic-3
# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) 0.01
print(pow(4 , pow(3 , 2))) #212144
import  builtins
print(builtins . pow(2 , 3))  #8
print(builtins . pow(-2 , -3)) # -0.125
#Topic-4
# Find  outputs
#How  to  import   kw  list 
from  keyword import *
#How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
print(kwlist)
#How  to  print  number  of  keywords  i.e.  35
print(len(kwlist))
#How  to  print  type  of kwlist  i.e.  <class 'list'>
print(type(kwlist))
import keyword
print(keyword . kwlist) #full list 35 keywords

#Topic-5
#  Find  outputs  (Home  work)
#How  to  import   keyword  module
import keyword
#How  to  print  kwlist
print(keyword . kwlist)
#How  to  print  number  of  keywords
print(len(keyword . kwlist))
#How  to  print  type  of kwlist
print(type(keyword . kwlist))
#print(kwlist) # error there is no that kind of object

#Topic-6
# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) #”5+12j”
print(type(x)) # <class ‘complex’>
print(x) #5 + 12j
#Topic-7
#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) #hyd
hyd = 'Sec'
print(eval('hyd')) #Sec
sec = '25'
print(eval('sec')) #25 (str)
#print(eval(sec)) #25 (int)
cyb = 10.8
print(eval('cyb')) #10.8
#print(eval(cyb))  #error it is not in string
#Topic-8
#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) #Hyd 
			      #None (After print it returns None)
#Topic-9
#  Find  outputs  (Home  work)
print(bool('False')) #True
print(eval('False')) #False
print(bool('')) #False
print(eval('  ""  ')) #<empty>
#print(eval('')) # empty sting is not allowed
print(eval('  " "   ')) #<empty>
#print(eval(' ')) # empty sting is not allowed

#Topic-10
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) # checkers the type of String object
print(type(x)) #<class ‘object_type’>
print(x) #object
#Topic-11
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') #Hello
print(len(a)) #5
print(a) # Hello
b = eval(input('Enter   any  string  : ')) #Sharma
print(len(b)) #6
print(b)#Sharma
