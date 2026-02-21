#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) #36
print(abs(-27))   #27
print(abs(29.5))  #29
print(abs(32))    #32
import  builtins
print(builtins . abs(-25)) #25



from  builtins  import   max , min
print(max(10.8 , 20.6))   # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) # 5.9
print(max(25 , 10.8))    #25
import  builtins 
print(builtins . max(10 , 20 , 30))  #30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #5


from  builtins  import  pow
print(pow(10 , -2))   #0.01
print(pow(4 , pow(3 , 2))) # 4^9
import  builtins
print(builtins . pow(2 , 3))   #8
print(builtins . pow(-2 , -3)) #-0.125


How  to  import   kw  list     # import keyword  
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
How  to  print  number  of  keywords  i.e.  35 # len(keyword.kwlist)
How  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword . kwlist)   # list of 35 keyword will be printed


How  to  import   keyword  module   # from keyword import kwlist
How  to  print  kwlist    #print(kwlist)
How  to  print  number  of  keywords #len(kwlist)
How  to  print  type  of kwlist   #print(type(kwlist))
print(kwlist) # list of 35 keyword will be printed


x = complex(input('Enter  complex  number  :  '))
print(type(x))  # <class 'complex'>
print(x)       # given complex number

# Find  outputs  (Home  work)
print(eval("    'hyd'   "))    #hyd
hyd = 'Sec'
print(eval('hyd'))    # sec
sec = '25'
print(eval('sec'))    # 25
print(eval(sec))      # 25
cyb = 10.8
print(eval('cyb'))    # 10.8
print(eval(cyb))      #Error


#  Find  output  (Home  work)
print(eval('print("Hyd")'))  # Hyd\n None


print(bool('False'))  # True
print(eval('False'))  # False
print(bool(''))       # False
print(eval('  ""  ')) # Empty Str                         #
print(eval(''))       # Error
print(eval('  " "   ')) # Empty str
print(eval(' '))        #Error


x = eval(input('Enter  any  input  :  '))
print(type(x))  # given input
print(x)        # given input is printed

a = input('Enter  any  string  :  ')
print(len(a))  # len() of input
print(a)       #given input is printed
b = eval(input('Enter   any  string  : '))
print(len(b)) #len() of input
print(b)      #given input is printed