#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))	#35.8
print(abs(-27))		#27
print(abs(29.5))	#29.5
print(abs(32))		#32
import  builtins
print(builtins . abs(-25))  #25


#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))			#20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))	#5.9
print(max(25 , 10.8))			#25
import  builtins
print(builtins . max(10 , 20 , 30))	#30
print(builtins . min(10 , 20 , 15 , 5 , 12))   #5


# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))		#0.01
print(pow(4 , pow(3 , 2)))	#262144
import  builtins
print(builtins . pow(2 , 3))	#8
print(builtins . pow(-2 , -3))	#-0.125


# Find  outputs
import keyword
kwlist=keyword.kwlist
print(kwlist)		#list of keywords
print(len(kwlist))	#35
print(type(kwlist))	#<class list> 
print(keyword . kwlist)


#  Find  outputs  (Home  work)
How  to  import   keyword  module  	#import keyword
How  to  print  kwlist		   	#kwlist=keyword.kwlist
How  to  print  number  of  keywords	#print(kwlist)
How  to  print  type  of kwlist		#print(len(kwlist))
print(kwlist)				#print(type(kwlist))
					#print(kwlist)

# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x))			#<class complex>
print(x)			#(3+4j)


#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))	#hyd
hyd = 'Sec'
print(eval('hyd'))		#sec
sec = '25'
print(eval('sec'))		#25
print(eval(sec))		#25
cyb = 10.8
print(eval('cyb'))		#10.8
print(eval(cyb))		#error because it must be a string


#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))	#Hyd
				#None

#  Find  outputs  (Home  work)
print(bool('False'))		#True
print(eval('False'))		#False
print(bool('')) 		#False
print(eval('  ""  '))		#space
print(eval(''))			#error invalid syntax
print(eval('  " "   '))		#space		
print(eval(' '))		#error invalid syntax


# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x))
print(x)


# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')		#Hyd
print(len(a))					#3
print(a)					#Hyd
b = eval(input('Enter   any  string  : '))	#'25'
print(len(b))					#2
print(b)					#25