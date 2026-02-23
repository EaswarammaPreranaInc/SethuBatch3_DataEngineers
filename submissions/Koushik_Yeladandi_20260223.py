# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')  # 25, 10.8, 'Hyd'
print(a , b , c , sep = '\t')  # 26	10.8	'Hyd'
print(a , b , c , sep = '---') # 26---10.8---'Hyd'
print(a , b , c , sep = '\n') 
 # 20
10.8
Hyd
print(a , b , c)  # 25 10.8 Hyd
print(a , b , c , separator = ':') # 25:10.8:Hyd



# Find outputs  (Home  work)
print('Hyd') # Hyd 
print() # Nothing
print('Sec')  # 'Sec'
print()  # Nothing
print('Cyb') # 'Cyb'


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')  # 25,10.8,'Hyd'---
print(a , b , c , sep = ',,,')  # 25,,,10.8,,,'Hyd'
print(a , b , c , sep = ':::' , end = '\t\t\t') #25:::10.8:::'Hyd'   
print(a , b , c) # 25 10.8 'Hyd'


# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)  # [10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}


#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # 25.000000
print(type(b)) # <class str>
x = 10.8
y = '%i'  %x 
print(y) # 10
print(type(y)) # <class str>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # [10 , 20 , 15 , 18]
print(type(n)) # <class str>


# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #      10.92
print('%9.1f'  %a)  #       10.9       
print('%10.3f'  %a) #        10.927
print('%.2f'  %a)   #10.92
print('%.6f'  %a)   #10.927400
print('%f'  %a)     #10.927400
print('%g'  %a)     #10.927400


# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)  #     Hyd
print('%-7s'  %a) # Error 
print('%2s'  %a)  #  Hyd 
print('%s'  %a)   #Hyd
print('%s' , a)   # Hyd Hyd
print('%s'  a)    # 
print('%s' , %a) # Error
print(a) # Hyd


# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)
print('%s' , a)
print('%s'  a)
print('%s' , %a)
print('%l'  %a)
print(a)


#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))
print('%i    %g    %s'    %(a , b , c))
print('%s    %s    %s'  %(a , b , c))
print('%d    %g    %s'  , a , b , c)
print('%d    %g      %s'   a , b , c)
print('%d    %g    %s'  ,  %(a , b , c))
print('%d    %g    %s'    %a%b%c)
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)


#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)
print(type(y))
x = 10.8
y = F'{x}'
print(y)
print(type(y))
x = [10,20,30,40]
y = F'{x}'
print(y)
print(type(y))


#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')
print(F'{a=}  \t   {b=}   \t  {c=}')
print(F'{a:}  \t   {b:}   \t  {c:}')
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')
print(F'a  =  a  \t  b  =  b  \t  c  =  c')
print(F'{x =}  \t   {y =}   \t  {z =}')


#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}')
print(F'{{{{{x}}}}}')
print(F'{{{{{{x}}}}}}')
print(F'{{{{{{{x}}}}}}}')
print(F'{{{{{{{{x}}}}}}}}')