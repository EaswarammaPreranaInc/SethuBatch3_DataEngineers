from builtins import max, min
from builtins import pow
import builtins
 #  abs()  function  demo  program
from builtins import abs
print(abs(-35.8))  # 35.8
print(abs(-27))  # 27
print(abs(29.5))  # 29.5
print(abs(32))  # 32
print(builtins . abs(-25))  # 25

 #  max()  and  min()   functions  demo  program
print(max(10.8, 20.6))  # 20.6
print(min(10.8, 20.6, 5.9, 12.3))  # 5.9
print(max(25, 10.8))  # 25
print(builtins . max(10, 20, 30))  # 30
print(builtins . min(10, 20, 15, 5, 12))  # 5


# pow()  function  demo  program
print(pow(10, -2))  # 0.01
print(pow(4, pow(3, 2)))  # 262144
print(builtins . pow(2, 3))  # 8
print(builtins . pow(-2, -3))  # -0.125

 # Find  outputs
How  to import kw  list  # import keyword
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....] #import keyword
                                                                                       print(
                                                                                           keyword.kwlist)
How  to print number  of  keywords  i.e.  35  # import keyword
                                                print(len(keyword.kwlist))

How  to print type  of kwlist  i.e. < class 'list' >  # import keyword
                                                         print(
                                                             type(keyword.kwlist))

print(keyword . kwlist)  # error

 #  Find  outputs  (Home  work)
How  to import keyword  module  # import keyword
How  to print kwlist  # print(keyword.kwlist)
How  to print number  of  keywords  # print(len(keyword.kwlist))
How  to print type  of kwlist  # print(type(keyword.kwlist))
print(kwlist)  # error because kwlist is not defined

 # How  to  read  complex  input ? # complex(input())
x = complex(input('Enter  complex  number  :  '))  # 3+4j
print(type(x))  # <class 'complex'>
print(x)   # 3+4j


#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))  # 'hyd'
hyd = 'Sec'
print(eval('hyd'))  # sec
sec = '25'
print(eval('sec'))  # 25
print(eval(sec))  # 25
cyb = 10.8
print(eval('cyb'))  # 10.8
print(eval(cyb))  # error because it must be string

 #  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')  # None

#  Find  outputs  (Home  work)
print(bool('False'))  # True
print(eval('False'))  # False
print(bool(''))  # False
print(eval('  ""  '))  # empty
print(eval(''))  # error
print(eval('  " "   '))  # empty
print(eval(' '))  # error



# What  is  the  advantage  of  eval(input()) #converts string to appropriate object
x=eval(input('Enter  any  input  :  '))  # 100
print(type(x))  # <class'int'>
print(x)  # 100


 # What  is  a  better  approach  to  read  string  input ? # always returns a string
a=input('Enter  any  string  :  ')  # 3000
print(len(a))  # 4
print(a)  # 3000
b=eval(input('Enter   any  string  : '))  # "srilekha"
print(len(b))  # 8
print(b)  # srilekha
