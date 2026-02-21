#  abs()  function  demo  program
from  builtins  import  abs  #abs converts negative numbers into normal number
print(abs(-35.8))  #35.8 without importing bulitins or abs it works because it is bulitin module
print(abs(-27))  #27
print(abs(29.5))  #29.5
print(abs(32))  #32
import  builtins
print(builtins . abs(-25))  #25



#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))  #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  #5.9
print(max(25 , 10.8))  #25
import  builtins
print(builtins . max(10 , 20 , 30))  #30
print(builtins . min(10 , 20 , 15 , 5 , 12))  #5



# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))  #0.01
print(pow(4 , pow(3 , 2)))  #262144
import  builtins
print(builtins . pow(2 , 3))  #8
print(builtins . pow(-2 , -3))  #-0.125


# Find outputs
How to import kw list     	
How to print kw list i.e [and, or, not, is, in, None, True, False, .....]
How to print number of keywords i.e 35
How to print type of kwlist i.e  <class 'list'>
print(keyword.kwlist)



#  Find  outputs  (Home  work)
How  to  import   keyword  module  #import keyword
How  to  print  kwlist
How  to  print  number  of  keywords  #35
How  to  print  type  of kwlist  # <class 'list'>
print(kwlist)



# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))  # 3 input always reads as string then convert into complex  	
print(type(x))  # <class 'complex'>
print(x)  # 3+0j



#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))  #hyd
hyd = 'Sec'
print(eval('hyd'))  #Sec
sec = '25'
print(eval('sec'))  #25
print(eval(sec))  #25
cyb = 10.8
print(eval('cyb'))  #10.8
print(eval(cyb))  #error


#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))  #Hyd
                              None


#  Find  outputs  (Home  work)
print(bool('False'))  #True 'False' is not non-empty string
print(eval('False'))  #False
print(bool(''))  #False '' it is empty string so that's why it is False
print(eval('  ""  '))  # "" empty
print(eval(''))  #error it acts as object not value
print(eval('  " "   '))  #" " empty
print(eval(' '))  #error it is acts as object not value



# What  is  the  advantage  of  eval(input()) ?  #it convert string input into appropriate object
x = eval(input('Enter  any  input  :  '))  #108
print(type(x))  # <class 'int'>
print(x)  #108



# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')  #vishal
print(len(a))  #6
print(a)  #vishal
b = eval(input('Enter   any  string  : '))  #vishal
print(len(b))  #error
print(b)  #error