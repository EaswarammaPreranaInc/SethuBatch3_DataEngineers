from  builtins  import  abs
print(abs(-35.8))               # 35.8
print(abs(-27))                 # 27
print(abs(29.5))                #29.5
print(abs(32))                  #32
import  builtins
print(builtins . abs(-25))        # 25

2) #  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))        			#  20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) 		 # 5.9
print(max(25 , 10.8))  				# 25
import  builtins
print(builtins . max(10 , 20 , 30))	        # 30
print(builtins . min(10 , 20 , 15 , 5 , 12))  	# 5

3) # pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) 			 # 0.01
print(pow(4 , pow(3 , 2))) 		 # 262144
import  builtins
print(builtins . pow(2 , 3))   		# 8
print(builtins . pow(-2 , -3))  	# -0.125

4) # Find  outputs
How  to  import   kw  list  								# import keyword
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]  # print(keyword.kwlist)
How  to  print  number  of  keywords  i.e.  35  					# print(len(keyword.kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'> 					# print(type(keyword.kwlist))
print(keyword . kwlist)  								# ['False', 'None', 'True', 'and', 'as', 'assert', 'async','await', 'break', 'class', 'continue', 'def', 'del','elif', 'else', 'except', 'finally', 'for', 'from','global', 'if', 'import', 'in', 'is', 'lambda','nonlocal', 'not', 'or', 'pass', 'raise','return', 'try', 'while', 'with', 'yield']

5) # How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) 					# 3+4j
print(type(x))  									# class<'complex'>
print(x)  										# 3+4j

6) #  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))       							# hyd
hyd = 'Sec'
print(eval('hyd'))            								# Sec
sec = '25'
print(eval('sec'))             								# 25
print(eval(sec))  									# 25
cyb = 10.8
print(eval('cyb'))  									# 10.8
print(eval(cyb))  									# 10.8

7) #  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))  								# Hyd

8) #  Find  outputs  (Home  work)
print(bool('False'))  									# True
print(eval('False'))  									# False
print(bool(''))  									# False
print(eval('  ""  '))  									# ' '
print(eval(''))  # ''
print(eval('  " "   ')) 								#  ' '
print(eval(' ')) 									# ' '

9) # # What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))  						# 25
print(type(x))  									# class<'int'>
print(x)  										# 25

10) # # What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')  							# Hyd and it is the best choice than eval
print(len(a))  										# 3
print(a)  Hyd
b = eval(input('Enter   any  string  : '))  					        # 'Hyd' if we enter hyd without quotes it will search for variable name Hyd and since there is no Hyd it will give error
print(len(b))  										# 3
print(b)  										# Hyd