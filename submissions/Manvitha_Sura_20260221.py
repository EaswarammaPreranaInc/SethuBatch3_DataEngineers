#  abs()  function  demo  program
from  builtins  import  abs  #members of builtins module are automatically imported-we dont need to write explicitly
print(abs(-35.8))  #35.8
print(abs(-27))  #27
print(abs(29.5))  #29.5
print(abs(32))  #32
import  builtins  #builtins module is imported
print(builtins . abs(-25))  #25


# max()  and  min()   functions  demo  program
from  builtins  import   max , min  #members of builtins module are automatically imported-we dont need to write explicitly
print(max(10.8 , 20.6))  #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  #5.9
print(max(25 , 10.8))  #25
import  builtins
print(builtins . max(10 , 20 , 30))  #30
print(builtins . min(10 , 20 , 15 , 5 , 12))  #20


# pow()  function  demo  program
from  builtins  import  pow  ##members of builtins module are automatically imported-we dont need to write explicitly
print(pow(10 , -2))  #0.01
print(pow(4 , pow(3 , 2)))  #4^9
import  builtins
print(builtins . pow(2 , 3))  #8
print(builtins . pow(-2 , -3))  #-0.125



# Find  outputs
How  to  import   kw  list  #either by importing kwlist or by keywords module
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]   '''import keyword
   print(keyword.kwlist)
   or
   from keyword import kwlist
   print(kwlist)
'''

How  to  print  number  of  keywords  i.e.  35   #print(len(kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'>  #print(type(keyword.kwlist))
print(keyword . kwlist)  #gives list of keywords


#  Find  outputs  (Home  work)
How  to  import   keyword  module  #import keyword
How  to  print  kwlist  #print(keyword.kwlist)
How  to  print  number  of  keywords  #print(len(keyword.kwlist))
How  to  print  type  of kwlist  #print(type(kwlist))
print(kwlist)  #gives list of keywords


# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))  #Enter  complex  number  : 5+6j
print(type(x))  #<class 'complex'>
print(x)  #5+6j


#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))  #'hyd'
hyd = 'Sec'
print(eval('hyd'))  #'Sec'
sec = '25'
print(eval('sec'))  #'25'
print(eval(sec))  #25
cyb = 10.8
print(eval('cyb'))  #10.8
print(eval(cyb))  #error-argument must be a string



#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))  #Hyd<next line>None            eval('print("Hyd")')->Hyd is printed,eval('None')->None


#  Find  outputs  (Home  work)
print(bool('False'))  #True
print(eval('False'))  #False
print(bool(''))  #False
print(eval('  ""  '))  #""
print(eval(''))  #error-arguments must be present
print(eval('  " "   '))  #" "
print(eval(' '))  #error-space is not treated as argument


# What  is  the  advantage  of  eval(input()) ?  '''we can read  any kind of input with eval() without using different type of functions like int ,float etc'''
x = eval(input('Enter  any  input  :  '))  #Enter  any  input  : 10
print(type(x))  #<class 'int'>
print(x)  #10



# What  is  a  better  approach  to  read  string  input ?  #input()
a = input('Enter  any  string  :  ')  #Enter  any  string  : Hyd
print(len(a))  #3
print(a)  #Hyd
b = eval(input('Enter   any  string  : '))  #Enter   any  string  : "Hyd"(must be given in quotes if not,treated as an object)
print(len(b))  #3
print(b)  #Hyd (if quotes are not given,then error-since there is no object Hyd