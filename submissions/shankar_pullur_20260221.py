print(abs(-35.8))                    # 35.8
print(abs(-27))                      #  27
print(abs(29.5))                     # 29.5
print(abs(32))                       # 32
print(abs(0.0))                      #0.0


print(max(10.8 , 20.6))                     #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))        # 5.9
print(max(25 , 10.8))                       # 25
import  builtins
print(builtins . max(10 , 20 , 30))         # 30
print(builtins . min(10 , 20 , 15 , 5 , 12))# 5

 
print(pow(10 , -2))                         #0.01
print(pow(4 , pow(3 , 2)))                 # 262144
import  builtins
print(builtins . pow(2 , 3))                # 8
print(builtins . pow(-2 , -3))              #-0.125


'''How  to  import   kw  list
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]
How  to  print  number  of  keywords  i.e.  35
How  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword . kwlist)'''
import keyword 
print(keyword.kwlist)
'''['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']'''
print(len(keyword.kwlist))               # 35
print(type(keyword.kwlist))              # <class 'list'>


x = complex(input('Enter  complex  number  :  '))  # 3+4j
print(type(x))                                     # <class 'complex'>
print(x)                                           # 3+4j


print(eval("    'hyd'   "))                     #hyd        
hyd = 'Sec'
print(eval('hyd'))                              #sec
sec = '25'
print(eval('sec'))                              #25
print(eval(sec))                                #25
cyb = 10.8       
print(eval('cyb'))                             #10.8
#print(eval(cyb))

print(eval('print("Hyd")'))                    #None

print("new Liner")
print(bool('False'))                         # True
print(eval('False'))                         #False
print(bool(''))                              #False
print(eval('  ""  '))                        #''      
#print(eval(''))                            
print(eval('  " "   '))                      #' '
#print(eval(' '))                            #error


x = eval(input('Enter  any  input  :  '))     # 25
print(type(x))                                #<class 'int'>
print(x)                                      # 25


a = input('Enter  any  string  :  ')          # shankar
print(len(a))                                 # 7
print(a)                                      # shankar
b = eval(input('Enter   any  string  : '))    # shankar error or ''
print(len(b))                                 #  error(if give number)
print(b)                                      # 