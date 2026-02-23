# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')  # 25,10.8,Hyd 
print(a , b , c , sep = '\t') # 25	10.8	Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25
                              # 10.8
                              # Hyd
print(a , b , c) # 25 10.8 Hyd
print(a , b , c , separator = ':') # Error Because Separator Is Unexpected Key Word 



# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') #  25 10.8 Hyd---
print(a , b , c , sep = ',,,') # 25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t') # 25:::10.8:::Hyd	(tab)
print(a , b , c) # 25 10.8 Hyd 



# Find outputs  (Home  work)
print('Hyd') # Hyd
print() # 
print('Sec')# Sec
print() # 
print('Cyb') # Cyb 



# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # [10, 20, 30, 40] (10, 20, 30, 40) {10, 20, 30, 40}



#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # 25.000000 (String)
print(type(b)) # <class 'str'>
x = 10.8
y = '%i'  %x
print(y) # 10 (float to int)
print(type(y)) # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # [10 , 20 , 15 , 18]
print(type(n)) #  <class 'str'>




# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a) # 10.93
print('%9.1f'  %a) # 10.9
print('%10.3f'  %a) # 10.927
print('%.2f'  %a) # 10.93
print('%.6f'  %a) # 10.927400
print('%f'  %a) # 10.927400
print('%g'  %a) # 10.9274



# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a) #	Hyd(right Aligned 7 chars)
print('%-7s'  %a)# Hyd(left Aligned 7 Chars)
print('%2s'  %a) # Hyd(minmum 2 Chars)
print('%s'  %a) # Hyd
print('%s' , a) # %s Hyd
print('%s'  a) # Error because there is no comma
print('%s' , %a) # Error Invalid Syntax
print(a) # Error Because It Never Reached



# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) # [10 , 20 , 30 , 40]
print('%s' , a) # %s [10, 20, 30, 40]
print('%s'  a) # Error there is no format
print('%s' , %a) # Error there is no format
print('%l'  %a) # Error %1 Is no format
print(a) # Error



#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # 25 10.927400 Hyd
print('%i    %g    %s'    %(a , b , c)) # 25 10.9274 Hyd
print('%s    %s    %s'  %(a , b , c)) # 25 10.9274 Hyd 
print('%d    %g    %s'  , a , b , c) # Error Because , Is After Format
print('%d    %g      %s'   a , b , c) # Error No comma after format string
print('%d    %g    %s'  ,  %(a , b , c)) # Error Invalid In % Operator
print('%d    %g    %s'    %a%b%c) # Error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25 10.927400 Hyd




#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y) # 25
print(type(y)) # <class 'str'>
x = 10.8
y = F'{x}'
print(y) # 10.8
print(type(y)) # <class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) # [10,20,30,40]
print(type(y)) # <class 'str'>



#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') # 25 10.8 Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a = 25 b = 10.8 c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') # a=25 b=10.8 c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}')# Error		
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # a  =  {a}	 b  =  {b}	 c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a  =  a	 b  =  b	 c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}') # Error x,y,z Are Not Defined



#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}') # {{x}}
print(F'{{{{{x}}}}}') # {{{25}}}
print(F'{{{{{{x}}}}}}') # {{{{x}}}}
print(F'{{{{{{{x}}}}}}}') # {{{{{25}}}}}
print(F'{{{{{{{{x}}}}}}}}') # {{{{{{x}}}}}}
