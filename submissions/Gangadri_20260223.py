# 1 . a , b , c = 25 , 10.8 , 'Hyd'

print(a , b , c , sep = ',')  
# => output : 25,10.8,Hyd

print(a , b , c , sep = '\t')  
# => output : 25	10.8	Hyd

print(a , b , c , sep = '---')  
# => output : 25---10.8---Hyd

print(a , b , c , sep = '\n')  
# => output :
# 25
# 10.8
# Hyd

print(a , b , c)  
# => output : 25 10.8 Hyd

print(a , b , c , separator = ':')  
# => output : TypeError (unexpected keyword argument 'separator')



# 2 . a , b , c = 25 , 10.8 , 'Hyd'

print(a , b , c , end = '---')  
# => output : 25 10.8 Hyd---

print(a , b , c , sep = ',,,')  
# => output : 25,,,10.8,,,Hyd

print(a , b , c , sep = ':::' , end = '\t\t\t')  
# => output : 25:::10.8:::Hyd			

print(a , b , c)  
# => output : 25 10.8 Hyd


 # 3 .print('Hyd')  
# => output : Hyd

print()  
# => output : (prints blank line)

print('Sec')  
# => output : Sec

print()  
# => output : (prints blank line)

print('Cyb')  
# => output : Cyb



# 4 . l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}

print(l , t , s)  
# => output : [10, 20, 30, 40] (10, 20, 30, 40) {40, 10, 20, 30}


# 5 . a = 25
b = '%f'  %a
print(b)  
# => output : 25.000000

print(type(b))  
# => output : <class 'str'>

x = 10.8
y = '%i'  %x
print(y)  
# => output : 10

print(type(y))  
# => output : <class 'str'>

m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)  
# => output : [10, 20, 15, 18]

print(type(n))  
# => output : <class 'str'>



# 6 . a = 10.9274

print('%8.2f'  %a)  
# => output :   10.93

print('%9.1f'  %a)  
# => output :      10.9

print('%10.3f'  %a)  
# => output :    10.927

print('%.2f'  %a)  
# => output : 10.93

print('%.6f'  %a)  
# => output : 10.927400

print('%f'  %a)  
# => output : 10.927400

print('%g'  %a)  
# => output : 10.9274


# 7 . a = 'Hyd'

print('%7s'  %a)  
# => output :     Hyd

print('%-7s'  %a)  
# => output : Hyd    

print('%2s'  %a)  
# => output : Hyd

print('%s'  %a)  
# => output : Hyd

print('%s' , a)  
# => output : %s Hyd

print('%s'  a)  
# => output : SyntaxError (missing % operator)

print('%s' , %a)  
# => output : SyntaxError (invalid syntax)

print(a)  
# => output : Hyd


# 8 a = [10 , 20 , 30 , 40]

print('%s'  %a)  
# => output : [10, 20, 30, 40]

print('%s' , a)  
# => output : %s [10, 20, 30, 40]

print('%s'  a)  
# => output : SyntaxError (missing % operator)

print('%s' , %a)  
# => output : SyntaxError (invalid syntax)

print('%l'  %a)  
# => output : TypeError (unsupported format character 'l')

print(a)  
# => output : [10, 20, 30, 40]

# 9 a = 25
b = 10.9274
c = 'Hyd'

print('%d    %f    %s'  %(a , b , c))  
# => output : 25    10.927400    Hyd

print('%i    %g    %s'    %(a , b , c))  
# => output : 25    10.9274    Hyd

print('%s    %s    %s'  %(a , b , c))  
# => output : 25    10.9274    Hyd

print('%d    %g    %s'  , a , b , c)  
# => output : %d    %g    %s 25 10.9274 Hyd

print('%d    %g      %s'   a , b , c)  
# => output : SyntaxError (missing % operator)

print('%d    %g    %s'  ,  %(a , b , c))  
# => output : SyntaxError (invalid syntax)

print('%d    %g    %s'    %a%b%c)  
# => output : TypeError (not enough arguments / wrong formatting)

print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)  
# => output : 25 10.927400 Hyd


# 10 .x = 25
y = F'{x}'
print(y)  
# => output : 25

print(type(y))  
# => output : <class 'str'>


x = 10.8
y = F'{x}'
print(y)  
# => output : 10.8

print(type(y))  
# => output : <class 'str'>


x = [10,20,30,40]
y = F'{x}'
print(y)  
# => output : [10, 20, 30, 40]

print(type(y))  
# => output : <class 'str'>


# 11 .a ,  b , c = 25 , 10.8 , 'Hyd'

print(F'{a}  \t   {b}   \t  {c}')  
# => output : 25  	   10.8   	  Hyd

print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')  
# => output : a = 25  	  b  =  10.8  	  c  =  Hyd

print(F'{a=}  \t   {b=}   \t  {c=}')  
# => output : a=25  	   b=10.8   	  c='Hyd'

print(F'{a:}  \t   {b:}   \t  {c:}')  
# => output : 25  	   10.8   	  Hyd

print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')  
# => output : a  =  {a}  	  b  =  {b}  	  c  =   {c}

print(F'a  =  a  \t  b  =  b  \t  c  =  c')  
# => output : a  =  a  	  b  =  b  	  c  =  c

print(F'{x =}  \t   {y =}   \t  {z =}')  
# => output : NameError (x, y, z are not defined)

# 12 .x = 25

print(F'{x}')  
# => output : 25

print(F'{{x}}')  
# => output : {x}

print(F'{{{x}}}')  
# => output : {25}

print(F'{{{{x}}}}')  
# => output : {{x}}

print(F'{{{{{x}}}}}')  
# => output : {{25}}

print(F'{{{{{{x}}}}}}')  
# => output : {{{x}}}

print(F'{{{{{{{x}}}}}}}')  
# => output : {{{25}}}

print(F'{{{{{{{{x}}}}}}}}')  
# => output : {{{{x}}}}
