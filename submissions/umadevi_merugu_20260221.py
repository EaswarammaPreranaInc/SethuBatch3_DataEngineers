#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) #35.8
print(abs(-27)) #27
print(abs(29.5))#29.5
print(abs(32))#32
###########################################################
import  builtins
print(builtins . abs(-25)) #25
###########################################################3
#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) #5.9
print(max(25 , 10.8)) #25
######################################################
import  builtins
print(builtins . max(10 , 20 , 30)) #30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #5
###########################################################
# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) #10^-2=0.01
print(pow(4 , pow(3 , 2))) # 4^(3^2)==>4^9=262144
###########################################################
import  builtins
print(builtins . pow(2 , 3)) # 2^3=8
print(builtins . pow(-2 , -3)) #-2^-3=-0.125
###########################################################
# Find  outputs
How  to  import   kw  list #import keyword
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....] from keyword import kwlist
How  to  print  number  of  keywords  i.e.  35 #print(keyword.kwlist)
How  to  print  type  of kwlist  i.e.  <class 'list'> #print(type*(keyword.kwlist))
print(keyword . kwlist) #prints all keywords
############################################################
#Find  outputs  (Home  work)
How  to  import   keyword  module #import keyword
How  to  print  kwlist #kwlist = keyword.kwlist
print(kwlist)  
How  to  print  number  of  keywords #print(len(kwlist))
How  to  print  type  of kwlist #print(type(kwlist)) 
print(kwlist) #Complete list of Python reserved keywords
###########################################################
# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x)) #<class 'complex')
print(x) #complex number
###########################################################
#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) #hyd
hyd = 'Sec'#error
print(eval('hyd')) #error
sec = '25' 
print(eval('sec'))#25
print(eval(sec)) #25
cyb = 10.8
print(eval('cyb')) #10.8
print(eval(cyb)) #error
###########################################################
#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) #Hyd None
###########################################################
 #  Find  outputs  (Home  work)
print(bool('False')) #1
print(eval('False')) #0
print(bool('')) #0
print(eval('  ""  '))#empty string
print(eval(''))#error
print(eval('  " "   '))# empty string
print(eval(' '))# error
###########################################################
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x)) #<class 'typeofobject'>
print(x) #value of object
###########################################################
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a)) #len of a str
print(a) #prints str object
b = eval(input('Enter   any  string  : '))
print(len(b)) #length of an object
print(b) #prints value of an object