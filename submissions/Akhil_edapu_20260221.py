#  abs()  function  demo  program
#from builtins import abs

print(abs(-35.8)) #35.8
print(abs(-27)) #27
print(abs(29.5)) #29
print(abs(32)) #32

import builtins # No need of writing this the builtins module directly imports.Automatically #Error
print(builtins.abs(-25)) #Error 


#  max()  and  min()   functions  demo  program
from  builtins  import   max , min

print(max(10.8,20.6)) #max value is 20.6
print(mix(10.8,20.6,5.9,12.3)) # min value is 5.9
print(max(25,10.8)) #max value is 25
import  builtins
print(builtins . max(10 , 20 , 30)) #30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #5




# pow()  function  demo  program
from  builtins  import  pow

print(pow(10,-2)) #0.01
print(pow(4,pow(3,2))) #6561

import builtins
print(builtins.pow(2,3)) #9
print(builtins.pow(-2,-3)) #-0.125


# Find  outputs
How  to  import   kwlist
how to print kwlist i.e [and,or,not,is,False,True,yield,int,float,.........]

How to print number of keywords i.e. 35
How to print type of kwlist i.e <class 'list'>
print(keyword.kwlist)

#  Find  outputs  (Home  work)
How  to  import   keyword  module
How  to  print  kwlist
How  to  print  number  of  keywords
How  to  print  type  of kwlist
print(kwlist)


# How  to  read  complex  input ?

x = complex(input('Enter complex number:'))# takes input from keyboard
print(type(x)) # class 'complex'
print(x) # 3+4j

#Tricky program
# Find  outputs  (Home  work)

print(eval(" 'hyd' ")) #hyd is printed
hyd ='Sec' 
print(eval('hyd')) #Sec is printed there object with hyd here

sec = '25'
print(eval('sec')) #25 is printed
print(eval(sec)) #Error

cyb = 10.8
print(eval('cyb')) #10.8
print(eval(cyb)) #Error


#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) #prints hyd on screen
#moves to next 


#  Find  outputs  (Home  work)

print(bool('False')) #True
print(eval('False')) #False
print(bool('')) #False
print(eval(' "" ')) #"" are printed
print(eval('')) #Error
print(eval(' "" ')) #"" are printed
print(eval('')) #Error


# What  is  the  advantage  of  eval(input()) ?

x = eval(input("Enter any input: ")) #eval converts the gives values from string to to coresponding values.
print(type(x)) #based on input the output is printed
print(x) #anything what you type.


# What  is  a  better  approach  to  read  string  input ?

a input("Enter any string: ") #Data engineering batch-3.
print(len(a)) #24
print(a) #Data engineering batch-3.

b = eval(input("Enter any string:")) # Sri sathya sai skill development
print(len(b)) #Error
print(b) # Error





















































