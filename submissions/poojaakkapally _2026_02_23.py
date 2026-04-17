1. # sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')-------25,10.8,Hyd
print(a , b , c , sep = '\t')--------25	10.8	Hyd
print(a , b , c , sep = '---')--------25---10.8---Hyd
print(a , b , c , sep = '\n')------25
                                  10.8 
                                  'Hyd'
print(a , b , c)--------25 , 10.8 , 'Hyd'
print(a , b , c , separator = ':')-----error (separator invalid key)

2. # Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')------------25 , 10.8 , 'Hyd' ---
print(a , b , c , sep = ',,,')-----------25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')--------25:::10.8:::Hyd	
print(a , b , c)-------25 , 10.8 , 'Hyd'

3.Find outputs  (Home  work)
print('Hyd')--------'Hyd'
print()------empty
print('Sec')------'Sec'
print()----empty
print('Cyb')----'Cyb'

4. # Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)--------[10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}

5. #  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)--------25.000000
print(type(b))# <class 'str'>
x = 10.8
y = '%i'  %x
print(y)------10
print(type(y))# <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)------[10 , 20 , 15 , 18]
print(type(n))# <class 'str'>

6. # Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)-------____10.93
print('%9.1f'  %a)------_____10.9
print('%10.3f'  %a)-----____10.927
print('%.2f'  %a)------10.93
print('%.6f'  %a)-------10.927400
print('%f'  %a)-------10.927400
print('%g'  %a)------10.9274

7. # Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a) # ____Hyd  
print('%-7s'  %a) # Hyd
print('%2s'  %a) # Hyd
print('%s'  %a) # Hyd  
print('%s' , a)  # %s Hyd  
print('%s'  a) # error
print('%s' , %a) # error
print(a) # 'Hyd'  

8. # Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) # [10, 20, 30, 40]
print('%s' , a) #[10, 20, 30, 40]
print('%s'  a) #error
print('%s' , %a) #error
print('%l'  %a) #error
print(a) #[10, 20, 30, 40]

9. #Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # 25    10.927400    Hyd
print('%i    %g    %s'    %(a , b , c)) # 25    10.927400    Hyd
print('%s    %s    %s'  %(a , b , c)) # 25    10.927400    Hyd
print('%d    %g    %s'  , a , b , c) #  %d    %g    %s 25 10.9274 Hyd
print('%d    %g      %s'   a , b , c) # error
print('%d    %g    %s'  ,  %(a , b , c)) # error
print('%d    %g    %s'    %a%b%c) # error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25 10.927400 Hyd

10. #  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y) #25
print(type(y)) # <class 'str'>
x = 10.8
y = F'{x}'
print(y) # 10.8
print(type(y)) # <class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) # [10,20,30,40]
print(type(y)) # <class 'str'>

11. #Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') # 25  	   10.8   	  Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a = 25  	  b  =  10.8  	  c  =  Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') # a=25  	   b=10.8   	  c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') # 25  	   10.8   	  Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') #a  =  {a}  	  b  =  {b}  	  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') #a  =  a  	  b  =  b  	  c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}') # error(name x y z is not defined)

12. #  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}') # {x}
print(F'{{{{{x}}}}}') # {25}
print(F'{{{{{{x}}}}}}') # {x}
print(F'{{{{{{{x}}}}}}}') #{25}
print(F'{{{{{{{{x}}}}}}}}') # {x}

 

