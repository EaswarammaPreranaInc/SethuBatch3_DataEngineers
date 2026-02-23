#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) #38
print(abs(-27)) #27
print(abs(29.5)) #29
print(abs(32)) #33
import  builtins
print(builtins . abs(-25))#25

#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))#5.9
print(max(25 , 10.8))#25
import  builtins
print(builtins . max(10 , 20 , 30))#30
print(builtins . min(10 , 20 , 15 , 5 , 12))#5


# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))##0.01
print(pow(4 , pow(3 , 2)))#262144
import  builtins
print(builtins . pow(2 , 3))#8
print(builtins . pow(-2 , -3))#-0.125


# Find  outputs
from keyword  import kwlist How  to  import   kw  list
print(kwlist)#How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....] 
print(len(kwlist))#How  to  print  number  of  keywords  i.e.  35#
print(type(kwlist))#How  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword . kwlist)

#  Find  outputs  (Home  work)
#import keyword #How  to  import   keyword  module
print(keyword.kwlist)#How  to  print  kwlist
print(len(keyword.kwlist))#How  to  print  number  of  keywords
print(type(keyword.kwlist))#How  to  print  type  of kwlist
print(kwlist)#Error it should be keyword.kwlist


# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) # enter 3+4j
print(type(x)) <class complex>
print(x) #3+4j

# Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) #"hyd"
hyd = 'Sec'
print(eval('hyd'))#sec
sec = '25'
print(eval('sec'))#'25'
print(eval(sec)) #25
cyb = 10.8
print(eval('cyb'))#10.8
print(eval(cyb))#error

 #  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))#None

 #  Find  outputs  (Home  work)
print(bool('False'))#True
print(eval('False'))#False
print(bool(''))#False
print(eval('  ""  '))#"
print(eval(''))
print(eval('  " "   '))
print(eval(' '))


 # What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))takes string and stores the actual type of an input #False considers as bool
print(type(x))#bool
print(x)#False


 # What  is  a  better  approach  to  read  string  input ?#input() is better
a = input('Enter  any  string  :  ')#simply reads the input as string #hyd
print(len(a))#3
print(a)#hyd
b = eval(input('Enter   any  string  : '))#evaluates the string input so if you give hyd it searches for the object Hyd but if you give"hyd" it considers string hyd 
print(len(b))#Error  since there is no object Hyd 
print(b)
