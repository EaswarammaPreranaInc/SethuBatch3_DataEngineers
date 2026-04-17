#abs() Function Homework
from  builtins  import  abs
print(abs(-35.8)) # 35.8
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32)) # 32
import  builtins
print(builtins . abs(-25)) #25


#max() and min() Functions Homework
from  builtins  import   max , min
print(max(10.8 , 20.6)) # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) # 5.9
print(max(25 , 10.8)) # 25
import  builtins
print(builtins . max(10 , 20 , 30)) # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5


#pow() Function Homework
from  builtins  import  pow
print(pow(10 , -2)) # 0.01
print(pow(4 , pow(3 , 2))) # 262144
import  builtins
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) # -0.125


#Outputs Homework #1
How  to  import   kw  list # from keyword import kwlist
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....] # print(kwlist)
How  to  print  number  of  keywords  i.e.  35 # print(len(kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'> # print(type(kwlist))
print(keyword . kwlist) # prints kwlist when keyword module is imported


#Outputs Homework #2
How  to  import   keyword  module # import keyword
How  to  print  kwlist # print(keyword . kwlist)
How  to  print  number  of  keywords # print(len(keyword . kwlist))
How  to  print  type  of kwlist # print(type(keyword.kwlist))
print(kwlist) # error the current module does not contain any function kwlist, it needs to have 'keyword . ' to print the list from keywords module


Complex Input Homework
x = complex(input('Enter  complex  number  :  ')) # (3 + 4j)
print(type(x)) # <class 'complex'>
print(x) # 3 + 4j


#Tricky Program
#Outputs Homework #3
print(eval("    'hyd'   ")) # 'hyd'
hyd = 'Sec'
print(eval('hyd')) # 'Sec'
sec = '25'
print(eval('sec')) # str '25'
print(eval(sec)) # error because eval() needs the argument in a string
cyb = 10.8
print(eval('cyb')) # float 10.8
print(eval(cyb)) # error because eval() needs the argument in a string


#Most Tricky Program
#Outputs Homework #4
print(eval('print("Hyd")')) #None
# print function prints returns None to the function call

#Outputs Homework #5
print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # empty string
print(eval('')) # error because eval() needs the argument in a string
print(eval('  " "   ')) # <space>
print(eval(' ')) # error because eval() needs the argument in a string


#eval(input()) Homework
x = eval(input('Enter  any  input  :  '))
print(type(x)) # based on the input, returns the appropriate class
print(x) # prints the input given by the user


#What is a better approach to read string input?
a = input('Enter  any  string  :  ')
print(len(a)) # the number of characters in the given string
print(a) # prints the string input given by the user
b = eval(input('Enter   any  string  : '))
print(len(b)) # the number of characters in the given string
print(b) # prints the string input given by the user
# because the input() function already takes all the given inputs as string, there is no need for an eval() function
