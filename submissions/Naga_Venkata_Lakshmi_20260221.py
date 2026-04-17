#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) #35.8
print(abs(-27)) #27
print(abs(29.5)) #29.5
print(abs(32)) #32
import  builtins
print(builtins . abs(-25)) #25


#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) #5.9
print(max(25 , 10.8)) #25
import  builtins
print(builtins . max(10 , 20 , 30)) #30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #5



# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) #0.01
print(pow(4 , pow(3 , 2))) #262144
import  builtins
print(builtins . pow(2 , 3)) #8
print(builtins . pow(-2 , -3)) #-0.125


# Find  outputs
import keyword
kwlist = keyword.kwlist
print(keyword.kwlist)
print(len(keyword.kwlist)
print(type(keyword.kwlist)
print(keyword . kwlist)



#  Find  outputs  (Home  work)
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist)
print(type(keyword.kwlist)
print(kwlist)



# How  to  read  complex  input ?
To read complex input we use the Complex() function along with input().
x = complex(input('Enter  complex  number  :  ')) #'3+4j'
print(type(x)) #<class 'complex'>
print(x) # (3+4j)



#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) #'hyd'
hyd = 'Sec'
print(eval('hyd')) #Sec
sec = '25'
print(eval('sec')) #25
print(eval(sec)) #25
cyb = 10.8
print(eval('cyb')) #10.8
print(eval(cyb)) #10.8




#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) #Hyd
                             None



#  Find  outputs  (Home  work)
print(bool('False')) #True
print(eval('False')) #False
print(bool('')) #False
print(eval('  ""  '))  #Empty string
print(eval('')) #Error
print(eval('  " "   ')) #" " 

print(eval(' ')) #Error


# What  is  the  advantage  of  eval(input()) ?
The Advantage of eval input is here the user can enter any value whether it is a int,float,complex,bool or str.whatever the input that the user given 
based on that eval will return the output.It is user friendly.Even we can give the multiple inputs in a single line which reduces the lines of code.

x = eval(input('Enter  any  input  :  ')) # '16'

print(type(x)) #<class 'int'>
print(x) #16  Here the eval removes the quotes of an integer.


# What  is  a  better  approach  to  read  string  input ?
To use input() alone for strings and explicit conversion(like
int(), float()) for specific types.


a = input('Enter  any  string  :  ') # "Lakshmi"
print(len(a)) #7
print(a) #Lakshmi
b = eval(input('Enter   any  string  : ')) # "Sushma"
print(len(b)) #6
print(b) #Sushma














