#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) #O/P: 35.8
print(abs(-27))   #O/P: 27
print(abs(29.5))  #O/P:29.5
print(abs(32))    #O/P:32
import  builtins
print(builtins . abs(-25)) #O/P:25


 #  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) #O/P: 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) #O/P: 5.9
print(max(25 , 10.8)) #O/P: 10.8
import  builtins
print(builtins . max(10 , 20 , 30)) #O/P:30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #O/P:5


 # pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) #O/P: 1/10^-2 = 1/100 = 0.01
print(pow(4 , pow(3 , 2))) #O/P: 3^2=9 = pow(4,9)=4^9 =262144
import  builtins
print(builtins . pow(2 , 3)) #O/P: 2^3 = 8
print(builtins . pow(-2 , -3)) #O/P: 1/-2^3=1/-8 = -0.125


 #  Find  outputs  (Home  work)
How  to  import   keyword  module #O/P: import keyword
How  to  print  kwlist # O/P: print(keyword.kwlist)
How  to  print  number  of  keywords # O/P:print(len(keyword.kwlist))
#O/P:
print(kwlist)
'''import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))'''

 # How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) # O/P:Enter complex number :2+4j
print(type(x)) # O/P: <class 'complex'>
print(x) # O/P:2+4j





 #  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) #O/P:'hyd'
hyd = 'Sec'
print(eval('hyd')) #O/P:'Sec'
sec = '25'
print(eval('sec')) #O/P:'25'
print(eval(sec))   #O/P:'25'
cyb = 10.8
print(eval('cyb'))  #O/P:'10.8'
print(eval(cyb))    O/P : TypeError


 #  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) #O/P : "Hyd"


 #  Find  outputs  (Home  work)
print(bool('False')) #O/P : True
print(eval('False'))#O/P : False
print(bool(''))  #O/P : False
print(eval('  ""  ')) #O/P : 'empty str'
print(eval('')) #O/P : Error
print(eval('  " "   ')) #O/P : 'empty str'
print(eval(' ')) #O/P : SyntaxError



 # What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) #O/P : entering input : 25
print(type(x)) #O/P : <class 'int'>
print(x) #O/P : 25


 # What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') #O/P : Better
print(len(a))#O/P : 6
print(a) #O/P : Better
b = eval(input('Enter   any  string  : ')) #O/P: entering input :Windows
print(len(b))#O/P : 7
print(b) #O/P : Windows

