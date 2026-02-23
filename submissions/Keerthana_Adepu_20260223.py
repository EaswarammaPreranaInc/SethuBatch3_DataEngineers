#sep argument Homework 
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',') # 25 , 10.8 , 'Hyd'
print(a , b , c , sep = '\t') # 25 <tab> 10.8 <tab>  'Hyd'
print(a , b , c , sep = '---') 25 --- 10.8 --- 'Hyd'
print(a , b , c , sep = '\n') 25 <next line> 10.8 <next line> 'Hyd'
print(a , b , c) # 25 10.8 'Hyd'
print(a , b , c , separator = ':') # error because sep is the keyword for separator not the word separator itself


#Outputs Homework #1
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') # 25 10.8 'Hyd' ---
print(a , b , c , sep = ',,,') # 25 ,,, 10.8 ,,, 'Hyd'
print(a , b , c , sep = ':::' , end = '\t\t\t') # 25 ::: 10.8 ::: 'Hyd' <tab> <tab> <tab>
print(a , b , c) # 25 10.8 'Hyd'


#Outputs Homework #2
print('Hyd') # 'Hyd'
print() # empty
print('Sec') # 'Sec'
print() #empty
print('Cyb') # 'Cyb'


#Outputs Homework #3
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # [10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}


#Outputs Homework #4
a = 25
b = '%f'  %a
print(b) # '25.000000'
print(type(b)) # <class 'str'>
x = 10.8
y = '%i'  %x
print(y) # '10'
print(type(y)) # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # '[10 , 20 , 15 , 18]'
print(type(n)) # <class 'str'>


#Outputs Homework #5
a = 10.9274
print('%8.2f'  %a) # '<space><space><space>10.92'
print('%9.1f'  %a) # '<space><space><space><space><space>10.9'
print('%10.3f'  %a) # '<space><space><space><space>10.927'
print('%.2f'  %a) # '10.92'
print('%.6f'  %a) # '10.927400'
print('%f'  %a) # '10.927400'
print('%g'  %a) # '10.9274'


#Outputs Homework #6
a = 'Hyd'
print('%7s'  %a) # '<space><space><space><space>Hyd'
print('%-7s'  %a) # 'Hyd'
print('%2s'  %a) # 'Hyd'
print('%s'  %a) # 'Hyd'
print('%s' , a) # '%s Hyd'
print('%s'  a) # error because there needs to be either comma or % before a
print('%s' , %a) # error because when there is a comma, %a gives an error
print(a) # 'Hyd'


#Outputs Homework #7
a = [10 , 20 , 30 , 40]
print('%s'  %a) # '[10, 20, 30, 40]' 
print('%s' , a) # '%s [10, 20, 30, 40]
print('%s'  a) # error because there needs to be either a comma or % before a
print('%s' , %a) # error because both comma and percentile together are invalid format
print('%l'  %a) # error because # %l is not a specified format
print(a) # [10, 20, 30, 40]


#Outputs Homework #8
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # '25 10.924700 Hyd'
print('%i    %g    %s'    %(a , b , c)) # '25 10.924 Hyd'
print('%s    %s    %s'  %(a , b , c)) # '25 10.924 Hyd'
print('%d    %g    %s'  , a , b , c) # '%d %g %s' 25 10.9247 'Hyd'
print('%d    %g      %s'   a , b , c) # error because there needs to be either % or comma before the objects
print('%d    %g    %s'  ,  %(a , b , c)) # error because both % and comma together are not permitted 
print('%d    %g    %s'    %a%b%c) # error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # '25' '10.9247' 'Hyd'


#Outputs Homework #9
x = 25
y = F'{x}'
print(y) # '25'
print(type(y)) # <class 'str'>
x = 10.8
y = F'{x}'
print(y) # '10.8'
print(type(y)) # <class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) # '[10,20,30,40]' 
print(type(y)) # <class 'str'>


#Outputs Homework #10
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') # '25 <tab> 10.8 <tab> Hyd'
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # 'a = 25 <tab> b = 10.8 <tab> c = Hyd'
print(F'{a=}  \t   {b=}   \t  {c=}') # 'a = 25 <tab> b = 10.8 <tab> c = Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') # '25 <tab> 10.8 <tab> Hyd'
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # 'a = {a} <tab> b = {b} <tab> c = {c}'
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # 'a = a <tab> b = b <tab> c = c'
print(F'{x =}  \t   {y =}   \t  {z =}') # error because x, y and z are not defined


#Outputs Homework #11
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}') # {{x}}
print(F'{{{{{x}}}}}') # {{25}}
print(F'{{{{{{x}}}}}}') # {{{x}}}
print(F'{{{{{{{x}}}}}}}') # {{{25}}}
print(F'{{{{{{{{x}}}}}}}}') # {{{{x}}}}

 

'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''
