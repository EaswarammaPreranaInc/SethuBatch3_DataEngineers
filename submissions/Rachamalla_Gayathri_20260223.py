# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',') #25,10.8, Hyd
print(a , b , c , sep = '\t')#25 10.8 Hyd
print(a , b , c , sep = '---')#25---10.8---Hyd
print(a , b , c , sep = '\n')
#25
10.8
Hyd
print(a , b , c)#25 10.8 Hyd
print(a , b , c , separator = ':')#invalid

# Find outputs  (Home  work)
print('Hyd')#Hyd
print()
print('Sec')#Sec
print()
print('Cyb')#Cyb
# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)#[10 , 20 , 30 , 40] (10 , 20 , 30 , 40)  {10 , 20 , 30 , 40}
 #  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)25.000000
print(type(b))#<class 'str'>
x = 10.8
y = '%i'  %x 
print(y) #10
print(type(y)) #<class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)[10 , 20 , 15 , 18]
print(type(n))<class 'str'>
 # Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)#10.93
print('%9.1f'  %a)#10.9
print('%10.3f'  %a)#10.927
print('%.2f'  %a)#10.93
print('%.6f'  %a)#10.927400
print('%f'  %a)#10.927400
print('%g'  %a)#10.9274
[6:27 pm, 23/02/2026] Gaya3: # Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)#Hyd
print('%-7s'  %a)#Hyd
print('%2s'  %a)#Hyd
print('%s'  %a)#Hyd
print('%s' , a)%s Hyd
print('%s'  a)#syntax error
print('%s' , %a)#syntax error
print(a)#Hyd
# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)#[10 , 20 , 30 , 40]
print('%s' , a)%s [10 , 20 , 30 , 40]
print('%s'  a)#error
print('%s' , %a)#error
print('%l'  %a)#error
print(a)#[10 , 20 , 30 , 40]
#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))#25 10.9274 'Hyd'
print('%i    %g    %s'    %(a , b , c))#25 10.9274 'Hyd'
print('%s    %s    %s'  %(a , b , c))#25 10.9274 'Hyd'
print('%d    %g    %s'  , a , b , c)#25 10.9274 'Hyd'
print('%d    %g      %s'   a , b , c)#syntax error
print('%d    %g    %s'  ,  %(a , b , c))#Syntax error
print('%d    %g    %s'    %a%b%c)#Type error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)#25 10.9274 'Hyd'
[6:27 pm, 23/02/2026] Gaya3: #  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)#25
print(type(y))#<class 'str'>
x = 10.8
y = F'{x}
print(y)#10.8
print(type(y))#<class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y)#[10,20,30,40]
print(type(y))#<class 'str'>
 #Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')#25
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
print(F'{{{{x}}}}')#{{x}}
print(F'{{{{{x}}}}}')# {{25}}
print(F'{{{{{{x}}}}}}')#{{{x}}}
print(F'{{{{{{{x}}}}}}}')#{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#{{{x}}}

 
