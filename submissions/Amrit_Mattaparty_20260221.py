#1
#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) #35.8
print(abs(-27)) #27
print(abs(29.5)) #29.5
print(abs(32)) #32
import  builtins
print(builtins.abs(-25)) #25



#2
#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) #5.9
print(max(25 , 10.8)) #10.8
import  builtins
print(builtins.max(10 , 20 , 30)) #30
print(builtins.min(10 , 20 , 15 , 5 , 12)) #5



#3
# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) #10 ^ -2 = 0.01
print(pow(4 , pow(3 , 2))) #4 ^ 9 = 262144
import  builtins
print(builtins.pow(2 , 3)) #2 ^ 3 = 8
print(builtins.pow(-2 , -3)) # -2 ^ -3 = -0.125



#4
# Find  outputs
import keyword #To  import   kw  list
print(keyword.kwlist) #To  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
print(len(keyword.kwlist)) #To  print  number  of  keywords  i.e.  35
print(type(keyword.kwlist)) #To  print  type  of kwlist  i.e.  <class 'list'>
print(keyword.kwlist) #[kw1, kw2, kw3 .... kw35] i.e. list of 35 keywords of python



#5
#  Find  outputs  (Home  work)
import keyword #To  import   keyword  module 
print(keyword.kwlist) #To  print  kwlist i.e.  [and , or , not , is , in , None , True , False , .....]
print(len(keyword.kwlist)) #To  print  number  of  keywords i.e. 35
print(type(keyword.kwlist)) #To  print  type  of kwlist i.e.  <class 'list'>
print(kwlist) #Error as 'kwlist' object is no where defined in the program #5 earlier



#6
# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) #Input: 1+2j => complex("1+2j") i.e complex coverts string 1 + 2j to complex => 1+2j
print(type(x)) #class 'complex'
print(x) #1 + 2j



#7
#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) #hyd i.e. string hyd
hyd = 'Sec'
print(eval('hyd')) #Sec
sec = '25'
print(eval('sec')) #25
print(eval(sec)) #Error as eval argument should be always a string except "" and " "
cyb = 10.8
print(eval('cyb')) #10.8
print(eval(cyb)) #Error as eval argument should be always a string except "" and " "



#8
#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) #print("Hyd") => Output: Hyd, inner print() returns None to eval, eval returns None to the outer print() i.e print(None) => None final output: Hyd<next line>None



#9
#  Find  outputs  (Home  work)
print(bool('False')) #True
print(eval('False')) #False
print(bool('')) #False
print(eval('  ""  ')) #Empty string i.e. Empty
print(eval('')) #Error as an empty string can't be given to eval() function as nothing will be processed
print(eval('  " "   ')) #Empty string i.e. Empty
print(eval(' ')) #Error as spaces are ignored which results to be empty string and which can't be given as argument to eval() function



#10
# What  is  the  advantage  of  eval(input())? #Automatic object type conversion without making use of type converters like int(), float(), bool(), complex() , list() .. etc.
x = eval(input('Enter  any  input  :  ')) #3+3j
print(type(x)) #class 'complex'
print(x) #3+3j



#11
# What  is  a  better  approach  to  read  string  input ?
#Better/Simple approach
a = input('Enter  any  string  :  ') #Python
print(len(a)) #6
print(a) #Python
#The Risky/Complex Approach
b = eval(input('Enter   any  string  : ')) #'Program' - Input should be given in quotes to avoid error, as it looks for object Program if no quotes 
print(len(b)) #7
print(b) #Program