# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',') #Output:25, 10.8, 'Hyd'
print(a , b , c , sep = '\t') #Output:25 <tab> 10.8 <tab> 'Hyd'
print(a , b , c , sep = '---') #Output:25---10.8----'Hyd'
print(a , b , c , sep = '\n') #Output:25
                                      10.8
                                      'Hyd'
print(a , b , c) #Output: 25 10.8 'Hyd'
print(a , b , c , separator = ':') #Output:Error
#Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') 
print(a , b , c , sep = ',,,') 
print(a , b , c , sep = ':::' , end = '\t\t\t') 	
print(a , b , c) #Output:25 10.8 Hyd---25,,,10.8,,,Hyd
                         25:::10.8:::Hyd			25 10.8 Hyd
# Find outputs  (Home  work)
print('Hyd') #Output:'Hyd'
print() #Output:<empty>
print('Sec') #Output:'Sec'
print() #Output:<empty>
print('Cyb') #Output:'Cyb'
# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) #Output:[10, 20, 30, 40] (10, 20, 30, 40) {40, 10, 20, 30}
#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) #Output:'25.000000'
print(type(b)) #Output:<class 'str'>
x = 10.8
y = '%i'  %x
print(y) #Output:'10'
print(type(y)) #Output:<class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) #Output:'[10 , 20 , 15 , 18]'
print(type(n)) #Output:<class 'str'>
# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a) #Output:   10.93
print('%9.1f'  %a) #Output:     10.9
print('%10.3f'  %a) #Output:     10.927
print('%.2f'  %a) #Output: 10.93
print('%.6f'  %a) #Output: 10.927400
print('%f'  %a) #Output: 10.927400
print('%g'  %a) #Output:10.9274
# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a) #Output:     'Hyd'
print('%-7s'  %a) #Output:'Hyd'
print('%2s'  %a) #Output:'Hyd'
print('%s'  %a) #Output:'Hyd'
print('%s' , a) #Output:%s 'Hyd'
print('%s'  a) #Output:Error
print('%s' , %a) #Output:Error
print(a) #Output:'Hyd'
# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) #Output:[10, 20, 30, 40]
print('%s' , a) #Output:%s [10, 20, 30, 40]
print('%s'  a) #Output:Error
print('%s' , %a) #Output:Error
print('%l'  %a) #Output:Error
print(a) #Output:[10 , 20 , 30 , 40]
#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) #Output:25    10.927400    Hyd
print('%i    %g    %s'    %(a , b , c)) #Output:25    10.9274    Hyd
print('%s    %s    %s'  %(a , b , c)) #Output:25    10.9274    Hyd
print('%d    %g    %s'  , a , b , c) #Output:%d    %g    %s 25 10.9274 Hyd
print('%d    %g      %s'   a , b , c) #Output:Error
print('%d    %g    %s'  ,  %(a , b , c)) #Output:Error
print('%d    %g    %s'    %a%b%c) #Output:Error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) #Output:25 10.927400 Hyd
#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y) #Output:'25'
print(type(y)) #Output:<class 'str'>
x = 10.8
y = F'{x}'
print(y) #Output:'10.8'
print(type(y)) #Output:<class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) #Output:'[10,20,30,40]'
print(type(y)) #Output:<class 'str'>
#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') #Output:25  	   10.8   	  Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') #Output:a=25  	   b=10.8   	  c='Hyd'     
print(F'{a=}  \t   {b=}   \t  {c=}') #Output:a=25  	   b=10.8   	  c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') #Output:25  	   10.8   	  Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') #Output:a  =  {a}  	  b  =  {b}  	  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') #Output:a  =  a  	  b  =  b  	  c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}') #Output:Error
#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}') #Output:{{x}}
print(F'{{{{{x}}}}}') #Output:{{25}}
print(F'{{{{{{x}}}}}}') #Output:{{{x}}}
print(F'{{{{{{{x}}}}}}}') #Output:{{{25}}}
print(F'{{{{{{{{x}}}}}}}}') #Output:{{{{x}}}}

 

'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''