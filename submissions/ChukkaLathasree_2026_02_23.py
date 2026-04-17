# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')---> # 25,10.8,'Hyd'
print(a , b , c , sep = '\t')---> # 25 10.8 'Hyd'
print(a , b , c , sep = '---')---> # 25---10.8---''Hyd'
print(a , b , c , sep = '\n')---> #25 10.8 'Hyd'
print(a , b , c)---> #  25 10.8 'Hyd'
print(a , b , c , separator = ':')---> # 25:10.8:'Hyd'

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')---> # 25 10.8 'Hyd'---
print(a , b , c , sep = ',,,')---># 25,,,10.8,,,'Hyd' 
print(a , b , c , sep = ':::' , end = '\t\t\t')---> 25:::10.8:::'Hyd'			
print(a , b , c)----> # 25 10.8 'Hyd'

# Find outputs  (Home  work)
print('Hyd')
print()---> # Hyd
print('Sec')
print()---> # sec
print('Cyb') ---> Cyb

#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)---> # 25.000000
print(type(b)) ---> int
x = 10.8
y = '%i'  %x
print(y)---> # 10
print(type(y))---> # float
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) ---> # 10 , 20 , 15 , 18
print(type(n)) ---> # list

# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)---> # 
print('%9.1f'  %a)
print('%10.3f'  %a)
print('%.2f'  %a)
print('%.6f'  %a)
print('%f'  %a)---> # 10.924700
print('%g'  %a) --> # 10.9247

# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) ---> # 10 , 20 , 30 , 40
print('%s' , a)---> # Error
print('%s'  a)---> # %s
print('%s' , %a)---> # Error
print('%l'  %a)---> # Error
print(a)---> # 10 , 20 , 30 , 40

# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)---> # 10 , 20 , 30 , 40
print('%s' , a)---> # Error
print('%s'  a) ---> # %s
print('%s' , %a)---> # Error
print('%l'  %a)---> # error
print(a)---> # 10 , 20 , 30 , 40

#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) ----> # 25 10.924700 'Hyd'
print('%i    %g    %s'    %(a , b , c))----> # 25 10.9247 'Hyd'
print('%s    %s    %s'  %(a , b , c))----> # '25' '10.9247' 'Hyd'
print('%d    %g    %s'  , a , b , c)---> # Error 
print('%d    %g      %s'   a , b , c)---> # Error
print('%d    %g    %s'  ,  %(a , b , c))---> # error
print('%d    %g    %s'    %a%b%c)---> #  25 10.924700 'Hyd'
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) ---> # 25 ,10.924700 , 'Hyd'

#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)---> # 25
print(type(y))---> int
x = 10.8
y = F'{x}'
print(y)---> # 10.8
print(type(y))---> float
x = [10 , 20 , 30 , 40]
y = F'{x}'
print(y)---> # 10 , 20 , 30 , 4
print(type(y))---> #list

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')---> # 25	10.8	'Hyd'
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') ---># a=25	b=10.8	c='Hyd'
print(F'{a=}  \t   {b=}   \t  {c=}')--->#  a=25		b=10.8		c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}')---> #  a=25		b=10.8		c='Hyd'
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')---># error
print(F'a  =  a  \t  b  =  b  \t  c  =  c')--->#  a=25		b=10.8		c='Hyd'
print(F'{x =}  \t   {y =}   \t  {z =}')---> #  a=25		b=10.8		c='Hyd'

#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}')---># '25'
print(F'{{{{{x}}}}}')----># {{25}}
print(F'{{{{{{x}}}}}}')---># '25'
print(F'{{{{{{{x}}}}}}}')---># {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')---># '25'

 

'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''

