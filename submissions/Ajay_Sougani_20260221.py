#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))        # 35.8
print(abs(-27))          # 27
print(abs(29.5))         # 29.5
print(abs(32))           # 32
import  builtins
print(builtins.abs(-25)) # 25


#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))              # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  # 5.9
print(max(25 , 10.8))                # 25
import  builtins
print(builtins.max(10 , 20 , 30))    # 30
print(builtins.min(10 , 20 , 15 , 5 , 12))  # 5


# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))          # 0.01
print(pow(4 , pow(3 , 2)))   # 262144
import  builtins
print(builtins.pow(2 , 3))   # 8
print(builtins.pow(-2 , -3)) # -0.125


import keyword
print(keyword.kwlist)          # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', ...]
print(len(keyword.kwlist))     # 35
print(type(keyword.kwlist))    # <class 'list'>
print(keyword.kwlist)          # ['False', 'None', 'True', ...]


import keyword
kwlist = keyword.kwlist
print(kwlist)              # ['False', 'None', 'True', ...]
print(len(kwlist))         # 35
print(type(kwlist))        # <class 'list'>
print(kwlist)              # ['False', 'None', 'True', ...]


x = complex(input('Enter  complex  number  :  '))
print(type(x))   # <class 'complex'>
print(x)         # (3+4j)


print(eval("    'hyd'   "))   # hyd
hyd = 'Sec'
print(eval('hyd'))            # Sec
sec = '25'
print(eval('sec'))            # 25
print(eval(sec))              # 25
cyb = 10.8
print(eval('cyb'))            # 10.8
print(eval(cyb))              # TypeError


print(eval('print("Hyd")'))  
# Hyd
# None


print(bool('False'))       # True
print(eval('False'))       # False
print(bool(''))            # False
print(eval('  ""  '))      # 
print(eval(''))            # SyntaxError
print(eval('  " "   '))    #  
print(eval(' '))           # SyntaxError



x = eval(input('Enter  any  input  :  '))
print(type(x))   # <class 'int'>
print(x)         # 10


a = input('Enter  any  string  :  ')
print(len(a))   # length of full string
print(a)        # prints string exactly as entered

b = eval(input('Enter   any  string  : '))
print(len(b))   # length after evaluation (quotes removed)
print(b)        # prints string