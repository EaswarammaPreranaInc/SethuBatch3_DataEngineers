#1.abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))  # 35.8
print(abs(-27))    # 27
print(abs(29.5))   # 29.5
print(abs(32))     # 32
import  builtins
print(builtins . abs(-25))  # 25



#2.max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))  # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  # 5.9
print(max(25 , 10.8)) # 25
import  builtins
print(builtins . max(10 , 20 , 30))  # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5



#3.pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))         # 0.01
print(pow(4 , pow(3 , 2)))  # 262144
import  builtins
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) # -0.125


#4.Find  outputs
from keyword import kwlist
print(kwlist)
print(len(kwlist))
print(type(kwlist))
print(keyword . kwlist) # Error

#5.Find  outputs  (Home  work)
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))
print(kwlist)    # Error



#6.How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x))   # <class 'complex'>
print(x)         # user entered number



#7.Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))  # 'hyd'
hyd = 'Sec' 
print(eval('hyd'))           # 'Sec'
sec = '25'
print(eval('sec'))           # 25
print(eval(sec))             # 25
cyb = 10.8
print(eval('cyb'))           # 10.8
print(eval(cyb))             # Error



#8.Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))   # Hyd None



#8.Find  outputs  (Home  work)
print(bool('False'))  # True
print(eval('False'))  # False
print(bool(''))       # False
print(eval('  ""  ')) # empty
print(eval(''))       # Error
print(eval('  " "   ')) # Space
print(eval(' '))        # Error



#9.What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x))  # the type depends on user input
print(x)        # what user enters that will come as output



#10.What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a))    # the len decides on user input
print(a)         # user inpput
b = eval(input('Enter   any  string  : '))
print(len(b))  # it gives Error if the user enters string or anything
print(b)       # Error
 









