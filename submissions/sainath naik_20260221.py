# 1. abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))  # => 35.8
print(abs(-27))   # => 27
print(abs(29.5))  # => 29.5
print(abs(32))    # => 32
import  builtins
print(builtins . abs(-25)) # => 25



# 2. max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))               # => 20,6
print(min(10.8 , 20.6 , 5.9 , 12.3))  # => 5.9
print(max(25 , 10.8))                 # => 25
import  builtins
print(builtins . max(10 , 20 , 30))   # => 30
print(builtins . min(10 , 20 , 15 , 5 , 12)  #=> 5

# 3. pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))  #=>  0.01
print(pow(4 , pow(3 , 2))) # => 262144
import  builtins
print(builtins . pow(2 , 3)) # => 8
print(builtins . pow(-2 , -3)) # => -0.125


# 4. Find  outputs
How  to  import   kw  list
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
How  to  print  number  of  keywords  i.e.  35
How  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword . kwlist)


#  5. Find  outputs  (Home  work)
How  to  import   keyword  module
How  to  print  kwlist      # => ['False', 'None', 'True', 'and', 'as',...]  
How  to  print  number  of  keywords # => 35
How  to  print  type  of kwlist # => <class 'list'>
print(kwlist)  # => [int ,float ,complex ,bool ,Nonetype]


# 6. How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x)) # => <class 'complex'>
print(x)  # => 3+4j


# 7. Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # => hyd
hyd = 'Sec'
print(eval('hyd'))  # => Sec
sec = '25'
print(eval('sec'))  # => 25
print(eval(sec))    # => 25
cyb = 10.8
print(eval('cyb'))  # => 10.8
print(eval(cyb))    # => Error
 


# 8. Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # => Hyd


# 9. Find  outputs  (Home  work)
print(bool('False')) # => True
print(eval('False')) # => False
print(bool(''))      # => False
print(eval('  ""  ')) # => ''
print(eval(''))        # => Error
print(eval('  " "   ')) # => ' '
print(eval(' '))       # => Error


# 10. What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x))  # => <class 'int'>
print(x)      # => 10


# 11. What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a))   # => Always returns string (SAFE)
print(a)
b = eval(input('Enter   any  string  : ')) # => Converts to python type (UNSAFE for strings)
print(len(b))     
print(b)
