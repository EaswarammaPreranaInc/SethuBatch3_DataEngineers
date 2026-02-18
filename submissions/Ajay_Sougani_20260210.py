a = 10.8 
print(a)           
print(type(a))      
print(id(a))       
b = 25. 
print(b)            
print(type(b))     
c = .689 
print(c)           
d = 3.4E2 
print(d)            
print(type(d))     
e = 9.62e-2 
print(e)            
print(9.8.2)       
a = 3 + 4j 
print(a)               
print(type(a))          
print(id(a))            
print(a.real)           
print(a.imag)           
 # 10.8 
# <class 'float'> 
 # memory address (varies) 
# 25.0 
 # <class 'float'> 
 # 0.689 
# 340.0 
 # <class 'float'> 
# 0.0962 
 # SyntaxError: invalid syntax 
 # (3+4j) 
# <class 'complex'> 
# memory address (varies) 
# 3.0 
# 4.0 
print(type(a.real))     # <class 'float'> 
print(type(a.imag))     # <class 'float'> 
a = 6j 
print(a)           
print(type(a))      
print(a.real)      
print(a.imag)      
print(5 + j6)       
print(3 + 4i)      
 # 6j 
# <class 'complex'> 
 # 0.0 
 # 6.0 
# SyntaxError 
 # SyntaxError 
print(4+j)          
# NameError: name 'j' is not defined 
print(4 + 1j)       
print(4 + 0j)       
a = True 
print(a)               
print(type(a))          
print(id(a))            
b = False 
print(b)                
print(type(b))          
# (4+1j) 
# (4+0j) 
 # True 
# <class 'bool'> 
# memory address (varies) 
# False 
# <class 'bool'> 
print(True + True)      
# 2 
print(True + False)     # 1 
print(False + True)     # 1 
print(False + False)    # 0 
print(True + True + True) # 3 
print(25 + 10.8 + True) # 36.8 
print(True > False)     # True 
print(True)            
print(False)            
print(true)             
print(false)            
a = 0O6247 
print(a)           
print(type(a))      
print(id(a))       
b = 0o6247 
print(id(b))        
print(b)            
c = 3239 
print(c)           
print(id(c))        
 # True 
# False 
# NameError 
# NameError 
 # 3239 
# <class 'int'> 
 # memory address (varies) 
# memory address (may be same as a) 
# 3239 
 # 3239 
# memory address (may be same) 
print(0o9248)       
# SyntaxError: invalid digit 
a = 0XA7B9 
print(a)           
print(type(a))      
b = 0xBEEF 
print(b)            
print(A7B9)         
print('A7B9')       
print(0XBEER)       
print(0XHYD)        
 # 42937 
# <class 'int'> 
# 48879 
# NameError 
# A7B9 
# SyntaxError 
# SyntaxError 
print(0xA7G9B)      
a = 9248 
print(a)           
# SyntaxError 
 # 9248 
print(type(a))      
# <class 'int'> 