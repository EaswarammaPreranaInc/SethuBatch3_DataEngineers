
 #  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))	#35.8
print(abs(-27))		#27
print(abs(29.5))	#29
print(abs(32))		 #32
import  builtins
print(builtins . abs(-25))#25
_______________________________________________________
 #  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))			#20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))	#5.9
print(max(25 , 10.8))			#25
import  builtins
print(builtins . max(10 , 20 , 30))	     #30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #5
_____________________________________________________
 # pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))		#10^-2=0.01
print(pow(4 , pow(3 , 2)))	#4^3^2=4^9=262144
import  builtins
print(builtins . pow(2 , 3))	#2^3=8
print(builtins . pow(-2 , -3))	#-2^-3=-0.12
______________________________________________________
 # Find  outputs
How  to  import   kw  list	#import keyword
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]	#print(keyword.kwlist)
How  to  print  number  of  keywords  i.e.  35 		#print(len(keyword.kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'>	#print(type(keyword.kwlist))
print(keyword . kwlist)		#[and , or , not , is , in , None , True , False , .....]
___________________________________________________
 #  Find  outputs  (Home  work)
How  to  import   keyword  module	#import   keyword
How  to  print  kwlist		#print(keyword.kwlist)
How  to  print  number  of  keywords	#print(len(keyword.kwlist))
How  to  print  type  of kwlist		#print(type(keyword.kwlist))# <class 'list'>
print(kwlist)	#syntax error

________________________________________________________
 # How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))	#x = complex(input('3+4j'))#x=3+4j
print(type(x))			#<class 'complex'>
print(x)			#3+4j
_______________________________________________________ 
#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))#'hyd'
hyd = 'Sec'
print(eval('hyd'))	#Sec
sec = '25'
print(eval('sec'))	#25
print(eval(sec))	#25
cyb = 10.8
print(eval('cyb'))	#10.8
print(eval(cyb))	#10.8
________________________________________________________
 #  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))	#Hyd #None
________________________________________________
 #  Find  outputs  (Home  work)
print(bool('False'))	#True
print(eval('False'))	#False
print(bool(''))		#False
print(eval('  ""  '))	#error
print(eval(''))		#''
print(eval('  " "   '))	#error
print(eval(' '))	#empty
_________________________________________________
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))	#x = eval(input('25'))#x=25
print(type(x))	#<class 'int'>
print(x)	#25
___________________________________________________________ 
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')	#a = input('Hyd ')
print(len(a))	#3
print(a)	#Hyd
b = eval(input('Enter   any  string  : '))#b = eval(input('"Sita"'))
print(len(b))#4
print(b)#Sita