#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) #35.8
print(abs(-27)) #27
print(abs(29.5)) #29.5
print(abs(32)) #32.0
import  builtins 
print(builtins . abs(-25)) #25.0
turns negative values to positive float values 

#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) # 5.9
print(max(25 , 10.8)) # 25
import  builtins
print(builtins . max(10 , 20 , 30)) #30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #5
returns the max or min values based on the function we use 

# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) # 10^-2 = 0.01
print(pow(4 , pow(3 , 2))) # first inner function executes and then outer executes 3^2=9 4^9262144
import  builtins
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) # -0.125
# Find  outputs
How  to  import   kw  list # import keyword
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....] # print(keyword.kwlist)
How  to  print  number  of  keywords  i.e.  35 # print(len(keyword.kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'>  # print(type(keyword.kwlist))

# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x)) # <class ‘complex’>
print(x) # 3+4j

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) #’hyd’
hyd = 'Sec' 
print(eval('hyd')) #sec
sec = '25' 
print(eval('sec')) # 25
print(eval(sec)) # 25
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # Error as args must be having string

#  Most  tricky  program
#  Find  output  (Home  work)
X = print(eval('print("Hyd")') # Hyd, None

 #  Find  outputs  (Home  work)
print(bool('False')) #True
print(eval('False'))#False
print(bool(''))#False
print(eval('  ""  ')) # Empty
print(eval('')) #Error
print(eval('  " "   '))# Empty
print(eval(' ')) #Error
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) #5
print(type(x)) #<class ‘int’>
print(x) # 5
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') #hi
print(len(a)) #2
print(a)#”hi”
b = eval(input('Enter   any  string  : ')) # hi
print(len(b)) #Throws Error 
print(b) 
