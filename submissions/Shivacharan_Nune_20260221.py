 #  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))           #35.8
print(abs(-27))             #27
print(abs(29.5))            #29.5
print(abs(32))              #32
import  builtins          
print(builtins . abs(-25))  #25
#-------------------------------------------------------------------
#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))                #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))   #5.9
print(max(25 , 10.8))                  #25
import  builtins
print(builtins . max(10 , 20 , 30))    #30
print(builtins . min(10 , 20 , 15 , 5 , 12))  #5
#==-----------------------------------------------------------
 # pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))              #0.01
print(pow(4 , pow(3 , 2)))       #4**9
import  builtins
print(builtins . pow(2 , 3))     #8
print(builtins . pow(-2 , -3))   #-0.125
#==============================================================================
 # Find  outputs
How  to  import   kw  list
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]    #import keyword
                                                                                          # print(keyword.kwlist)
How  to  print  number  of  keywords  i.e.  35               
                                                                                         #import keyword
                                                                                         #print(len(keyword.kwlist))      
How  to  print  type  of kwlist  i.e.  <class 'list'>                                     #import keyword
                                                                                         #print(type(keyword.kwlist))
#print(keyword . kwlist)                  
#--------------------------------------------------------------------------------------------                                                  
 # How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x))                                               #<class 'complex'>
print(x)                                                     #what ever complex number user entered
 #  Tricky  program
#-------------------------------------------------------------------
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))                                  #'hyd'
hyd = 'Sec'                                                  
print(eval('hyd'))                                           #Sec
sec = '25'                                                   
print(eval('sec'))                                            #25 :str
print(eval(sec))                                              #25 :int
cyb = 10.8                                                   #10.8
print(eval('cyb'))
print(eval(cyb))                                             :#Error
#-------------------------------------------------------------------
#  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))                                 #Hyd
                                                            #None
#-------------------------------------------------------------------
#  Find  outputs  (Home  work)
print(bool('False'))                                      #True
print(eval('False'))                                      #False
print(bool(''))                                           #False
print(eval('  ""  '))                                     #"":empty string
print(eval(''))                                           #Error:expects string
print(eval('  " "   '))                                   #" ":space
print(eval(' '))                                          #Error
#-------------------------------------------------------------------
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x))                                  #what ever the type user enters
print(x)                                        #what ever the value user enters
#-------------------------------------------------------------------
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')                      #Hyd
print(len(a))                                             #better approach,3
print(a)                                                  #Hyd
b = eval(input('Enter   any  string  : '))                #Error
print(len(b))                                             
print(b)