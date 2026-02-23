[4:18 pm, 23/02/2026] 🍕: # sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')#OUTPUT:25, 10.8,Hyd
print(a , b , c , sep = '\t')#OUTPUT:25  10.8 Hyd
print(a , b , c , sep = '---')#OUTPUT:25 -- 10.8 --Hyd
print(a , b , c , sep = '\n')#OUTPUT;25 , 10.8 , 'Hyd
print(a , b , c)#OUTPUT:25 10.8  Hyd
print(a , b , c , separator = ':')#OUTPUT:25 :10.8 : Hyd



# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')#output:25 -- 10.8 -- Hyd
print(a , b , c , sep = ',,,')#output:25 ,,,10.8 ,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')#output:25 ::: 10.8 :::Hyd   
print(a , b , c)  #output:  25 10.8 Hyd                                                       


# Find outputs  (Home  work)
print('Hyd')#output:Hyd
print()#output:None
print('Sec')#output:Sec
print()#output:None
print('Cyb')  #output:Cyb                                         

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)#output:[10, 20,30,40] (10, 20,30,40) {10, 20,30,40}

#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)#output:25
print(type(b))#output:<class 'str'>
x = 10.8
y = '%i'  %x
print(y)#output:10
print(type(y))#output:<class 'str,'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)#output:[10 , 20 , 15 , 18]
print(type(n))#output:<class 'str'>

# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)#output:   10.93
print('%9.1f'  %a)#output:     10.9
print('%10.3f'  %a)#output:    10.927
print('%.2f'  %a)#output:10.93
print('%.6f'  %a)#output:10.927400
print('%f'  %a)#output:10.924700
print('%g'  %a)#output:10.9274                    


# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)#output:       Hyd
print('%-7s'  %a)#output:Hyd
print('%2s'  %a)#output:  Hyd
print('%s'  %a)#output:Hyd
print('%s' , a)#output:%s Hyd
print('%s'  a)#output:error
print('%s' , %a)#output:error
print(a)#output:Hyd

# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)#output:[10 , 20 , 30 , 40]
print('%s' , a)#output:%s [10 , 20 , 30 , 40]
print('%s'  a)#output:error
print('%s' , %a)#output:error
print('%l'  %a)#output:error
print(a)#output:[10 , 20 , 30 , 40]


#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))#output:25  10.927400  Hyd
print('%i    %g    %s'    %(a , b , c))#output:25  10.9274  Hyd
print('%s    %s    %s'  %(a , b , c))#output:25    10.9274   Hyd'
print('%d    %g    %s'  , a , b , c)#output:%d    %g    %s 25 10.9274 Hyd  
print('%d    %g      %s'   a , b , c)#output:error
print('%d    %g    %s'  ,  %(a , b , c))#output:error
print('%d    %g    %s'    %a%b%c)#output:error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)#output:25 10.9274 Hyd


#  Find  outputs  (Home  work)
x = 25
y = F'{x}'#output:25
print(y)#output:25
print(type(y))#output:<class 'str'>
x = 10.8
y = F'{x}'
print(y)#output:10.8
print(type(y))#output:<class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y)#output:[10,20,30,40]
print(type(y))#output:<class 'str'>


#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')#output:25  10.8  Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')#output:a = 25  b = 10.8  c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')#output:a = 25  b = 10.8  c = Hyd
print(F'{a:}  \t   {b:}   \t  {c:}')#output:25  10.8  Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')#output:a  =  {a}   b  =  {b}   c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')#output:a  =  a    b  =  b    c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}')#output:error



#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}')#output:{{x}}
print(F'{{{{{x}}}}}')#output:{{25}}
print(F'{{{{{{x}}}}}}')#output:{{{x}}}
print(F'{{{{{{{x}}}}}}}')#output:{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#output:{{{{x}}}}
